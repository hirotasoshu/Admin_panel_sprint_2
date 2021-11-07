from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_rating(rating: float) -> None:
    if not 0 <= rating <= 10:
        raise ValidationError(
            _("%(rating)s не находится в диапозоне от 0 до 10!"),
            params={"rating": rating},
        )
