# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site', models.CharField(max_length=500)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('active_or_dead', models.BooleanField()),
                ('parentSite', models.ForeignKey(to='sites.Sites', null=True)),
            ],
        ),
    ]
