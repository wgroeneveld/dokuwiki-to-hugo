import os
import shutil

from hugo_front_matter import HugoFrontMatter
from markdown_converter import MarkdownConverter


class DokuWikiToHugo:
    root_dir = ""

    def __init__(self, root=None, frontmatter_tags=True):
        self.header_converter = HugoFrontMatter()
        self.frontmatter_tags = frontmatter_tags
        DokuWikiToHugo.root_dir = root
        pass

    def create_output_dir(self):
        if os.path.exists('output'):
            print('output already exists, deleting old conversion stuff')
            shutil.rmtree('output')
        os.mkdir('output')

    def doku_to_hugo(self, directory):
        self.create_output_dir()
        for root, subFolders, files in os.walk(directory):
            files = [f for f in files if not f[0] == '.']
            for file in files:
                try:
                    self.process_file(root, file)
                except:
                    print('failed to convert ' + file)

    def process_file(self, root, file):
        destination_dir = 'output/' + root
        source_file = root + '/' + file
        destination_file = '_index.md' if file == 'home.txt' else os.path.splitext(file)[0] + '.md'

        print('generating ' + destination_dir + '/' + destination_file + '\n')

        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        header = self.header_converter.create(source_file, frontmatter_tags=self.frontmatter_tags)
        converted_text = MarkdownConverter(source_file).convert()

        with open(destination_dir + '/' + destination_file, "w") as text_file:
            text_file.write(header)
            text_file.write('\n')
            text_file.write(converted_text)
