from django.forms import widgets
from django import forms
from .models import Post,Yorum

class PostForm(forms.ModelForm):
  tags = forms.CharField(required=False)
  class Meta:
    model = Post
    fields = ['title','content', 'image','tags']

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['title'].widget = widgets.TextInput(attrs={"class":"block w-full text-white rounded-md border-0 px-3 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-indigo-600 placeholder:text-gray-400 bg-transparent focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6","placeholder":"Konu başlığı"})
    self.fields['content'].widget = forms.Textarea(attrs={"class":"block w-full text-white rounded-md border-0 px-3 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-indigo-600 placeholder:text-gray-400 bg-transparent focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6","placeholder":"Neler oluyor?","rows":"3"})
    self.fields['image'].widget.attrs['class'] = 'custom-css-class'




class YorumForm(forms.ModelForm):
  class Meta:
    model = Yorum
    fields = ['content', 'image']

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['content'].widget = forms.Textarea(attrs={"class":"block w-full text-white rounded-md border-0 px-3 py-1.5 text-gray-900 shadow-sm focus:outline-none placeholder:text-gray-400 bg-transparent focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6","placeholder":"Yanıtını gönder","rows":"3"})
    self.fields['image'].widget.attrs['class'] = 'custom-css-class'