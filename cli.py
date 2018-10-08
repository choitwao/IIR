from argparse import ArgumentParser


class Cli:

    @staticmethod
    def create_parser():
        # create the main parser for CLI
        command_parser = ArgumentParser(prog="SPIMI",
                                        description="SPIMI query tester")
        # create branches for PHRASE, AND and OR
        method_parsers = command_parser.add_subparsers(help='[command] help',
                                                       dest="subparser_name")
        method_parsers.required = True
        # create a general template for GET and POST
        template_parser = ArgumentParser(add_help=False,
                                         conflict_handler='resolve')
        template_parser.add_argument('URL',
                                     metavar="term1,term2,term3N",
                                     action="store",
                                     help="The terms of your choice")
        # INIT command
        init_parser = method_parsers.add_parser('init')
        init_parser.add_argument('-m',
                                 dest='memory_size',
                                 action='store',
                                 metavar='INT',
                                 help='User defined maximum memory size.')
        init_parser.add_argument('-b',
                                 dest='block_size',
                                 action='store',
                                 metavar='INT',
                                 help='User defined block size.')
        # PHRASE command
        get_parser = method_parsers.add_parser('phrase', parents=[template_parser])
        # AND command
        get_parser = method_parsers.add_parser('and', parents=[template_parser])
        # OR command
        get_parser = method_parsers.add_parser('or', parents=[template_parser])
        return command_parser