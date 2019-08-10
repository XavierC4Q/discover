import graphene
from graphql_jwt.decorators import login_required
from .models import User, Comment, Post, Profile
from .types import UserObjectType, PostObjectType, CommentObjectType, ProfileObjectType


class Query(graphene.ObjectType):
    users = graphene.List(UserObjectType)
    single_user = graphene.Field(UserObjectType, id=graphene.Int())
    user_profile = graphene.Field(ProfileObjectType, profile_id=graphene.Int())

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_single_user(self, info, id):
        return User.objects.get(id=id)

    @login_required
    def resolve_user_profile(self, info, profile_id):
        return Profile.objects.get(id=profile_id)
