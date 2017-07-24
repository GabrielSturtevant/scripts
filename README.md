# This repository is depricated.

### scripts

This is a test:
```
export SCRIPTS_URL='git@github.com:csun-metalab/etd-v3.git' && export SCRIPTS_URL_NAME='etdv3' && export SCRIPTS_DIR_NAME='ETD-V3' && export SCRIPTS_DIR_PATH='Code/Meta' && export SCRIPTS_CORES='2' && curl https://raw.githubusercontent.com/GabrielSturtevant/scripts/master/ubuntuHomestead.py | python3
```


```
./ubuntuHomestead.py -u git@github.com:csun-metalab/etd-v3.git -n etdv3 -d Code/Meta -D ETD-V3 -c 2

```

```
curl https://raw.githubusercontent.com/GabrielSturtevant/scripts/master/installer.sh | bash
```

These scripts are for my own personal use. Use these with caution as I have not written them with systems other than my own in mind

If you want to use them, these are the commands to follow:

If you would like to use the Homestead installation script, it needs to be downloaded to your system. It is intended to only work on Ubuntu systems
```
git clone https://github.com/GabrielSturtevant/scripts.git; ./scripts/homestead.sh
```
This command is still a work in progress:
```
curl https://raw.githubusercontent.com/GabrielSturtevant/scripts/master/homestead.sh | bash
```

The JetBrains Toolbox installer is mostly distribution agnostic. It does require you to be on a linux system. The following coomand will install the software:
```shell
curl https://raw.githubusercontent.com/GabrielSturtevant/scripts/master/jetbrains-toolbox.sh | bash
```
