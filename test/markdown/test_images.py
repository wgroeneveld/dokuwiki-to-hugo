from unittest import TestCase

from src.markdown.images import MarkdownImages


class TestMarkdownImages(TestCase):
    def setUp(self):
        self.converter = MarkdownImages()

    def test_simple_image_embed(self):
        src = "{{img.png}}"
        expected = "<img style='' src='/img/img.png'>"
        self.assertEqual(expected, self.converter.convert(src))

    def test_image_in_subdir(self):
        src = "{{:dir:subdir:img.png}}"
        expected = "<img style='' src='/img//dir/subdir/img.png'>"  # I really don't care about the double slash
        self.assertEqual(expected, self.converter.convert(src))

    def test_image_left_aligned(self):
        src = "{{ img.png}}"
        expected = "<img style='float: left;' src='/img/img.png'>"
        self.assertEqual(expected, self.converter.convert(src))

    def test_image_right_aligned(self):
        src = "{{img.png }}"
        expected = "<img style='float: right;' src='/img/img.png'>"
        self.assertEqual(expected, self.converter.convert(src))

    def test_image_right_aligned_with_specific_dimensions(self):
        src = "{{ img.png?500x400}}"
        expected = "<img style='float: left; width: 500px; height: 400px;' src='/img/img.png'>"
        self.assertEqual(expected, self.converter.convert(src))

    def test_image_center_aligned(self):
        src = "{{ img.png }}"
        expected = "<img style='margin-left: auto; margin-right: auto;' src='/img/img.png'>"
        self.assertEqual(expected, self.converter.convert(src))

    def test_image_with_specific_dimensions(self):
        src = "{{img.png?500x400}}"
        expected = "<img style='width: 500px; height: 400px;' src='/img/img.png'>"
        self.assertEqual(expected, self.converter.convert(src))

    def test_image_with_specific_width(self):
        src = "{{img.png?500}}"
        expected = "<img style='width: 500px;' src='/img/img.png'>"
        self.assertEqual(expected, self.converter.convert(src))
