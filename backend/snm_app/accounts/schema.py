import graphene
from graphql import GraphQLError
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from snm_app.users.schema import UserType

from .models import Account

class AccountType(DjangoObjectType):
	class Meta:
		model = Account


class Query(graphene.ObjectType):
	accounts = graphene.List(AccountType)

	def resolve_accounts(self, info, **kwargs):
		return Account.objects.all()


class CreateAccount(graphene.Mutation):
	name = graphene.String()
	balance = graphene.Int()
	user = graphene.Field(UserType)

	class Arguments:
		name = graphene.String(required=True)
		balance = graphene.Int()

	def mutate(self, info, name, balance):
		user = info.context.user
		if user.is_anonymous:
			raise GraphQLError("You must be logged in")
		account = Account(
			name=name,
			balance=balance,
			user=user
		)
		account.save()
		return CreateAccount(
			name=account.name,
			balance=account.balance,
			user=user
		)


class Mutation(graphene.ObjectType):
	create_account = CreateAccount.Field()

