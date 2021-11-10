from typing import TYPE_CHECKING, Any, Dict, List, TypedDict

from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django_stubs_ext import ValuesQuerySet, WithAnnotations

from ...models import FilmWork


class AnnotatedData(TypedDict):
    genres: List[str]
    actors: List[str]
    directors: List[str]
    writers: List[str]


# https://github.com/typeddjango/django-stubs/issues/719
if TYPE_CHECKING:
    AnnotatedFilmWork = WithAnnotations[FilmWork, AnnotatedData]
else:
    AnnotatedFilmWork = WithAnnotations[FilmWork]


class MoviesApiMixin:
    model = FilmWork
    http_method_names = ["get"]

    def get_queryset(
        self,
    ) -> ValuesQuerySet[AnnotatedFilmWork, Dict[str, Any]]:
        queryset = (
            FilmWork.objects.prefetch_related("genres", "persons")
            .values("id", "title", "description", "creation_date", "rating", "type")
            .annotate(
                genres=ArrayAgg("genres__name"),
                actors=ArrayAgg(
                    "persons__full_name", filter=Q(personfilmwork__role="actor")
                ),
                directors=ArrayAgg(
                    "persons__full_name", filter=Q(personfilmwork__role="director")
                ),
                writers=ArrayAgg(
                    "persons__full_name", filter=Q(personfilmwork__role="writer")
                ),
            )
        )
        return queryset

    def render_to_response(
        self, context: Dict[str, Any], **response_kwargs: Any
    ) -> JsonResponse:
        return JsonResponse(context)
