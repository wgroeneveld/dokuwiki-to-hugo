from unittest import TestCase

from src.markdown.code import MarkdownCode, MarkdownFile


class TestMarkdownCode(TestCase):
    def setUp(self):
        self.code_converter = MarkdownCode()
        self.file_converter = MarkdownFile()

    def test_convert_file_without_language(self):
        src = """
        blabla
        <file>
            this
            that
        </file>
        blehbleh
        """

        expected = """
        blabla
        ```
            this
            that
        ```
        blehbleh
        """

        self.assertEqual(expected, self.file_converter.convert(src))

    def test_convert_file_with_some_language(self):
        src = """
        blabla
        <file php myfile.php>
            $cool = "yoo";
            echo $cool;
        </file>
        blehbleh
        """

        expected = """
        blabla
        ```php
            $cool = "yoo";
            echo $cool;
        ```
        blehbleh
        """

        self.assertEqual(expected, self.file_converter.convert(src))

    def test_convert_code_with_specific_language(self):
        src = """
        blabla
        <code php>
            $_REQUEST = 'sup';
            echo "yoo";
        </code>
        blehbleh
        """

        expected = """
        blabla
        ```php
            $_REQUEST = 'sup';
            echo "yoo";
        ```
        blehbleh
        """

        self.assertEqual(expected, self.code_converter.convert(src))

    def test_convert_code_without_language(self):
        src = """
        blabla
        <code>
            this
            that
        </code>
        blehbleh
        """

        expected = """
        blabla
        ```
            this
            that
        ```
        blehbleh
        """

        self.assertEqual(expected, self.code_converter.convert(src))
