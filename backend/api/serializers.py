from rest_framework import serializers
from market.models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('sn', 'company', 'prevclosep', 'closep', 'diff',)