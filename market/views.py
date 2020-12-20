from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from .models import Stock
import json

# Create your views here.
# class SharePriceView(ListView):
#     model = Stock
#     template_name = "shareprice.html"

def SharePriceView(request):
    page = request.GET.get('page') or 1
    date = request.GET.get('date')
    company = request.GET.get('company')
    rows = request.GET.get('rows') or 30
    year, month, day = None, None, None
    if date:
        year, month, day = date.split('-')
        objects = Stock.objects.filter(date_saved__year=year, date_saved__day=19, date_saved__month=month)
    else:
        day = 19
        objects = Stock.objects.filter(date_saved__day=day)
    
    paginator = Paginator(objects, rows)
    page_obj = paginator.get_page(page)

    return render(request, 'shareprice.html', context={'object_list': objects, 'page_obj':  page_obj})


def ShareDetailView(request, sn: int):
    object = Stock.objects.filter(sn=sn)[0]
    return render(request, 'sharedetail.html', context={'object': object})
