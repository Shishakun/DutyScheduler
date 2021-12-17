from django.db import models
from django.urls import reverse


class Rank(models.Model):
    rank = models.TextField('Звание')
    def __str__(self):
        return self.rank

    class Meta:
        verbose_name = "Звание"
        verbose_name_plural = "Звания"

class Fakultet(models.Model):
    number = models.TextField('Факультет')
    descriptions = models.TextField("Описание", max_length= 100,default="")
    url = models.SlugField(max_length=150,unique=True)
    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"
    


class Office(models.Model):
    name = models.TextField('Имя',max_length=100)
    surname = models.TextField('Фамилия',max_length=100,default = "")
    rank = models.ManyToManyField(Rank,'Звание',max_length=30)
    number = models.ManyToManyField(Fakultet,verbose_name="Факультет")
    url = models.SlugField(max_length=150,unique=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("list_detail.html", kwargs={"slug": self. url})

    class Meta:
        verbose_name = "Офицер"
        verbose_name_plural = "Офицеры"

