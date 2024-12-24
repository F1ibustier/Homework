from app.models import *
from app.schemas import CreateUser, UpdateUser
from app.backend.db_depends import get_db
from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, insert, select, update, delete
from sqlalchemy.orm import relationship, Session
from sqlalchemy.schema import CreateTable
from typing import Annotated
from slugify import slugify
from fastapi import APIRouter, Depends, status, HTTPException

router = APIRouter(prefix='/user', tags=['user'])

# Напишите логику работы функций маршрутов:
# Каждая из нижеперечисленных функций подключается к базе данных в момент обращения при помощи
# функции get_db - Annotated[Session, Depends(get_db)]

# Функция all_users ('/'):
# Должна возвращать список всех пользователей из БД. Используйте scalars, select и all
@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users

# Функция user_by_id ('/user_id'):
# Для извлечения записи используйте ранее импортированную функцию select. Дополнительно принимает user_id.
# Выбирает одного пользователя из БД. Если пользователь не None, то возвращает его.
# В противном случае выбрасывает исключение с кодом 404 и описанием "User was not found"
@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is not None:
        return user
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

# Функция create_user ('/create'):
# Для добавления используйте ранее импортированную функцию insert.
# Дополнительно принимает модель CreateUser.
# Подставляет в таблицу User запись значениями указанными в CreateUser.
# В конце возвращает словарь {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
# Обработку исключения существующего пользователя по user_id или username можете сделать по желанию.
@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db.execute(insert(User).values(username=create_user.username,
                                    firstname=create_user.firstname,
                                    lastname=create_user.lastname,
                                    age=create_user.age,
                                    slug=slugify(create_user.username)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

# Функция update_user ('/update'):
# Для обновления используйте ранее импортированную функцию update.
# Дополнительно принимает модель UpdateUser и user_id.
# Если находит пользователя с user_id, то заменяет эту запись значениям из модели UpdateUser.
# Далее возвращает словарь {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}
# В противном случае выбрасывает исключение с кодом 404 и описанием "User was not found"
@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser):
    user_updated = db.scalar(select(User).where(User.id == user_id))
    if user_updated is not None:
        db.execute(update(User).where(User.id == user_id).values(firstname=update_user.firstname,
                                                                 lastname=update_user.lastname,
                                                                 age=update_user.age,
                                                                 slug=slugify(update_user.firstname)))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')


# Функция delete_user ('/delete'):
# Для удаления используйте ранее импортированную функцию delete.
# Всё должно работать аналогично функции update_user, только объект удаляется.
# Исключение выбрасывать то же.
@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user_delete = db.scalar(select(User).where(User.id == user_id))
    if user_delete is not None:
        db.execute(delete(User).where(User.id == user_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'User delete is successful!'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
