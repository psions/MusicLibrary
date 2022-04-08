from django.contrib import admin
from .models import Music
from.models import Post,Like

# Register your models here.
admin.site.register(Music)
admin.site.register(Post)
admin.site.register(Like)