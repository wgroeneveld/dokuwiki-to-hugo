from unittest import TestCase

from src.markdown.simplestyle import MarkdownBold, MarkdownItalic, MarkdownStrikeThrough, MarkdownLineBreak


class TestMarkdownSimpleStyles(TestCase):

    def test_some_linebreaks(self):
        src = '''
        hello \\
        is it me you're looking for?\\
        i can see it in your eyes...
        '''
        expected = '''
        hello <br/>
        is it me you're looking for?<br/>
        i can see it in your eyes...
        '''

        self.assertEqual(expected, MarkdownLineBreak().convert(src))

    def test_some_strikethrough_style(self):
        src = 'some <del>deleted</del> style'
        self.assertEqual('some ~~deleted~~ style', MarkdownStrikeThrough().convert(src))

    def test_some_italic_styles(self):
        src = '//italic// stuff right //there// bam!'
        self.assertEqual('*italic* stuff right *there* bam!', MarkdownItalic().convert(src))

    def test_some_bold_styles(self):
        src = '** this is bold** and so is **this**'
        self.assertEqual(src, MarkdownBold().convert(src))