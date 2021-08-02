
from abc import abstractmethod
from resources.resource import RDStationResource

class RDEventResource(ABC, RDStationResource):
	"""
		The event's endpoint is responsible for receiving different event
		types in which RD Station Contacts take part in.
		"""
	path = "/".join((RDFieldsResource.path, "plataform"))

	@abstractmethod
	def __call__(self):
		pass


class RDEvent(RDEventResource):
	"""
	The event's endpoint is responsible for receiving different event
	types in which RD Station Contacts take part in.
	"""
	path = "/".join((RDEventResource.path, "events"))

	def __call__(self, event_body,  **kwargs):
		"""
		:param event_type: The event type that diferentiates the event.
			For the conversion event it should be sent as "CONVERSION".
		:param event_family: The family of the event for processing purposes.
			It currently accepts only "CDP" as valid option.
		:param conversion_identifier: The name of the conversion event.
		example request body:
		{
		  "event_type": "CONVERSION",
		  "event_family":"CDP",
		  "payload": {
			"conversion_identifier": "Name of the conversion event",
			"name": "Nome",
			"email": "email@email.com",
			"job_title": "job title value",
			"state": "state of the contact",
			"city": "city of the contact",
			"country": "country of the contact",
			"personal_phone": "phone of the contact",
			"mobile_phone": "mobile_phone of the contact",
			"twitter": "twitter handler of the contact",
			"facebook": "facebook name of the contact",
			"linkedin": "linkedin user name of the contact",
			"website": "website of the contact",
			"cf_custom_field_api_identifier": "custom field value",
			"company_name": "company name",
			"company_site": "company website",
			"company_address": "company address",
			"client_tracking_id": "lead tracking client_id",
			"traffic_source": "Google",
			"traffic_medium": "cpc",
			"traffic_campaign": "easter-50-off",
			"traffic_value": "easter eggs",
			"tags": ["mql", "2019"],
			"available_for_mailing": true,
			"legal_bases": [
			  {
				"category": "communications",
				"type": "consent",
				"status": "granted"
			  }
			]
		  }
		}
		:param kwargs: Other's params
		:return: JsonResponse
			Success | Code: 200
		{
		  "event_uuid": "5408c5a3-4711-4f2e-8d0b-13407a3e30f3"
		}
		"""

		return self._post(self, event_body, **kwargs)

	def _post(self, data, **kwargs):
		return self.send_response("POST", data=data, **kwargs)



class RDEventBatch(RDEventResource):
	"""
	The events batch endpoint allows RD Station to receive more than one
	event at once. Thus allowing events of order placed and order placed
	items to be sent without the need of multiple requests.
	"""
	path = "/".join((RDEventResource.path, "events", 'batch'))

	def __call__(self, event_body,  **kwargs):
		"""
		:param event_type: The event type that diferentiates the event.
			For the conversion event it should be sent as "CONVERSION".
		:param event_family: The family of the event for processing purposes.
			It currently accepts only "CDP" as valid option.
		:param conversion_identifier: The name of the conversion event.
		example request body:
		{
		  "event_type": "CONVERSION",
		  "event_family":"CDP",
		  "payload": {
			"conversion_identifier": "Name of the conversion event",
			"name": "Nome",
			"email": "email@email.com",
			"job_title": "job title value",
			"state": "state of the contact",
			"city": "city of the contact",
			"country": "country of the contact",
			"personal_phone": "phone of the contact",
			"mobile_phone": "mobile_phone of the contact",
			"twitter": "twitter handler of the contact",
			"facebook": "facebook name of the contact",
			"linkedin": "linkedin user name of the contact",
			"website": "website of the contact",
			"cf_custom_field_api_identifier": "custom field value",
			"company_name": "company name",
			"company_site": "company website",
			"company_address": "company address",
			"client_tracking_id": "lead tracking client_id",
			"traffic_source": "Google",
			"traffic_medium": "cpc",
			"traffic_campaign": "easter-50-off",
			"traffic_value": "easter eggs",
			"tags": ["mql", "2019"],
			"available_for_mailing": true,
			"legal_bases": [
			  {
				"category": "communications",
				"type": "consent",
				"status": "granted"
			  }
			]
		  }
		}
		:param kwargs: Other's params
		:return: JsonResponse
			Success | Code: 200
		{
		  "event_uuid": "5408c5a3-4711-4f2e-8d0b-13407a3e30f3"
		}
		"""

		return self._post(self, event_body, **kwargs)

	def _post(self, data, **kwargs):
		return self.send_response("POST", data=data, **kwargs)


# end-of-file