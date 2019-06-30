# -*- coding: utf-8 -*-

import sys
import logging
import unittest

logging.basicConfig(level=logging.INFO)

def test_suite(suites=[], cases=[]):
    new_suites = [x.Tests for x in suites]
    new_cases = [unittest.makeSuite(x.Tests) for x in cases]
    return unittest.TestSuite(new_cases + new_suites)

from . import super_move

Tests = test_suite(cases=[
    super_move,
], suites=[
])
