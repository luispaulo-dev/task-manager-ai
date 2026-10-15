from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

# Schema base 
class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Título da tarefa")
    description: Optional[str] = Field(None, max_length=500, description="Descrição detalhada da tarefa")
    completed: bool = Field(False, description="Status de conclusão da tarefa")

# Schema para criação (o usuário envia no POST)
class TaskCreate(TaskBase):
    pass

# Schema para atualização (PUT/PATCH)
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    completed: Optional[bool] = None

# Schema de resposta 
class TaskResponse(TaskBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True