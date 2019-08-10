import graphene
from graphql_jwt.decorators import login_required
from .models import User, Profile, Post
from .types import UserObjectType, ProfileObjectType, PostObjectType


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


class EditUserMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()
        search_distance = graphene.Int()

    updated = graphene.Boolean()

    @login_required
    def mutate(self, info, *args, **kwargs):
        user_id = kwargs.pop('id')
        target = User.objects.get(id=user_id)

        if target is not None:
            if kwargs.get('password'):
                new_password = kwargs.pop('password')
                target.set_password(new_password)
            try:
                for (key, value) in kwargs.items():
                    setattr(target, key, value)
            except:
                raise Exception('Invalid update field')
            target.save()
            return EditUserMutation(updated=True)
        return EditUserMutation(updated=False)


class CreateProfileMutation(graphene.Mutation):
    class Arguments:
        description = graphene.String()
        categories = graphene.List(graphene.String)

    new_profile = graphene.Field(ProfileObjectType)

    @login_required
    def mutate(self, info, description, categories):
        new_profile = Profile.objects.create(
            owner=info.context.user, description=description, categories=categories)
        return CreateProfileMutation(new_profile=new_profile)

class CreatePostMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        text = graphene.String(required=True)

    new_post = graphene.Field(PostObjectType)

    @login_required
    def mutate(self, info, title, text):
        new_post = Post.objects.create(
            owner=info.context.user, title=title, text=text)
        return CreatePostMutation(new_post=new_post)


class Mutation(graphene.ObjectType):
    signup = SignupMutation.Field()
    edit_user = EditUserMutation.Field()
    create_profile = CreateProfileMutation.Field()
    create_post = CreatePostMutation.Field()
