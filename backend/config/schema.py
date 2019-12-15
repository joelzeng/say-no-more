import graphene
import snm_app.accounts.schema
import snm_app.users.schema

class Query(
	snm_app.accounts.schema.Query,
	snm_app.users.schema.Query,
	graphene.ObjectType,
):
	pass

class Mutation(
	snm_app.accounts.schema.Mutation,
	snm_app.users.schema.Mutation,
	graphene.ObjectType
):
	pass

schema = graphene.Schema(query=Query, mutation=Mutation)