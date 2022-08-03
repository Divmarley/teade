from django.db import models

# Create your models here.
class Track(models.Model):
    user = models.CharField(max_length=400)
    tracking_id=models.CharField(max_length=30)
    deposit_number =models.CharField(max_length=30)
    reference_number= models.CharField(max_length=30)
