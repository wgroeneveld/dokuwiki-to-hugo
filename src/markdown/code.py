from abc import ABC
from re import compile

from src.markdown_converter import MarkdownConverter


# PEP8 fault, could be static or function instead of method (not in class context)
def strip_lang(language):
    if language is '':
        return language

    lang = language[1:len(language)]
    if ' ' in lang:
        lang = lang[0:lang.index(' ')]
    return lang


class BaseMarkdownCode(ABC):
    markdown = "```"

    def __init__(self, tag):
        self.tag = tag
        self.pattern = compile('(<' + tag + '(.*?)>)')

    def convert(self, text):
        result = text
        for match in self.pattern.findall(text):
            language = strip_lang(match[1])
            result = result.replace(match[0], BaseMarkdownCode.markdown + language)
        return result.replace('</' + self.tag + '>', BaseMarkdownCode.markdown)


@MarkdownConverter.register
class MarkdownFile(BaseMarkdownCode):
    def __init__(self):
        super().__init__('file')


@MarkdownConverter.register
class MarkdownCode(BaseMarkdownCode):
    def __init__(self):
        super().__init__('code')

