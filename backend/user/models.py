from django.db import models
from django.contrib.auth.models import User
from deduction.models import Deductions
from PIL import Image
from customer.choices import OPTION_CLERKS, OPTION_COLLECTOR, OPTION_CUSTOMER_GROUP, OPTION_STATUS
from customer.models import PayerGroup
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission



class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=OPTION_STATUS, blank=True, default='Open')
    collector = models.CharField(max_length=100, choices=OPTION_COLLECTOR, blank=True,null=True)    
    payer_group = models.ForeignKey(PayerGroup, on_delete=models.SET_NULL, blank=True, null=True)  # Add the payer_group field
    
    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name}'s Settings"
    

    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = '1. Settings'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} Profile"
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height >300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = '2. Profiles'

