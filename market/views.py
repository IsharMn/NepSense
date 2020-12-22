from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.core.serializers import serialize

from .models import Stock
import json

# Create your views here.
# class SharePriceView(ListView):
#     model = Stock
#     template_name = "shareprice.html"

expected_date = None

def SharePriceView(request):
    page = request.GET.get('page') or 1
    date = request.GET.get('date')
    company = request.GET.get('company')
    rows = request.GET.get('rows') or 24
    if not date:
        with open('updated_date') as f:
            date = f.readline().strip()
    year, month, day = date.split('-')
    global expected_date
    expected_date = year, month, day
    objects = Stock.objects.filter(date_saved__year=year, date_saved__day=day, date_saved__month=month)
    
    paginator = Paginator(objects, rows)
    page_obj = paginator.get_page(page)

    return render(request, 'shareprice.html', context={'object_list': objects, 'page_obj':  page_obj})


def ShareDetailView(request, sn: int):
    objects = Stock.objects.filter(sn=sn)
    filtered_date = request.GET.get('date')
    if filtered_date:
        date = filtered_date.split('-')
        if obj := Stock.objects.filter(date_saved__year=date[0], date_saved__month=date[1],
                                    date_saved__day=date[2], sn=sn):
            obj = obj[0]
        
    else:
        if not expected_date:
            obj = objects[0]
        else:
            date = expected_date
            obj = Stock.objects.filter(date_saved__year=date[0], date_saved__month=date[1],
                                            date_saved__day=date[2], sn=sn)[0]

    ser_objects = serialize('json', objects)
    return render(request, 'sharedetail.html', context={'object': obj, 'objects': ser_objects})
