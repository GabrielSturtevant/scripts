import os, shutil, time, subprocess, requests, hashlib


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


FILE_HASH = "66bedeb9271515f1714a70ee857b51a6"

cs()
print('Running Ubuntu Homestead installation script')
#  Checks whether the user has configured an ssh key
if not os.path.isfile(os.path.expanduser('~') + '/.ssh/id_rsa.pub'):
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
