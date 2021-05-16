from django import forms
#from views import add_to_base
from django.core.exceptions import ValidationError

from .models import *
class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'analysis', 'problem', 'shortdescription', 'description', 'curator']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 45:
            raise ValidationError('Длина превышает 45 символов')
            print('error')
        else:
            print('lol')
        return title


