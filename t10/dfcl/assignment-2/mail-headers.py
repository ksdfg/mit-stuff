from argparse import ArgumentParser
from email import message_from_bytes
from email.parser import HeaderParser
from imaplib import IMAP4_SSL

# set commandline arguments
parser = ArgumentParser(description="Get email headers using IMAP")
parser.add_argument('-u', '--username', help="Email Address", type=str, required=True)
parser.add_argument('-p', '--password', help="Password", type=str, required=True)
parser.add_argument('--host', help="IMAP Host", type=str, default="imap.gmail.com")
args = parser.parse_args()

# connect to mail server
imap = IMAP4_SSL(args.host)
imap.login(args.username, args.password)

# fetch email
_, messages = imap.select('inbox')
_, msg = imap.fetch(messages[0].decode('utf-8'), 'rfc822')

# iterate over response and print headers
headers = []
parser = HeaderParser()
for response in msg:
    if isinstance(response, tuple):
        headers.extend(parser.parsestr(message_from_bytes(response[1]).as_string()).items())

# print headers
print("\n\n".join(f"{key}:\n{value}" for key, value in headers))
