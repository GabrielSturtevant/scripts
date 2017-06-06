#!/usr/bin/env bash
FILE='tempFile.tmp'
curl https://raw.githubusercontent.com/GabrielSturtevant/scripts/master/ubuntuHomestead.py > $FILE
python3 $FILE
rm $FILE