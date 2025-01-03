from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

# Измените и дополните ранее описанные 4 CRUD запроса:
# 1. get запрос по маршруту '/users' теперь возвращает список users.
@app.get('/users')
async def get_all_users() -> List[User]:
    return users

# 2. post запрос по маршруту '/user/{username}/{age}', теперь:
# Добавляет в список users объект User.
# id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
# Все остальные параметры объекта User - переданные в функцию username и age соответственно.
# В конце возвращает созданного пользователя.
@app.post('/user/{username}/{age}')
async def create_user(user: User,
                      username: Annotated[str, Path(min_length=3,
                                                    max_length=20,
                                                    description='Enter username',
                                                    example='UrbanUser')],
                      age: Annotated[int, Path(ge=18,
                                               le=120,
                                               description='Enter age',
                                               example=24)]) -> str:
    if users:
        current_index = max(user.id for user in users) + 1
    else:
        current_index = 1
    user.id = current_index
    user.username = username
    user.age = age
    users.append(user)
    return f"User {current_index} is registered"

# 3. put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
# Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
# В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
@app.put('/user/{user_id}/{username}/{age}')
async def put_user(user_id: Annotated[int, Path(ge=1,
                                                le=999,
                                                description='Enter user_id',
                                                example=1)],
                    username: Annotated[str, Path(min_length=3,
                                                  max_length=20,
                                                  description='Enter username',
                                                  example='UrbanUser')],
                    age: Annotated[int, Path(ge=18,
                                             le=120,
                                             description='Enter age',
                                             example=24)]) -> str:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return f"The user {user_id} is updated: {user}."
    raise HTTPException(status_code=404, detail="User was not found.")

# 4. delete запрос по маршруту '/user/{user_id}', теперь:
# Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
# В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1,
                                                le=999,
                                                description='Enter user_id',
                                                example=1)],) -> str:
    for index, existing_user in enumerate(users):
        if existing_user.id == user_id:
            users.pop(index)
            return f"User {user_id} deleted: {existing_user}."
    raise HTTPException(status_code=404, detail="User was not found")
