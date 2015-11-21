# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from django.db import models

from django_extensions.db.fields.json import JSONField


DIRECTION_CHOICES = list(enumerate(["auto", "ltr", "rtl"]))
WHITESPACE_CHOICES = list(enumerate(["default", "preserve"]))

NOTE_APPLIES_TO_CHOICES = list(enumerate(["source", "target"]))
SEGMENT_STATE_CHOICES =  list(
    enumerate(
        ["intial", "translated", "reviewed", "final"]))


class XLIFFElementModel(models.Model):

    class Meta:
        abstract = True

    # xliff.id
    xid = models.CharField(max_length=32)
    # xliff.canResegment
    can_resegment = models.NullBooleanField(blank=True, null=True)
    translate = models.NullBooleanField(blank=True, null=True)
    # xliff.srcDir
    src_dir = models.IntegerField(choices=DIRECTION_CHOICES, blank=True, null=True)
    # xliff.targetDir
    target_dir = models.IntegerField(choices=DIRECTION_CHOICES, blank=True, null=True)
    # xliff.xml:space
    xml_space = models.IntegerField(choices=WHITESPACE_CHOICES, blank=True, null=True)
    extra_attrs = JSONField(blank=True, null=True)


class File(XLIFFElementModel):
    # http://docs.oasis-open.org/xliff/xliff-core/v2.0/xliff-core-v2.0.html#file

    original = models.URLField(blank=True, null=True)

    # unimplemented - skeleton

    def serialize(self):
        pass

    def deserialize(self):
        pass


class Group(XLIFFElementModel):
    # http://docs.oasis-open.org/xliff/xliff-core/v2.0/xliff-core-v2.0.html#group

    file = models.ForeignKey(
        "File", related_name='all_groups')
    group = models.ForeignKey(
        "Group", related_name='groups', null=True, blank=True)
    name = models.CharField(max_length=32, null=True, blank=True)
    # xliff.type
    group_type = models.ForeignKey(
        "GroupType", related_name='groups', null=True, blank=True)


class GroupType(models.Model):
    name = models.CharField(max_length=32)



class NoteCategory(models.Model):
    name = models.CharField(max_length=32)


class Note(models.Model):
    # http://docs.oasis-open.org/xliff/xliff-core/v2.0/xliff-core-v2.0.html#note

    file = models.ForeignKey(
        "File", related_name='notes')
    group = models.ForeignKey(
        "Group", related_name='notes', null=True, blank=True)
    unit = models.ForeignKey(
        "Unit", related_name='notes', null=True, blank=True)

    # xliff.id
    xid = models.CharField(max_length=32)
    category = models.ForeignKey(
        "NoteCategory", related_name='notes', null=True, blank=True)
    priority = models.IntegerField(blank=True, null=True, choices=list(enumerate(range(1, 11))))
    # xliff.appliesTo
    applies_to = models.IntegerField(choices=NOTE_APPLIES_TO_CHOICES, null=True, blank=True)
    text = models.CharField(max_length=4096, blank=False)


class Segment(models.Model):
    # http://docs.oasis-open.org/xliff/xliff-core/v2.0/xliff-core-v2.0.html#segment

    xid = models.CharField(max_length=32)
    ignorable = models.BooleanField(default=False)
    unit = models.ForeignKey(
        "Unit", related_name='segments', unique=True)
    # xliff.canResegment
    can_resegment = models.NullBooleanField(blank=True, null=True)
    state = models.IntegerField(choices=SEGMENT_STATE_CHOICES, blank=True, null=True)
    # xliff.subState
    sub_state = models.ForeignKey(
        "SegmentSubState", related_name='sources', null=True, blank=True)


class SegmentSubState(models.Model):
    name = models.CharField(max_length=32)


class Source(models.Model):
    segment = models.ForeignKey(
        "Segment", related_name='source', unique=True)
    text = models.CharField(max_length=4096, blank=False)


class Target(models.Model):
    segment = models.ForeignKey(
        "Segment", related_name='target', unique=True)
    text = models.CharField(max_length=4096, blank=False)


class Unit(XLIFFElementModel):
    # http://docs.oasis-open.org/xliff/xliff-core/v2.0/xliff-core-v2.0.html#unit

    file = models.ForeignKey(
        "File", related_name='units')
    group = models.ForeignKey(
        "Group", related_name='units', null=True, blank=True)
    # xliff.type
    unit_type = models.ForeignKey(
        "UnitType", related_name='units', null=True, blank=True)


class UnitType(models.Model):
    name = models.CharField(max_length=32)

