import graphene
from server.api.users.types import UserObjectType

class Query(graphene.ObjectType):
    logged_in_user = graphene.Field(UserObjectType)

    def resolve_logged_in_user(self, info):
        return info.context.user