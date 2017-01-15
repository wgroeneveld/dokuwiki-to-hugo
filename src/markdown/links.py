import re
from os import walk

from src.markdown_converter import MarkdownConverter


@MarkdownConverter.Register
class MarkdownLinks():
    # see http://pythex.org/
    pattern = re.compile('(\[\[)(.*?)(\]\])')

    def convert(self, text):
        result = text
        for regex_link in MarkdownLinks.pattern.findall(text):
            origlink = ''.join(regex_link)
            convertedlink = ""
            if "http" in origlink or "www" in origlink:
                convertedlink = self.convert_as_external_link(origlink)
            elif ">" in origlink:
                convertedlink = self.convert_as_interwiki_link(origlink)
            else:
                convertedlink = self.convert_as_internal_link(origlink)
            result = result.replace(origlink, convertedlink)
        return result

    def parseUrl(self, text):
        return text[2:text.index('|')]

    def parseInternalUrl(self, text):
        return text[2:len(text)-2].replace(":", "/")

    def parseTitle(self, text):
        return text[text.index('|') + 1: text.index(']]')]

    def convert_as_interwiki_link(self, text):
        interwiki_shortcode = text[2:text.index('>')]
        self.assert_interwiki_is_known(interwiki_shortcode)
        interwiki_urlpart = text[text.index('>') + 1 : len(text) - 2]

        return """{{< %s %s >}}""" % (interwiki_shortcode, interwiki_urlpart)

    def convert_as_internal_link(self, text):
        if "|" not in text:
            return """{{< relref "%s" >}}""" % (self.parseInternalUrl(text))

        url = self.parseUrl(text).replace(":", "/")
        title = self.parseTitle(text)

        return """[%s]({{< relref "%s" >}})""" % (title, url)

    def convert_as_external_link(self, text):
        url = self.parseUrl(text)
        title = self.parseTitle(text)

        return "[" + title + "](" + url + ")"

    def assert_interwiki_is_known(self, shortcode):
        shortcodes = []
        for (dirpath, dirnames, filenames) in walk("../layouts/shortcodes"):
            shortcodes.extend(filenames)
            break
        if not shortcode in map(lambda x: x.replace(".html", ""), shortcodes):
            raise ValueError("Unknown Interwiki code " + shortcode + " - please add a shortcode in the layouts dir!")