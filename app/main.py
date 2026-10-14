from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.session import get_db
from app.models.task import TaskModel

app = FastAPI(title="Task Manager AI", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "API rodando com sucesso no Docker!"}

# Rota para testar a conexão com o banco e inserir uma tarefa de teste
@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    try:
        # Testa a conexão executando um comando simples
        db.execute(text("SELECT 1"))
        
        # Cria uma tarefa de teste no banco
        nova_tarefa = TaskModel(title="Tarefa de Teste", description="Testando a conexão com o PostgreSQL")
        db.add(nova_tarefa)
        db.commit()
        db.refresh(nova_tarefa)
        
        return {
            "status": "Sucesso!",
            "message": "Conexão com o PostgreSQL e inserção funcionando perfeitamente!",
            "tarefa_criada": {
                "id": nova_tarefa.id,
                "title": nova_tarefa.title,
                "description": nova_tarefa.description
            }
        }
    except Exception as e:
        return {"status": "Erro", "details": str(e)}