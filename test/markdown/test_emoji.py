from unittest import TestCase

from src.markdown.emoji import MarkdownEmoji


class TestMarkdownEmoji(TestCase):
    def setUp(self):
        self.converter = MarkdownEmoji()

    def test_replace_one_emoji(self):
        self.assertEqual(":simple_smile:", self.converter.convert(":-)"))

    def test_replace_some_emojis_in_one_line(self):
        src = "hi! :-) how are you? :-/ heh"
        expected = "hi! :simple_smile: how are you? :confused: heh"

        self.assertEqual(expected, self.converter.convert(src))
