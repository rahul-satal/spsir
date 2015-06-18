# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spsir_website', '0005_auto_20150616_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mystudent',
            name='student_name1',
        ),
        migrations.RemoveField(
            model_name='mystudent',
            name='student_name10',
        ),
        migrations.RemoveField(
            model_name='mystudent',
            name='student_name2',
        ),
        migrations.RemoveField(
            model_name='mystudent',
            name='student_name3',
        ),
        migrations.RemoveField(
            model_name='mystudent',
            name='student_name4',
        ),
        migrations.RemoveField(
            model_name='mystudent',
            name='student_name5',
        ),
        migrations.RemoveField(
            model_name='mystudent',
            name='student_name6',
        ),
        migrations.RemoveField(
            model_name='mystudent',
            name='student_name7',
        ),
        migrations.RemoveField(
            model_name='mystudent',
            name='student_name8',
        ),
        migrations.RemoveField(
            model_name='mystudent',
            name='student_name9',
        ),
        migrations.RemoveField(
            model_name='myteacher',
            name='teacher_name1',
        ),
        migrations.RemoveField(
            model_name='myteacher',
            name='teacher_name10',
        ),
        migrations.RemoveField(
            model_name='myteacher',
            name='teacher_name2',
        ),
        migrations.RemoveField(
            model_name='myteacher',
            name='teacher_name3',
        ),
        migrations.RemoveField(
            model_name='myteacher',
            name='teacher_name4',
        ),
        migrations.RemoveField(
            model_name='myteacher',
            name='teacher_name5',
        ),
        migrations.RemoveField(
            model_name='myteacher',
            name='teacher_name6',
        ),
        migrations.RemoveField(
            model_name='myteacher',
            name='teacher_name7',
        ),
        migrations.RemoveField(
            model_name='myteacher',
            name='teacher_name8',
        ),
        migrations.RemoveField(
            model_name='myteacher',
            name='teacher_name9',
        ),
        migrations.AddField(
            model_name='mystudent',
            name='student_name',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myteacher',
            name='teacher_name',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
