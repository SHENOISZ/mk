# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0002_contador'),
    ]

    operations = [
        migrations.AddField(
            model_name='contador',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=12, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contador',
            name='count',
            field=models.IntegerField(),
        ),
    ]
