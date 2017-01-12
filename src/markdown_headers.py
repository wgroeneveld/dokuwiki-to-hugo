
class MarkdownHeader:

    def convert(self, text):
        if not text.startswith("="):
            return text
        elif text.startswith("== "):
            return "######" + self.strip(text)
        return "##"

    def strip(self, text):
        return text.replace("=", "")
