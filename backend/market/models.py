from django.db import models
from django.urls import reverse

# Create your models here.
class Stock(models.Model):
    company = models.CharField(max_length=250)
    symbol = models.CharField(max_length=25, null=True)
    transno = models.PositiveIntegerField()
    maxp = models.PositiveIntegerField()
    minp = models.PositiveIntegerField()
    closep = models.PositiveIntegerField()
    tradedshares = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    prevclosep = models.PositiveIntegerField()
    diff = models.IntegerField()
    date_saved = models.DateTimeField(auto_now_add=True)
    sn = models.IntegerField()

    def __str__(self):
        return str(self.company)
    

class FloorSheet(models.Model):
    contractnum = models.BigIntegerField()
    symbol = models.CharField(max_length=25)
    buyerbroker = models.IntegerField()
    sellerbroker = models.IntegerField()
    quantity = models.IntegerField()
    rate = models.IntegerField()
    amount = models.FloatField()
    date_saved = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.contractnum)

class CompanyList(models.Model):
    name = models.CharField(unique=True, max_length=100, blank=True, null=True)
    symbol = models.CharField(unique=True, max_length=20, blank=True, null=True)
    sector = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        db_table = 'company_list'
