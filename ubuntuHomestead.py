import os

print('Running Ubuntu Homestead installation script')
#  Checks whether the user has configured an ssh key
if not os.path.isfile(os.path.expanduser('~') + '/.ssh/id_rsa.pub'):
    print('ssh key has not been configured.')
    email = input('Please enter your email address:')
    print('Sweeet')

#
