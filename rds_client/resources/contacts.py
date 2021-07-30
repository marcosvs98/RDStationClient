from abc import ABC, abstractmethod
from resources.resource import RDStationResource

"""
ref: https://developers.rdstation.com/en/reference/contacts
"""

class RDContactsResource(RDStationResource):
	"""
	The main object of the RD Station API is the Contact and, in order to be able to manage
	the Contacts information in an RD Station account, we provide some endpoints that bring
	a lot of flexibility of integration with your solution.

	ref: https://developers.rdstation.com/en/reference/contacts
	"""
	path = 'plataform'

	@abstractmethod
	def __call__(self):
		pass


class RDContactsUUID(RDStationResource):
	"""
	Returns data about a specific Contact per UUID.

	ref: https://developers.rdstation.com/en/reference/contacts
	"""
	url = "/".join((RDAuthentication.url, "plataform", "contacts"))

	def __call__(self, uuid, **kwargs):
		"""
		:uuid : type: string : The unique uuid associated to each RD Station Contact.  
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
		# set uuid
		RDContactsUUID.url = "/".join((RDAuthentication.url, uuid))
		
		return self._get(self, **kwargs)

	def _get(self, **kwargs):
		return self.send_response("GET", **kwargs)


class RDContactsEmail(RDStationResource):
	"""
	Returns data about a specific Contact per E-mail.

	ref: https://developers.rdstation.com/en/reference/contacts
	"""
	url = "/".join((RDAuthentication.url, "plataform", "contacts"))

	def __call__(self, email, **kwargs):
		"""
		:uuid : type: string : The unique uuid associated to each RD Station Contact.
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
		RDContactsUUID.url = "/".join((RDAuthentication.url, f'email:{email}'))

		return self._get(self, **kwargs)

	def _get(self, **kwargs):
		return self.send_response("GET", **kwargs)


class RDUpdateContactPerUUID(RDStationResource):
	"""
	Updates the properties of a Contact per UIID.

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

		return self._patch(self, **kwargs)

	def _patch(self, **kwargs):
		return self.send_response("PATCH", **kwargs)


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

		return self._pach(self, **kwargs)

	def _patch(self, **kwargs):
		return self.send_response("PATCH", **kwargs)


# end-of-file