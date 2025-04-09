from fastapi import APIRouter, HTTPException, status

from src.schemas.user import CreateUser, UserInfo
from src.fake_db import db

router = APIRouter()

@router.get("", status_code=status.HTTP_200_OK, response_model=UserInfo, responses={404: {"detail": "User not found"}})
async def get_user(email: str):
    '''Получение пользователя по email'''
    user = db.get_user_by_email(email)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return UserInfo(
        id=user['id'],
        name=user['name'],
        email=user['email']
    )
    
@router.post("", status_code=status.HTTP_201_CREATED, response_model=int,
             responses={409: {"detail": "User with this email already exists"}})
async def create_user(data: CreateUser):
    '''Создание пользователя'''
    if db.get_user_by_email(data.email) is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with this email already exists")
    db.create_user(data.name, data.email)
    return db.get_user_by_email(data.email)['id']

@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(email: str):
    '''Удаление пользователя'''
    db.delete_user_by_email(email)
