from unittest import TestCase

from src.dokuwiki_to_hugo import DokuWikiToHugo
from src.markdown.links import MarkdownLinks


class TestMarkdownLinks(TestCase):

    def setUp(self):
        self.converter = MarkdownLinks()

    def tearDown(self):
        DokuWikiToHugo.root_dir = None

    def text_convert_no_link_returns_text(self):
        self.assertEquals("sup", self.converter.convert("sup"))

    def test_do_not_convert_starting_with_space(self):
        # I actually should be looking for ``` to see if this shouldn't be converted
        # but that would be way too complex for a simple onetime conversion so fuck that.
        no_real_doku_link = """if [[ "$line" =~ "|" ]]; then"""
        self.assertEqual(no_real_doku_link, self.converter.convert(no_real_doku_link))

    def test_internal_link_with_space_converted_to_underscore(self):
        md_link = """[magic properties]({{< relref "magic_properties.md" >}})"""
        doku_link = "[[magic properties]]"

        self.assertEqual(md_link, self.converter.convert(doku_link))

    def test_internal_link_to_home_converted_to_index(self):
        md_link = """[subpage/home]({{< relref "subpage/_index.md" >}})"""
        doku_link = "[[subpage/home]]"

        self.assertEqual(md_link, self.converter.convert(doku_link))

    def test_internal_link_with_ref_to_root_not_prefixed_with_root_dir(self):
        DokuWikiToHugo.root_dir = "pages"
        md_link = """[Download SaveGame #one]({{< relref "/games/Wizardry8/Wizardry8_Saves01.rar" >}})"""
        doku_link = """[[/games/Wizardry8/Wizardry8_Saves01.rar|Download SaveGame #one]]"""

        self.assertEqual(md_link, self.converter.convert(doku_link))

    def test_internal_link_prefixed_with_configured_root_dir_if_subdir(self):
        DokuWikiToHugo.root_dir = "pages"
        md_link = """[bla/blie]({{< relref "pages/bla/blie.md" >}})"""
        doku_link = "[[bla:blie]]"

        self.assertEqual(md_link, self.converter.convert(doku_link))

    def test_internal_links_not_prefixed_with_configured_root_dir_if_currdir(self):
        DokuWikiToHugo.root_dir = "pages"
        md_link = """[bla]({{< relref "bla.md" >}})"""
        doku_link = "[[bla]]"

        self.assertEqual(md_link, self.converter.convert(doku_link))

    def test_internal_links_without_text_converted_properly(self):
        md_link = """[bla]({{< relref "bla.md" >}})"""
        doku_link = "[[bla]]"

        self.assertEqual(md_link, self.converter.convert(doku_link))

    def test_internal_links_with_sublink_converted_properly(self):
        md_link = """[text]({{< relref "bla/blie.md" >}})"""
        doku_link = "[[bla:blie|text]]"

        self.assertEqual(md_link, self.converter.convert(doku_link))

    def test_multiple_links_in_text_converted_properly(self):
        md_link = """[bla]({{< relref "bla.md" >}}) wow this looks cool and so does [this]({{< relref "this.md" >}}) and such"""
        doku_link = "[[bla]] wow this looks cool and so does [[this]] and such"

        self.assertEqual(md_link, self.converter.convert(doku_link))

    def test_internal_links_with_some_text_in_line_converted_properly(self):
        md_link = """[text]({{< relref "bla.md" >}}) wow this looks cool"""
        doku_link = "[[bla|text]] wow this looks cool"

        self.assertEqual(md_link, self.converter.convert(doku_link))

    def test_internal_link_with_image_tag(self):
        doku_link = "[[code|<img src='code.jpg'>]]"
        md_link = """[<img src='code.jpg'>]({{< relref "code.md" >}})"""

        self.assertEqual(md_link, self.converter.convert(doku_link))

    def test_internal_links_with_extension_not_suffixed_with_md(self):
        md_link = """[text]({{< relref "bla.zip" >}})"""
        doku_link = "[[bla.zip|text]]"

        self.assertEqual(md_link, self.converter.convert(doku_link))

    def test_internal_links_converted_properly(self):
        md_link = """[text]({{< relref "bla.md" >}})"""
        doku_link = "[[bla|text]]"

        self.assertEqual(md_link, self.converter.convert(doku_link))

    def test_unknown_interwiki_link_throws_exception(self):
        with self.assertRaises(ValueError):
            self.converter.convert("[[whaddapdawg>Wiki]]")

    def test_known_interwiki_link_with_some_spaces(self):
        md_link = """{{< lib "Purple Cow: Transform Your Business by Being Remarkable" >}}"""
        doku_link = "[[lib>Purple Cow: Transform Your Business by Being Remarkable]]"

        self.assertEqual(md_link, self.converter.convert(doku_link))

    def test_known_interwiki_link_converts_successfully(self):
        # see https://gohugo.io/extras/shortcodes/
        md_link = """{{< wp "Wiki" >}}"""
        doku_link = "[[wp>Wiki]]"

        self.assertEqual(md_link, self.converter.convert(doku_link))

    def test_external_link_without_title(self):
        md_link = "[https://www.google.com](https://www.google.com)"
        doku_link = "[[https://www.google.com]]"

        self.assertEqual(md_link, self.converter.convert(doku_link))

    def test_external_links_converted_properly(self):
        md_link = "[Wouter Groeneveld](https://github.com/wgroeneveld/)"
        doku_link = "[[https://github.com/wgroeneveld/|Wouter Groeneveld]]"

        self.assertEqual(md_link, self.converter.convert(doku_link))
