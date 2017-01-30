import argparse

from src.dokuwiki_to_hugo import DokuWikiToHugo


def main(directory, root):
    DokuWikiToHugo(root).doku_to_hugo(directory)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", help="the directory of your DokuWiki pages collection", required=True)
    parser.add_argument("-r", "--root", help="the root directory name in your hugo content where to link to",
                        required=False)
    opts = parser.parse_args()
    main(opts.dir, opts.root)
