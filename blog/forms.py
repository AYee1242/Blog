from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]


class SignInForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
