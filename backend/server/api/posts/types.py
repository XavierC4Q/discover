import graphene
from graphene_django.types import DjangoObjectType
from server.api.models import Post, Comment

class PostObjectType(DjangoObjectType):
    class Meta:
        model = Post
        exclude = ('owner.password', )

class CommentObjectType(DjangoObjectType):
    class Meta:
        model = Comment
        exclude = ('owner.password', )