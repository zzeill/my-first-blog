from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)


class RegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

