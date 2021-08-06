import sys
import time
import logging
from types import SimpleNamespace
from rest_client import RDStationRestClient, RDStationClient

def main():

	l = {
		'format'   : f'[%(asctime)s.%(msecs)03d]'
					 f'[PID-%(process)s]'
					 f'[%(threadName)s]'
					 f'[%(module)s:%(funcName)s:%(lineno)d]'
					 f'[%(name)s:%(levelname)s]'
					 f''
					 f': %(message)s',
		'datefmt'  : '%Y-%m-%d %H:%M:%S',
		'level'    : logging.DEBUG,
		'stream'   : sys.stderr
	}

	# https://app.rdstation.com.br/api/platform/auth?client_id=cc3fbf81-3a32-4591-823e-8cf49d2116ab&redirect_uri=https://github.com/MarcosVs98/

	logging.basicConfig(**l)

	client = SimpleNamespace(**{
		"client_id": "cc3fbf81-3a32-4591-823e-8cf49d2116ab",
		"client_secret": "e52fc0ef6053427ca197c35a494f667b",
		"code": "b195210be81df23d1b9b3f312fbb7555",
		"redirect_uri": "https://github.com/MarcosVs98/"
	})
	rdclient = RDStationRestClient(client)
	rdclient.connect()
	#while True:
	#	rdclient.connect()
	#	time.sleep(5)
	rdclient.run()
	#print(rdclient.get_access_token)
	#print(rdclient.get_refresh_token)
	#print(rdclient.get_expires_in)


if __name__ == '__main__':
	main()



'''
import json

class RDSJsonResponse():

	def __init__(self, json_response, status_code, raise_status=False, safe=False):

		if safe and isinstance(json_response, dict):
			raise TypeError(
				'In order to allow non-dict objects to be serialized set the '
				'safe parameter to False.'
			)
		for key, value in json_response.items():
			setattr(self, key, value)

		self.response_errors = []

		if self.errors:
			for r in self.errors:
				rd_code, message = r['error_message'].split(': ')
				self.response_errors.append(
					(status_code, r['error_type'], int(rd_code), message))
		try:
			post_data = {}
			for data in self.post_data.split("&"):
				key, value = data.split('=')
				post_data[key] = value
		except AttributeError:
			post_data = ''

		setattr(self, 'post_data', post_data)


c = RDSJsonResponse({
	'query_string': '',
	'request_method': 'POST',
	'request_path': '/api/platform/token',
	#'post_data': 'client_id=cc3fbf81-3a32-4591-823e-8cf49d2116ab&client_secret=e52fc0ef6053427ca197c35a494f667b',
	'errors': [{
			'error_type': 'BAD_REQUEST',
			'error_message': "822: unexpected token at 'client_id=cc3fbf81-3a32-4591-823e-8cf49d2116ab&client_secret=e52fc0ef6053427ca197c35a494f667b'",
			'error_class': 'ActionDispatch::Http::Parameters::ParseError'
				},
	]}, 400)

print(c.response_errors)
print(c.post_data)

from types import SimpleNamespace

client = SimpleNamespace(**{
	"client_id": "cc3fbf81-3a32-4591-823e-8cf49d2116ab",
	"client_secret": "e52fc0ef6053427ca197c35a494f667b",
	"code": "d7f5872ac866a70c219674a1513807e4",
	"redirect_uri": "https://github.com/MarcosVs98/"

})

# https://app.rdstation.com.br/api/platform/auth?client_id=cc3fbf81-3a32-4591-823e-8cf49d2116ab&redirect_uri=https://github.com/MarcosVs98/
import json
import requests

headers = {
	'Content-Type': 'application/json',
}
params = dict(
	client_secret="e52fc0ef6053427ca197c35a494f667b",
	client_id="cc3fbf81-3a32-4591-823e-8cf49d2116ab",
	code="d7f5872ac866a70c219674a1513807e4"
)

data = json.dumps(params)

r = requests.post('https://api.rd.services/auth/token',
				  headers=headers, data=data)

print(r.json())



requests.get('https://app.rdstation.com.br/api/platform/auth', headers={

  'authority': 'app.rdstation.com.br',
  'origin': 'https://app.rdstation.com.br',
  'content-type': 'application/json',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
  'referer': 'https://app.rdstation.com.br/api/platform/auth?client_id=cc3fbf81-3a32-4591-823e-8cf49d2116ab&redirect_uri=https://github.com/MarcosVs98/'})


'''