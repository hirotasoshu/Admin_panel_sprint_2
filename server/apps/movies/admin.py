from typing import Final

from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from .models import FilmWork, Genre, GenreFilmWork, Person, PersonFilmWork

_LIST_PER_PAGE: Final = 30


class GenreInline(admin.TabularInline):
    model = GenreFilmWork
    extra = 0
    verbose_name = "Жанр"
    autocomplete_fields = ("genre",)

    def get_queryset(self, request: HttpRequest) -> QuerySet[GenreFilmWork]:
        return super().get_queryset(request).select_related("genre", "film_work")


class PersonRoleInline(admin.TabularInline):
    model = PersonFilmWork
    extra = 0
    verbose_name = "Роль"
    autocomplete_fields = ("person",)

    def get_queryset(self, request: HttpRequest) -> QuerySet[PersonFilmWork]:
        return super().get_queryset(request).select_related("person", "film_work")


@admin.register(FilmWork)
class FilmworkAdmin(admin.ModelAdmin):
    list_filter = ("type",)
    search_fields = ("title", "description", "id")
    list_display = ("title", "type", "creation_date", "rating")
    fields = (
        "title",
        "type",
        "description",
        "creation_date",
        "certificate",
        "file_path",
        "rating",
    )
    inlines = [
        GenreInline,
        PersonRoleInline,
    ]
    ordering = ("title",)
    list_per_page = _LIST_PER_PAGE


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ("full_name", "birth_date", "id")
    list_display = ("full_name", "birth_date", "created_at", "updated_at")
    ordering = ("full_name",)
    list_per_page = _LIST_PER_PAGE


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "description", "created_at", "updated_at")
    ordering = ("name",)
    list_per_page = _LIST_PER_PAGE
