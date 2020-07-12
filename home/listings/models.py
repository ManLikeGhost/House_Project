from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length= 200 )
    address = models.CharField(max_length= 200 )
    city = models.CharField(max_length= 100 )
    state = models.CharField(max_length= 100 )
    zipcode = models.CharField(max_length= 100 )
    description = models.TextField(blank=True )
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1) 
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%d/%m/%Y')
    photo_main_1 = models.ImageField(upload_to='photos/%d/%m/%Y', blank=True)
    photo_main_2 = models.ImageField(upload_to='photos/%d/%m/%Y', blank=True)
    photo_main_3 = models.ImageField(upload_to='photos/%d/%m/%Y', blank=True)
    photo_main_4 = models.ImageField(upload_to='photos/%d/%m/%Y', blank=True)
    photo_main_5 = models.ImageField(upload_to='photos/%d/%m/%Y', blank=True)
    photo_main_6 = models.ImageField(upload_to='photos/%d/%m/%Y', blank=True)
    photo_main_7 = models.ImageField(upload_to='photos/%d/%m/%Y', blank=True)
    photo_main_8 = models.ImageField(upload_to='photos/%d/%m/%Y', blank=True)
    photo_main_9 = models.ImageField(upload_to='photos/%d/%m/%Y', blank=True)
    photo_main_10 = models.ImageField(upload_to='photos/%d/%m/%Y', blank=True)
    photo_main_11 = models.ImageField(upload_to='photos/%d/%m/%Y', blank=True)
    photo_main_12 = models.ImageField(upload_to='photos/%d/%m/%Y', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    
    
    def __str__(self):
        return self.title