import argparse

from src.dokuwiki_to_hugo import DokuWikiToHugo


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def main(directory, options):
    DokuWikiToHugo(options.root, front_matter=options.front_matter).doku_to_hugo(directory)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", help="the directory of your DokuWiki pages collection", required=True)
    parser.add_argument("-r", "--root", help="the root directory name in your hugo content where to link to",
                        required=False)
    parser.add_argument("--front_matter", default=True, type=str2bool,
                        help="whether to generate front matter in the converted markdown.")
    opts = parser.parse_args()
    main(opts.dir, opts)
