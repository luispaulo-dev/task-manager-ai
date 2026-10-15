# 🚀 Task Manager AI

API RESTful moderna desenvolvida com **FastAPI**, **PostgreSQL** e **Docker**, projetada com arquitetura limpa (Clean Architecture / Separation of Concerns) e (futuramente) integrada com recursos de Inteligência Artificial para gerenciamento inteligente de tarefas.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.11** / **FastAPI** (Framework web assíncrono de alta performance)
* **PostgreSQL** (Banco de dados relacional)
* **SQLAlchemy** (ORM para mapeamento objeto-relacional)
* **Alembic** (Gerenciamento de migrações de banco de dados)
* **Docker & Docker Compose** (Containerização e orquestração de ambiente)
* **Pydantic** (Validação de dados)

---

## 📂 Arquitetura do Projeto

O projeto segue uma estrutura modular limpa, separando responsabilidades entre rotas, regras de negócio, persistência e modelos:

```text
task-manager-ai/
├── alembic/              # Migrações de banco de dados
├── app/
│   ├── api/v1/           # Endpoints da API (Rotas do CRUD)
│   ├── core/             # Configurações globais e variáveis de ambiente
│   ├── db/               # Sessão e conexão com o banco de dados
│   ├── models/           # Modelos ORM (SQLAlchemy)
│   ├── repositories/     # Camada de acesso aos dados
│   ├── schemas/          # Schemas de validação e serialização (Pydantic)
│   ├── services/         # Regras de negócio e integração com IA
│   └── main.py           # Ponto de entrada da aplicação FastAPI
├── docker-compose.yml    # Orquestração dos containers (App + PostgreSQL)
├── Dockerfile            # Configuração da imagem Docker da aplicação
├── requirements.txt      # Dependências do projeto Python
└── README.md             # Documentação do projeto
``




🗺️ Roadmap do Projeto

    [x] Infraestrutura e Containerização: Configuração do ambiente com Docker e PostgreSQL.

    [x] Configuração de Banco de Dados: Mapeamento ORM e controle de migrações via Alembic.

    [x] Schemas e Validação: Implementação de contratos de dados com Pydantic.

    [x] CRUD Completo: Desenvolvimento dos endpoints de criação, leitura, atualização e exclusão de tarefas.

    [ ] Integração com Inteligência Artificial: Análise inteligente de tarefas via API de IA.

    [ ] Documentação e Testes: Testes automatizados e documentação final de uso.

⚙️ Como Executar o Projeto Localmente

Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.

    Clone o repositório: [Repositório no GitHub](https://github.com/luispaulo-dev/task-manager-ai.git)

    Bash

    git clone https://github.com/luispaulo-dev/task-manager-ai.git
    cd task-manager-ai

    Suba os containers da aplicação e do banco de dados:

    Bash

    docker compose up -d --build

    A aplicação estará rodando em: http://localhost:8000

    Acesse a documentação interativa (Swagger UI) em: http://localhost:8000/docs

👨‍💻 Autor

Desenvolvido por Luís Paulo Andrade Silva
