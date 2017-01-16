from src.markdown_converter import MarkdownConverter
from re import compile

@MarkdownConverter.Register
class MarkdownImages:
    pattern = compile('{{(\s?)(.*?)(\s?)}}')

    def parse_style(self, match):
        style = []
        left = match[0]
        src = match[1]
        right = match[2]

        def parse_dimensions():
            if not '?' in src:
                return
            dimensions = src.split("?")[1]
            if 'x' in dimensions:
                (width, height) = dimensions.split("x")
                style.append("width: " + width + "px;")
                style.append("height: " + height + "px;")
            else:
                style.append("width: " + dimensions + "px;")
        def parse_position():
            if len(left) > 0 and len(right) > 0:
                style.append("margin-left: auto; margin-right: auto;")
            elif len(left) > 0:
                style.append("float: left;")
            elif len(right) > 0:
                style.append("float: right;")

        parse_position()
        parse_dimensions()
        return ' '.join(style)

    def parse_source(self, src):
        source = src if not '?' in src else src.split('?')[0]
        return source.replace(':', '/')

    def convert(self, text):
        result = text
        for match in MarkdownImages.pattern.findall(text):
            replaced = "<img style='%s' src='/img/%s'>" % (self.parse_style(match), self.parse_source(match[1]))
            result = result.replace('{{' + ''.join(match) + '}}', replaced)
        return result