from dependency_injector import containers, providers
from src.infrastructure.data.DataService import DataService


class DiContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    # api_client = providers.Singleton(
    #     ApiClient,
    #     api_key=config.api_key,
    #     timeout=config.timeout,
    # )

    data_service_factory = providers.Factory(
        DataService
    )
