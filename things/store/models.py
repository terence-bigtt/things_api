# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class ThingData(models.Model):
    device_id = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    name1 = models.CharField(max_length=30)
    value1 = models.CharField(max_length=30)
    name2 = models.CharField(max_length=30, null=True)
    value2 = models.CharField(max_length=30, null=True)
    name3 = models.CharField(max_length=30, null=True)
    value3 = models.CharField(max_length=30, null=True)
    name4 = models.CharField(max_length=30, null=True)
    value4 = models.CharField(max_length=30, null=True)
    name5 = models.CharField(max_length=30, null=True)
    value5 = models.CharField(max_length=30, null=True)
    name6 = models.CharField(max_length=30, null=True)
    value6 = models.CharField(max_length=30, null=True)
    name7 = models.CharField(max_length=30, null=True)
    value7 = models.CharField(max_length=30, null=True)
    name8 = models.CharField(max_length=30, null=True)
    value8 = models.CharField(max_length=30, null=True)
