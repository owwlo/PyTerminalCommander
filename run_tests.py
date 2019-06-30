# -*- coding: utf-8 -*-

import sys
import unittest

import PyTerminalCommander.tests

res = unittest.TextTestRunner().run(PyTerminalCommander.tests.Tests)
sys.exit(len(res.failures))
