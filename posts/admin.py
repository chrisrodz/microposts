from django.contrib import admin
from posts.models import Post, Follower

admin.site.register(Post)
admin.site.register(Follower)