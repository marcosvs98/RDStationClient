""" https://developers.rdstation.com/en/overview """

import ssl
import settings
import logging
import threading
#from socket import websocket
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

class RDSWebsocketClient():
	"""
	Classe responsável pela implementação de um cliente RDStation
	ref: https://developers.rdstation.com/en/overview
	"""
	def __init__(self, client):
		"""
		:param api: The instance of :class:`RDStationRestClient
            <rds.api.RDStationRestClient>`.
		"""
		self.client = client
		self.wss = websocket.WebSocketApp(
			self.client.wss_url, on_message=self.on_message,
			on_error=self.on_error, on_close=self.on_close,
			on_open=self.on_open
		)

	def on_message(self, message):
		"""
		Classe responsável pela implementação de um cliente RDStation
		ref: https://developers.rdstation.com/en/overview
		"""
		pass

	@staticmethod
	def on_error(wss, error):
		"""
		Classe responsável pela implementação de um cliente RDStation
		ref: https://developers.rdstation.com/en/overview
		"""
		pass

	@staticmethod
	def on_open(wss):
		"""
		method to process websocket open.
		"""
		pass

	@staticmethod
	def on_close(wss):
		"""
		Method to process websocket close.
		"""
		pass


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
		self._wss_url = kwargs.get('socket', settings.RDSTATION['endpoints']['socket'])
		self._headers = kwargs.get('headers', settings.RDSTATION['default_headers'])
		self.session = Session()

	@property
	def get_lead(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		pass

	def update_lead(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		pass

	def create_app(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		pass

	@property
	def get_access_token(self):
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
			method=method, url=url, data=data, headers=self._headers, **kwargs
		) # pylint disable=bad-continuation
		logger.debug(response)
		logger.debug(response.text)
		logger.debug(response.headers)
		logger.debug(response.cookies)
		return response.json()

	@property
	def websocket(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<rds_client.resources.appinit.Appinit>`.
		"""
		return self._websocket_client.wss

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

	# https://developers.rdstation.com/en/reference/fields

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
		"""
		if not self.acess_token:
			self.headers['Authorization'] = f"Bearer {self.get_access_token}"
		pass

	def start_websocket(self):
		"""
		Propriedade para obter recurso da RD Station websocket, obter um canal de velas.
		:returns: A instância de :class:`GetCandles
			<rds_client.ws.chanels.candles.GetCandles>`.
		"""
		self._websocket_client = RDSWebsocketClient(self)
		self._websocket_thread = threading.Thread(
			target=self.websocket.run_forever, kwargs={'sslopt': {
			"check_hostname": False, "cert_reqs": ssl.CERT_NONE,
			"ca_certs": "cacert.pem"}}) # pylint disable=bad-continuation
		# for fix pyinstall error: cafile, capath and cadata cannot be  omitted
		self._websocket_thread.daemon = True
		self._websocket_thread.start()
		while True:
			pass

	def close(self):
		"""
		método responsável por finalizar uma conexão via websockets.
			:return:
		"""
		self._websocket.close()
		self._websocket_thread.join()  # pylint disable=no-member

	def websocket_alive(self):
		"""
	    método responsável por validar a thread de conexão.
		"""
		self._websocket_thread.join() # pylint disable=no-member


# end-of-file

# Token público 90b15f9c2c2b3df3076d4239113749f3
# Token privado e931486421528bb08f0792ed818df9d6

#client = RDStationClient(
#	access_token='access_token',
#	client_id='cc3fbf81-3a32-4591-823e-8cf49d2116ab',
#	client_secret='e52fc0ef6053427ca197c35a494f667b'
#)

client = RDStationClient(**{
  "access_token": 'access_token',
  "client_id": "049bf777-bbbb-0000-9e09-7ebe2972b8b0",
  "client_secret": "952e14d9dbad9c28d2247da9a19645d8",
})


rdclient = RDStationRestClient(client)
print(rdclient.get_access_token())

# end-of-file