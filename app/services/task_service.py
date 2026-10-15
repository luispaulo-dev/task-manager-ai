from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse

class TaskService:
    def __init__(self, db: Session):
        self.repository = TaskRepository(db)

    def create_task(self, task_data: TaskCreate) -> TaskResponse:
        return self.repository.create(task_data)

    def get_task(self, task_id: int) -> TaskResponse:
        task = self.repository.get_by_id(task_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Tarefa com ID {task_id} não encontrada."
            )
        return task

    def list_tasks(self, skip: int = 0, limit: int = 100) -> List[TaskResponse]:
        return self.repository.get_all(skip=skip, limit=limit)

    def update_task(self, task_id: int, task_data: TaskUpdate) -> TaskResponse:
        db_task = self.repository.get_by_id(task_id)
        if not db_task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Tarefa com ID {task_id} não encontrada."
            )
        return self.repository.update(db_task, task_data)

    def delete_task(self, task_id: int) -> dict:
        db_task = self.repository.get_by_id(task_id)
        if not db_task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Tarefa com ID {task_id} não encontrada."
            )
        self.repository.delete(db_task)
        return {"message": f"Tarefa {task_id} removida com sucesso."}