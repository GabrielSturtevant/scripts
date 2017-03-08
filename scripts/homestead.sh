#!/bin/bash

#Asks for email address to setup ssh key
read -p "What's your email address? " email
echo $email

#Ensures dependencies are met
if ! type git > /dev/null; then
   sudo apt install git -y
fi
if ! type virtualbox > /dev/null; then
    sudo apt install virtualbox -y
fi
if ! type vim > /dev/null; then
   sudo apt install vim -y
fi
if ! type pip > /dev/null; then
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
curl https://raw.githubusercontent.com/GabrielSturtevant/scripts/master/scripts/GetVagrantLink.py > temp.py

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
touch /tmp/hosts
echo "192.168.10.10     homestead.app" > /tmp/hosts
sudo cp /etc/hosts /etc/hosts.BAK
cat /etc/hosts >> /tmp/hosts
sudo rm /etc/hosts
sudo mv /tmp/hosts /etc/
sudo rm -f /etc/hosts.BAK

#Change to home directory
cd

#Install the correct vagrant box
echo "3" | vagrant box add laravel/homestead

#clones the homestead repo
git clone https://github.com/laravel/homestead.git Homestead

#Creates the directory where code will be placed
mkdir Code

#clone the laravel framework to the correct place
cd Code
git clone https://github.com/laravel/laravel.git Laravel

#Initiate homestead and create the SSH keys to be able to utilize the application
cd
cd Homestead
bash init.sh
ssh-keygen -t rsa -b 4096 -C "$email"

#edit the homestead configuraion file
vim Homestead.yaml
exit
