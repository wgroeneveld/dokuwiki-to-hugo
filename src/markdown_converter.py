from functools import reduce

from src.markdown.links import MarkdownLinks

from src.markdown.headers import MarkdownHeader
from src.markdown.simplestyle import MarkdownItalic, MarkdownBold, MarkdownStrikeThrough


class MarkdownConverter:

    def __init__(self, file):
        self.file = file
        self.converters = (
            # TODO auto-discover these. How do I do that, without interfaces?
            MarkdownHeader(),
            MarkdownLinks(),
            MarkdownItalic(),
            MarkdownBold(),
            MarkdownStrikeThrough()
        )

    def convert(self):
        converted = []
        with open(self.file, 'r') as file:
            for line in file:
                converted.append(self.convert_line(line))

        return "\n".join(converted)

    def convert_line(self, line):
        convertfns = map(lambda converter: converter.convert, self.converters)
        massconvert = reduce(lambda red1, red2: lambda text: red1(red2(line)), convertfns, lambda text: text)
        return massconvert(line)
