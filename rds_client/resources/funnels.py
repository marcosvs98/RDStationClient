from abc import ABC, abstractmethod
from resources.resource import RDStationResource

"""
ref: https://developers.rdstation.com/en/reference/contacts/funnels
"""


class RDFunnelsResource(RDStationResource):
	"""
	The main object of the RD Station API is the Contact and, in order to be able to manage
	the Contacts information in an RD Station account, we provide some endpoints that bring
	a lot of flexibility of integration with your solution.

	ref: https://developers.rdstation.com/en/reference/contacts
	"""
	path = 'plataform'

	def __init__(self, client):
		super(RDFunnelsResource, self).__init__(client)

	@abstractmethod
	def __call__(self):
		pass


class RDContactsUUIDDetails(RDFunnelsResource):
	"""
	Returns a list of Funnels associated to the given contact.

	https://developers.rdstation.com/en/reference/contacts/funnels#methodGetByUuidDetails
	"""
	path = "/".join((RDFunnelsResource.path, "contacts"))

	def __call__(self, uuid, funnel_name, **kwargs):
		"""
		:uuid: type: string	: The unique uuid associated to RD Station Contact.
		:funnel_name: type: string: The contact funnel name. For now, the only accepted option is: "default".
		:param kwargs: type: dict args
		:return: json response
		{
		  "lifecycle_stage": "Client",
		  "opportunity": true,
		  "contact_owner_email": "email@example.org",
		  "fit": 60,
		  "interest": 100
		}
		"""
		# set uuid
		RDContactsUUIDDetails.path = "/".join(
			(RDContactsUUIDDetails.path, uuid, 'funnels', funnel_name)
		)
		return self._get(self, **kwargs)

	def _get(self, **kwargs):
		return self.send_response("GET", **kwargs)


class RDContactsEmailDetails(RDFunnelsResource):
	"""
	Returns a list of Funnels associated to the given contact.

	https://developers.rdstation.com/en/reference/contacts/funnels#methodGetByUuidDetails
	"""
	path = "/".join((RDFunnelsResource.path, "contacts"))

	def __call__(self, contact_email, funnel_name, **kwargs):
		"""
		:uuid: type: string	: The unique uuid associated to RD Station Contact.
		:funnel_name: type: string: The contact funnel name. For now, the only accepted option is: "default".
		:param kwargs: type: dict args
		:return: json response
		{
		  "lifecycle_stage": "Client",
		  "opportunity": true,
		  "contact_owner_email": "email@example.org",
		  "fit": 60,
		  "interest": 100
		}
		"""
		# set uuid
		RDContactsEmailDetails.path = "/".join(
			(RDContactsEmailDetails.path, f'email:{contact_email}', 'funnels', funnel_name))
		return self._get(self, **kwargs)

	def _get(self, **kwargs):
		return self.send_response("GET", **kwargs)


class RDUpdateContactsDetails(RDFunnelsResource):
	"""
	Updates the funnel information about the current contact.

	ref: https://developers.rdstation.com/en/reference/contacts
	"""
	path = "/".join((RDFunnelsResource.path, "contacts"))

	def __call__(self, lifecycle_stage, opportunity,  contact_owner_email, **kwargs):
		"""
		:param lifecycle_stage: The stage in the funnel which the contact belongs to. Valid options: 'Lead',
		'Qualified Lead' and 'Client'.
		:param opportunity: It indicates whether the contact is an opportunity or not in the funnel.
		:param contact_owner_email: The email of the user responsible for the contact. Can be defined as null
		for disassociate the current owner.
		:param kwargs: type: dict args
		:return: json response
		{
		  "lifecycle_stage": "Client",
		  "opportunity": true,
		  "contact_owner_email": "email@example.org",
		  "fit": 60,
		  "interest": 100
		}
		"""
		# set email
		RDUpdateContactsDetails.path = "/".join(
			(RDUpdateContactsDetails.path, uuid, f"|email:{contact_owner_email}", "funnels", funnel_name)
		)
		data = {
		    "lifecycle_stage": lifecycle_stage,
		    "opportunity": opportunity,
		    "contact_owner_email": contact_owner_email
		}
		return self._put(self, data=data, **kwargs)

	def _put(self, data, **kwargs):
		return self.send_response("PUT", data, **kwargs)


# end-of-file