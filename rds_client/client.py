import ssl
import time
import json
import logging
import threading

from resources.auth import RDAuth
from resources.leads import RDLead
from resources.apikey import RDAPIKey
from resources.webhook import RDWebhook
from resources.contacts import RDContacts
from resources.callback import RDURLCallback
from resources.token import RDGettingAcessToken
from resources.token import RDRefreshExpiredToken
from resources.token import RDRevokingAcessToken
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

	def __init__(self, *args, **kwargs):
		self.wss_url = "wss://{host}/echo/websocket".format(host=host)
		self.websocket_client = None
		
		self.client = RDStationClient(**kwargs)

	def connect(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

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

	def get_access_token(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

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

	def send_request(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	@property
	def websocket(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		return self.websocket_client.wss

	# https://developers.rdstation.com/en/reference/account_infos

	def get_account_information(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	def get_tracking_code(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	# https://developers.rdstation.com/en/reference/contacts

	def get_by_uiid(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	def get_by_email(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	# https://developers.rdstation.com/en/reference/contacts/funnels

	def get_by_contact_uuid(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

	def get_by_contact_email(self):
		"""
		Propriedade para obter recursos da IQ Option, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`Appinit
		<restservice.resources.appinit.Appinit>`.
		"""
		pass

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