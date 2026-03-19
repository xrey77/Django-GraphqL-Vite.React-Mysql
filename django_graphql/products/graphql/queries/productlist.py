import graphene
from products.graphql.types.productType import ProductModelType
from products.models import Product
from django.core.paginator import Paginator
from graphql import GraphQLError
from django.core.paginator import EmptyPage

class ProductsPaginatedType(graphene.ObjectType):
    page = graphene.Int()
    totpage = graphene.Int()
    totalrecords = graphene.Int()
    products = graphene.List(ProductModelType)

class ProductsList(graphene.ObjectType):
    products_list = graphene.Field(
        ProductsPaginatedType, 
        page=graphene.Int(required=True)
    )

    def resolve_products_list(root, info, page):
        queryset = Product.objects.all().order_by('id')

        if not queryset.exists():        
            raise Exception("No record(s) found.")


        per_page = 5
        paginator = Paginator(queryset, per_page)

        try:
            page_obj = paginator.page(page) 
        except EmptyPage:
            raise GraphQLError("That page contains no results")
        except Exception as e:
            raise GraphQLError(str(e))


        return ProductsPaginatedType(
            page=page_obj.number,
            totpage=paginator.num_pages,
            totalrecords=paginator.count,
            products=page_obj.object_list
        )

# =====REQUEST======
# query pageProducts($page: Int!) {    
#     pageProducts {
#       productsList(page: $page) {
#         page
#         totpage
#         totalrecords
#         products {
#           id
#           category
#           descriptions
#           qty
#           unit
#           costprice
#           sellprice
#           saleprice
#           productpicture
#           alertstocks
#           criticalstocks
#         }
#       }
#   }
# }

# ======VARIABLES=====
# {
#     "page": 1
# }

