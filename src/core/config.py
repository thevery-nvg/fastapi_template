from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8000


class DBConfig(BaseModel):
    db_url: str


class PrefixConfig(BaseModel):
    api: str = '/api'


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    prefix: PrefixConfig = PrefixConfig()
    DB: DBConfig = DBConfig()


settings = Settings()
