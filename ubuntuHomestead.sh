#!/bin/bash

#Asks for email address to setup ssh key
if [ ! -f ~/.ssh/id_rsa ]; then
    printf "\nYou have not configured an ssh key.\n"
    read -p "What's your email address? " email < /dev/tty
    ssh-keygen -f ~/.ssh/id_rsa -t rsa -b 4096 -C "$email" -N '' > /dev/null
fi

#Ensures dependencies are met
if ! type git > /dev/null; then
    printf "\nInstalling Git\n"
    sudo apt install git -y
fi
if ! type virtualbox > /dev/null; then
    printf "\nInstalling VirtualBox\n"
    sudo apt install virtualbox -y
fi
if ! type vim > /dev/null; then
    printf "\nInstalling Vim\n"
    sudo apt install vim -y
fi
if ! type pip > /dev/null; then
    printf "\nInstalling Python-pip\n"
    sudo apt install python-pip -y
fi

#Ensures dependencies of custom python script are met
sudo pip install beautifulsoup4
sudo pip install requests
sudo pip install lxml

#Create temporary file to house python script that retrieves correct vagrant url
touch temp.py

#removes any previous vagrant deb files in the working directory
rm -rf vagrant*.deb

#Loads python script into temporary file
curl https://raw.githubusercontent.com/GabrielSturtevant/scripts/master/GetVagrantLink.py > temp.py

#check the integrity of the contents recieved via curl
value=($(md5sum temp.py))
if [[ "$value" = "66bedeb9271515f1714a70ee857b51a6" ]]; then
    #uses output of python file to initiate a download of most recent vagrant installation file
    wget $(python temp.py)
else
    printf "\n\nPython script integrity compromised!"
    exit
fi

#removes temporary python file
rm -f temp.py

#installs vagrant
sudo dpkg -i vagrant*.deb

#removes vagrant installation file
rm -rf vagrant*.deb

#Adds url entry used by homestead to hosts file
echo "Attempting to manipulate /etc/hosts, a backup will be created: /etc/hosts.BAK"
touch /tmp/hosts
echo "192.168.10.10     homestead.app" > /tmp/hosts
sudo cp /etc/hosts /etc/hosts.BAK
cat /etc/hosts >> /tmp/hosts
sudo rm /etc/hosts
sudo mv /tmp/hosts /etc/
sudo chmod 644 /etc/hosts
sudo rm -f /etc/hosts.BAK
echo "Manipulation successful, /etc/hosts.BAK deleted"

#Change to home directory
cd

#Install the correct vagrant box
vagrant box add laravel/homestead --provider virtualbox

#clones the homestead repo
git clone https://github.com/laravel/homestead.git Homestead

#Creates the directory where code will be placed
mkdir Code

#clone the laravel framework to the correct place
cd Code
git clone https://github.com/laravel/laravel.git Laravel

#Initiate homestead
cd ~/Homestead
chmod +x init.sh
./init.sh

#edit the homestead configuraion file
vim Homestead.yaml < /dev/tty
exit
