from datetime import datetime
from os import utime
from time import mktime
from unittest import TestCase

from src.hugo_front_matter import HugoFrontMatter


class TestHugoFrontMatter(TestCase):
    def set_file_timestamp(self):
        date = datetime(2014, 10, 10, 12)
        u_time = mktime(date.timetuple())
        utime('test/dokuwiki_header_example.txt', (u_time, u_time))
        utime('test/subdir/moar/dokuwiki_header_in_subdir.txt', (u_time, u_time))

    def setUp(self):
        self.set_file_timestamp()
        self.header = HugoFrontMatter()

    def test_dokuwiki_in_subdir_creates_tags_for_each_dir(self):
        expected_header = """+++
title = "dokuwiki_header_in_subdir"
draft = false
tags = [
    "test",
    "subdir",
    "moar",
    "dokuwiki_header_in_subdir"
]

date = "2014-10-10"
+++"""

        actual_header = self.header.create('test/subdir/moar/dokuwiki_header_in_subdir.txt')
        self.assertEqual(expected_header, actual_header)

    def test_dokuwiki_header_example(self):
        expected_header = """+++
title = "dokuwiki_header_example"
draft = false
tags = [
    "test",
    "dokuwiki_header_example"
]

date = "2014-10-10"
+++"""

        actual_header = self.header.create('test/dokuwiki_header_example.txt')
        self.assertEqual(expected_header, actual_header)
