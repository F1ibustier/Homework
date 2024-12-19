from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

# Реализуйте 4 CRUD запроса:
# 1. get запрос по маршруту '/users', который возвращает словарь users.
@app.get('/users')
async def get_users() -> dict:
    return users

# 2. post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по максимальному
# значению ключа значение строки "Имя: {username}, возраст: {age}". И возвращает строку "User <user_id> is registered".
@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5,
                                                   max_length=20,
                                                   description='Enter username',
                                                   example='UrbanUser')],
                     age: Annotated[int, Path(ge=18,
                                              le=120,
                                              description='Enter age',
                                              example=24)]):
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'

# 3. put запрос по маршруту '/user/{user_id}/{username}/{age}', который обновляет значение из словаря users
# под ключом user_id на строку "Имя: {username}, возраст: {age}". И возвращает строку "The user <user_id> is updated"
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str,
                      username: Annotated[str, Path(min_length=5,
                                                   max_length=20,
                                                   description='Enter username',
                                                   example='UrbanUser')],
                      age: Annotated[int, Path(ge=18,
                                              le=120,
                                              description='Enter age',
                                              example=24)]):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'

# 4. delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару.
@app.delete('/user/{user_id}')
async def delete_user(user_id: str):
    users.pop(user_id)
    return f'User {user_id} has been deleted'
