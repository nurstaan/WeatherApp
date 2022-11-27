from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length = 30, verbose_name = 'Имя города')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Города'
        verbose_name_plural = 'Поселки'
