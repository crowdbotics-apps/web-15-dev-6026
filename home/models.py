from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    bvfjghfghfj = models.PositiveIntegerField(null=True, blank=True,)
    ghfjghfjhgfj = models.FloatField(null=True, blank=True,)
    hgfjhgfjh = models.PositiveIntegerField(null=True, blank=True,)
    khgfjhgfkhgf = models.PositiveSmallIntegerField(null=True, blank=True,)
    hfkhgfhkjhg = models.SlugField(max_length=50, null=True, blank=True,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
