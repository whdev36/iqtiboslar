from django.shortcuts import render
from .models import Quote

# Home view
def home_view(request):
    quotes = Quote.objects.all()
    return render(request, 'home.html', {'quotes': quotes})
