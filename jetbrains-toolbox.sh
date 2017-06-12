#!/bin/bash
# This script installs the jetbrains toolbox application
if ! type jq > /dev/null; then
    apt install jq -y
fi
pushd $HOME/Downloads
rm -f jetbrains-toolbox*.tar.gz
wget $(curl https://data.services.jetbrains.com/products/releases?code=TBA | jq -r .TBA[0].downloads.linux.link)
sudo rm -rf /opt/jetbrains*
sudo mv jetbrains-toolbox* /opt/
pushd /opt/
sudo mv jetbrains-toolbox*.tar.gz jetbrains-toolbox.tar.gz
sudo tar -zxf jetbrains-toolbox.tar.gz
sudo rm -rf jetbrains*.tar.gz
sudo mv jetbrains-toolbox-* jetbrains-toolbox
./jetbrains-toolbox/jetbrains-toolbox
