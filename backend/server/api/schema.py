import graphene
from graphql_jwt.decorators import login_required
from .queries import Query
from .mutations import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
