#!/usr/bin/env python
#
#    Copyright (C) 2009 Google Inc.
#
#   Licensed under the Apache License 2.0;
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


# This module is used for version 2 of the Google Data APIs.


# __author__ = 'j.s@google.com (Jeff Scudder)'

import unittest

from gdata.test_config import settings

from . import all_tests

settings.RUN_LIVE_TESTS = True
settings.CACHE_RESPONSES = True
settings.CLEAR_CACHE = True


def suite():
    return unittest.TestSuite((atom_tests.core_test.suite(),))


if __name__ == '__main__':
    unittest.TextTestRunner().run(all_tests.suite())