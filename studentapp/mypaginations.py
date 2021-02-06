#use for per view paginagtion concept
from rest_framework.pagination import LimitOffsetPagination
class MyPageNumberPagination(LimitOffsetPagination):
    default_limit = 6
    limit_query_param = 'l' #default limit is there but know l=10
    offset_query_param = 'off'#defualt offset is there but know off=same number
    max_limit = 10

