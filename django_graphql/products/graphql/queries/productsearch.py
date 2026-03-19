import graphene
from products.graphql.types.productType import ProductModelType
from products.models import Product
from django.core.paginator import Paginator
from graphql import GraphQLError
from django.core.paginator import EmptyPage

import graphene
from django.db.models import Q
from django.core.paginator import Paginator
from products.models import Product
from products.graphql.types.productType import ProductModelType

class PaginatedProductsType(graphene.ObjectType):
    page = graphene.Int()
    totpage = graphene.Int()
    totalrecords = graphene.Int()
    products = graphene.List(ProductModelType)

class SearchProduct(graphene.ObjectType):
    search_product = graphene.Field(
        PaginatedProductsType, 
        page=graphene.Int(required=True),
        keyword=graphene.String()
    )

    def resolve_search_product(root, info, page, keyword=None):
        queryset = Product.objects.all().order_by('id')
         
        if keyword:
            queryset = queryset.filter(descriptions__icontains=keyword)

        if not queryset.exists():        
            raise GraphQLError("No records found")

        per_page = 5
        paginator = Paginator(queryset, per_page)
        
        try:
            page_obj = paginator.page(page) 
        except EmptyPage:
            raise GraphQLError("That page contains no results")
        except Exception as e:
            raise GraphQLError(str(e))


        return PaginatedProductsType(
            page=page_obj.number,
            totpage=paginator.num_pages,
            totalrecords=paginator.count,
            products=page_obj.object_list
        )



# =====REQUEST======
# query SearchProduct($page: Int!, $keyword: String!) {
#  searchProducts{
#   searchProduct(page: $page, keyword: $keyword) {
#     page
#     totpage
#     totalrecords
#     products {
#       id
#       category
#       descriptions
#       qty
#       unit
#       costprice
#       sellprice
#       saleprice
#       productpicture
#       alertstocks
#       criticalstocks
#     }
#   }
# }
# }

# ======VARIABLES======
# {
#     "page": 1,
#     "keyword": "cineo"
# }