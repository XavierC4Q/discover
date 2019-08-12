import graphene
from graphql_jwt.decorators import login_required
from server.api.models import User, Profile
from .types import UserObjectType, ProfileObjectType


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


class Mutation(graphene.ObjectType):
    edit_user = EditUserMutation.Field()
    create_user_profile = CreateProfileMutation.Field()
