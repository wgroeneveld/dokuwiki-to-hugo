from abc import ABC
from re import compile

from src.markdown_converter import MarkdownConverter

class BaseMarkdownCode(ABC):
    markdown = "```"

    def __init__(self, tag):
        self.tag = tag
        self.pattern = compile('(<' + tag + '(.*?)>)')

    def strip_lang(self, language):
        if(language is ''):
            return language

        lang = language[1:len(language)]
        if(' ' in lang):
            lang = lang[0:lang.index(' ')]
        return lang

    def convert(self, text):
        result = text
        for match in self.pattern.findall(text):
            language = self.strip_lang(match[1])
            result = result.replace(match[0], BaseMarkdownCode.markdown + language)
        return result.replace('</' + self.tag + '>', BaseMarkdownCode.markdown)

@MarkdownConverter.Register
class MarkdownFile(BaseMarkdownCode):
    def __init__(self):
        super().__init__('file')

@MarkdownConverter.Register
class MarkdownCode(BaseMarkdownCode):
    def __init__(self):
        super().__init__('code')

