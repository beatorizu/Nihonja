from django.shortcuts import render
from .models import Card

def index(request):
    cards = Card.objects.all()
    template_name = 'cards/index.html'
    context = {
        'cards': cards
    }
    return render(request, template_name, context)

def review(request, pk):
    card = Card.objects.get(pk=pk)
    template_name = 'cards/review.html'
    context = {
        'card': card
    }
    return render(request, template_name, context)
