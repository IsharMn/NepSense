from django.db import models
from django.urls import reverse

# Create your models here.
class Stock(models.Model):
    company = models.CharField(max_length=250)
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
        return self.company
    