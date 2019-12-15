import uuid
from django.db import models

# Create your models here.
class User(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=256)

class Account(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=256)
	balance = models.IntegerField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)