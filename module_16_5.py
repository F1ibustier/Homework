from fastapi import FastAPI, Path, HTTPException, Request
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")
users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

# Измените и дополните ранее описанные CRUD запросы:
# Напишите новый запрос по маршруту '/':
# Функция по этому запросу должна принимать аргумент request и возвращать TemplateResponse.
# TemplateResponse должен подключать ранее заготовленный шаблон 'users.html', а также передавать
# в него request и список users. Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.

@app.get("/")
def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

# 1. Измените get запрос по маршруту '/user' на '/user/{user_id}':
# Функция по этому запросу теперь принимает аргумент request и user_id.
# Вместо возврата объекта модели User, теперь возвращается объект TemplateResponse.
# TemplateResponse должен подключать ранее заготовленный шаблон 'users.html', а также передавать в него request
# и одного из пользователей - user. Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.

@app.get('/user/{user_id}')
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request":request, "user": users[user_id-1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")

# 2. post запрос по маршруту '/user/{username}/{age}', теперь:
# Добавляет в список users объект User.
# id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
# Все остальные параметры объекта User - переданные в функцию username и age соответственно.
# В конце возвращает созданного пользователя.

@app.post('/user/{username}/{age}')
async def post_user(user: User,
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
async def update_user(user_id: Annotated[int, Path(ge=1,
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
            return f"The user {user_id} is updated."
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
            return f"User {user_id} deleted."
    raise HTTPException(status_code=404, detail="User was not found")
