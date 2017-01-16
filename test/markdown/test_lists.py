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

    def test_ordered_lists_super_deeply_deeper_than_deep_nested(self):
        src = '''
  - bla
    - blie
    - bloe
      - blee
  - bleh
        '''
        expected = '''
  1. bla
    1. blie
    2. bloe
      1. blee
  2. bleh
        '''
        actual = self.converter.convert(src)
        self.assertEqual(expected, actual)


    def test_ordered_lists_nested(self):
        src = '''
  - Werkt zoals Rummikub:
    - men kan combinaties van minimum 3 kaarten afleggen: 1,2,3
    - of 3,3,3 of meer
    - joker vult eender wat aan.
    - kaarten aanleggen aan bestaande combinaties mag ook
  - Ieder krijgt 7 kaarten, de rest vormt een hoop en men draait 1 kaart (de pot en de "vuilbak")
  - Om beurt trekken spelers kaarten (mag ook de bovenste zichtbare van de vuilbak zijn), speelt zijn ronde en legt verplicht één kaart op de vuilbak.
        '''
        expected = '''
  1. Werkt zoals Rummikub:
    1. men kan combinaties van minimum 3 kaarten afleggen: 1,2,3
    2. of 3,3,3 of meer
    3. joker vult eender wat aan.
    4. kaarten aanleggen aan bestaande combinaties mag ook
  2. Ieder krijgt 7 kaarten, de rest vormt een hoop en men draait 1 kaart (de pot en de "vuilbak")
  3. Om beurt trekken spelers kaarten (mag ook de bovenste zichtbare van de vuilbak zijn), speelt zijn ronde en legt verplicht één kaart op de vuilbak.
        '''

        actual = self.converter.convert(src)
        self.assertEqual(expected, actual)

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