from sqlalchemy import Boolean, String, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column

from src.core.base.enums import Role
from src.core.base.models import Base


class User(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(200), unique=True)
    username: Mapped[str] = mapped_column(String(200), unique=True)
    role: Mapped[str] = mapped_column(
        SAEnum(Role, names="user_role_enum"), default=Role.CUSTOMER
    )
    first_name: Mapped[str | None] = mapped_column(String(200), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(200), nullable=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    password: Mapped[str]  # hashed password

    def __str__(self) -> str:
        return self
