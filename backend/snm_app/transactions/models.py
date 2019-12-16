from django.conf import settings
from django.db import models
from snm_app.models import Account

class Transaction(models.Model):
	name = models.CharField(max_length=256)
	amount = models.IntegerField()
	sender = models.ForeignKey(
		Account,
		on_delete=models.CASCADE,
		related_name='sender'
	)
	recipient = models.ForeignKey(
		Account,
		on_delete=models.CASCADE,
		related_name='recipient'
	)