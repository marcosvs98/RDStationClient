""" https://developers.rdstation.com/en/overview """

import json
import time
import logging
from dataclasses import dataclass, field
from requests import Session

import settings
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
	"""Classe responsável pela implementação de um cliente RDStation
	ref: https://developers.rdstation.com/en/overview """

	client_id: str
	client_secret: str
	access_token: str = field(default=None)
	code: str = field(default=None)
	redirect_url: str = field(default=None)
	refresh_token: str = field(default=None)

# pylint disable=too-many-public-methods

class RDStationRestClient():  # pylint: disable=too-many-instance-attributes
	""" Class responsible for implementing an RDStation client
	ref: https://developers.rdstation.com/en/overview """

	def __init__(self, client, **kwargs):
		self.client = client
		self.session = Session()
		self._access_token = None
		self._expires = None
		self._refresh_token = None
		self._endpoint = kwargs.get('endpoint', settings.RDSTATION['endpoints']['base_domain'])
		self._headers = kwargs.get('headers', settings.RDSTATION['default_headers'])

	@property
	def access_token(self):
		"""
		propriedade responsável por implementar um recurso de obtenção de token
			:returns: A instância de :class:`RDAuthenticationResource
		<rds_clinet.resources.auth.RDGettingAcessToken>`.
		"""
		return RDGettingAcessToken(self)

	def refresh_token(self):
		"""
		método para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`RDAuthenticationResource
		<rds_client.resources.auth.RDRefreshExpiredToken>`.
		"""
		return RDRefreshExpiredToken(self)

	def revoke_access_token(self):
		"""
		método para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`RDAuthenticationResource
		<rds_client.resources.auth.RDRevokingAcessToken>`.
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
		# pylint disable=bad-continuation
		response = self.session.request(method=method, url=url,
			data=json.dumps(data), headers=self._headers, **kwargs)
		# pylint disable=bad-continuation
		logger.debug(response)
		logger.debug(response.text)
		logger.debug(response.headers)
		logger.debug(response.cookies)

		return response.json()

	def get_account_info(self):
		"""
		returns the account name from your RD Station Marketing account.
			:returns: A instância de :class:`RDMarketingResource
		<rds_client.resources.marketing.RDMarketingAccountInfo>`.
		"""
		return RDMarketingAccountInfo(self)

	def get_tracking_code(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`RDMarketingResource
		<rds_client.resources.marketing.RDMarketingTrackingCode>`.
		"""
		return RDMarketingTrackingCode(self)

	def get_contacts_by_uiid(self, uuid):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`RDContactsResource
		<rds_client.resources.contacts.RDContactsUUID>`.
		"""
		return RDContactsUUID(self, uuid)

	def get_contacts_by_email(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`RDContactsResource
		<rds_client.resources.contacts.RDContactsEmail>`.
		"""
		return RDContactsEmail(self)

	def update_contacts_by_uuid(self, uuid):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`RDContactsResource
		<rds_client.resources.appinit.RDUpdateContactPerUUID>`.
		"""
		return RDUpdateContactPerUUID(self, uuid)

	def upsert_contact_per_identifier(self, indentifier, value):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`RDContactsResource
		<rds_client.resources.appinit.RDUpsertContactIndentifier>`.
		"""
		return RDUpsertContactIndentifier(self, indentifier, value)

	def get_contacts_by_uuid_funnel(self, uuid):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`RDFunnelsResource
		<rds_client.resources.funnels.RDContactsUUIDDetails>`.
		"""
		return RDContactsUUIDDetails(self, uuid)

	def get_contacts_by_email_funnel(self, email):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`RDFunnelsResource
		<rds_client.resources.funnels.RDContactsEmailDetails>`.
		"""
		return RDContactsEmailDetails(self, email)

	def update_contact_by_indetifier_funnel(self, indentifier, **kwargs):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`RDFunnelsResource
		<rds_client.resources.funnels.RDUpdateContactsDetails>`.
		"""
		return RDUpdateContactsDetails(self, indentifier, **kwargs)

	def get_fields(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`RDFieldsResource
		<rds_client.resources.fields.RDListFields>`.
		"""
		return RDListFields(self)

	def insert_field(self, body):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`RDFieldsResource
		<rds_client.resources.fields.RDInsertFieldCurrentAccount>`.
		"""
		return RDInsertFieldCurrentAccount(self, body)

	def update_field(self, body):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`RDFieldsResource
		<rds_client.resources.fields.RDUpdateFieldCurrentAccount>`.
		"""
		return RDUpdateFieldCurrentAccount(self, body)

	def delete_field(self, body):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`RDFieldsResource
		<rds_client.resources.fields.RDDeleteFieldCurrentAccount>`.
		"""
		return RDDeleteFieldCurrentAccount(self, body)

	# https://developers.rdstation.com/en/reference/webhooks

	def receive_webhook(self):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`RDWebhooksResource
		<rds_client.resources.webhook.RDDWebhooksReceiver>`.
		"""
		return RDDWebhooksReceiver(self)

	def create_webhook(self, body):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`RDWebhooksResource
		<rds_client.resources.webhook.RDWebhooksFactory>`.
		"""
		return RDWebhooksFactory(self, body)

	def update_webhook_by_uuid(self, uuid):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`RDWebhooksResource
		<rds_client.resources.webhook.RDUpdateWebhookPerUUID>`.
		"""
		return RDUpdateWebhookPerUUID(self, uuid)

	def delete_webhook(self, uuid):
		"""
		Propriedade para obter recursos da RD Station, recurso de inicialização do aplicativo.
			:returns: A instância de :class:`RDWebhooksResource
		<rds_client.resources.webhook.Appinit>`.
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
			<rds_client.RDStationClient.connect>`.
		"""
		if not self._access_token:
			data = self.access_token()
			try:
				self._access_token = data['access_token']
				self._expires = data['expires_in']
				self._refresh_token = data['refresh_token']
				self._headers['Authorization'] = f"Bearer {self._refresh_token}"
			except KeyError:
				return

		logger = logging.getLogger(__name__)
		logger.debug(f"access-token: {self._access_token}")
		logger.debug(f"refresh-token: {self._refresh_token}")
		logger.debug(f"expire-in: {self._expires}")
		self._access_token = self._refresh_token

	def run(self):
		"""
		método responsável por ativar uma conexão com a api da RD Station.
			<rds_client.RDStationClient.connect>`.
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

	@property
	def get_access_token(self):
		""" Propriedade para obter token de acesso atual. """
		return self._access_token

	@property
	def get_refresh_token(self):
		""" Propriedade para obter refresh token de acesso atual. """
		return self._refresh_token

	@property
	def get_expires_in(self):
		""" Propriedade para obter o expire token atual """
		return self._expires

	@property
	def get_headers(self):
		""" Obter os headers atuais da sessão http"""
		return self._headers

	def __enter__(self):
		self.connect()
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		if exc_val:
			logger = logging.getLogger(__name__)
			logger.warning(f'exc_type: {exc_type}')
			logger.warning(f'exc_value: {exc_val}')
			logger.warning(f'exc_traceback: {exc_tb}')

	def __repr__(self):
		# pylint disable=bad-continuation
		return (f'RDStation ('
		        f'refresh-token={self._refresh_token[0:10]}.., '
		        f'expire-in={self._expires})')

# end-of-file