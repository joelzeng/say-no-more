from django.conf import settings
from django.db import models

class Account(models.Model):
	name = models.CharField(max_length=256)
	balance = models.IntegerField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)