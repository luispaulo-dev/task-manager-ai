from fastapi import FastAPI

app = FastAPI(title="Task Manager AI", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "API rodando com sucesso no Docker!"}