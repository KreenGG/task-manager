from sqlalchemy import String
from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    is_done: Mapped[bool] = mapped_column(default=False)

    def __str__(self) -> str:
        return self.title
