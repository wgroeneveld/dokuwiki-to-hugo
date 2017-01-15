from abc import ABC
from re import compile

from src.markdown_converter import MarkdownConverter


class NopStyle(ABC):
    def convert(self, text):
        return text

class SimpleReplacementStyle(ABC):
    def __init__(self, markdown_style, dokuwiki_style):
        self.markdown_style = markdown_style
        self.dokuwiki_style = dokuwiki_style

    def convert(self, text):
        return text.replace(self.dokuwiki_style, self.markdown_style)

class SimpleStyleBetweenTags(ABC):

    def __init__(self, markdown_style, dokuwiki_style_begin, dokuwiki_style_end = None):
        if dokuwiki_style_end is None:
            dokuwiki_style_end = dokuwiki_style_begin
        self.pattern = compile('(' + dokuwiki_style_begin + ')(.*?)(' + dokuwiki_style_end + ')')
        self.markdown_style = markdown_style

    def convert(self, text):
        result = text
        for regex_head in self.pattern.findall(text):
            orig_header = ''.join(regex_head)
            new_header = self.markdown_style + regex_head[1] + self.markdown_style
            result = result.replace(orig_header, new_header)
        return result

@MarkdownConverter.Register
class MarkdownLineBreak(SimpleReplacementStyle):
    def __init__(self):
        super().__init__('<br/>', '\\')

# inline html is supported with Hugo, don't need the tags.
@MarkdownConverter.Register
class MarkdownInlineHtml():
    def convert(self, text):
        return text.replace('<html>', '').replace('</html>', '')

# bold in Doku is bold in MD
@MarkdownConverter.Register
class MarkdownBold(NopStyle):
    pass

@MarkdownConverter.Register
class MarkdownItalic(SimpleStyleBetweenTags):
    def __init__(self):
        super().__init__('*', '//')

@MarkdownConverter.Register
class MarkdownStrikeThrough(SimpleStyleBetweenTags):
    def __init__(self):
        super().__init__('~~', '<del>', '</del>')

@MarkdownConverter.Register
class MarkdownInlineCode(SimpleStyleBetweenTags):
    def __init__(self):
        super().__init__('`', "''", "''")