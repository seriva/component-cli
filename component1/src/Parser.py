import sys
import argparse

from Log import Log
from Config import Config
from info import info

class Parser:
    def __init__(self, init=None, apply=None):
        self.logger = Log('main')
        self.config = Config()
        self.init = init
        self.apply = apply

        self.parser = argparse.ArgumentParser(
            description=__doc__,
            usage='''<command> [<args>]''',
            formatter_class=argparse.RawTextHelpFormatter)
        subparsers = self.parser.add_subparsers()

        def info_parser(subparsers):
            sub_parser = subparsers.add_parser('info', description='info')
            def run_info(args):
                return info()
            sub_parser.set_defaults(func=run_info)
        info_parser(subparsers)

        try:
            if self.init != None:
                def init_parser(subparsers):
                    sub_parser = subparsers.add_parser('init', description='init')
                    def run_init(args):
                        return self.init(args)
                    sub_parser.set_defaults(func=run_init)
                init_parser(subparsers)
            else:
                raise Exception('Missing "init" inferface')

            if self.apply != None:
                def apply_parser(subparsers):
                    sub_parser = subparsers.add_parser('apply', description='apply')
                    def run_apply(args):
                        print('apply')
                    sub_parser.set_defaults(func=run_apply)
                apply_parser(subparsers)
            else:
                raise Exception('Missing "apply" inferface')

            #TODO: add complete interface here.
        except Exception as e:
            self.logger.error(e, exc_info=(self.config.debug > 0))
            sys.exit(1)

    def run(self, args):
        if len(args) < 2:
            self.parser.print_help()
            return 0

        arguments = args[1:]
        args = self.parser.parse_args(arguments)

        try:
            return args.func(args)
        except Exception as e:
            logger.error(e, exc_info=(config.debug > 0))
            return 1
