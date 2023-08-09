from .models import Post
from django import forms


class BlogPost(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ("category", "subject")
        fields = "__all__"
