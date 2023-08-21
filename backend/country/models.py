from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    abbrevation = models.CharField(max_length=2)
    language = models.CharField(max_length=20)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = '1. Countries'
