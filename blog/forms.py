from .models import Post, Comment
from django import forms


class BlogPost(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ("category", "subject")
        fields = ["category", "subject", "content", "image"]


class BlogComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
