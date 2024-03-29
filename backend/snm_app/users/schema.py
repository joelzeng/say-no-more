import graphene
from graphql import GraphQLError
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

class UserType(DjangoObjectType):
	class Meta:
		model = get_user_model()


class CreateUser(graphene.Mutation):
	user = graphene.Field(UserType)

	class Arguments:
		username = graphene.String(required=True)
		password = graphene.String(required=True)
		email = graphene.String(required=True)

	def mutate(self, info, username, password, email):
		user = get_user_model()(
			username=username,
			email=email
		)
		user.set_password(password)
		user.save()

		return CreateUser(user=user)


class Query(graphene.ObjectType):
	users = graphene.List(UserType)
	me = graphene.Field(UserType)

	def resolve_users(self, info, **kwargs):
		return get_user_model().objects.all()

	def resolve_me(self, info):
		user = info.context.user
		if user.is_anonymous:
			raise GraphQLError("You must be logged in")
		return user


class Mutation(graphene.ObjectType):
	create_user = CreateUser.Field()