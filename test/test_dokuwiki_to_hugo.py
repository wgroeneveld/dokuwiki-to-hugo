import shutil
from unittest import TestCase

from pathlib import Path

from src.dokuwiki_to_hugo import DokuWikiToHugo


class TestDokuWikiToHugo(TestCase):

    def tearDown(self):
        shutil.rmtree('output')

    def test_doku_to_hugo_converts_home_to_index_markdown_files(self):
        DokuWikiToHugo().doku_to_hugo('subdir')
        expected = Path("output/subdir/_index.md").read_text()

        self.assertIn('subdir index', expected)

    def test_convert_whole_dir(self):
        DokuWikiToHugo().doku_to_hugo('subdir')
        expected = Path("output/subdir/moar/dokuwiki_header_in_subdir.md").read_text()

        self.assertIn('+++', expected)                  # header is there, check
        self.assertIn('##### some header', expected)    # some conversion done, check