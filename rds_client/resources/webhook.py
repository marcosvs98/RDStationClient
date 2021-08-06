from abc import ABC, abstractmethod
from resources.resource import RDStationResource


class RDWebhooksResource(RDStationResource):
	"""
	Webhooks provide the ability to receive real-time data updates about your contact activity.

	Choose to receive data based on certain actions, re-cast or marked as an opportunity,and
	have all applicable data sent to a URL of your choice. You can then use your own custom
	application to read, save, and do actions with that data. This is a powerful option that
	allows you to keep all your data in sync and opens the possibility for all types
	of integration.

	ref: https://developers.rdstation.com/en/reference/webhooks
	"""
	path = 'integrations'

	def __init__(self, client):
		super(RDWebhooksResource, self).__init__(client)

	@abstractmethod
	def __call__(self):
		pass


class RDDWebhooksReceiver(RDWebhooksResource):
	"""
	Returns a list with all webhook subscriptions from your account.

	ref: https://developers.rdstation.com/en/reference/webhooks
	"""
	path = "/".join((RDWebhooksResource.path, "webhooks"))

	def __call__(self, **kwargs):
		"""
		:param kwargs: type: dict args
		:return: json response
		{
		  "webhooks": [
			{
			  "uuid": "5408c5a3-4711-4f2e-8d0b-13407a3e30f3",
			  "event_type": "WEBHOOK.CONVERTED",
			  "event_identifiers": ["newsletter"],
			  "entity_type": "CONTACT",
			  "url": "http://my-url.com",
			  "http_method": "POST",
			  "include_relations": []
			},
			{
			  "uuid": "642d985c-487c-4c53-b9de-2c1223841cae",
			  "event_type": "WEBHOOK.MARKED_OPPORTUNITY",
			  "event_identifiers": [],
			  "entity_type": "CONTACT",
			  "url": "http://my-url.com",
			  "http_method": "POST",
			  "include_relations": ["COMPANY", "CONTACT_FUNNEL"]
			}
		  ]
		}
		"""
		return self._get(self, **kwargs)

	def _get(self, **kwargs):
		return self.send_response("GET", **kwargs)


class RDWebhooksFactory(RDWebhooksResource):
	"""
	It creates a webhook subscription.

	ref: https://developers.rdstation.com/en/reference/webhooks
	"""
	path = "/".join((RDWebhooksResource.path, "webhooks"))

	def __call__(self, webhook, **kwargs):
		"""
		:webhook : type: string : The unique uuid associated to each RD Station Contact.
		webhook body example;
		{
		  "entity_type": "CONTACT",
		  "event_type": "WEBHOOK.CONVERTED",
		  "event_identifiers": ["newsletter"],
		  "url": "http://my-url.com",
		  "http_method": "POST",
		  "include_relations": ["COMPANY", "CONTACT_FUNNEL"]
		}
		:param kwargs: type: dict args
		:return: json response
		{
		  "uuid": "5408c5a3-4711-4f2e-8d0b-13407a3e30f3",
		  "event_type": "WEBHOOK.CONVERTED",
		  "event_identifiers": ["newsletter"],
		  "entity_type": "CONTACT",
		  "url": "http://my-url.com",
		  "http_method": "POST",
		  "include_relations": ["COMPANY", "CONTACT_FUNNEL"]
		}
		"""
		# set email
		RDWebhooksFactory.path = \
			"/".join((RDWebhooksFactory.path, f'email:{email}'))
		return self._post(self, webhook, **kwargs)

	def _post(self, data, **kwargs):
		return self.send_response("POST", data=data, **kwargs)


class RDUpdateWebhookPerUUID(RDWebhooksResource):
	"""
	It updates a webhook subscription.

	ref: https://developers.rdstation.com/en/reference/contacts
	"""
	path = "/".join((RDWebhooksResource.path, "webhooks"))

	def __call__(self, uuid, body, **kwargs):
		"""
		:uuid : type: string : The unique uuid associated to each RD Station Contact.
		:body: type: dict : Request Body Default Parameters
		:param kwargs: type: dict args
		:return: json response

		{
		  "name": "RD Station Developer",
		  "email": "contact@example.com",
		  "job_title": "Developer",
		  "bio": "This documentation explains the RD Station API.",
		  "website": "https://developers.rdstation.com/",
		  "linkedin": "rd_station",
		  "personal_phone": "+55 48 3037-3600",
		  "city": "Florianópolis",
		  "state": "SC",
		  "country": "Brasil",
		  "tags": ["developer", "rdstation", "api"],
		  "extra_emails": ["contact2@example.com"],
		  "cf_custom_field_2": "custom field value2",
		  "legal_bases": [
			{
			  "category": "communications",
			  "type": "consent",
			  "status": "granted"
			}
		  ]
		}
		"""
		# set uiid to path
		RDUpdateWebhookPerUUID.path = \
			"/".join((RDUpdateWebhookPerUUID.path, uuid))
		return self._put(self, body, **kwargs)

	def _put(self, data, **kwargs):
		return self.send_response("GET", datra=data, **kwargs)


class RDDeleteWebhookPerUUID(RDWebhooksResource):
	"""
	It updates a webhook subscription.

	ref: https://developers.rdstation.com/en/reference/contacts
	"""
	path = "/".join((RDWebhooksResource.path, "webhooks"))

	def __call__(self, uuid, **kwargs):
		"""
		:uuid : type: string : The unique uuid associated to each RD Station Contact.
		:param kwargs: type: dict args
		:return: json response
		Response examples:
		Success | Code: 204
		"""
		# set uiid to path
		RDDeleteWebhookPerUUID.path = \
			"/".join((RDDeleteWebhookPerUUID.path, uuid))
		return self._delete(self, **kwargs)

	def _detlete(self, data, **kwargs):
		return self.send_response("DELETE", **kwargs)

# end-of-file