from unittest import TestCase

from src.markdown.headers import MarkdownHeader


class TestMarkdownHeader(TestCase):

    def setUp(self):
        self.converter = MarkdownHeader()

    def test_convert_does_nothing_if_no_header(self):
        self.assertEqual("blabla", self.converter.convert("blabla"))

    def test_convert_h1(self):
        result = self.converter.convert("====== Classes ======")
        self.assertEqual(result, "# Classes ")

    def test_convert_h2(self):
        result = self.converter.convert("===== Classes =====")
        self.assertEqual(result, "## Classes ")

    def test_convert_h3(self):
        result = self.converter.convert("==== Classes ====")
        self.assertEqual(result, "### Classes ")

    def test_convert_h4(self):
        result = self.converter.convert("=== Classes ===")
        self.assertEqual(result, "#### Classes ")

    def test_convert_h5(self):
        result = self.converter.convert("== Classes ==")
        self.assertEqual(result, "##### Classes ")
