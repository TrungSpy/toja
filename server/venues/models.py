from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    image = models.TextField(default='')


class Venue(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    name_jp = models.CharField(max_length=100, blank=True, default='')
    gurunavi_id = models.CharField(max_length=100, blank=True, default='')
    gurunavi_url = models.CharField(max_length=100, blank=True, default='')
    address = models.TextField()
    phone = models.CharField(max_length=100, blank=True, default='')
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    images = models.TextField(default='')
    budget = models.FloatField(default=0.0)
    description = models.TextField(default='')
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ('gurunavi_id', )


class Food(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    name_jp = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(default='')
    image = models.TextField(default='')
    venue = models.ForeignKey(Venue)
