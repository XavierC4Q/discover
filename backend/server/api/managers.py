from django.db import models


class ProfileManager(models.Manager):

    def get_profile_posts(self, id):
        from .models import Post
        posts = Post.objects.filter(owner__id=id)
        return posts


class PostManager(models.Manager):
    
    def get_posts_comments(self, id):
        from .models import Comment
        comments = Comment.objects.filter(posts__id=id)
        return comments
