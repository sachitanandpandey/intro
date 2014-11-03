from django.contrib.auth.models import User
from django.forms import ModelForm
from member.models import Member
from django import forms
import re

#class RegistrationForm(ModelForm):
class RegistrationForm(forms.Form):
    name                =forms.CharField(label=(u'Name'))
    username            =forms.CharField(label=(u'User Name'))
    email               =forms.EmailField(label=(u'Email Address'))
    password            =forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password1           =forms.CharField(label=(u'Verify Password'),widget=forms.PasswordInput(render_value=False))


    class Meta:
        model = Member
        exclude = ('user',)


    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
#            return username
            return self.cleaned_data['username']
        raise forms.ValidationError("Username is not available please Try again")


    def clean(self):
        password = self.cleaned_data['password']
        password1 = self.cleaned_data ['password1']
        if password != password1:
            raise forms.ValidationError("Password did not matched")
        return self.cleaned_data


class LoginForm(forms.Form):
    username            = forms.CharField(label=(u'User Name'))
    password            = forms.CharField(label=(u'Password'),widget=forms.PasswordInput(render_value=False))