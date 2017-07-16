#!/usr/bin/python3
import os
import requests
import getpass
import sys
import json

sys.stdin = open('/dev/tty')

fail_condition = False
if not False:
    while not fail_condition:
        user_name = input('What\'s your github username? ')
        password = getpass.getpass('What\'s your github password? ')
        # print(password)
        # sys.exit()
        key = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDAkbwY9rgM/8Gu/XKe6XUDd4I4g4PgKKv/Hk5yQRHsSWQvaIqvO7lDd7Mkp0QmcBILVYTIAtZ+SYYQhMdswzaXXqHvSjR57s+CmFBn75clZFcOmtVoEnob5Ai7rJkx0KrWQHhgokhI8zis73yPsIzcPRW/wpbTk5PdSAm79jGEReUBV4oXq3CcEYSp9D/JK5rRHLqx7IZtuFmXQ2d3Tkx4dEY2+0paPPfBO+EgJCNFctmLFqy1hyr+s41jYjGwgnKvHyPQbZFxSrW6hAE3WPpqWHf103bEUwn7IB17O9Ey4rx24ngIq4iFLa5p0ERuB7ruZynXOFsjZhyJT6PFUzCiZskRv54nxp2UIDTntw+JjBOxDQGIAB/wnFFauvh9y4Tk/3VDpubox3PyGsISZodYOdhJ6//r89BbY4PGoETHL4mUXyAEvdCsD6GpTmWmCXep3MW0nNjr7N0Opsyrz5Fx+SaJOZGJsMlHis+bsAVeKlQstz0IMTFwzpQ/EG6XWKsu4/byJXPidS7oCw2J7NDcowQb/kbeKxhXgHL72zhlqfYHe/m4ZvK2oN1Ty1NgLmImH8dHSRHd3oId8UvgrFejkMjgebBTrbE6vpHXU2hHydxMF0++DrrIMi7LR8G6WRyddC6IUE5biB9WfHewyRR4UAw5pXkEMS5oVdttYVxmvQ== gsturtevant87@gmail.com'
        url = 'https://api.github.com/user/keys'
        data = {
            'key': key,
            'title': 'fooobar'
        }
        # r = requests.get(url, auth=(user_name, password))
        r = requests.post(url, auth=(user_name, password), data=json.dumps(data))
        if r.status_code == 201:
            fail_condition = True
        else:
            os.system('clear')
            print(json.dumps(data))
            print(r.status_code)
            print('Your username and/or password were incorrect\n')



            # print('ssh key has not been configured.')
            # email = input('Please enter your email address:\n')
            # os.system('ssh-keygen -f ~/.ssh/id_rsa -t rsa -b 4096 -C "{}" -N ""'.format(email))
            # ssh_key = open(os.environ['HOME'] + '/.ssh/id_rsa.pub', 'r').read()
            # print("You will need to add this ssh key to github")
            # username = input('Please enter your github username:\n')
            # title = input('Please enter a name for your computer:\n')
            # to_send = 'curl -u "{}" --data \'{{"title":"{}","key":"{}"}}\' https://api.github.com/user/keys'.format(username,
            #                                                                                                         title,
            #                                                                                                         ssh_key)
            # to_send = to_send.replace('\n', '')
            # os.system(to_send)