from typing import Any, Dict, Final

from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from server.apps.movies.utils.mixins.api import MoviesApiMixin

_PAGINATE_BY: Final = 50


# ignored because of django-stubs bug:
# error: Definition of "model" in base class "MoviesApiMixin" is incompatible with
# definition in base class "MultipleObjectMixin"
class MoviesListApi(MoviesApiMixin, BaseListView):  # type: ignore
    ordering = ["title"]
    paginate_by = _PAGINATE_BY

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()

        paginator = context["paginator"]
        page = context["page_obj"]

        count = paginator.count
        total_pages = paginator.num_pages
        previous_page = page.previous_page_number() if page.has_previous() else None
        next_page = page.next_page_number() if page.has_next() else None
        results = list(context["object_list"])

        context = {
            "count": count,
            "total_pages": total_pages,
            "prev": previous_page,
            "next": next_page,
            "results": results,
        }
        return context


# ignored because of same django-stubs bug
class MoviesDetailApi(MoviesApiMixin, BaseDetailView):  # type: ignore
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_object()
        return context
