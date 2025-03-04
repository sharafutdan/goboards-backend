from typing import TYPE_CHECKING

from sqlalchemy import orm

from utils.db.base import BaseORMModel


if TYPE_CHECKING:
    from core.auth.models import SessionORM
    from core.games.models import GameORM
    from core.meetups.models import MeetupORM, MeetupUserORM
    from core.oauth.models import SocialAccountORM


class UserORM(BaseORMModel):
    __tablename__ = "users"

    first_name: orm.Mapped[str]
    last_name: orm.Mapped[str]
    is_admin: orm.Mapped[bool] = orm.mapped_column(default=False)

    social_accounts: orm.Mapped[list["SocialAccountORM"]] = orm.relationship(
        back_populates="user"
    )
    games: orm.Mapped[list["GameORM"]] = orm.relationship(
        back_populates="user"
    )
    sessions: orm.Mapped[list["SessionORM"]] = orm.relationship(back_populates="user")
    meetups: orm.Mapped[list["MeetupORM"]] = orm.relationship(secondary="meetups_users", back_populates="users")
    meetup_associations: orm.Mapped["MeetupUserORM"] = orm.relationship(back_populates="user")


    @property
    def username(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"<{self.__class__.__name__}> #{self.id}, Name - {self.username}"
