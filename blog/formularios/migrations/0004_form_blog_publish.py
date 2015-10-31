# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0003_auto_20150925_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='form_blog',
            name='publish',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
