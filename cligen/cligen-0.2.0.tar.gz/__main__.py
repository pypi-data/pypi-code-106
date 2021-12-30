# coding: utf-8
# flake8: noqa
# cligen: 0.1.7, dd: 2021-12-30

import argparse
import importlib
import sys

from . import __version__


class DefaultVal:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)


class CountAction(argparse.Action):
    """argparse action for counting up and down

    standard argparse action='count', only increments with +1, this action uses
    the value of self.const if provided, and +1 if not provided

    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', action=CountAction, const=1,
            nargs=0)
    parser.add_argument('--quiet', '-q', action=CountAction, dest='verbose',
            const=-1, nargs=0)
    """

    def __call__(self, parser, namespace, values, option_string=None):
        if self.const is None:
            self.const = 1
        try:
            val = getattr(namespace, self.dest) + self.const
        except TypeError:  # probably None
            val = self.const
        setattr(namespace, self.dest, val)


def main(cmdarg=None):
    cmdarg = sys.argv if cmdarg is None else cmdarg
    parsers = []
    parsers.append(argparse.ArgumentParser(formatter_class=SmartFormatter))
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), dest='_gl_verbose', metavar='VERBOSE', nargs=0, help='D|increase verbosity level', action=CountAction)
    parsers[-1].add_argument('--debug', default=None, dest='_gl_debug', action='store_true', help='insert debug statements in generated code')
    parsers[-1].add_argument('--version', action='store_true', help='show program\'s version number and exit')
    subp = parsers[-1].add_subparsers()
    px = subp.add_parser('gen', help='execute show related commands', formatter_class=SmartFormatter)
    px.set_defaults(subparser_func='gen')
    parsers.append(px)
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), nargs=0, help='D|increase verbosity level', action=CountAction)
    parsers[-1].add_argument('--debug', default=DefaultVal(False), action='store_true', help='insert debug statements in generated code')
    px = subp.add_parser('replace', help='replace a string in the _cligen_data/cli.yaml', formatter_class=SmartFormatter)
    px.set_defaults(subparser_func='replace')
    parsers.append(px)
    parsers[-1].add_argument('--from', dest='frm', help='original string to match', required=True)
    parsers[-1].add_argument('--to', help='replacement string', required=True)
    parsers[-1].add_argument('--backup', action='store_true', help='make a timestamped backup of the file (.YYYYMMDD-HHMMSS)')
    parsers[-1].add_argument('path', nargs='*', help='path pattern to scan for replacement (default: %(default)s)')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), nargs=0, help='D|increase verbosity level', action=CountAction)
    parsers[-1].add_argument('--debug', default=DefaultVal(False), action='store_true', help='insert debug statements in generated code')
    px = subp.add_parser('convert', help='analyse argument file and generate cligen data', formatter_class=SmartFormatter)
    px.set_defaults(subparser_func='convert')
    parsers.append(px)
    parsers[-1].add_argument('--append', action='store_true', help='append _cligen_data to __init__.py')
    parsers[-1].add_argument('path')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), nargs=0, help='D|increase verbosity level', action=CountAction)
    parsers[-1].add_argument('--debug', default=DefaultVal(False), action='store_true', help='insert debug statements in generated code')
    px = subp.add_parser('comment', help='show cligen_data comments (from cligen.__init__.py)', formatter_class=SmartFormatter)
    px.set_defaults(subparser_func='comment')
    parsers.append(px)
    parsers[-1].add_argument('--update', help='update cligen_data comments in __init__.py (argument can be directory or file)')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), nargs=0, help='D|increase verbosity level', action=CountAction)
    parsers[-1].add_argument('--debug', default=DefaultVal(False), action='store_true', help='insert debug statements in generated code')
    parsers.pop()
    # sp: gen
    _subparser_found = False
    for arg in cmdarg[1:]:
        if arg in ['-h', '--help', '--version']:  # global help if no subparser
            break
    else:
        for sp_name in ['gen', 'replace', 'convert', 'comment']:
            if sp_name in cmdarg[1:]:
                break
        else:
            # insert default in first position, this implies no
            # global options without a sub_parsers specified
            cmdarg.insert(1, 'gen')
    if '--version' in cmdarg[1:]:
        if '-v' in cmdarg[1:] or '--verbose' in cmdarg[1:]:
            return list_versions(pkg_name='cligen', version=None, pkgs=['ruamel.yaml'])
        print(__version__)
        return
    if '--help-all' in cmdarg[1:]:
        try:
            parsers[0].parse_args(['--help'])
        except SystemExit:
            pass
        for sc in parsers[1:]:
            print('-' * 72)
            try:
                parsers[0].parse_args([sc.prog.split()[1], '--help'])
            except SystemExit:
                pass
        sys.exit(0)
    args = parsers[0].parse_args(args=cmdarg[1:])
    for gl in ['verbose', 'debug']:
        glv = getattr(args, '_gl_' + gl, None)
        if isinstance(getattr(args, gl, None), (DefaultVal, type(None))) and glv is not None:
            setattr(args, gl, glv)
        delattr(args, '_gl_' + gl)
        if isinstance(getattr(args, gl), DefaultVal):
            setattr(args, gl, getattr(args, gl).val)
    cls = getattr(importlib.import_module('cligen.cligen'), 'CligenLoader')
    obj = cls(args)
    funcname = getattr(args, 'subparser_func', None)
    if funcname is None:
        parsers[0].parse_args('--help')
    fun = getattr(obj, args.subparser_func)
    return fun()


class SmartFormatter(argparse.HelpFormatter):
    """
    you can only specify one formatter in standard argparse, so you cannot
    both have pre-formatted description (RawDescriptionHelpFormatter)
    and ArgumentDefaultsHelpFormatter.
    The SmartFormatter has sensible defaults (RawDescriptionFormatter) and
    the individual help text can be marked ( help="R|" ) for
    variations in formatting.
    version string is formatted using _split_lines and preserves any
    line breaks in the version string.
    If one help string starts with D|, defaults will be added to those help
    lines that do not have %(default)s in them
    """

    _add_defaults = True  # make True parameter based on tag?

    def __init__(self, *args, **kw):
        super(SmartFormatter, self).__init__(*args, **kw)

    def _fill_text(self, text, width, indent):
        return ''.join([indent + line for line in text.splitlines(True)])

    def _split_lines(self, text, width):
        if text.startswith('D|'):
            SmartFormatter._add_defaults = True
            text = text[2:]
        elif text.startswith('*|'):
            text = text[2:]
        if text.startswith('R|'):
            return text[2:].splitlines()
        return argparse.HelpFormatter._split_lines(self, text, width)

    def _get_help_string(self, action):
        if SmartFormatter._add_defaults is None:
            return argparse.HelpFormatter._get_help_string(self, action)
        help = action.help
        if '%(default)' not in action.help:
            if action.default is not argparse.SUPPRESS:
                defaulting_nargs = [argparse.OPTIONAL, argparse.ZERO_OR_MORE]
                if action.option_strings or action.nargs in defaulting_nargs:
                    help += ' (default: %(default)s)'
        return help

    def _expand_help(self, action):
        """mark a password help with '*|' at the start, so that
        when global default adding is activated (e.g. through a helpstring
        starting with 'D|') no password is show by default.
        Orginal marking used in repo cannot be used because of decorators.
        """
        hs = self._get_help_string(action)
        if hs.startswith('*|'):
            params = dict(vars(action), prog=self._prog)
            if params.get('default') is not None:
                # you can update params, this will change the default, but we
                # are printing help only after this
                params['default'] = '*' * len(params['default'])
            return self._get_help_string(action) % params
        return super(SmartFormatter, self)._expand_help(action)


def list_versions(pkg_name, version, pkgs):
    version_data = [
        ('Python', '{v.major}.{v.minor}.{v.micro}'.format(v=sys.version_info)),
        (pkg_name, __version__ if version is None else version),
    ]
    for pkg in pkgs:
        try:
            version_data.append(
                (pkg,  getattr(importlib.import_module(pkg), '__version__', '--'))
            )
        except ModuleNotFoundError:
            version_data.append((pkg, 'NA'))
        except KeyError:
            pass
    longest = max([len(x[0]) for x in version_data]) + 1
    for pkg, ver in version_data:
        print('{:{}s} {}'.format(pkg + ':', longest, ver))


if __name__ == '__main__':
    sys.exit(main())
