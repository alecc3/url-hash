from urllib.parse import urlparse
import hashlib
import functools
import sys


def shorten_url(url):
    def get_hash(arg):
        return hashlib.sha256(arg.encode('utf-8')).hexdigest()
    parsed = urlparse(url)
    # Hash the Netloc and truncate
    hashes = [get_hash(parsed.netloc)[:16]]
    for attr in parsed[2:]:
        if attr and attr != '/':
            hashes.append(get_hash(attr)[:16])
    hash = functools.reduce(lambda a, b: hex(
        int(a, 16) ^ int(b, 16)), hashes)[2:]
    return 'alec.short/' + hash


try:
    print(shorten_url(sys.argv[1]))
except IndexError:
    print('Error - you may not have provided an argument')
