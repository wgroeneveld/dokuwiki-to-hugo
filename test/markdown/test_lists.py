from unittest import TestCase

from src.markdown.lists import MarkdownOrderedList


class TestMarkdownLists(TestCase):
    def setUp(self):
        self.converter = MarkdownOrderedList()

    def test_dont_convert_if_no_list_found(self):
        self.assertEqual('hello there', self.converter.convert('hello there'))

    def test_only_convert_dashes_if_beginning_sentence(self):
        src = '''
- one-two-three
- four

five - six
        '''
        expected = '''
1. one-two-three
2. four

five - six
        '''

        self.assertEqual(expected, self.converter.convert(src))

    def test_multiple_ordered_lists_in_text(self):
        src = '''
- one
- two

three
- four
- five
six
        '''
        expected = '''
1. one
2. two

three
1. four
2. five
six
        '''

        self.assertEqual(expected, self.converter.convert(src))

    def test_single_ordered_list(self):
        src = '''
- one
- two

three
        '''
        expected = '''
1. one
2. two

three
        '''

        self.assertEqual(expected, self.converter.convert(src))