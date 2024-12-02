from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pydantic import PostgresDsn

class RunConfig(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8000


class DBConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 5
    max_overflow: int = 10


class PrefixConfig(BaseModel):
    api: str = '/api'


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    prefix: PrefixConfig = PrefixConfig()
    db: DBConfig = DBConfig()


settings = Settings()