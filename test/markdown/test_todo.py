from unittest import TestCase

from src.markdown.todo import MarkdownTodo


class TestMarkdownTodo(TestCase):

    def setUp(self):
        self.converter = MarkdownTodo()

    def test_converts_todos_with_marked_as_done(self):
        src = '''
            <todo>item 1</todo>
            <todo #>item 2</todo>
            '''
        expected = '''
            - [ ] item 1
            - [x] item 2
            '''
        self.assertEqual(expected, self.converter.convert(src))

    def test_converts_todos(self):
        src = '''
            <todo>item 1</todo>
            <todo>item 2</todo>
            '''
        expected = '''
            - [ ] item 1
            - [ ] item 2
            '''
        self.assertEqual(expected, self.converter.convert(src))
