from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn


class RunConfig(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8000


class DBConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 100


class PrefixConfig(BaseModel):
    api: str = '/api'


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_nested_delimiter='__',
        env_prefix="FASTAPI_CONFIG__",
        env_file='.env'
    )
    run: RunConfig = RunConfig()
    prefix: PrefixConfig = PrefixConfig()
    db: DBConfig


settings = Settings()
