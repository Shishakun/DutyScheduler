from django.forms import ModelForm

from . models import Office

class OfficeForm(ModelForm):
    class Meta:
        model = Office
        fields= '__all__'