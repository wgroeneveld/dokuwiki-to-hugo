import os
import shutil

from src.hugo_file_config import HugoFileConfig
from src.markdown_converter import MarkdownConverter


class DokuWikiToHugo:

    def __init__(self):
        self.header_converter = HugoFileConfig()
        pass

    def create_output_dir(self):
        if os.path.exists('output'):
            print('output already exists, deleting old conversion stuff')
            shutil.rmtree('output')
        os.mkdir('output')

    def doku_to_hugo(self, dir):
        self.create_output_dir()
        for root, subFolders, files in os.walk(dir):
            for file in files:
                self.process_file(root, file)

    def process_file(self, root, file):
        destination_dir = 'output/' + root
        source_file = root + '/' + file
        print('generating ' + destination_dir + '/' + file + '\n')

        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        header = self.header_converter.create(source_file)
        converted_text = MarkdownConverter(source_file).convert()
        with open(destination_dir + '/' + file, "w") as text_file:
            text_file.write(header)
            text_file.write('\n')
            text_file.write(converted_text)
