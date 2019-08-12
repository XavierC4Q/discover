import graphene
import graphql_jwt
from server.api.models import User
from server.api.users.types import UserObjectType


class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(UserObjectType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)

class SignupMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    new_user = graphene.Field(UserObjectType)

    def mutate(self, info, email, username, password):
        try:
            create_user = User.objects.create_user(
                username, email=email, password=password)
            create_user.save()
            return SignupMutation(new_user=create_user)
        except:
            raise Exception('Failed to create user')


class Mutation(graphene.ObjectType):
    get_token = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    signup = SignupMutation.Field()
