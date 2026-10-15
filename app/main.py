from fastapi import FastAPI
from app.api.v1 import tasks

app = FastAPI(title="Task Manager AI", version="1.0.0")

# Inclui as rotas de tarefas
app.include_router(tasks.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "API Task Manager AI rodando com sucesso no Docker!"}