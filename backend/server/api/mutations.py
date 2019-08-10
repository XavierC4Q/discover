import graphene
from graphql_jwt.decorators import login_required
from .models import User, Profile
from .types import UserObjectType, ProfileObjectType

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
        owner_id = graphene.ID(required=True)
        description = graphene.String()
        categories = graphene.List(graphene.String)

    new_profile = graphene.Field(ProfileObjectType)

    @login_required
    def mutate(self, info, owner_id, description, categories):
        get_owner = User.objects.get(id=owner_id)
        if get_owner:
            new_profile = Profile.objects.create(owner=get_owner, description=description, categories=categories)
            return CreateProfileMutation(new_profile=new_profile)
        return CreateProfileMutation(new_profile=None)




class Mutation(graphene.ObjectType):
    signup = SignupMutation.Field()
    edit_user = EditUserMutation.Field()
    create_profile = CreateProfileMutation.Field()