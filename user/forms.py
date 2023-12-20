from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets


class CreateUser(UserCreationForm):
  name = forms.CharField(max_length=30)
  surname = forms.CharField(max_length=50)

  class Meta:
    model = User
    fields = ('name','surname','username','email')

  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)

    for fieldname in ['name','surname','username','email','password1','password2']:
      self.fields[fieldname].help_text = None

    self.fields['name'].widget = widgets.TextInput(attrs={'class':"block px-2 w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6","placeholder":"isim"})
    self.fields['surname'].widget = widgets.TextInput(attrs={"class":"block px-2 w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6","placeholder":"soyisim"})
    self.fields['username'].widget = widgets.TextInput(attrs={"class":"block px-2 w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6","placeholder":"kullanıcı adı"})
    self.fields['email'].widget = widgets.EmailInput(attrs={'class':"block px-2 w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6","placeholder":"email"})
    self.fields['password1'].widget = widgets.PasswordInput(attrs={"class":"block px-2 w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6","placeholder":"şifre"})
    self.fields['password2'].widget = widgets.PasswordInput(attrs={"class":"block px-2 w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6","placeholder":"şifre tekrar"})


class LoginUser(forms.Form):
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"block px-2 w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6","placeholder":"email"}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"block px-2 w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6","placeholder":"şifre"}))

  def clean_email(self,*args,**kwargs):
    email = self.cleaned_data.get('email')
    if not User.objects.filter(email = email).exists():
      self.add_error(email, "Bu email mevcut değil")
    return email