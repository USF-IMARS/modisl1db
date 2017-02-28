#!/usr/bin/env python

# std modules:
import unittest
import subprocess

# dependencies:
from StationTester.TestHelper import TestHelper

class Test_modisl1db_usingBashScripts(unittest.TestCase):
    def setup(self):
        TestHelper.mySetup()

    def teardown(self):
        TestHelper.myTeardown()

    def _run_bash_test(self, script, products, errfiles):
        subprocess.call(script, stdout=TestHelper.FNULL, stderr=subprocess.STDOUT)
        TestHelper._test_products_and_errfiles(self, products, errfiles)

    # tests:
    ##################################
    def test_l0_to_l1_aqua(self):
        self._run_bash_test(
            './run-l0tol1_aqua',
            ['L1AAqua.hdf', 'GEOAqua.hdf'],
            ['errfileAquaGEO', 'errfileL1A']
        )

    def test_l0_to_l1_terra(self):
        self._run_bash_test(
            './run-l0tol1_terra',
            ['L1ATerra.hdf', 'GEOTerra.hdf'],
            ['errfileTerraGEO', 'errfileL1A']
        )

    def test_l1a_to_b_aqua(self):
        self._run_bash_test(
            './run-l1atob_aqua',
            ['L1B1KMAqua.hdf', 'L1BHKMAqua.hdf', 'L1BQKMAqua.hdf'],
            ['errfileL1B']
        )

    def test_l1a_to_b_terra(self):
        self._run_bash_test(
            './run-l1atob_terra',
            ['L1B1KMTerra.hdf', 'L1BHKMTerra.hdf', 'L1BQKMTerra.hdf'],
            ['errfileL1B']
        )
