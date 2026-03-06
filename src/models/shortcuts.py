from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class ShortcutsModel(Base):
    __tablename__ = "shortcuts"

    original: Mapped[str] = mapped_column(String, nullable=False)
    visits: Mapped[int] = mapped_column(Integer, default=0)
