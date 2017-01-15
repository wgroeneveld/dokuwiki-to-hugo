from re import compile

from src.markdown_converter import MarkdownConverter


@MarkdownConverter.Register
class MarkdownHeader():
    pattern = compile('(=+)(.*?)(=+)')
    head = "="
    config = {
        '======': 1,
        '=====': 2,
        '====': 3,
        '===': 4,
        '==': 5
    }

    def convert(self, text):
        result = text
        for regex_head in MarkdownHeader.pattern.findall(text):
            orig_header = ''.join(regex_head)
            new_header = ('#' * MarkdownHeader.config[regex_head[0]]) + regex_head[1]
            result = result.replace(orig_header, new_header)
        return result
