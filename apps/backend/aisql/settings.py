from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    api_key: str

    pg_conn_str: str = "postgresql://postgres:1234@localhost:5432/aisql"

    vector_collection_name: str = "aisql_docs"

    # 自动读取 .env 文件
    model_config = SettingsConfigDict(env_file=".env", env_prefix='aisql_')

settings = Settings()
