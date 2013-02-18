# -*- coding: utf-8 -*-

import argparse
import watcher


def main():
    args = parse()
    watcher.process(args.watchpath, args.outputpath)


def parse():
    parser = argparse.ArgumentParser(
        description='Easy and Simple TODO Logger')
    parser.add_argument(
        'watchpath', help="watch TODO file.")
    parser.add_argument(
        'outputpath', help="output Logging TODO diff.")

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()
