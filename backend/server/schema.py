import graphene
import graphql_jwt

from .api import schema as apiSchema
from .api.types import UserObjectType


class Query(
    apiSchema.Query,
    graphene.ObjectType
):
    pass

#Add user to token request
class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(UserObjectType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)

class Mutation(
    apiSchema.Mutation,
    graphene.ObjectType,
):
    get_token = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)