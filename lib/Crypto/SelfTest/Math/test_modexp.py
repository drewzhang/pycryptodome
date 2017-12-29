#
#  SelfTest/Math/test_modexp.py: Self-test for module exponentiation
#
# ===================================================================
#
# Copyright (c) 2017, Helder Eijs <helderijs@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ===================================================================

"""Self-test for the custom module exponentiation"""

import unittest

from Crypto.SelfTest.st_common import list_test_cases

from Crypto.Util.py3compat import *

from Crypto.Util._raw_api import (load_pycryptodome_raw_lib,
                                  c_size_t, expect_byte_string)

c_defs = """
int monty_pow(const uint8_t *base,
               const uint8_t *exp,
               const uint8_t *modulus,
               uint8_t       *out,
               size_t len,
               uint64_t seed)
"""

_raw_montgomery = load_pycryptodome_raw_lib("Crypto.Math._montgomery", c_defs)


class TestModExp(unittest.TestCase):

    def test_kat(self):
        pass


def get_tests(config={}):
    tests = []
    tests += list_test_cases(TestModExp)
    return tests


if __name__ == '__main__':
    suite = lambda: unittest.TestSuite(get_tests())
    unittest.main(defaultTest='suite')