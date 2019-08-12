import graphene
from graphql_jwt.decorators import login_required
from server.api.models import User, Profile
from .types import UserObjectType, ProfileObjectType


class Query(graphene.ObjectType):
    users = graphene.List(UserObjectType)
    single_user = graphene.Field(UserObjectType, id=graphene.ID())
    user_profile = graphene.Field(ProfileObjectType, owner_id=graphene.ID())

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_single_user(self, info, id):
        return User.objects.get(id=id)

    def resolve_user_profile(self, info, owner_id):
        return Profile.objects.get(owner__id=owner_id)