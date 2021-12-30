import argparse
import datetime

_parameters = """\
default: today
"""


class DateAction(argparse.Action):
    """argparse action for parsing dates with or without dashes

    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', action=DateAction)
    """

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs != 1 and nargs not in [None, '?', '*']:
            raise ValueError('DateAction can only have one argument')
        default = kwargs.get('default')
        if isinstance(default, str):
            kwargs['default'] = self.special(default)
        super(DateAction, self).__init__(option_strings, dest, nargs=nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        # this is only called if the option is specified
        if values is None:
            return None
        s = values
        for c in './-_':
            s = s.replace(c, '')
        try:
            val = datetime.datetime.strptime(s, '%Y%m%d').date()
        except ValueError:
            val = self.special(s)
        #    val = self.const
        setattr(namespace, self.dest, val)

    def special(self, date_s):
        if isinstance(date_s, str):
            today = datetime.date.today()
            one_day = datetime.timedelta(days=1)
            if date_s == 'today':
                return today
            if date_s == 'yesterday':
                return today - one_day
            if date_s == 'tomorrow':
                return today + one_day
            raise ValueError
