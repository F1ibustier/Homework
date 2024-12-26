from app.models import *
from app.schemas import CreateTask, UpdateTask
from app.backend.db_depends import get_db
from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, insert, select, update, delete
from sqlalchemy.orm import relationship, Session
from typing import Annotated
from slugify import slugify
from fastapi import APIRouter, Depends, status, HTTPException

router = APIRouter(prefix='/task', tags=['task'])

# Функция all_tasks ('/') - идентично all_users.
@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks

# Функция task_by_id ('/task_id') - идентично user_by_id (тоже по id)
@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(User).where(Task.id == task_id))
    if task is not None:
        return task
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')

# Функция create_task ('/create'):
# Дополнительно принимает модель CreateTask и user_id.
# Подставляет в таблицу Task запись значениями указанными в CreateUser и user_id, если пользователь найден.
# Т.е. при создании записи Task вам необходимо связать её с конкретным пользователем User.
# В конце возвращает словарь {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
# В случае отсутствия пользователя выбрасывает исключение с кодом 404 и описанием "User was not found"
@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], user_id: int, create_task: CreateTask):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    db.execute(insert(Task).values(title=create_task.title,
                                    content=create_task.content,
                                    priority=create_task.priority,
                                    user_id=user_id,
                                    slug=slugify(create_task.title)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

#Функция update_task ('/update') - идентично update_user.
@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, update_task: UpdateTask):
    task_updated = db.scalar(select(Task).where(Task.id == task_id))
    if task_updated is not None:
        db.execute(update(Task).where(Task.id == task_id).values(title=update_task.title,
                                                                 content=update_task.content,
                                                                 priority=update_task.priority,
                                                                 slug=slugify(update_task.title)))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')

# Функция delete_task ('/delete') - идентично delete_user.
@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task_delete = db.scalar(select(Task).where(Task.id == task_id))
    if task_delete is not None:
        db.execute(delete(Task).where(Task.id == task_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'Task delete is successful!'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')
