from django import forms
from .models import Contact, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            "type": "text",
            "class": "form-control",
            "placeholder": "Your Name"
        })
        self.fields['email'].widget.attrs.update({
            "type": "text",
            "class": "form-control",
            "placeholder": "Your Email"
        })
        self.fields['subject'].widget.attrs.update({
            "type": "text",
            "class": "form-control",
            "placeholder": "Subject"
        })
        self.fields['message'].widget.attrs.update({
            "cols": 30,
            "rows": 7,
            "class": "form-control",
            "placeholder": "Message"
        })


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'article', 'description')
        exclude = ('author', 'article')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({
            "class": "form_group",
            "cols": 50,
            "rows": 7,
            "id": "message",
            "textarea": "textarea",
        })


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=221, help_text='Enter a valid email text')

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
