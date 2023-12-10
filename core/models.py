from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время публикации")
    modified = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    class Meta:
        abstract = True

