from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.schemas import UserResponse, UserForm
from app import models
# from ..repositories import UserResponse

router = APIRouter(tags=['user'], prefix='/user')

@router.get('', response_model=list[UserResponse], status_code=status.HTTP_200_OK)
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.Users).all()
    return users

@router.post('')
def create_user(request: UserForm, db: Session = Depends(get_db)):
    pass