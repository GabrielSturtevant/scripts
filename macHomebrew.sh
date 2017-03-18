#!/bin/bash

#Asks for email address to setup ssh key
if [ ! -f ~/.ssh/id_rsa ]; then
    printf "\nYou have not configured an ssh key.\n"
    read -p "What's your email address? " email < /dev/tty
    ssh-keygen -f ~/.ssh/id_rsa -t rsa -b 4096 -C "$email" -N '' > /dev/null
fi

#Ensures dependencies are met
if ! type virtualbox > /dev/null; then
    printf "\nInstalling VirtualBox\n"
    brew cask install virtualbox
fi
if ! type vim > /dev/null; then
    printf "\nInstalling Vim\n"
    brew cask install vagrant
fi

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
bash init.sh

#edit the homestead configuraion file
vim Homestead.yaml < /dev/tty
exit
