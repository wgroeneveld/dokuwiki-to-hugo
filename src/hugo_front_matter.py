import os.path
import time


class HugoFrontMatter:

    def filename(self, location):
        return location.split('/')[-1][0:-4]

    def strip_extension(self, filename):
        if '.' in filename:
            return filename[0:len(filename) - 4]
        return filename

    def create(self, file_location, frontmatter_tags=True):
        title = self.filename(file_location)
        tags = list(map(self.strip_extension, file_location.split('/')))
        tags_content = '''\ntags = [
%s
]\n''' % (',\n'.join(map(lambda tag: '    "' + tag + '"', tags)))
        date = time.strftime('%Y-%m-%d', time.gmtime(os.path.getmtime(file_location)))
        return """+++
title = "%s"
draft = false%s
date = "%s"
+++""" % (title, tags_content if frontmatter_tags else '', date)
