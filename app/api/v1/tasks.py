
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tarefas"])

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.create_task(task_data)

@router.get("/", response_model=List[TaskResponse])
def list_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.list_tasks(skip=skip, limit=limit)

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.get_task(task_id)

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.update_task(task_id, task_data)

@router.delete("/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.delete_task(task_id)