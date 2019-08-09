from django.db import models
from django.utils import timezone

# Create your models here.
class Building(models.Model) :
    room_name = models.TextField(default='name')
    tele_num = models.TextField(default='number')
    address = models.TextField(default='address')
    room_img = models.ImageField(upload_to='images/',blank=True)
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return self.room_name

class Address(models.Model):
    add = models.TextField(default='address')

    def __str__(self):
        return self.add