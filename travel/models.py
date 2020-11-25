from django.db import models

# Create your models here.
class travelling(models.Model):
    location    = models.CharField(max_length=20)
    description = models.TextField()
    price       = models.DecimalField(max_digits=5,decimal_places=2)
    available   = models.IntegerField()
    offer       = models.BooleanField(default=False)
    image       = models.ImageField(upload_to='pics')