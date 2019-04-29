
from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
     name = forms.CharField(label='Nome')
     email = forms.EmailField(label='E-mail')
     mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)

     def sendEmail(self):
         name = self.cleaned_data['name']
         email = self.cleaned_data['email']
         message = self.cleaned_data['mensagem']
         message = 'Nome: {0}\nE-mail: {1}\n{2}'.format(name,email,message)
         send_mail('Contato do Django E-Commerce', message, settings.DEFAULT_FROM_EMAIL,
                     [settings.DEFAULT_FROM_EMAIL])
