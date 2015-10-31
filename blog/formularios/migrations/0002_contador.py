# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contador',
            fields=[
                ('count', models.IntegerField(serialize=False, primary_key=True)),
            ],
        ),
    ]
