from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_key: str

    db_conn_str: str

    vector_collection_name: str

    # 自动读取 .env 文件
    model_config = SettingsConfigDict(env_file=".env", env_prefix="aisql_")


settings = Settings()
