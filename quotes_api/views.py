from django.shortcuts import render
from .models import Quote
from rest_framework import viewsets
from .serializers import QuoteSerializers


# Create your views here.
class QuotesView(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializers

