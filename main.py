from fastapi import FastAPI
from sqlmodel import SQLModel
from infrastructure.database import database

from interface.api.users import router as users_router

# Importar os routers
# from interface.api.users import router as users_router
# from interface.api.other_module import router as other_router  # exemplo adicional

# Criar a aplicação FastAPI
app = FastAPI(
    title="FastAPI DDD with SQLModel",
    description="API seguindo Domain-Driven Design com SQLModel",
    version="0.1.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc"
)

# Configurar os routers
app.include_router(users_router, prefix="/api/v1")
# app.include_router(users_router, prefix="/api/v1")
# app.include_router(other_router, prefix="/api/v1")  # exemplo adicional


@app.on_event("startup")
def on_startup():
    """Evento executado ao iniciar a aplicação"""
    # Criar tabelas no banco de dados
    SQLModel.metadata.create_all(database.engine)

    # Outras inicializações podem ser feitas aqui
    # Ex: Popular dados iniciais, conectar serviços externos, etc.


@app.on_event("shutdown")
def on_shutdown():
    """Evento executado ao encerrar a aplicação"""
    # Limpeza de recursos
    # Ex: Desconectar serviços, fechar conexões, etc.


# Health Check Endpoint
@app.get("/health", tags=["health"])
def health_check():
    """Endpoint para verificar se a API está online"""
    return {"status": "healthy"}


def start_server():
    import uvicorn
    uvicorn.run(
        app,  # Diretamente o objeto app
        host="localhost",
        port=8000,
        workers=1
    )

if __name__ == "__main__":
    start_server()