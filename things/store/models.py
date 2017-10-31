# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models


def generate_api_key():
    return uuid.uuid4().hex + uuid.uuid4().hex


# Create your models here.
class ThingDevice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=50, null=True)
    api_key = models.CharField(max_length=64, editable=False, default=generate_api_key)
    callback_url = models.URLField(editable=True, null=True)
    callback_format = models.CharField(max_length=50, null=True, editable=True)


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
