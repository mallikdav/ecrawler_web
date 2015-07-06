# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites',
            name='active_or_dead',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sites',
            name='added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
