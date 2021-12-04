"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from app.models import Chat, Question
from django.core import validators
from django.core.exceptions import ValidationError

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class RegisterForm(UserCreationForm):
    '''def validate_email(value):
        if value.endswith('@mylaurier.com'):
            raise forms.ValidationError("invalid email")
    def clean(self):
        raise forms.ValidationError({"email": "raise an error"})'''

    

    email = forms.EmailField()
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@mylaurier.ca'):
            raise forms.ValidationError({"email": "raise an error"})
        return email

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
  

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('name', 'message', )
        widget = {'message' : forms.TextInput(attrs={'class' : 'w-75'}) }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('name', 'question', )
        

class AnswerForm(forms.Form):
    id = forms.IntegerField(min_value=1)
    answer = forms.CharField(max_length=1000)
    name = forms.CharField(max_length=1000)

