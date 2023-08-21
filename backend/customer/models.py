from django.db import models
from country.models import Country
from .choices import OPTION_CLERKS, OPTION_COLLECTOR, OPTION_CUSTOMER_GROUP
from PIL import Image


class PayerGroup(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Payer Group'
        verbose_name_plural = '1. Payer Groups'
    

class Customer(models.Model):
    OPTION_CHANNEL = [
        ('ON-TRADE','On Trade'),
        ('OFF-TRADE','Off Trade'),
    ]

    OPTION_GENDER = [
        ('WOMAN','Woman'),
        ('MAN','Man'),
    ]
        
    payer = models.IntegerField(unique=True, blank=True, null=True)
    vendor_id = models.IntegerField(blank=True, null=True)
    payer_name = models.CharField(max_length=100)
    payer_group = models.ForeignKey(PayerGroup, on_delete=models.CASCADE, blank=True, null=True)
    clerk = models.CharField(max_length=100, choices=OPTION_CLERKS)
    channel = models.CharField(max_length=100, choices=OPTION_CHANNEL)
    collector = models.CharField(max_length=100, choices=OPTION_COLLECTOR)
    contact_name = models.CharField(max_length=100, blank=True)
    contact_surname = models.CharField(max_length=100,blank=True)
    contact_gender = models.CharField(max_length=100, choices=OPTION_GENDER, blank=True)
    phone_num = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=300, blank=True,default="")
    edi = models.BooleanField(default=False)
    logo = models.ImageField(default='default_cust.jpg', upload_to='customer_pics', blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.payer_name
    
    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)

        img = Image.open(self.logo.path)
        if img.height >300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.logo.path)

    class Meta:
        verbose_name = 'Payer'
        verbose_name_plural = '2. Payers'