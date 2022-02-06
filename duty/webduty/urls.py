from django.urls import path
from .views import OfficeListView
from . import views
urlpatterns = [
    path('', OfficeListView.as_view()),
    path('officers/',views.index2, name="index2"),
    path('raspred/',views.index3, name="index3" ),
]
