from django import template
from django.db.models.fields import SlugField
from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
from django.template import RequestContext

from .forms import OfficeForm
from .models import Office

from loguru import logger

class OfficeMain:
    def get_office(self):
        return Office.objects.all()

    
class OfficeListView(OfficeMain,generic.ListView):
    model=Office
    queryset=Office.objects.all()
    template_name="webduty/list.html"

def index2(request):
    get_office = Office.objects.all()
    return render(request,'webduty/list_detail.html',{'get_office': get_office})

def index3(request):
    get_office = Office.objects.all()
    return render(request,'webduty/raspred.html',{'get_office': get_office})

# def form(request):
#     form = OfficeForm()
#     if request.method=='POST':
#         form=OfficeForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {'form':form}