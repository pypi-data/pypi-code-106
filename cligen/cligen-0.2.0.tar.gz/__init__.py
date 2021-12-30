# coding: utf-8
# flake8: noqa


_package_data = dict(
    full_package_name='cligen',
    version_info=(0, 2, 0),
    __version__='0.2.0',
    version_timestamp='2021-12-30 11:09:11',
    author='Anthon van der Neut',
    author_email='a.van.der.neut@ruamel.eu',
    description='generate __main__.py with argparse setup generated from YAML',
    keywords='pypi statistics',
    data_files=["_action/*", ],
    entry_points='cligen=cligen.__main__:main',
    # entry_points=None,
    license='MIT',
    since=2021,
    # status="α|β|stable",  # the package status on PyPI
    # data_files="",
    # universal=True,  # py2 + py3
    install_requires=['ruamel.yaml'],
    tox=dict(env='3', ),  # *->all p->pypy
    python_requires='>=3',
    print_allowed=True,
)


version_info = _package_data['version_info']
__version__ = _package_data['__version__']


_cligen_data = """\
# all tags start with an uppercase char and can often be shortened to three and/or one
# characters. If a tag has multiple uppercase letter, only using the uppercase letters is a
# valid shortening
# Tags used:
# !Commandlineinterface, !Cli,
# !Option, !Opt, !O
  # - !Option [all, !Action store_true, !Help build sdist and wheels for all platforms]
# !PreSubparserOption, !PSO
# !Help, !H
# !Argument, !Arg
  # - !Arg [files, nargs: '*', !H files to process]
# !Module   # make subparser function calls imported from module
# !Instance # module.Class: assume subparser method calls on instance of Class imported from module
# !Main     # function to call/class to instantiater,, no subparsers
# !Action # either one of the actions in subdir _action (by stem of the file) or e.g. "store_action"
# !Config YAML/INI/PON  read defaults from config file
# !AddDefaults ' (default: %(default)s)'
# !Prolog (sub-)parser prolog/description text (for multiline use | )
# !Epilog (sub-)parser epilog text (for multiline use | )
# !NQS used on arguments, makes sure the scalar is non-quoted e.g for instance/method/function
#      call arguments, when cligen knows about what argument a keyword takes, this is not needed
!Cli 0:
- !Instance cligen.cligen.CligenLoader
- !Option [verbose, v, !Help D|increase verbosity level, !Action count]
- !Option [debug, !Action store_true, !H insert debug statements in generated code]
# - !PSO [config, !Help directory to store, default: '~/.config/test42/']
- gen:
  - !DefaultSubparser
  - !Help execute show related commands
- replace:
  - !Help replace a string in the _cligen_data/cli.yaml
  - !ReqOption [from, dest: frm, !H original string to match]
  - !ReqOption [to, !H replacement string]
  - !Option [backup, !Action store_true, !H make a timestamped backup of the file (.YYYYMMDD-HHMMSS)]
  - !Argument [path, nargs: '*',
               default: ['**/__init__.py', '**/cli.yaml', '**/cligen/_test/data/*.yaml'],
               !H 'path pattern to scan for replacement (default: %(default)s)']
- convert:
  - !H analyse argument file and generate cligen data
  - !Option ['append', !Action store_true, !H append _cligen_data to __init__.py]
  - !Argument [path] 
- comment:
  - !H show cligen_data comments (from cligen.__init__.py)
  - !Option ['update', !H update cligen_data comments in __init__.py (argument can be directory or file)]
"""
