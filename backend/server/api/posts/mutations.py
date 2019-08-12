import graphene
from graphql_jwt.decorators import login_required
from server.api.models import Post
from .types import PostObjectType

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


class RemovePostMutation(graphene.Mutation):
    class Arguments:
        post_id = graphene.ID(required=True)

    success = graphene.Boolean()

    @login_required
    def mutate(self, info, post_id):
        Post.objects.get(id=post_id).delete()
        return RemovePostMutation(success=True)


class EditPostMutation(graphene.Mutation):
    class Arguments:
        post_id = graphene.ID(required=True)
        title = graphene.String()
        text = graphene.String()

    updated_post = graphene.Field(PostObjectType)

    @login_required
    def mutate(self, info, *args, **kwargs):
        post_id = kwargs.pop('post_id')
        target_post = Post.objects.get(id=post_id)

        try:
            for (key, value) in kwargs.items():
                setattr(target_post, key, value)
        except:
            raise Exception('Invalid post update field')

        target_post.save()

        return EditPostMutation(updated_post=target_post)
        

class Mutation(graphene.ObjectType):
    create_post = CreatePostMutation.Field()
    remove_post = RemovePostMutation.Field()
    edit_post = EditPostMutation.Field()