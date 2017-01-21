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
        mdLink = """[magic properties]({{< relref "magic_properties.md" >}})"""
        dokuLink = "[[magic properties]]"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_internal_link_to_home_converted_to_index(self):
        mdLink = """[subpage/home]({{< relref "subpage/_index.md" >}})"""
        dokuLink = "[[subpage/home]]"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_internal_link_with_ref_to_root_not_prefixed_with_root_dir(self):
        DokuWikiToHugo.root_dir = "pages"
        mdLink = """[Download SaveGame #one]({{< relref "/games/Wizardry8/Wizardry8_Saves01.rar" >}})"""
        dokuLink = """[[/games/Wizardry8/Wizardry8_Saves01.rar|Download SaveGame #one]]"""

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_internal_link_prefixed_with_configured_root_dir_if_subdir(self):
        DokuWikiToHugo.root_dir = "pages"
        mdLink = """[bla/blie]({{< relref "pages/bla/blie.md" >}})"""
        dokuLink = "[[bla:blie]]"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_internal_links_not_prefixed_with_configured_root_dir_if_currdir(self):
        DokuWikiToHugo.root_dir = "pages"
        mdLink = """[bla]({{< relref "bla.md" >}})"""
        dokuLink = "[[bla]]"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_internal_links_without_text_converted_properly(self):
        mdLink = """[bla]({{< relref "bla.md" >}})"""
        dokuLink = "[[bla]]"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_internal_links_with_sublink_converted_properly(self):
        mdLink = """[text]({{< relref "bla/blie.md" >}})"""
        dokuLink = "[[bla:blie|text]]"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_multiple_links_in_text_converted_properly(self):
        mdLink = """[bla]({{< relref "bla.md" >}}) wow this looks cool and so does [this]({{< relref "this.md" >}}) and such"""
        dokuLink = "[[bla]] wow this looks cool and so does [[this]] and such"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_internal_links_with_some_text_in_line_converted_properly(self):
        mdLink = """[text]({{< relref "bla.md" >}}) wow this looks cool"""
        dokuLink = "[[bla|text]] wow this looks cool"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_internal_link_with_image_tag(self):
        dokuLink = "[[code|<img src='code.jpg'>]]"
        mdLink = """[<img src='code.jpg'>]({{< relref "code.md" >}})"""

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_internal_links_with_extension_not_suffixed_with_md(self):
        mdLink = """[text]({{< relref "bla.zip" >}})"""
        dokuLink = "[[bla.zip|text]]"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_internal_links_converted_properly(self):
        mdLink = """[text]({{< relref "bla.md" >}})"""
        dokuLink = "[[bla|text]]"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_unknown_interwiki_link_throws_exception(self):
        with self.assertRaises(ValueError):
            self.converter.convert("[[whaddapdawg>Wiki]]")

    def test_known_interwiki_link_with_some_spaces(self):
        mdLink = """{{< lib "Purple Cow: Transform Your Business by Being Remarkable" >}}"""
        dokuLink = "[[lib>Purple Cow: Transform Your Business by Being Remarkable]]"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_known_interwiki_link_converts_successfully(self):
        # see https://gohugo.io/extras/shortcodes/
        mdLink = """{{< wp "Wiki" >}}"""
        dokuLink = "[[wp>Wiki]]"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_external_link_without_title(self):
        mdLink = "[https://www.google.com](https://www.google.com)"
        dokuLink = "[[https://www.google.com]]"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))

    def test_external_links_converted_properly(self):
        mdLink = "[Wouter Groeneveld](https://github.com/wgroeneveld/)"
        dokuLink = "[[https://github.com/wgroeneveld/|Wouter Groeneveld]]"

        self.assertEqual(mdLink, self.converter.convert(dokuLink))
