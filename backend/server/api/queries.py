import graphene
from graphql_jwt.decorators import login_required
from .models import User, Comment, Post, Profile
from .types import UserObjectType, PostObjectType, CommentObjectType, ProfileObjectType


class Query(graphene.ObjectType):
    users = graphene.List(UserObjectType)
    single_user = graphene.Field(UserObjectType, id=graphene.ID())
    user_profile = graphene.Field(ProfileObjectType, owner_id=graphene.ID())
    posts = graphene.List(PostObjectType)
    user_posts = graphene.List(PostObjectType, user_id=graphene.ID())
    single_post = graphene.Field(PostObjectType, post_id=graphene.ID())

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_single_user(self, info, id):
        return User.objects.get(id=id)

    def resolve_user_profile(self, info, owner_id):
        return Profile.objects.get(owner__id=owner_id)

    def resolve_posts(self, info):
        return Post.objects.all()

    def resolve_user_posts(self, info, user_id):
        return Post.objects.filter(owner__id=user_id)

    def resolve_single_post(self, info, post_id):
        return Post.objects.get(id=post_id)
