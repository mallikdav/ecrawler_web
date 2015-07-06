from django.db import models

# Create your models here.

class Sites(models.Model):
    site = models.CharField(max_length=500, null=False)
    added = models.DateTimeField(auto_now=True)
    parentSite = models.ForeignKey('Sites', null=True)
    active_or_dead = models.BooleanField(default=False)