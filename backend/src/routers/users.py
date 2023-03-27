from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.src.schemas.schemas import User, SimpleUser
from backend.src.infra.sqlalchemy.repositories.user import RepositoryUser
from backend.src.infra.sqlalchemy.config.database import get_db

router = APIRouter()


@router.get("/users", response_model=list[SimpleUser])
def get_all_users(db: Session = Depends(get_db)):
    users = RepositoryUser(db).get_all()
    return users


@router.post(
        "/users", status_code=status.HTTP_201_CREATED, response_model=SimpleUser
)
def create_user(user: User, db: Session = Depends(get_db)):
    new_user = RepositoryUser(db).create(user)
    return new_user
