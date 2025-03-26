from application.service.user_service import UserService
from infrastructure.impl_repository.sql_user_repository import SQLModelUserRepository


def get_user_service():
    # Cria o repositório concreto
    repo = SQLModelUserRepository()

    # Cria o serviço injetando o repositório
    service = UserService(repo)

    return service