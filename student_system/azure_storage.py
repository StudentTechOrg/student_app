
import os
from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    account_name = 'c2087665'
    account_key = 'FXyZTY5wiUX3/Np/ugZuGJqwhrlAYMzjmmuJk3EHQs8KrGqp7RHmpB0h6XnXMMLRPKkRnMQyt5pp+AStWHutmA=='
    azure_container = 'media'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = 'c2087665'
    account_key = 'FXyZTY5wiUX3/Np/ugZuGJqwhrlAYMzjmmuJk3EHQs8KrGqp7RHmpB0h6XnXMMLRPKkRnMQyt5pp+AStWHutmA=='
    azure_container = 'static'
    expiration_secs = None