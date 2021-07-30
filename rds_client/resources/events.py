from resources.resource import RDStationResource

class RDConversionEvent(RDStationResource):
	"""
	The event's endpoint is responsible for receiving different event
	types in which RD Station Contacts take part in.
	"""
	path = "/".join((RDFieldsResource.path, "plataform", "events"))

	def __call__(self):

		data = {
			"event_type": "CONVERSION",
			"event_family" :"CDP",
			"payload": {
				"conversion_identifier": "Name of the conversion event",
				"name": "name of the contact",
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
				"company_name": "company name",
				"company_site": "company website",
				"company_address": "company address",
				"client_tracking_id": "lead tracking client_id",
				"traffic_source": "Google",
				"traffic_medium": "cpc",
				"traffic_campaign": "easter-50-off",
				"traffic_value": "easter eggs",
				"tags": ["mql", "2019"],
				"available_for_mailing": True,
				"legal_bases": [
					{
						"category": "communications",
						"type": "consent",
						"status": "granted"
					}
				],
				"cf_my_custom_field": "custom field value"
			}
		}


# end-of-file