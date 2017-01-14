import re

class MarkdownOrderedList:
    pattern = re.compile('(^-\s)(.*)', re.MULTILINE)

    def convert(self, text):
        lines = text.split('\n')
        last_used_linenr = 0
        index = 0
        result = text

        for match in MarkdownOrderedList.pattern.findall(text):
            line = ''.join(match)
            linenr = lines.index(line)

            if last_used_linenr + 1 is linenr:
                index = index + 1
            else:
                index = 1
            last_used_linenr = linenr

            result = result.replace(line, str(index) + '. ' + match[1])

        return result