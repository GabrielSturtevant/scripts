import os
import sys
import shutil
import time
import requests
import hashlib
import getopt


# Program constants
FILE_HASH = "66bedeb9271515f1714a70ee857b51a6"
STATIC_IP = "192.168.10.10"
INITIAL_PATH = os.getcwd()
HOST_PERMISSIONS = "644"

# User Definable Variables
SSH_LINK = False
INSTALLED_SSH = False
FRAMEWORK_PATH = "Code"
URL_NAME = "homestead.app"
DEFAULT_FRAMEWORK_URL = "https://github.com/laravel/laravel.git"
DEFAULT_FW_DIR_NAME = 'Laravel'
NUMBER_OF_CPUS = '1'

# System modifications
sys.stdin = open('/dev/tty')


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def cs():
    os.system('clear')


def install(program_name, common_name):
    print('Checking whether {} is installed'.format(common_name))
    if shutil.which(program_name) is None:
        print('{} is not installed, installing now'.format(common_name))
        os.system('sudo apt install {} -y'.format(program_name))
    else:
        print('{} is already installed'.format(common_name))

    time.sleep(.5)
    cs()

help_out = 'This provides a small list of command line arguments that this \nprogram will accept:\n' \
           '\t-u\tEnter a custom url to fetch a Laravel repository from\n' \
           '\t-n\tEnter a custom application name\n' \
           '\t-d\tEnter a custom directory path to install Laravel in\n' \
           '\t-D\tEnter a custom name for your Laravel directory\n' \
           '\t-c\tEnter the number of cores to assign to your VM\n' \
           '\t-h\tHelp screen'

try:
    opts, args = getopt.getopt(sys.argv[1:],"hu:n:l:d:D:c:", ['help'])
except getopt.GetoptError:
    print('names.py -f -l -e -d -n <number of names to print>')
    sys.exit(2)

for opt, arg in opts:
    if opt in ('-h', '--help'):
        print(help_out)
        sys.exit(1)
    elif opt in ('-u'):
        DEFAULT_FRAMEWORK_URL = arg
        if 'git@github.com' in DEFAULT_FRAMEWORK_URL:
            SSH_LINK = True
    elif opt in ('-n'):
        URL_NAME = arg + '.app'
    elif opt in ('-D'):
        DEFAULT_FW_DIR_NAME = arg
    elif opt in ('-d'):
        FRAMEWORK_PATH = arg
    elif opt in ('-c'):
        NUMBER_OF_CPUS = arg

cs()
print('Running Ubuntu Homestead installation script')
#  Checks whether the user has configured an ssh key
if not os.path.isfile(os.path.expanduser('~') + '/.ssh/id_rsa.pub'):
    INSTALLED_SSH = True
    print('ssh key has not been configured.')
    email = input('Please enter your email address:')
    os.system('ssh-keygen -f ~/.ssh/id_rsa -t rsa -b 4096 -C "{}" -N ""'.format(email))

time.sleep(1)
cs()

# Update system
print('Updating system')
os.system('sudo apt update')

time.sleep(1)
cs()

# Ensures dependencies are met
install('git', 'Git')
install('virtualbox', 'VirtualBox')
install('vim', 'Vim')
install('python-pip', 'Pip')

# Install python dependencies
os.system('sudo pip install beautifulsoup4')
os.system('sudo pip install requests')
os.system('sudo pip install lxml')

os.system('rm -rf vagrant*.deb')

time.sleep(1)
file_name = 'temp.py'
python_program = open(file_name, 'w+')
r = requests.get('https://raw.githubusercontent.com/GabrielSturtevant/scripts/master/GetVagrantLink.py')
python_program.write(r.content.decode('utf-8'))
python_program.close()

if md5(file_name) == FILE_HASH:
    os.system('wget $(python {})'.format(file_name))
else:
    print('Python script integrity compromised. Exiting now')
    exit(1)

os.system('rm -f {}'.format(file_name))

os.system('sudo dpkg -i vagrant*.deb')

os.system('rm -rf vagrant*.deb')

print('Attempting to edit /etc/hosts, a backup will be created at /etc/hosts.BAK')
new_hosts = open('hosts', 'w+')
old_hosts = open('/etc/hosts', 'r')
new_hosts.write(old_hosts.read())

old_hosts.close()
os.system('sudo cp /etc/hosts /etc/hosts.BAK')

to_write = "\n# Homestead ip address and url\n"
to_write += "{}\t{}".format(STATIC_IP, URL_NAME)
new_hosts.write(to_write)
new_hosts.close()

os.system('sudo rm /etc/hosts')
os.system('mv hosts /etc/hosts')
os.system('sudo chmod {} /etc/hosts'.format(HOST_PERMISSIONS))
print('Finished editing hosts file')

# Go to home directory
os.chdir(os.path.expanduser('~'))

os.system('vagrant box add laravel/homestead --provider virtualbox')

os.system('git clone https://github.com/laravel/homestead.git Homestead')

path = FRAMEWORK_PATH

while True:
    path = path.split('/')
    if path[0] == '':
        path.pop()

    try:
        os.makedirs(os.path.join(os.path.expanduser('~'), *path))
        FRAMEWORK_PATH = '/'.join(path)
        break
    except FileExistsError:
        print('Oops, looks like that directory already exists\n')
        path = input('Please enter a new path to place the framework'
                     ' in \n(type N to place it in existing directory):\n')
        if path.lower() == 'n':
            break

os.system('cd {}'.format(FRAMEWORK_PATH))
os.system('git clone {} {}'.format(DEFAULT_FRAMEWORK_URL, DEFAULT_FW_DIR_NAME))

os.chdir(os.path.expanduser('~') + '/Homestead')
os.system('chmod +x init.sh; ./init.sh')

homestead_yaml = open('Homestead.yaml', 'r+')
new_yaml = open('Homestead.yaml.new', 'r+')
info = homestead_yaml.read()

for line in info:
    if 'Code/Laravel/Public' in line:
        line = line.replace('Code/Laravel', '{}/{}'.format(FRAMEWORK_PATH, DEFAULT_FW_DIR_NAME))

    if 'cpus: 1' in line:
        line = line.replace('1', NUMBER_OF_CPUS)

    if 'homestead.app' in line:
        line = line.replace('homestead.app', URL_NAME)
    new_yaml.write(line)
os.system('rm Homestead.yaml; mv Homestead.yaml.new Homestead.yaml')

