from unittest import TestCase

from src.markdown.links import MarkdownLinks


class TestMarkdownLinks(TestCase):

    def setUp(self):
        self.converter = MarkdownLinks()

    def text_convert_no_link_returns_text(self):
        self.assertEquals("sup", self.converter.convert("sup"))

    def test_internal_links_without_text_converted_properly(self):
        mdLink = """{{< relref "bla" >}}"""
        dokuLink = "[[bla]]"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_unknown_interwiki_link_throws_exception(self):
        with self.assertRaises(ValueError):
            self.converter.convert("[[whaddapdawg>Wiki]]")

    def test_known_interwiki_link_converts_successfully(self):
        # see https://gohugo.io/extras/shortcodes/
        mdLink = """{{< wp Wiki >}}"""
        dokuLink = "[[wp>Wiki]]"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_internal_links_with_sublink_converted_properly(self):
        mdLink = """[text]({{< relref "bla/blie" >}})"""
        dokuLink = "[[bla:blie|text]]"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_multiple_links_in_text_converted_properly(self):
        mdLink = """{{< relref "bla" >}} wow this looks cool and so does {{< relref "this" >}} and such"""
        dokuLink = "[[bla]] wow this looks cool and so does [[this]] and such"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_internal_links_with_some_text_in_line_converted_properly(self):
        mdLink = """[text]({{< relref "bla" >}}) wow this looks cool"""
        dokuLink = "[[bla|text]] wow this looks cool"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_internal_links_converted_properly(self):
        mdLink = """[text]({{< relref "bla" >}})"""
        dokuLink = "[[bla|text]]"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_external_links_converted_properly(self):
        mdLink = "[Wouter Groeneveld](https://github.com/wgroeneveld/)"
        dokuLink = "[[https://github.com/wgroeneveld/|Wouter Groeneveld]]"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))
