import graphene
import graphql_jwt
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
	token_auth = graphql_jwt.ObtainJSONWebToken.Field()
	verify_token = graphql_jwt.Verify.Field()
	refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)