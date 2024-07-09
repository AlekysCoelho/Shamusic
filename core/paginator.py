import math

from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response


class CustomPageTracks(PageNumberPagination):
    page_size = 5
    max_page_size = 1000
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        # show page size in response
        if self.request.query_params.get("page_size"):
            self.page_size = int(self.request.query_params.get("page_size"))

        # count total page from request by total and page_size
        total_page = math.ceil(self.page.paginator.count / self.page_size)
        total_tracks = self.page.paginator.count

        return Response(
            {
                "count": self.page.paginator.count,
                "total_page": total_page,
                "page_size": self.page_size,
                "total_tracks": total_tracks,
                "current": self.page.number,
                "previous": self.get_previous_link(),
                "next": self.get_next_link(),
                "results": data,
            }
        )
