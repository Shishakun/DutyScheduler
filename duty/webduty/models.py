from django.db import models
from django.urls import reverse
   
class Duty(models.Model):
    name = models.TextField('Название наряда', max_length= 100)
    ratio = models.FloatField('Коэффициент',default="")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Наряд по"
        verbose_name_plural = "Наряд по"

class Office(models.Model):
    name = models.TextField('Фамилия Имя',max_length=100)
    rank = models.TextField('Звание',max_length=30)
    number = models.TextField(verbose_name="Факультет",max_length=30)
    url = models.SlugField(max_length=150,unique=True)
    
    def __str__(self):
        return self.name

    def get_all_objects(self):
        queryset = self._meta.model.objects.all()
        return queryset
        
    class Meta:
        verbose_name = "Офицер"
        verbose_name_plural = "Офицеры"

