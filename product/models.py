from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.CharField(max_length=100)
	quantity = models.IntegerField(blank=True, null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)

