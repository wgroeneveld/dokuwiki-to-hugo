from collections import OrderedDict
from re import compile

class MarkdownHeader:
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
            orig_header = regex_head[0] + regex_head[1] + regex_head[2]
            new_header = ('#' * MarkdownHeader.config[regex_head[0]]) + regex_head[1]
            result = result.replace(orig_header, new_header)
        return result
