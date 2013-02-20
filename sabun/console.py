# -*- coding: utf-8 -*-

import argparse
import watcher


def main():
    args = parse()
    watcher.process(args)


def parse():
    parser = argparse.ArgumentParser(
        description='Easy and Simple TODO Logger')
    parser.add_argument(
        'watchpath', help="watch TODO file.")
    parser.add_argument(
        'outputpath', help="output Logging TODO diff.")
    parser.add_argument(
        '--color', action="store_true", help="logging terminal with color.")
    parser.add_argument(
        '--debug', action="store_true", help="debug mode for develover.")

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()
