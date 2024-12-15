from pydantic import BaseModel


class UserRead(BaseModel):
    __tablename__ = "users"
    id: int
    username: str
    password: str
    email: str
    is_active: bool
    is_admin: bool
    is_superuser: bool

