from abc import ABC, abstractmethod
from resources.resource import RDStationResource


class RDWebhooksResource(RDStationResource):
	"""
	Webhooks provide the ability to receive real-time data updates about your contact activity.

	Choose to receive data based on certain actions, re-cast or marked as an opportunity,
	and have all applicable data sent to a URL of your choice. You can then use your own
	custom application to read, save, and do actions with that data. This is a powerful option
	that allows you to keep all your data in sync and opens the
	 possibility for all types of integration.

	ref: https://developers.rdstation.com/en/reference/webhooks
	"""
	path = 'integrations'

	@abstractmethod
	def __call__(self):
		pass


class RDDWebhooksReceiver(RDWebhooksResource):
	"""
	Returns a list with all webhook subscriptions from your account.

	ref: https://developers.rdstation.com/en/reference/webhooks
	"""
	path = "/".join((RDAuthentication.path, "webhooks"))

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
	path = "/".join((RDAuthentication.path, "webhooks"))

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
		RDContactsUUID.url = "/".join((RDAuthentication.url, f'email:{email}'))

		return self._post(self, webhook, **kwargs)

	def _post(self, data, **kwargs):
		return self.send_response("POST", data=data, **kwargs)


class RDUpdateWebhookPerUUID(RDStationResource):
	"""
	It updates a webhook subscription.

	ref: https://developers.rdstation.com/en/reference/contacts
	"""
	path = "/".join((RDAuthentication.path, "plataform", "contacts"))

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
		# set email
		RDContactsUUID.path = "/".join((RDAuthentication.path, uuid))

		return self._path(self, **kwargs)

	def _path(self, **kwargs):
		return self.send_response("GET", **kwargs)


class RDUpsertContactIndentifier(RDStationResource):
	"""
	Updates the properties of a Contact per UIID.

	ref: https://developers.rdstation.com/en/reference/contacts
	"""
	path = "/".join((RDAuthentication.path, "plataform", "contacts"))

	def __call__(self, identifier, value, **kwargs):
		"""
		:identifier : type: string : The api_identifier of the Contact Field that uniquely identifies the Lead.
		                             Currently only email or uuid are supported.
		:value: type: string : The value for the given identifier
		                             e.g. contact@example.org or 5408c5a3-4711-4f2e-8d0b-13407a3e30f3.
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
		# set email
		RDContactsUUID.path = "/".join((RDAuthentication.path, f"{identifier}:{value}"))

		return self._path(self, **kwargs)

	def _path(self, **kwargs):
		return self.send_response("GET", **kwargs)

# end-of-file