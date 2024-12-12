from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main_page():
    return {"Главная страница"}

@app.get("/user/admin")
async def admin_login():
    return {"Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def users_login(user_id: int):
    return {f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/")
async def users_info(username: str, age: int):
    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
