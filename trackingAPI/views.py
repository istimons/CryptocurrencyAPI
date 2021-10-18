from django.shortcuts import render
from rest_framework import generics
from .models import Cryptocurrency
from .serializers import CryptocurrencySerializer

# create your views here


class ListCryptocurrencyView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer

def show_data(request):
    data = Cryptocurrency.objects
    return render(request, 'cryptocurrencytrack/home.html', {'cryptocurrencytrack': data})

