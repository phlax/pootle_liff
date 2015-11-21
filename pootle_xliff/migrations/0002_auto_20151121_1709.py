# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_xliff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='file',
            old_name='name',
            new_name='xid',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='name',
            new_name='xid',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='name',
            new_name='xid',
        ),
        migrations.RenameField(
            model_name='segment',
            old_name='name',
            new_name='xid',
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='name',
            new_name='xid',
        ),
        migrations.AddField(
            model_name='file',
            name='can_resegment',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='file',
            name='extra_attrs',
            field=django_extensions.db.fields.json.JSONField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='file',
            name='original',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='file',
            name='src_dir',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'auto'), (1, b'ltr'), (2, b'rtl')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='file',
            name='target_dir',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'auto'), (1, b'ltr'), (2, b'rtl')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='file',
            name='translate',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='file',
            name='xml_space',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'default'), (1, b'preserve')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='group',
            field=models.ForeignKey(related_name='groups', blank=True, to='pootle_xliff.Group', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='applies_to',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'source'), (1, b'target')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='category',
            field=models.ForeignKey(related_name='notes', blank=True, to='pootle_xliff.NoteCategory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='priority',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='text',
            field=models.CharField(default='', max_length=4096),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='file',
            field=models.ForeignKey(related_name='groups', to='pootle_xliff.File'),
            preserve_default=True,
        ),
    ]
