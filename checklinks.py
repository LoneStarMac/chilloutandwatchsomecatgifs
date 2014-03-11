#!/usr/bin/env python
import requests

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

def main():
    thumb_file = 'catgifs.txt'
    for thumb in thumbnail_list(thumb_file):
        try:
            r = requests.head(thumb)
        except Exception as e:
            print thumb, str(e)
            continue
        if r.status_code in [301, 302]:
            print thumb, FAIL + str(r.status_code)
            if r.headers['location'] != 'http://i.imgur.com/removed.png':
                print '  ' + HEADER + r.headers['location'] + ENDC
            else:
                print '  ' + HEADER + 'removed by imgur.' + ENDC
        elif r.status_code != 200:
            print thumb, FAIL + str(r.status_code) + ENDC


def thumbnail_list(name = None):
    if name is None:
        raise Exception('Thumbnail file not defined')
    with open(name) as f:
        for row in f.read().splitlines():
            link = row.strip()
            if link and not link.startswith('#'):
                yield link


if __name__ == '__main__':
    main()
