from django import forms
from django.forms import ModelForm
from chatApp.models import ChatMessage

class ChatMessageForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'forms',
        'rows' : 3,
        'cols' : 8,
        'placeholder' : 'Type message here'
    }))
    class Meta:
        model = ChatMessage
        fields = ["body",]
