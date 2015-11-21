# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_xliff', '0003_auto_20151121_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='SegmentSubState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UnitType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='note',
            name='file',
            field=models.ForeignKey(related_name='notes', default=None, to='pootle_xliff.File'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='group',
            field=models.ForeignKey(related_name='notes', blank=True, to='pootle_xliff.Group', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='unit',
            field=models.ForeignKey(related_name='notes', blank=True, to='pootle_xliff.Unit', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='segment',
            name='can_resegment',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='source',
            name='state',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'intial'), (1, b'translated'), (2, b'reviewed'), (3, b'final')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='source',
            name='sub_state',
            field=models.ForeignKey(related_name='sources', blank=True, to='pootle_xliff.SegmentSubState', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='unit',
            name='can_resegment',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='unit',
            name='extra_attrs',
            field=django_extensions.db.fields.json.JSONField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='unit',
            name='src_dir',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'auto'), (1, b'ltr'), (2, b'rtl')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='unit',
            name='target_dir',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'auto'), (1, b'ltr'), (2, b'rtl')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='unit',
            name='translate',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='unit',
            name='unit_type',
            field=models.ForeignKey(related_name='units', blank=True, to='pootle_xliff.UnitType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='unit',
            name='xml_space',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'default'), (1, b'preserve')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='unit',
            name='group',
            field=models.ForeignKey(related_name='units', blank=True, to='pootle_xliff.Group', null=True),
            preserve_default=True,
        ),
    ]
