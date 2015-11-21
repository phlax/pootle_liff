# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_xliff', '0002_auto_20151121_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='group',
            name='can_resegment',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='extra_attrs',
            field=django_extensions.db.fields.json.JSONField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='group_type',
            field=models.ForeignKey(related_name='groups', blank=True, to='pootle_xliff.GroupType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=32, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='src_dir',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'auto'), (1, b'ltr'), (2, b'rtl')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='target_dir',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'auto'), (1, b'ltr'), (2, b'rtl')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='translate',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='xml_space',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'default'), (1, b'preserve')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='file',
            field=models.ForeignKey(related_name='all_groups', to='pootle_xliff.File'),
            preserve_default=True,
        ),
    ]
