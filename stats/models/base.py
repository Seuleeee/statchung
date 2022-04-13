from django.db import models


class TimeStampedModel(models.Model):
    create_datetime = models.DateTimeField(auto_created=True, null=True)
    update_datetime = models.DateTimeField(null=True)
    create_user = models.CharField(max_length=20, null=True)
    update_user = models.CharField(max_length=20, null=True)

    class Meta:
        abstract = True
