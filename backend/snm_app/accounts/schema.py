import graphene
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
		if not info.context.user.is_authenticated:
			return CreateAccount(
				errors=json.dumps("user not authenticated")
			)
		account = Account(
			name=name,
			balance=balance,
			user=info.context.user
		)
		account.save()
		return CreateAccount(
			name=account.name,
			balance=balance.name,
			user=info.context.user
		)


class Mutation(graphene.ObjectType):
	create_account = CreateAccount.Field()

