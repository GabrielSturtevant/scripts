#!/bin/bash
# This script installs the jetbrains toolbox application
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit
fi
if ! type jq > /dev/null; then
    apt install jq -y
fi
cd ~/Downloads
rm -f jetbrains-toolbox*.tar.gz
wget $(curl https://data.services.jetbrains.com/products/releases?code=TBA | jq -r .TBA[0].downloads.linux.link)
rm -rf /opt/jetbrains*
mv jetbrains-toolbox* /opt/
cd /opt/
mv jetbrains-toolbox*.tar.gz jetbrains-toolbox.tar.gz
tar -zxf jetbrains-toolbox.tar.gz
rm -rf jetbrains*.tar.gz
mv jetbrains-toolbox-* jetbrains-toolbox
sudo -k
./jetbrains-toolbox/jetbrains-toolbox
