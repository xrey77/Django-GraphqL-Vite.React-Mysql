import graphene
from sales.graphql.types.salestype import SalesModelType
from sales.models import Sales

class SalesQuery(graphene.ObjectType):
    sales_list = graphene.List(SalesModelType)

    def resolve_sales_list(root, info):                     
        return Sales.objects.all()


# =====REQUEST======
# query GetSales {
#   getSales{
#     salesList {
#       id
#       salesamount
#       salesdate
#     }
#   }
# }