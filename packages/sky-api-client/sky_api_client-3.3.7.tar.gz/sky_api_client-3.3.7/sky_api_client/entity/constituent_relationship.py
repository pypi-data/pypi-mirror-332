from sky_api_client.entity.base import Entity
from sky_api_client.entity.registry import EntityRegistry


@EntityRegistry.register('constituent_relationship')
class ConstituentRelationship(Entity):
    LIST_URL = '/constituent/v1/constituents/{id}/relationships'
