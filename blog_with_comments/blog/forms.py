from django import forms
from .models import Blogpost,Comment

class BlogpostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = '__all__'
        labels = {
            'title': 'Enter the title:',
            'author': 'Enter your name:',
            'content': 'Enter the post:',
        }
        error_messages = {
            'author': {
                'required' : 'Your name must not be empty!',
                'max_length' : 'Please enter a shorter name!',
                }
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['parent']
        labels = {
            'title': 'Enter the title:',
            'author': 'Enter your name:',
            'content': 'Enter your comment:',
        }
        error_messages = {
            'author': {
                'required' : 'Your name must not be empty!',
                'max_length' : 'Please enter a shorter name!',
                }
        }