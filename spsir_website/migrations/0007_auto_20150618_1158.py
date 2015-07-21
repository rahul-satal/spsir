# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spsir_website', '0006_auto_20150617_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpritualGuru',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SpritualGuru_name', models.TextField(max_length=500, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('workshop_name', models.CharField(max_length=200, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mystudent',
            name='link',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
