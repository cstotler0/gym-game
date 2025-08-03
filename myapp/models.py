from typing import Optional
import sqlalchemy as salc
import sqlalchemy.orm as sorm
from myapp import db


class User(db.Model):
    id: sorm.Mapped[int] = sorm.mapped_column(primary_key=True)
    username: sorm.Mapped[str] = sorm.mapped_column(salc.String(64), index=True, unique=True)
    email: sorm.Mapped[str] = sorm.mapped_column(salc.String(64), index=True, unique=True)
    password_hash: sorm.Mapped[Optional[str]] = sorm.mapped_column(salc.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)
