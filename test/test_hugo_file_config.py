from datetime import datetime
from os import utime
from time import mktime
from unittest import TestCase

from src.hugo_file_config import HugoFileConfig


class TestHugoFileConfig(TestCase):
    def set_file_timestamp(self):
        date = datetime(2014, 10, 10, 12)
        u_time = mktime(date.timetuple())
        utime('dokuwiki_header_example.txt', (u_time, u_time))
        utime('subdir/moar/dokuwiki_header_in_subdir.txt', (u_time, u_time))

    def setUp(self):
        self.set_file_timestamp()
        self.header = HugoFileConfig()

    def test_dokuwiki_in_subdir_creates_tags_for_each_dir(self):
        expected_header = """+++
title = "dokuwiki_header_in_subdir"
draft = false
tags = [
    "subdir",
    "moar",
    "dokuwiki_header_in_subdir"
]
date = "2014-10-10"
+++"""

        actual_header = self.header.create('subdir/moar/dokuwiki_header_in_subdir.txt')
        self.assertEqual(expected_header, actual_header)

    def test_dokuwiki_header_example(self):
        expected_header = """+++
title = "dokuwiki_header_example"
draft = false
tags = [
    "dokuwiki_header_example"
]
date = "2014-10-10"
+++"""

        actual_header = self.header.create('dokuwiki_header_example.txt')
        self.assertEqual(expected_header, actual_header)
