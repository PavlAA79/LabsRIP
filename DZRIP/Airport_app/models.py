from django.db import models
from datetime import date

from django.urls import reverse


class Plane(models.Model):
    """Самолеты"""
    name = models.CharField("Модель", max_length=50)
    seats = models.IntegerField("Количество мест",default = 0)
    cruising_speed = models.IntegerField("Крейсерская скорость",default = 0)
    flight_range = models.IntegerField("Дальность полета",default = 0)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Самолет"
        verbose_name_plural = "Самолеты"


class Flight(models.Model):
    """Рейсы"""
    departure_airport = models.CharField("Аэропорт вылета", max_length=100)
    data = models.DateField("Дата")
    time = models.TimeField("Время")
    status = models.TextField("Статус")
    planes = models.ManyToManyField(Plane, verbose_name="Самолет", related_name="plane_flight")

    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.departure_airport

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Рейс"
        verbose_name_plural = "Рейсы"