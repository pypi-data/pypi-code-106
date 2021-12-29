#!/usr/bin/env python
# Format mbox as HTML/XML
# Copyright (C) 2021  Nguyễn Gia Phong
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from argparse import ArgumentParser
from email.header import decode_header
from email.utils import parsedate_to_datetime
from functools import partial
from mailbox import mbox
from pathlib import Path
from urllib.parse import quote, unquote, urlencode

from bleach import clean, linkify
from markdown import markdown

sanitise = partial(clean, tags=('a', 'code', 'em', 'strong', 'sub', 'sup',
                                'blockquote', 'p', 'pre', 'ul', 'ol', 'li'),
                   protocols=('ftp', 'gemini', 'gopher', 'http', 'https',
                              'irc', 'ircs', 'mailto', 'matrix', 'xmpp'))


def extract(archive, parent):
    """Recursively extract emails in reply to given message ID."""
    for message_id, message in archive.copy().items():
        # TODO: handle multipart
        if message['In-Reply-To'] != parent: continue
        archive.pop(message_id)
        yield message, extract(archive, message_id)


def decode(header):
    """Return the decoded email header."""
    for string, charset in decode_header(header):
        encoding = 'utf-8' if charset is None else charset
        yield string.decode(encoding)


def reply_to(message):
    """Return mailto parameters for replying to the given email."""
    yield 'In-Reply-To', message['Message-ID']
    yield 'Cc', message.get('Reply-To', message['From'])
    subject = message['Subject']
    if subject is None: return
    if subject.lower().startswith('re:'):
        yield 'Subject', subject
    else:
        yield 'Subject', f'Re: {subject}'


def date(message):
    """Parse given email's Date header."""
    return parsedate_to_datetime(message['Date']).date()


def render(template, forest, parent):
    """Render the thread recursively based on given template."""
    for self, children in forest:
        message_id = self['Message-Id']
        try:
            author, address = decode(self['From'])
        except ValueError:
            author = self['From']
        body = sanitise(linkify(markdown(self.get_payload(),
                                         output_format='html5')))
        rendered_children = render(template, children, message_id)
        yield template.format(message_id=quote(message_id),
                              mailto_params=urlencode(dict(reply_to(self))),
                              date=date(self).isoformat(), author=author,
                              body=body, children='\n'.join(rendered_children))


def main():
    """Parse command-line arguments and pass them to routines."""
    parser = ArgumentParser(description='format mbox as HTML/XML')
    parser.add_argument('mbox', help='path to mbox file')
    parser.add_argument('id', type=unquote, help='root message ID')
    parser.add_argument('template', type=Path, help='path to template')
    args = parser.parse_args()

    archive = {m['Message-Id']: m for m in sorted(mbox(args.mbox), key=date)}
    template = args.template.read_text()
    print(*render(template, extract(archive, args.id), args.id),
          sep='', end='')


if __name__ == '__main__': main()
