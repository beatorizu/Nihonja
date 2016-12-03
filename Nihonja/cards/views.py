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
    context = {}
    if request.method == 'POST':
        form = ContactCard(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(card)
            form = ContactCard()
    else:
        form = ContactCard()
    template_name = 'cards/review.html'
    context['card'] = card
    context['form'] = form
    return render(request, template_name, context)
