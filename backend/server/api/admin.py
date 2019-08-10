from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Post, Comment, Profile


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Information', {'fields': ['username', 'email', ]}),
        ('Location', {'fields': ['latitude',
                                 'longitude', 'search_distance', ]}),
        ('Account Type', {'fields': ['account_type', ]})
    ]
    list_display = ('username', 'id', 'last_login',
                    'date_joined', 'email', 'account_type',)

admin.site.unregister(Group)

admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
