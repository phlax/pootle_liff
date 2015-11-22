#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

import os

import pytest

from pootle_xliff import xttk

EXAMPLES = os.path.realpath(os.path.join(os.path.dirname(__file__), "../data/examples"))


@pytest.mark.django
def __test_hello():

    with open(os.path.join(EXAMPLES, "xliff/metadata.xliff")) as f:
        li = xttk.LanguageInterchange(f.read().decode("utf-8"), "xliff")
    files =  li.files
    
    for f in files:
       for note in f.notes:
           print note.id

       for unit in f.units:
           for segment in unit.segments:
               text = segment.source.text

       for group in f.groups:
           import pdb; pdb.set_trace()

    li.src.serialize()


@pytest.mark.django
def __test_xliff_1_2():

    with open(os.path.join(EXAMPLES, "xliff_1_2/hello_world.xlf")) as f:
        li = xttk.LanguageInterchange(f.read().decode("utf-8"), "xliff_1_2")

    for f in li.files:
        import pdb; pdb.set_trace()


@pytest.mark.django
def test_po():

    with open(os.path.join(EXAMPLES, "po/tutorial.po")) as f:
        li = xttk.LanguageInterchange(f.read().decode("utf-8"), "po")

    for f in li.files:
        import pdb; pdb.set_trace()
