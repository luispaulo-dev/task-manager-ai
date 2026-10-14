from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Task Manager AI"
    DATABASE_URL: str = "postgresql://postgres:postgres@db:5432/task_manager_db"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()