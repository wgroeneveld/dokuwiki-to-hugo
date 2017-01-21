import re
from os import walk
from pathlib import Path

from src.dokuwiki_to_hugo import DokuWikiToHugo
from src.markdown_converter import MarkdownConverter


@MarkdownConverter.Register
class MarkdownLinks():
    # see http://pythex.org/
    pattern = re.compile('(\[\[)(.*?)(\]\])')

    def convert(self, text):
        result = text
        def starts_with_space(match):
            return match[1][0] is ' '

        for regex_link in MarkdownLinks.pattern.findall(text):
            if starts_with_space(regex_link):
                continue

            origlink = ''.join(regex_link)
            convertedlink = ""
            if "http" in origlink or "www" in origlink:
                convertedlink = self.convert_as_external_link(origlink)
            elif ">" in origlink and not "<" in origlink:
                convertedlink = self.convert_as_interwiki_link(origlink)
            else:
                convertedlink = self.convert_as_internal_link(origlink)
            result = result.replace(origlink, convertedlink)
        return result

    def parseUrl(self, text):
        return text[2:text.index('|')]

    def add_md_and_replace_home_with_index(self, src_url):
        url = src_url
        if "." not in url:
            url = url + ".md"
        return url.replace('home.md', '_index.md')
    def parseInternalUrl(self, text):
        url = text[2:len(text) - 2].replace(":", "/")
        return self.add_md_and_replace_home_with_index(url)
    def parseInternalUrlWithoutTitle(self, text):
        url = self.parseUrl(text).replace(":", "/")
        return self.add_md_and_replace_home_with_index(url)

    def parseTitle(self, text):
        return text[text.index('|') + 1: text.index(']]')]

    def convert_as_interwiki_link(self, text):
        interwiki_shortcode = text[2:text.index('>')]
        self.assert_interwiki_is_known(interwiki_shortcode)
        interwiki_urlpart = text[text.index('>') + 1 : len(text) - 2]

        return """{{< %s "%s" >}}""" % (interwiki_shortcode, interwiki_urlpart)

    def root_dir(self, url):
        if "/" not in url or DokuWikiToHugo.root_dir is None or url[0] is "/":
            return ""
        return DokuWikiToHugo.root_dir + "/"

    def convert_as_internal_link(self, text):
        url = ""
        title = ""
        if "|" not in text:
            url = self.parseInternalUrl(text)
            title = text[2:len(text)-2].replace(":", "/")
        else:
            url = self.parseInternalUrlWithoutTitle(text)
            title = self.parseTitle(text)

        return """[%s]({{< relref "%s%s" >}})""" % (title, self.root_dir(url), url.replace(' ', '_'))

    def convert_as_external_link(self, text):
        if '|' in text:
            url = self.parseUrl(text)
            title = self.parseTitle(text)
            return "[" + title + "](" + url + ")"
        url = text.replace('[', '').replace(']', '')
        return "[" + url + "](" + url + ")"

    def assert_interwiki_is_known(self, shortcode):
        shortcodes = []
        shortcodes_path = Path(__file__).parents[2].joinpath('layouts/shortcodes')
        for (dirpath, dirnames, filenames) in walk(shortcodes_path):
            shortcodes.extend(filenames)
            break
        if not shortcode in map(lambda x: x.replace(".html", ""), shortcodes):
            raise ValueError("Unknown Interwiki code " + shortcode + " - please add a shortcode in the layouts dir!")