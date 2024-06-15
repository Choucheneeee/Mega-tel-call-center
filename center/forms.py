from django.forms import ModelForm, Textarea
from django import forms
from .models import GroupMessage

class ChatmessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Add message...', 'class': 'form-control', 'rows': 3, 'autofocus': True}),
        }
