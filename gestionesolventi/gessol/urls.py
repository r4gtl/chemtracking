from django.urls import path
from .views import current_datetime, home, SupplierListView


urlpatterns = [
    path('prova/', current_datetime, name='date-time'),
    path('home/', home, name='homeview'),
    path('suppliers/', SupplierListView.as_view(), name='suppliers_list')
]
