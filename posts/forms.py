from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('url' ,'body')
        widgets = {
            'url': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Введите ссылку на фликер'}),
            'body': forms.Textarea(attrs={'class': 'input',
                                          'placeholder': 'Описание для вашего поста',
                                          'rows': 2, 'cols': 20,
                                          'class': 'font1 text-4xl'}),
        }


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', )
        labels = {
            'body' : '',

        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'class': 'font1 text-4xl'}),
        }