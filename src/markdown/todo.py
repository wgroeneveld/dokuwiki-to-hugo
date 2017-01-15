from src.markdown_converter import MarkdownConverter
from re import compile

@MarkdownConverter.Register
class MarkdownTodo():
    pattern = compile('(<todo(\s#)?>)(.*?)(</todo>)')
    todo = '- [ ] '
    done = '- [x] '

    def convert(self, text):
        result = text
        for match in MarkdownTodo.pattern.findall(text):
            prefix = MarkdownTodo.todo if match[1] is '' else MarkdownTodo.done
            result = result.replace(match[0] + match[2] + match[3], prefix + match[2])
        return result