from argparse import Action, SUPPRESS
from Ra.modules.network import * 

import sys as _sys

class NegateAction(Action):
    def __call__(self, parser, ns, values, option):
        setattr(ns, self.dest, option[2:4] != 'un')
        setattr(ns, self.dest, option[2:4] != 'no')

class WlansAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        networks = ...
        formatter = parser._get_formatter()
        formatter.add_text(networks)
        parser._print_message(formatter.format_help(), _sys.stdout)
        parser.exit()
