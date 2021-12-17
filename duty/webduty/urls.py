from django.urls import path
from .views import OfficeListView
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('officerslist/',OfficeListView.as_view(), name="list_detail"),
]
