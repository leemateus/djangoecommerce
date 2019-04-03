
from django import forms

class ContactForm(forms.Form):
     name = forms.CharField(label='Nome')
     email = forms.EmailField(label='E-mail')
     mensagem = forms.CharField(label='Mesagem', widget=forms.Textarea)
