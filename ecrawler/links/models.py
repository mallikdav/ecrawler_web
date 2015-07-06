from django.db import models
from sites.models import Sites

# Create your models here.

class Links(models.Model):
    url = models.URLField(max_length=200)
    parentSite = models.ForeignKey(Sites)
    added = models.DateTimeField(auto_now_add=True)
