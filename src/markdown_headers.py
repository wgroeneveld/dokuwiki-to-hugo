from collections import OrderedDict

class MarkdownHeader:
    head = "="
    config = {
        '======': 1,
        '=====': 2,
        '====': 3,
        '===': 4,
        '==': 5
    }

    def convert(self, text):
        config = OrderedDict(sorted(MarkdownHeader.config.items(), key = lambda t : t[1]))

        for key, val in config.items():
            if text.startswith(key):
                return ('#' * val) + self.strip(text)
        return text


    def strip(self, text):
        return text.replace(MarkdownHeader.head, "")
