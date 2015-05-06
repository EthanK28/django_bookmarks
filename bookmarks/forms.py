# encoding: utf-8

__author__ = 'es-mac'



from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
  username = forms.CharField(label='Username', max_length=30)
  email = forms.EmailField(label='Email')
  password1 = forms.CharField(
    label='비밀번호',
    widget=forms.PasswordInput()
  )
  password2 = forms.CharField(
    label='Password (Again)',
    widget=forms.PasswordInput()
  )

  def cleaned_password2(self):
    if 'password1' in self.clean_data:
      password1 = self.clean_data['password1']
      password2 = self.clean_data['password2']
      if password1 == password2:
        return password2
    raise forms.ValidationError('Passwords do not match.')

def clean_username(self):
  username = self.cleaned_data['username']
  if not re.search(r'^\w+$', username):
    raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
  try:
    User.objects.get(username=username)
  except ObjectDoesNotExist:
    return username
  raise forms.ValidationError('Username is already taken.')

class BookmarkSaveForm(forms.Form):
  url = forms.URLField(
    label='URL',
    widget=forms.TextInput(attrs={'size': 64})
)
  title = forms.CharField(
    label='Title',
    widget=forms.TextInput(attrs={'size': 64})
)
  tags = forms.CharField(
    label='Tags',
    required=False,
    widget=forms.TextInput(attrs={'size': 64})
)

  share = forms.BooleanField(
    label='Share on the main page',
    required=False
)


class SearchForm(forms.Form):
  query = forms.CharField(
    label='Enter a keyword to search for',
    widget=forms.TextInput(attrs={'size': 32})
  )





