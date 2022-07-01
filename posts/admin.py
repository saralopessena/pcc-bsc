from django.contrib import admin
from posts.models import Posts, Comments
from posts.forms import PostsForm
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget 


class PostsAdmin(admin.ModelAdmin):
    form = PostsForm


admin.site.register(Posts)
admin.site.register(Comments)