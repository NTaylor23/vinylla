from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 200
    page_size_query_param = "page-size"
    max_page_size = 1000
