from django import forms
from .models import Post,Comment

class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        exclude= ['author']
        
        
        
class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ['name','email','body']