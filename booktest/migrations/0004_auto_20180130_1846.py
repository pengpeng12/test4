# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_auto_20180130_1838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='heroinfo',
            old_name='book',
            new_name='hbook',
        ),
        migrations.RemoveField(
            model_name='bookinfo',
            name='bcomment',
        ),
        migrations.RemoveField(
            model_name='bookinfo',
            name='bread',
        ),
        migrations.RemoveField(
            model_name='bookinfo',
            name='isDelete',
        ),
        migrations.RemoveField(
            model_name='heroinfo',
            name='isDelete',
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='bpub_date',
            field=models.DateTimeField(),
        ),
    ]
