from sqlalchemy.orm import Session

from backend.src.schemas import schemas
from backend.src.infra.sqlalchemy.models import models


class RepositoryUser():
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: schemas.User):
        new_user = models.User(
            username=user.username,
            password=user.password,
            phone=user.phone,
        )

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return new_user

    def get_all(self):
        users = self.db.query(models.User).all()
        return users

    def get(self):
        pass

    def remove(self):
        pass