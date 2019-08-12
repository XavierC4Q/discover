import graphene
from graphene_django.types import DjangoObjectType
from server.api.models import User, Profile
from server.api.posts.types import PostObjectType

class UserObjectType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ('password', )

class ProfileObjectType(DjangoObjectType):
    profile_posts = graphene.List(PostObjectType)
    class Meta:
        model = Profile
        exclude = ('owner.password', )