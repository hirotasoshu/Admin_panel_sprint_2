from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class RoleType(TextChoices):
    ACTOR = "actor", _("актер")
    DIRECTOR = "director", _("режиссер")
    WRITER = "writer", _("сценарист")


class FilmType(TextChoices):
    MOVIE = "movie", _("фильм")
    TV_SHOW = "tv_show", _("ТВ шоу")
