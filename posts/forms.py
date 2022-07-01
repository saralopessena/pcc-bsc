from django import forms
from posts.models import Posts, Comments


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'description', 'link_img']

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']