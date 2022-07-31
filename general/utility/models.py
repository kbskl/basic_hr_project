from django.db import models
from django.utils import timezone

from general.utility.enums import ActivityStatusTypeEnum


class GeneralModel(models.Model):
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(editable=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    activity_status = models.CharField(choices=ActivityStatusTypeEnum.choices(), max_length=50, verbose_name='Aktiflik Durumu', default=ActivityStatusTypeEnum.active.value)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()

        self.updated_at = timezone.now()
        return super(GeneralModel, self).save(*args, **kwargs)
