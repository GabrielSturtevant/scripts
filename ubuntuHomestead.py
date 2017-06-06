import os, sys, shutil, termios
# fd = sys.stdin.fileno()
# old = termios.tcgetattr(fd)
# new = termios.tcgetattr(fd)
# try:
#     termios.tcsetattr(fd, termios.TCSADRAIN, new)
#     passwd = input('Enter something')
# finally:
#     termios.tcsetattr(fd, termios.TCSADRAIN, old)
#
# print(passwd)
print('say something')
value = sys.stdin()
print(value)

exit(0)

print('Running Ubuntu Homestead installation script')
#  Checks whether the user has configured an ssh key
if not os.path.isfile(os.path.expanduser('~') + '/.ssh/id_rsa.pub'):
    print('ssh key has not been configured.')
    # email = input('Please enter your email address:')

# Ensures dependencies are met
print('Checking whether Git is installed')
if shutil.which('git') is None:
    print('Git is not installed, installing now')
    # os.system('sudo apt install git -y')
else:
    print('Git is already installed')
