from django.shortcuts import render, get_object_or_404
from .models import Card
from .forms import ContactCard

def index(request):
    cards = Card.objects.all()
    template_name = 'cards/index.html'
    context = {
        'cards': cards
    }
    return render(request, template_name, context)

def review(request, slug):
    card = get_object_or_404(Card, slug=slug)
    if request.method == 'POST':
        form = ContactCard(request.POST)
    else:
        form = ContactCard()
    template_name = 'cards/review.html'
    context = {
        'card': card,
        'form': form
    }
    return render(request, template_name, context)
