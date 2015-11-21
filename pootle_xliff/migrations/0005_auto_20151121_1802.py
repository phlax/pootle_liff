# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_xliff', '0004_auto_20151121_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='state',
        ),
        migrations.RemoveField(
            model_name='source',
            name='sub_state',
        ),
        migrations.AddField(
            model_name='segment',
            name='state',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'intial'), (1, b'translated'), (2, b'reviewed'), (3, b'final')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='segment',
            name='sub_state',
            field=models.ForeignKey(related_name='sources', blank=True, to='pootle_xliff.SegmentSubState', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='source',
            name='text',
            field=models.CharField(default='', max_length=4096),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='target',
            name='text',
            field=models.CharField(default='', max_length=4096),
            preserve_default=False,
        ),
    ]
