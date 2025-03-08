#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from pathlib import Path
from smk2rst import codebase_parser


class TestCodebaseParser(unittest.TestCase):
    def setUp(self):
        self.basepath = Path(__file__).parent / "test_codebase"

    def test_digest_codebase(self):
        print(self.basepath)
        sources = codebase_parser(self.basepath)

        n_functions = sum([len(s.functions) for s in sources])
        n_rules = sum([len(s.rules) for s in sources])

        print(sources)

        assert len(sources) == 2
        assert n_functions == 1
        assert n_rules == 2
