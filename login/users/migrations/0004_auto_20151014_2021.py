# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20151014_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='contact_no',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
