# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0004_form_blog_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_blog',
            name='publish',
            field=models.CharField(max_length=200),
        ),
    ]
