import ssl
import time
import json
import logging
import threading

from resources.auth import RDGettingAcessToken
from resources.auth import RDRevokingAcessToken
from resources.auth import RDRefreshExpiredToken
from resources.marketing import RDMarketingAccountInfo
from resources.marketing import RDMarketingTrackingCode
from resources.contacts import RDContactsUUID
from resources.contacts import RDContactsEmail
from resources.contacts import RDUpdateContactPerUUID
from resources.contacts import RDUpsertContactIndentifier


from resources.leads import RDLead
from resources.webhook import RDWebhook
from resources.callback import RDURLCallback
from resources.conversion_event import RDConversionEvent

from exceptions import RDStationException
from exceptions import RDUserIsNotExists
from exceptions import RDUnauthorizedRequest
from exceptions import RDForbiddenResponse
from exceptions import RDPermissionDenied
from exceptions import RDExpiredCodeGrant
from exceptions import RDInvalidrefreshToken
from exceptions import RDResourceNotFound
from exceptions import RDUnsupportedMediaType
from exceptions import RDMalformedBodyRequest
from exceptions import RDInvalidFormat
from exceptions import RDUpperCaseTagsException
from exceptions import RDInvalidDataType
from exceptions import RDReadOnlyFieldsException
from exceptions import RDInexistentFields
from exceptions import RDConflictingField
from exceptions import RDEmailAlreadyInUse


# API CLIENT


class RDSWebsocketClient():
	"""
	Classe responsável pela implementação de um cliente RDStation
	ref: https://developers.rdstation.com/en/overview
	"""
	def __init__(self, api):
		"""
		:param api: The instance of :class:`RDStationRestClient
            <rds.api.RDStationRestClient>`.
		"""
		self.api = api
		self.wss = websocket.WebSocketApp(
			self.api.wss_url, on_message=self.on_message,
			on_error=self.on_error, on_close=self.on_close,
			on_open=self.on_open)

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
		self._endpoint =
		self._wss_url = "wss://{host}/echo/websocket".format(host=host)
		self._websocket_client = None
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
		pass

	def redirct_uri(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	def revoke_access_token(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	def conversion_identifier(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	def get_contact(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	def prepare_http_url(self, resource):
		"""
		método responsável pela construção da url com base no recurso solicitado

		:param resource: Instância de `<rds_client.resources.RDSResource>`.
		:return: O url completo.
		"""
		return "/".join((self._endpoint, resource.url))

	def send_request(self, resource, method, **kwargs):
		"""
		método responsável pelo envio do solicitação do recurso obtido
		:param resource: Instância de `<rds_client.resources.RDSResource>`.
		:param method: http method
		:param kwargs: others params
		   				
			:return: `<rds_client.RDSJsonResponse>`.
		"""
		# get url to of resource
		url = self.prepare_http_url(resource)

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

	# https://developers.rdstation.com/en/reference/account_infos

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

	# https://developers.rdstation.com/en/reference/contacts

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

	# https://developers.rdstation.com/en/reference/contacts/funnels

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

	# https://developers.rdstation.com/en/reference/fields

	def fields(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	# https://developers.rdstation.com/en/reference/webhooks

	def webhooks(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	# https://developers.rdstation.com/en/reference/events
	def get_events(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

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