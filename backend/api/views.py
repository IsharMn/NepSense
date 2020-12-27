from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import StockSerializer
from market.models import Stock

# Create your views here.
class StockListView(ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
