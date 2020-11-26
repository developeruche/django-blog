from django import forms
from .models import Post, Category, Comment


choices = Category.objects.all().values_list('name', 'name')

choices_list = [i for i in choices]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author',
                  'category', 'header_image', 'body', 'post_snippet')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'user',
                'type': 'hidden'
            }),
            # 'author': forms.Select(attrs={
            #     'class': 'form-control'
            # }),
            'category': forms.Select(choices=choices_list, attrs={
                'class': 'form-control'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'post_snippet': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'This field would be displayed at the home page of the blog so context should be something that relates the blog podt to the visitors...'
            }),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'header_image', 'body', 'post_snippet')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'post_snippet': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'This field would be displayed at the home page of the blog so context should be something that relates the blog podt to the visitors...'
            }),
        }

class MakeCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }
