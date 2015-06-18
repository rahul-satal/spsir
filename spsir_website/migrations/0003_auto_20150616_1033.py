# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spsir_website', '0002_mystudents'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyStudents',
            new_name='MyStudent',
        ),
        migrations.RenameField(
            model_name='mystudent',
            old_name='name',
            new_name='student_name',
        ),
        migrations.RenameField(
            model_name='myteacher',
            old_name='name',
            new_name='teacher_name',
        ),
    ]
