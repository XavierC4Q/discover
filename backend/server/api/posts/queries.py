import graphene
from server.api.models import User, Comment, Post, Profile
from .types import PostObjectType


class Query(graphene.ObjectType):
    posts = graphene.List(PostObjectType)
    user_posts = graphene.List(PostObjectType, user_id=graphene.ID())
    single_post = graphene.Field(PostObjectType, post_id=graphene.ID())

    def resolve_posts(self, info):
        return Post.objects.all()

    def resolve_user_posts(self, info, user_id):
        return Post.objects.filter(owner__id=user_id)

    def resolve_single_post(self, info, post_id):
        return Post.objects.get(id=post_id)