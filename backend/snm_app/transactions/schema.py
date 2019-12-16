import graphene
from graphql import GraphQLError
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from django.db.models import Q
from snm_app.accounts.schema import AccountType

from .models import Transaction, Account

class TransactionType(DjangoObjectType):
	class Meta:
		model = Transaction


class Query(graphene.ObjectType):
	transactions = graphene.List(
		TransactionType,
		search=graphene.String(),
		first=graphene.Int(),
		skip=graphene.Int(),
	)

	def resolve_transactions(self, info, search=None, first=None, skip=None, **kwargs):
		query_set = Transaction.objects.all()
		if search:
			filter = Q(name__icontains=search)
			query_set = query_set.filter(filter)
		if first:
			query_set = query_set[:first]
		if skip:
			query_set = query_set[skip:]
		return query_set


class CreateTransaction(graphene.Mutation):
	name = graphene.String()
	amount = graphene.Int()
	sender = graphene.Field(AccountType)
	recipient = graphene.Field(AccountType)

	class Arguments:
		name = graphene.String(required=True)
		amount = graphene.Int()
		sender_id = graphene.Int()
		recipient_id = graphene.Int()

	def mutate(self, info, name, amount, sender_id, recipient_id):
		if info.context.user.is_anonymous:
			raise GraphQLError("You must be logged in")
		sender = Account.objects.get(id=sender_id)
		recipient = Account.objects.get(id=recipient_id)
		if not sender or not recipient:
			raise Exception('Invalid sender or recipient')
		transaction = Transaction(
			name=name,
			amount=amount,
			sender=sender,
			recipient=recipient,
		)
		transaction.save()
		return CreateTransaction(
			name=transaction.name,
			amount=transaction.amount,
			sender=transaction.sender,
			recipient=transaction.recipient
		)


class Mutation(graphene.ObjectType):
	create_transaction = CreateTransaction.Field()

