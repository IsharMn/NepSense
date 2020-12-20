from django.urls import path
from .views import SharePriceView, ShareDetailView

urlpatterns = [
    path('', SharePriceView, name='shareprice'),
    path('filter/', SharePriceView, name='shareprice filter'),
    path('detail/<int:sn>', ShareDetailView, name='share detail'),

]