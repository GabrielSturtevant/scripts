#!/bin/bash

if [ $(uname) = "Darwin" ]; then
    curl https://raw.githubusercontent.com/GabrielSturtevant/scripts/master/macHomestead.sh | bash
elif [ $(uname) = "Linux" ]; then
    . /etc/lsb-release
    if [ "$DISTRIB_ID" = "Ubuntu" ]; then
        curl https://raw.githubusercontent.com/GabrielSturtevant/scripts/master/ubuntuHomestead.sh | bash
    else
        printf "\n\nYour version of Linux is not supported\n\n"
        printf "If you are using a Debian derivative, you can, at your own risk, try running the script defined here:\n"
        printf "https://github.com/GabrielSturtevant/scripts/blob/master/ubuntuHomestead.sh"
        exit
    fi
else
    printf "\n\nYour operating system is not yet supported"
    exit
fi
