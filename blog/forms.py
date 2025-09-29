from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем классы Bootstrap для стилизации
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем классы form-control ко всем полям для единообразия
        for field_name, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
            # Добавляем placeholder для улучшения UX
            if field_name == 'title':
                field.widget.attrs['placeholder'] = 'Введите заголовок поста'
            elif field_name == 'content':
                field.widget.attrs['placeholder'] = 'Напишите содержание вашего поста здесь...'
                field.widget.attrs['rows'] = 10  # Устанавливаем высоту текстового поля