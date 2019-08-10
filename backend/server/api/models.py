from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField
from .managers import ProfileManager, PostManager

CREATOR = 'creator'
VIEWER = 'viewer'

ACCOUNT_TYPE = ((CREATOR, 'Creator'), (VIEWER, 'Viewer'))


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True, blank=False, null=False, validators=[
                                MinLengthValidator(6, message='Username must be at least 6 characters')])
    email = models.EmailField(unique=True, blank=False, null=False)
    account_type = models.CharField(
        max_length=20, choices=ACCOUNT_TYPE, default=VIEWER)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, default=40.7128, validators=[
                                   MinValueValidator(1.00, message='Not a valid latitude')])
    longitude = models.DecimalField(max_digits=8, decimal_places=6, default=74.0060, validators=[
                                    MinValueValidator(1.00, message='Not a valid longitude')])
    search_distance = models.IntegerField(default=5, validators=[
                                          MinValueValidator(1, message='Not a valid search distance')])

    def __str__(self):
        return F'User: {self.id}-{self.username}'


class Post(models.Model):
    objects = PostManager()
    owner = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    text = models.CharField(max_length=300, blank=False, null=False)

    def __str__(self):
        return F'Post {self.id} by {self.owner.username}'

class Comment(models.Model):
    owner = models.ForeignKey('User', on_delete=models.CASCADE)
    posts = models.ForeignKey('Post', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=300, blank=False, null=False)

    def __str__(self):
        return F'Comment {self.id}'


class Profile(models.Model):
    objects = ProfileManager()
    owner = models.ForeignKey('User', on_delete=models.CASCADE)
    description = models.TextField(max_length=300, null=False, blank=False)
    categories = ArrayField(models.CharField(
        max_length=100, blank=False, null=False), default=list)

    @property
    def profile_posts(self):
        return Profile.objects.get_profile_posts(id=self.owner.id)

    def __str__(self):
        return F'Profile {self.owner.username}'
