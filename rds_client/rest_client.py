""" https://developers.rdstation.com/en/overview """

import ssl
import json
import time
import settings
import logging
import threading
from requests import Session
from dataclasses import dataclass, field

from resources.auth import RDGettingAcessToken
from resources.auth import RDRevokingAcessToken
from resources.auth import RDRefreshExpiredToken
from resources.contacts import RDContactsUUID
from resources.contacts import RDContactsEmail
from resources.fields import RDListFields
from resources.fields import RDInsertFieldCurrentAccount
from resources.fields import RDUpdateFieldCurrentAccount
from resources.fields import RDDeleteFieldCurrentAccount
from resources.webhook import RDWebhooksFactory
from resources.webhook import RDDWebhooksReceiver
from resources.webhook import RDUpdateWebhookPerUUID
from resources.webhook import RDDeleteWebhookPerUUID
from resources.contacts import RDUpdateContactPerUUID
from resources.contacts import RDUpsertContactIndentifier
from resources.marketing import RDMarketingAccountInfo
from resources.marketing import RDMarketingTrackingCode
from resources.funnels import RDContactsUUIDDetails
from resources.funnels import RDContactsEmailDetails
from resources.funnels import RDUpdateContactsDetails
from resources.event import RDEvent
from resources.event import RDEventBatch


# pylint disable=too-many-function-args


@dataclass
class RDStationClient:
	"""
	Classe responsável pela implementação de um cliente RDStation
	ref: https://developers.rdstation.com/en/overview """

	client_id      : str
	access_token   : str
	client_secret  : str
	#code           : str
	#redirect_url   : str
	#refresh_token  : str


class RDStationRestClient():  # pylint: disable=too-many-instance-attributes
	""" Class responsible for implementing an RDStation client
	ref: https://developers.rdstation.com/en/overview """
	
	def __init__(self, client , *args, **kwargs):

		self.client = client
		self._websocket = None
		self._websocket_client = None
		self._websocket_thread = None
		self._endpoint = kwargs.get('endpoint', settings.RDSTATION['endpoints']['base_domain'])
		self.wss_url = kwargs.get('socket', settings.RDSTATION['endpoints']['socket'])
		self._headers = kwargs.get('headers', settings.RDSTATION['default_headers'])
		self.session = Session()
		self._access_token = None
		self._expires = None
		self._refresh_token = None

	@property
	def get_access_token(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return self._access_token

	@property
	def get_refresh_token(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return self._refresh_token

	@property
	def get_expires_in(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return self._expires

	@property
	def get_headers(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return self._headers

	@property
	def access_token(self):
		"""
		Propriedade responsável por implementar um recurso de obtenção de token
			´<rds_clinet.resources.auth.RDGettingAcessToken>`.
		"""
		return RDGettingAcessToken(self)

	def refresh_token(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return RDRefreshExpiredToken(self)

	def revoke_access_token(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return RDRevokingAcessToken(self)

	def prepare_path(self, resource):
		"""
		método responsável pela construção da url com base no recurso solicitado

		:param resource: Instância de `<rds_client.resources.RDSResource>`.
		:return: O url completo.
		"""
		return "/".join((self._endpoint, resource.path))

	def send_request(self, resource, method, data=None, **kwargs): # pylint: disable=too-many-arguments
		"""
		método responsável pelo envio do solicitação do recurso obtido
		:param resource: Instância de `<rds_client.resources.RDSResource>`.
		:param method: http method
		:param kwargs: others params
		   				
			:return: `<rds_client.RDSJsonResponse>`.
		"""
		logger = logging.getLogger(__name__)

		# get url to of resource
		url = self.prepare_path(resource)
		response = self.session.request(
			method=method, url=url, data=json.dumps(data), headers=self._headers, **kwargs
		) # pylint disable=bad-continuation
		logger.debug(response)
		logger.debug(response.text)
		logger.debug(response.headers)
		logger.debug(response.cookies)

		return response.json()

	def get_account_info(self):
		"""
		Returns the account name from your RD Station Marketing account.

			<rds_client.resources.appinit.Appinit>`.
		"""
		return RDMarketingAccountInfo(self)

	def get_tracking_code(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return RDMarketingTrackingCode(self)

	def get_contacts_by_uiid(self, uuid):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return RDContactsUUID(self, uuid)

	def get_contacts_by_email(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return RDContactsEmail(self)

	def update_contacts_by_uuid(self, uuid):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return RDUpdateContactPerUUID(self, uuid)

	def upsert_contact_per_identifier(self, indentifier, value):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return RDUpsertContactIndentifier(self, indentifier, value)

	def get_contacts_by_uuid_funnel(self, uuid):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return RDContactsUUIDDetails(self, uuid)

	def get_contacts_by_email_funnel(self, email):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return RDContactsEmailDetails(self, email)

	def update_contact_by_indetifier_funnel(self, indentifier, **kwargs):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return RDUpdateContactsDetails(self, indentifier, **kwargs)

	def get_fields(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return RDListFields(self)

	def insert_field(self, body):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return RDInsertFieldCurrentAccount(self, body)

	def update_field(self, body):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return RDUpdateFieldCurrentAccount(self, body)

	def delete_field(self, body):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return RDDeleteFieldCurrentAccount(self, body)

	# https://developers.rdstation.com/en/reference/webhooks

	def receive_webhook(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return RDDWebhooksReceiver(self)

	def create_webhook(self, body):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return RDWebhooksFactory(self, body)

	def update_webhook_by_uuid(self, uuid):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return RDUpdateWebhookPerUUID(self, uuid)

	def delete_webhook(self, uuid):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return RDDeleteWebhookPerUUID(self, uuid)

	# https://developers.rdstation.com/en/reference/events
	def create_event(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.event.RDEvent>`.
		"""
		return RDEvent(self)

	def create_event_batch(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.event.RDEventBatch>`.
		"""
		return RDEventBatch(self)

	def connect(self):
		"""
		método responsável por ativar uma conexão com a api da RD Station.
		:returns: A instância de :class:`GetCandles
			<rds_client.ws.chanels.candles.GetCandles>`.
		"""
		if not self._access_token:
			data = self.access_token()
			try:
				self._access_token = data['access_token']
				self._expires = data['expires_in']
				self._refresh_token = data['refresh_token']
				self._headers['Authorization'] = f"Bearer {self._refresh_token}"
			except KeyError as e:
				return

		logger = logging.getLogger(__name__)
		logger.debug(f"access-token: {self._access_token}")
		logger.debug(f"refresh-token: {self._refresh_token}")
		logger.debug(f"expire-in: {self._expires}")
		self._access_token = self._refresh_token

	def run(self):
		"""
		método responsável por ativar uma conexão com a api da RD Station.
			:returns: A instância de :class:`GetCandles
		<rds_client.ws.chanels.candles.GetCandles>`.
		"""
		logger = logging.getLogger(__name__)
		while True:
			try:
				self.connect()
				self._expires -= 1
				time.sleep(1)
			except KeyboardInterrupt:
				logger.warning('CTRL+C Detected!')
				break


	def __enter__(self):
		self.conect()
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		if exc_val:
			log.warning(f'exc_type: {exc_type}')
			log.warning(f'exc_value: {exc_val}')
			log.warning(f'exc_traceback: {exc_tb}')

	def __repr__(self):
		return (f'RDStation ('
				f'refresh-token={self._refresh_token[0:10]}.., '
				f'expire-in={self._expires})')

# end-of-file


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

# end-of-file