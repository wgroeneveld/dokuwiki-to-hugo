from re import compile

from src.markdown_converter import MarkdownConverter


@MarkdownConverter.register
class MarkdownHeader:
    pattern = compile('(=+)(.*?)(=+)')
    head = "="
    config = {
        '======': 1,
        '=====': 2,
        '====': 3,
        '===': 4,
        '==': 5,
        '=': 6
    }

    def convert(self, text):
        result = text
        for regex_head in MarkdownHeader.pattern.findall(text):
            orig_header = ''.join(regex_head)
            src_header = regex_head[0]
            if src_header in MarkdownHeader.config:
                new_header = ('#' * MarkdownHeader.config[src_header]) + regex_head[1]
                result = result.replace(orig_header, new_header)
        return result
