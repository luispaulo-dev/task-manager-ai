from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.task import TaskModel
from app.schemas.task import TaskCreate, TaskUpdate

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, task_data: TaskCreate) -> TaskModel:
        db_task = TaskModel(**task_data.model_dump())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def get_by_id(self, task_id: int) -> Optional[TaskModel]:
        return self.db.query(TaskModel).filter(TaskModel.id == task_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> List[TaskModel]:
        return self.db.query(TaskModel).offset(skip).limit(limit).all()

    def update(self, db_task: TaskModel, task_data: TaskUpdate) -> TaskModel:
        update_data = task_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_task, key, value)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def delete(self, db_task: TaskModel) -> None:
        self.db.delete(db_task)
        self.db.commit()