from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField(default = timezone.now)
    file = models.FileField(verbose_name="",blank=True)