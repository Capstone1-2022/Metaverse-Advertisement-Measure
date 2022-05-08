from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class Content(models.Model):
    pub_date = models.DateTimeField(default = timezone.now)
    file = models.FileField(verbose_name="",blank=True)