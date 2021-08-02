""" https://developers.rdstation.com/en/overview """

import ssl
import time
import json
import logging
import threading

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

	self.refresh_token = None


@dataclasses
class RDStationClient:
	"""
	Step 1:
		Criar um aplicativo na RD Station App Store
		link: https://appstore.rdstation.com/en/publisher

	Classe responsável pela implementação de um cliente RDStation
	ref: https://developers.rdstation.com/en/overview
	"""
	client_id      : str
	access_token   : str
	client_secret  : str
	code           : str
	redirect_url   : str
	refresh_token  : str



class RDStationRestClient():
	"""
	Classe responsável pela implementação de um cliente RDStation
	ref: https://developers.rdstation.com/en/overview
	"""

	def __init__(self, api_key, *args, **kwargs):

		self.api_key = api_key
		self._client = RDStationClient(**kwargs)
		self._websocket_client = None
		self._endpoint = kwargs.get('endpoint', settings.RDSTATION['endpoints']['base_domain'])
		self._wss_url = kwargs.get('socket', settings.RDSTATION['endpoints']['socket'])
		self.headers = kwargs.get('headers', settings.RDSTATION['default_headers'])
				
	def login(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	def get_lead(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	def update_lead(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	def create_app(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
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
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDRefreshExpiredToken(self)

	def revoke_access_token(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDRevokingAcessToken(self)


	def prepare_path(self, resource):
		"""
		método responsável pela construção da url com base no recurso solicitado

		:param resource: Instância de `<rds_client.resources.RDSResource>`.
		:return: O url completo.
		"""
		return "/".join((self._endpoint, resource.path))

	def send_request(self, resource, method, **kwargs):
		"""
		método responsável pelo envio do solicitação do recurso obtido
		:param resource: Instância de `<rds_client.resources.RDSResource>`.
		:param method: http method
		:param kwargs: others params
		   				
			:return: `<rds_client.RDSJsonResponse>`.
		"""
		# get url to of resource
		url = self.prepare_path(resource)

		response = self.session.request(method=method, url=url, **kwargs)

		logger.debug(response)
		logger.debug(response.text)
		logger.debug(response.headers)
		logger.debug(response.cookies)
		response.raise_for_status()
		return response

	@property
	def websocket(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return self.websocket_client.wss

	def get_account_info(self):
		"""
		Returns the account name from your RD Station Marketing account.

			<restservice.resources.appinit.Appinit>`.
		"""
		return RDMarketingAccountInfo(self)

	def get_tracking_code(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDMarketingTrackingCode(self)

	def get_contacts_by_uiid(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDContactsUUID(self)

	def get_contacts_by_email(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDContactsEmail(self)

	def update_contacts_by_uuid(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDUpdateContactPerUUID(self)

	def upsert_contact_per_identifier(self, indentifier, value):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDUpsertContactIndentifier(self, indentifier, value)


	def get_contacts_by_uuid_funnel(self, uuid):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDContactsUUIDDetails(self)

	def get_contacts_by_email_funnel(self, email):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDContactsEmailDetails(self, email)

	def update_contact_by_indetifier_funnel(self, indentifier, **kwargs):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDUpdateContactsDetails(self, identifier, **kwargs)

	# https://developers.rdstation.com/en/reference/fields

	def get_fields(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDListFields(self)

	def insert_field(self, body):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDInsertFieldCurrentAccount(self, body)

	def update_field(self, body):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDUpdateFieldCurrentAccount(self, body)

	def delete_field(self, body):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDDeleteFieldCurrentAccount(self, body)

	# https://developers.rdstation.com/en/reference/webhooks

	def receive_webhook(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDDWebhooksReceiver(self)

	def create_webhook(self, body):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDWebhooksFactory(self, body)

	def update_webhook_by_uuid(self, uuid):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDUpdateWebhookPerUUID(self)

	def delete_webhook(self, uuid):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDDeleteWebhookPerUUID(self, uuid)

	# https://developers.rdstation.com/en/reference/events
	def create_event(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDEvent(self)

	def create_event_batch(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return RDEventBatch(self)

	def connect(self):
		"""
		método responsável por ativar uma conexão com a api da RD Station.
		"""
		if not self.acess_token:
			self.headers['Authorization'] = f'Bearer {self.get_access_token}
		pass

	def close(self):
		"""
		método responsável por finalizar uma conexão via websockets.
			:return:
		"""
		self.websocket.close()
		self.websocket_thread.jon()

	def websocket_alive(self):
		"""
	    método responsável por validar a thread de conexão.
		"""
		self.websocket_thread.join()

	def __str__(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	def __repr__(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	def __enter__(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	def __exit__(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	def __delete__(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

# end-of-file