from unittest import TestCase

from pathlib import Path

from src.markdown_converter import MarkdownConverter


class TestMarkdownHeader(TestCase):
    def setUp(self):
        self.converter = MarkdownConverter("dokuwiki_example.txt")

    def test_acceptance_test_case(self):
        # python 3.5 and up
        expected = Path("expected_markdown_output.txt").read_text()
        actual = self.converter.convert()

        print(actual)
        self.assertEqual(expected, actual, "Files not matching!")
