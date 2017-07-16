#!/usr/bin/python3
import os
import requests
import getpass
import sys
import json
from requests.auth import HTTPBasicAuth

sys.stdin = open('/dev/tty')

fail_condition = False
if not False:
	while not fail_condition:
		user_name = input('What\'s your github username? ')
		password = getpass.getpass('What\'s your github password? ')
		auth = HTTPBasicAuth(user_name, password)

		key = 'Enter key here'
		url = 'https://api.github.com/user/keys'

		data = {
			'title': 'Omen',
			'key': key,
		}
		fooo = requests.post(url, data=json.dumps(data), auth=auth)
		print(fooo.status_code)
		errors = None
		foobar = json.loads(fooo.text)

		# This is ugly. Need to change this
		if not foobar['errors'] == None:
			errors = foobar['errors']
			if not errors[0] == None:
				errors = errors[0]
				if not errors['message'] == None:
					print(errors['message'])
		sys.exit()
		if r.status_code == 201:
			fail_condition = True
			os.system('clear')
			print('Congratulations! ')
		else:
			os.system('clear')
			print(r.status_code)
			print('Your username and/or password were incorrect\n')
