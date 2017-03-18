#!/bin/bash

if [ $(uname) = "Darwin" ]; then
    echo "This is a mac"
elif [ $(uname) = "Linux" ]; then
    echo "This is Linux"
fi
