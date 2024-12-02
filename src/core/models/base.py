from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr

from utils import camel_case_to_snake_case


class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return f"{camel_case_to_snake_case(cls.__name__)}s"
