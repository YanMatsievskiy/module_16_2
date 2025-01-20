from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get('/')
async def main_page() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get('/user')
async def user_info(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

@app.get("/user/{id}")
async def get_page(id: int = Path(ge=1, le=100, description='Enter User ID', example='1')) -> dict:
    return {"message": f"Вы вошли как пользователь № {id}"}

@app.get("/user/{username}/{age}")
async def get_page(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                 example='UrbanUser')],
                   age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> dict:
    return {"message": f"Привет {username} {age}"}
