# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spsir_website', '0007_auto_20150618_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spritualguru',
            name='SpritualGuru_name',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workshop',
            name='workshop_name',
            field=models.TextField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
