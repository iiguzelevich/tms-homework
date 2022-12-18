from rest_framework.pagination import PageNumberPagination


class BasePagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page_size'
    max_page_size = 100


class StandardPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 100
