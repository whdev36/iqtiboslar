from django.shortcuts import render
from .models import Quote
import random

# Home view
def home_view(request):
    quotes = Quote.objects.all()
    random_quote = random.choice(quotes) if quotes else None
    return render(request, 'home.html', {'quote': random_quote})
