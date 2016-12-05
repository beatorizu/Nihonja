from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactCard

def home(request):
    return render(request, 'home.html')

def contact(request):
    context = {}
    if request.method == 'POST':
        form = ContactCard(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(card)
            form = ContactCard()
    else:
        form = ContactCard()
    template_name = 'contact.html'
    context['form'] = form
    return render(request, template_name, context)
