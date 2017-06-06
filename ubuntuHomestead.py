#!/usr/bin/python3.5
import os

print('Running Ubuntu Homestead installation script')
if os.path.isfile(os.path.expanduser('~') + '/.ssh/id_rsa.pub'):
    print('true')
else:
    print('false')
