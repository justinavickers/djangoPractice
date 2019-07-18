from django.conf import settings

from django.db import models

class Kitchen_layout(models.Model):

   fridge_brand = models.TextField()

   range_brand = models.TextField()

   description = models.TextField()


   def __str__(self):

       return self.description
