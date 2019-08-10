import graphene
from graphene_django.types import DjangoObjectType
from .models import User, Post, Comment, Profile

class UserObjectType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ('password', )

class PostObjectType(DjangoObjectType):
    class Meta:
        model = Post
        exclude = ('owner.password', )

class CommentObjectType(DjangoObjectType):
    class Meta:
        model = Comment
        exclude = ('owner.password', )

class ProfileObjectType(DjangoObjectType):
    profile_posts = graphene.List(PostObjectType)
    class Meta:
        model = Profile
        exclude = ('owner.password', )