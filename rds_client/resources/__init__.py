
def main():
	import sys
	import time
	from types import SimpleNamespace

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
		"code": "d7f28b82b9296f81207875429bbae99b",
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
