from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from .models import ChatMessage


class LoginForm(AuthenticationForm):
    class Meta:
        fields = ["__all__"]

class ChatMessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "forms", "rows":3, "placeholder": "Type in your "
                                                                                                   "message"}))

    class Meta:
        model = ChatMessage
        fields = [
            "body",
        ]
