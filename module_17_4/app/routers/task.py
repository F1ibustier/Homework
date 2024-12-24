from fastapi import APIRouter
from app.backend.db import Base
from app.schemas import CreateTask, UpdateTask
from app.models import *
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks():
    pass


@router.get('/task_id')
async def task_by_id():
    pass


@router.post('/create')
async def create_task():
    pass


@router.put('/update')
async def update_task():
    pass


@router.delete('/delete')
async def delete_task():
    pass
