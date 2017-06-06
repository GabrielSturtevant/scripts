import os, shutil

print('Running Ubuntu Homestead installation script')
#  Checks whether the user has configured an ssh key
if not os.path.isfile(os.path.expanduser('~') + '/.ssh/id_rsa.pub'):
    print('ssh key has not been configured.')
    email = input('Please enter your email address:')
    os.system('ssh-keygen -f ~/.ssh/id_rsa -t rsa -b 4096 -C "{}" -N "" >> /dev/null'.format(email))

# Ensures dependencies are met
print('Checking whether Git is installed')
if shutil.which('git') is None:
    print('Git is not installed, installing now')
    # os.system('sudo apt install git -y')
else:
    print('Git is already installed')
