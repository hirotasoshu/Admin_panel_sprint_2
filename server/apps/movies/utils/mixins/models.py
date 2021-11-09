import uuid

from django.db.models import DateTimeField, Model, UUIDField


class CreatedAtIDMixin(Model):
    id = UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CreatedUpdatedAtIDMixin(CreatedAtIDMixin):
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
