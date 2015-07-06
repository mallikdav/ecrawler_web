from django.forms import *    # fill in custom user info then save it
from models import Sites


class Site(ModelForm):
    class Meta:
        model = Sites
        fields = ('site',)
        labels = {
            'site': "Enter the url that you want me to CRAWL : "
        }