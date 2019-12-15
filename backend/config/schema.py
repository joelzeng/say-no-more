import graphene
import snm_app.schema

class Query(snm_app.schema.Query, graphene.ObjectType):
	pass

schema = graphene.Schema(query=Query)