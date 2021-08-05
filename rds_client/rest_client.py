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
	""" Class responsible for implementing input parameters for api.
	ref: https://developers.rdstation.com/en/overview """

	client_id: str
	client_secret: str
	access_token: str = field(default=None)
	code: str = field(default=None)
	redirect_url: str = field(default=None)
	refresh_token: str = field(default=None)

# pylint disable=too-many-public-methods

class RDStationRestClient():  # pylint: disable=too-many-instance-attributes
	"""Class responsible for implementing an RDStation API client.
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
		property responsible for implementing a token retrieval feature.
			:returns: the instance of :class:`RDAuthenticationResource
		<rds_clinet.resources.auth.RDGettingAcessToken>`.
		"""
		return RDGettingAcessToken(self)

	def refresh_token(self):
		"""
		método para obter recursos da estação RD, refresh access token.
			:returns: the instance of :class:`RDAuthenticationResource
		<rds_client.resources.auth.RDRefreshExpiredToken>`.
		"""
		return RDRefreshExpiredToken(self)

	def revoke_access_token(self):
		"""
		method to get resources from RD Station, revoke access token.
			:returns: the instance of :class:`RDAuthenticationResource
		<rds_client.resources.auth.RDRevokingAcessToken>`.
		"""
		return RDRevokingAcessToken(self)

	def prepare_path(self, resource):
		"""
		method responsible for constructing the url based on the requested resource

		:param resource: instance of `<rds_client.resources.RDSResource>`.
		:return: the complete url.
		"""
		return "/".join((self._endpoint, resource.path))

	def send_request(self, resource, method, data=None, **kwargs): # pylint: disable=too-many-arguments
		"""
		method responsible for sending resource request processing.
		:param resource: instance of `<rds_client.resources.RDSResource>`.
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
		method to returns the account name from your RD Station Marketing account.
			:returns: the instance of :class:`RDMarketingResource
		<rds_client.resources.marketing.RDMarketingAccountInfo>`.
		"""
		return RDMarketingAccountInfo(self)

	def get_tracking_code(self):
		"""
		method to obtain resource from RD Station, tracking code.
			:returns: the instance of :class:`RDMarketingResource
		<rds_client.resources.marketing.RDMarketingTrackingCode>`.
		"""
		return RDMarketingTrackingCode(self)

	def get_contacts_by_uiid(self, uuid):
		"""
		method to obtain resource from RD Station, get contact per uuid.
			:returns: the instance of :class:`RDContactsResource
		<rds_client.resources.contacts.RDContactsUUID>`.
		"""
		return RDContactsUUID(self, uuid)

	def get_contacts_by_email(self):
		"""
		method to obtain resource from RD Station, get contact per email.
			:returns: the instance of :class:`RDContactsResource
		<rds_client.resources.contacts.RDContactsEmail>`.
		"""
		return RDContactsEmail(self)

	def update_contacts_by_uuid(self, uuid):
		"""
		method to obtain resource from RD Station, update contact per uuid.
			:returns: the instance of :class:`RDContactsResource
		<rds_client.resources.contacts.RDUpdateContactPerUUID>`.
		"""
		return RDUpdateContactPerUUID(self, uuid)

	def upsert_contact_per_identifier(self, indentifier, value):
		"""
		method to obtain resource from RD Station, update and insert contact per indetifier.
			:returns: the instance of :class:`RDContactsResource
		<rds_client.resources.contacts.RDUpsertContactIndentifier>`.
		"""
		return RDUpsertContactIndentifier(self, indentifier, value)

	def get_contacts_by_uuid_funnel(self, uuid):
		"""
		method to obtain resource from RD Station, get contact per uuid.
			:returns: the instance of :class:`RDFunnelsResource
		<rds_client.resources.funnels.RDContactsUUIDDetails>`.
		"""
		return RDContactsUUIDDetails(self, uuid)

	def get_contacts_by_email_funnel(self, email):
		"""
		method to obtain resource from RD Station, get contact per email.
			:returns: the instance of :class:`RDFunnelsResource
		<rds_client.resources.funnels.RDContactsEmailDetails>`.
		"""
		return RDContactsEmailDetails(self, email)

	def update_contact_by_indetifier_funnel(self, indentifier, **kwargs):
		"""
		method to obtain resource from RD Station, update contacty by indetifier.
			:returns: the instance of :class:`RDFunnelsResource
		<rds_client.resources.funnels.RDUpdateContactsDetails>`.
		"""
		return RDUpdateContactsDetails(self, indentifier, **kwargs)

	def get_fields(self):
		"""
		method to obtain resource from RD Station, get field.
			:returns: the instance of :class:`RDFieldsResource
		<rds_client.resources.fields.RDListFields>`.
		"""
		return RDListFields(self)

	def insert_field(self, body):
		"""
		method to obtain resource from RD Station, insert a new field.
			:returns: the instance of :class:`RDFieldsResource
		<rds_client.resources.fields.RDInsertFieldCurrentAccount>`.
		"""
		return RDInsertFieldCurrentAccount(self, body)

	def update_field(self, body):
		"""
		method to obtain resource from RD Station, update field.
			:returns: the instance of :class:`RDFieldsResource
		<rds_client.resources.fields.RDUpdateFieldCurrentAccount>`.
		"""
		return RDUpdateFieldCurrentAccount(self, body)

	def delete_field(self, body):
		"""
		method to obtain resource from RD Station, delete field.
			:returns: the instance of :class:`RDFieldsResource
		<rds_client.resources.fields.RDDeleteFieldCurrentAccount>`.
		"""
		return RDDeleteFieldCurrentAccount(self, body)

	# https://developers.rdstation.com/en/reference/webhooks

	def receive_webhook(self):
		"""
		method to obtain resource from RD Station, retrieve a webhook.
			:returns: the instance of :class:`RDWebhooksResource
		<rds_client.resources.webhook.RDDWebhooksReceiver>`.
		"""
		return RDDWebhooksReceiver(self)

	def create_webhook(self, body):
		"""
		method to obtain resource from RD Station, create a new webhook.
			:returns: the instance of :class:`RDWebhooksResource
		<rds_client.resources.webhook.RDWebhooksFactory>`.
		"""
		return RDWebhooksFactory(self, body)

	def update_webhook_by_uuid(self, uuid):
		"""
		method to obtain resource from RD Station, update webhook per uuid.
			:returns: the instance of :class:`RDWebhooksResource
		<rds_client.resources.webhook.RDUpdateWebhookPerUUID>`.
		"""
		return RDUpdateWebhookPerUUID(self, uuid)

	def delete_webhook(self, uuid):
		"""
		method to obtain resource from RD Station, delete webhook.
			:returns: the instance of :class:`RDWebhooksResource
		<rds_client.resources.webhook.RDDeleteWebhookPerUUID>`.
		"""
		return RDDeleteWebhookPerUUID(self, uuid)

	# https://developers.rdstation.com/en/reference/events
	def create_event(self):
		"""
		method to get creation resource for RD Station default event.
			:returns: the instance of :class:`Appinit
		<rds_client.resources.event.RDEvent>`.
		"""
		return RDEvent(self)

	def create_event_batch(self):
		"""
		method to get creation resource for RD Station batch event.
			:returns: the instance of :class:`RDEventBatch
		<rds_client.resources.event.RDEventBatch>`.
		"""
		return RDEventBatch(self)

	def connect(self):
		"""
		method responsible for activating a connection with the RD Station api.
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
		method responsible for starting a running service with the RD Station api.
			<rds_client.RDStationClient.run>`.
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
		""" property to get current access token. """
		return self._access_token

	@property
	def get_refresh_token(self):
		""" property to get current access token refresh. """
		return self._refresh_token

	@property
	def get_expires_in(self):
		""" property to get current expire token """
		return self._expires

	@property
	def get_headers(self):
		""" get the current http session headers """
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