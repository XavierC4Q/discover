import graphene
import graphql_jwt
from .api.auth.schema import schema as authSchema
from .api.users.schema import schema as userSchema
from .api.posts.schema import schema as postSchema


class Query(
    authSchema.Query,
    userSchema.Query,
    postSchema.Query,
    graphene.ObjectType
):
    pass

class Mutation(
    authSchema.Mutation,
    userSchema.Mutation,
    postSchema.Mutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)