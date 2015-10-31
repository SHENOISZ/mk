# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='form_blog',
            fields=[
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('comment', models.TextField()),
            ],
        ),
    ]
