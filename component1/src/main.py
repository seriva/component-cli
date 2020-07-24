import sys
import argparse

from Parser import Parser

def init(args):
    print('init')
    return 0

def apply(args):
    print('apply')
    return 0

def _main() -> None:
    parser = Parser(
        init=init,
        apply=apply
    )
    return parser.run(sys.argv)

if __name__ == '__main__':
    exit(_main())