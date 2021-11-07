from typing import Final, final

from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .utils.mixins import CreatedAtIDMixin, CreatedUpdatedAtIDMixin
from .utils.types import FilmType, RoleType
from .utils.validators import validate_rating

_DB_SCHEMA: Final = '"content"'


@final
class FilmWork(CreatedUpdatedAtIDMixin):
    title = models.CharField(_("Название"), max_length=255)
    description = models.TextField(_("Описание"), null=True, blank=True)
    creation_date = models.DateField(_("Дата выхода"), null=True, blank=True)
    certificate = models.TextField(_("Cертификат"), null=True, blank=True)
    file_path = models.FileField(
        _("Файл"), upload_to="film_works/", blank=True, max_length=100
    )
    rating = models.FloatField(
        _("Рейтинг"),
        validators=[validate_rating],
        default=0.0,
    )
    type = models.CharField(_("Тип фильма"), max_length=20, choices=FilmType.choices)
    genres = models.ManyToManyField("Genre", through="GenreFilmWork")

    class Meta:
        verbose_name = _("Фильм")
        verbose_name_plural = _("Фильмы")
        db_table = f'{_DB_SCHEMA}."film_work"'

    def __str__(self) -> str:
        return self.title


@final
class Genre(CreatedUpdatedAtIDMixin):
    name = models.CharField(_("Название"), max_length=255)
    description = models.TextField(_("Описание"), null=True, blank=True)

    class Meta:
        verbose_name = _("Жанр")
        verbose_name_plural = _("Жанры")
        db_table = f'{_DB_SCHEMA}."genre"'

    def __str__(self) -> str:
        return self.name


@final
class GenreFilmWork(CreatedAtIDMixin):
    film_work = models.ForeignKey(
        "FilmWork", on_delete=models.CASCADE, to_field="id", db_column="film_work_id"
    )
    genre = models.ForeignKey(
        "Genre", on_delete=models.CASCADE, to_field="id", db_column="genre_id"
    )

    class Meta:
        indexes = [
            models.Index(fields=["film_work_id", "genre_id"], name="film_work_genre"),
        ]
        verbose_name = _("Жанр фильма")
        verbose_name_plural = _("Жанры фильмов")
        db_table = f'{_DB_SCHEMA}."genre_film_work"'

    def __str__(self) -> str:
        return f"{self.film_work}: {self.genre}"


@final
class Person(CreatedUpdatedAtIDMixin):
    full_name = models.CharField(
        _("Полное имя"), validators=[MinLengthValidator(3)], max_length=255
    )
    birth_date = models.DateField(_("Дата рождения"), null=True, blank=True)

    class Meta:
        verbose_name = _("Личность")
        verbose_name_plural = _("Личности")
        db_table = f'{_DB_SCHEMA}."person"'

    def __str__(self) -> str:
        return self.full_name


@final
class PersonFilmWork(CreatedAtIDMixin):
    film_work = models.ForeignKey(
        "FilmWork", on_delete=models.CASCADE, to_field="id", db_column="film_work_id"
    )
    person = models.ForeignKey(
        "Person", on_delete=models.CASCADE, to_field="id", db_column="person_id"
    )
    role = models.CharField(_("role"), max_length=20, choices=RoleType.choices)

    class Meta:
        verbose_name = _("Роль личности")
        verbose_name_plural = _("Роли личностей")
        db_table = f'{_DB_SCHEMA}."person_film_work"'
        indexes = [
            models.Index(
                fields=["film_work_id", "person_id", "role"],
                name="film_work_person_role",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.film_work}: {self.person}"
