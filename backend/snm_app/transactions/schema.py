import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from snm_app.accounts.schema import AccountType

from .models import Transaction, Account

class TransactionAccount(DjangoObjectType):
	class Meta:
		model = Transaction


class Query(graphene.ObjectType):
	accounts = graphene.List(AccountType)

	def resolve_transactions(self, info, **kwargs):
		return Transaction.objects.all()


class CreateAccount(graphene.Mutation):
	name = graphene.String()
	amount = graphene.Int()
	sender = graphene.Field(AccountType)
	recipient = graphene.Field(AccountType)

	class Arguments:
		name = graphene.String(required=True)
		amount = graphene.Int()

	def mutate(self, info, name, amount, sender_id, recipient_id):
		if not info.context.user.is_authenticated:
			return CreateTransaction(
				errors=json.dumps("user not authenticated")
			)
		sender = Account.objects.filter(id=sender_id)
		recipient = Account.objects.filter(id=recipient_id)
		transaction = Transaction(
			name=name,
			amount=amount,
			sender=sender,
			recipient=recipient,
		)
		transaction.save()
		return CreateTransaction(
			name=transaction.name,
			balance=transaction.balance,
			sender=transaction.sender,
			recipient=transaction.recipient
		)


class Mutation(graphene.ObjectType):
	create_account = CreateTransaction.Field()

