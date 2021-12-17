from django import template
from django.db.models.fields import SlugField
from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
from django.template import RequestContext

from .forms import OfficeForm
from .models import Office,Rank,Fakultet

from loguru import logger



def index(request):
    return render(request, 'webduty/list.html') 

class OfficeAll:
    def get_office(self):
        return Office.objects.all

class OfficeListView(OfficeAll,generic.ListView):
    model=Office
    queryset = Office.objects.all()
    template_name = "webduty/list_detail.html"
    
    

def form(request):
    form = OfficeForm()
    if request.method=='POST':
        form=OfficeForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}