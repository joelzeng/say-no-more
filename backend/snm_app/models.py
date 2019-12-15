from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=256)

class Account(models.Model):
	name = models.CharField(max_length=256)
	balance = models.IntegerField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)