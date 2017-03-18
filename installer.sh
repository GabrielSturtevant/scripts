#!/bin/bash

if [ $(uname) = "Darwin" ]; then
    curl https://raw.githubusercontent.com/GabrielSturtevant/scripts/master/macHomestead.sh | bash
elif [ $(uname) = "Linux" ]; then
    . /etc/lsb-release
    if [ "$DISTRIB_ID" = "Ubuntu" ]; then
        curl https://raw.githubusercontent.com/GabrielSturtevant/scripts/master/ubuntuHomestead.sh | bash
    else
        echo "Your version of Linux is not supported"
        exit
    fi
else
    echo "Your operating system is not yet supported"
fi
