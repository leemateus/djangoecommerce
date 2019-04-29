from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.views.generic import View, TemplateView

# def index(request):
#
#     return render(request, 'index.html', {})

class indexView(View):
    def get(self, request):
        return render(request, 'index.html')

    template_name = 'index.html'

index = indexView.as_view()


def contact(request):
    return render(request, 'contact.html', {})


def product(request):
    return render(request, 'product.html', {})

def contact(request):
    seucesso = False
    form = ContactForm(request.POST or None)
    if(form.is_valid()):
        ContactForm.sendEmail(form)
        secesso = True

    context = {
        'form' : form
    }
    return render(request, 'contact.html', context)
