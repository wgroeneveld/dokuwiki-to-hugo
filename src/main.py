import argparse

from src.dokuwiki_to_hugo import DokuWikiToHugo


def main(dir):
    DokuWikiToHugo().doku_to_hugo(dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", help="the root directory of your DokuWiki pages collection", required = True)
    opts = parser.parse_args()
    main(opts.dir)
