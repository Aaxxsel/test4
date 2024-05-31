from django import forms
from .models import PostSite


class PostForm(forms.ModelForm):
    class Meta:
        model = PostSite
        fields = ['title', 'text']
        labels = {
            'title': 'Введите Заголовок',
            'text': 'Введите Текст'
        }
