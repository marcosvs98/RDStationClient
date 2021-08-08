from abc import ABC, abstractmethod
from resources.resource import RDStationResource


class RDFieldsResource(RDStationResource):
	"""
	Class responsible for implementing the ´Fields´ api feature.
	"""
	path = 'platoform'

	def __init__(self, client):
		super(RDEventResource, self).__init__(client)

	@abstractmethod
	def __call__(self):
		pass


class RDListFields(RDFieldsResource):
	"""
	Returns a list of Fields and their attributes from the current account.
	A field can be either default or custom, as follow:
		* Default fields are standard fields that represent RD Station's Contact's basic information.
		* Custom fields are fields that represent unique Contact's information accordingly to your
		organization and that were created by RD Station's users.

	ref: https://developers.rdstation.com/en/reference/fields
	"""
	path = "/".join((RDFieldsResource.path, "contacts"))

	def __call__(self, **kwargs):
		"""
		:param kwargs: type: dict args
		:return: json response
		{
		  "fields": [
			{
			  "uuid": "fdeba6ec-f1cf-4b13-b2ea-e93d47c0d828",
			  "api_identifier": "name",
			  "custom_field": false,
			  "data_type": "STRING",
			  "name": {
				"default": "nome",
				"pt-BR": "nome"
			  },
			  "label": {
				"default": "Nome completo",
				"pt-BR": "Nome completo"
			  },
			  "presentation_type": "TEXT_INPUT",
			  "validation_rules": {}
			},
			{
			  "uuid": "f0a3dd8a-f044-432c-a1ce-1bb559d6edf4",
			  "api_identifier": "cf_language",
			  "custom_field":  true,
			  "data_type": "STRING[]",
			  "name": {
				"default": "Idioma",
				"pt-BR": "Idioma"
			  },
			  "label": {
				"default": "Selecione o idioma",
				"pt-BR": "Selecione o idioma"
			  },
			  "presentation_type": "CHECK_BOX",
			  "validation_rules": {
				"valid_options": [
				  {
					"value": "Português",
					"label": {
					  "default": "Português",
					  "pt-BR": "Português"
					}
				  },
				  {
					"value": "Inglês",
					"label": {
					  "default": "Inglês",
					  "pt-BR": "Inglês"
					}
				  },
				  {
					"value": "Espanhol",
					"label": {
					  "default": "Espanhol",
					  "pt-BR": "Espanhol"
					}
				  }
				]
			  }
			}
		  ]
		}
		"""
		RDListFields.path = "/".join((RDListFields.path, "fields"))
		return self._get(self, **kwargs)

	def _get(self, **kwargs):
		return self.send_response("GET", **kwargs)


class RDInsertFieldCurrentAccount(RDFieldsResource):
	"""
	Creates a Field for the current account.
	ref: https://developers.rdstation.com/en/reference/fields#methodGetDetails
	"""

	path = "/".join((RDFieldsResource.path, "contacts"))

	def __call__(self, fields, **kwargs):
		"""
		:param field: type: dict : Request Body
		Update all attributes:
		{
		  "name": {
			"pt-BR": "Meu campo customizado"
		  },
		  "label": {
			"pt-BR": "Selecione uma das opções"
		  },
		  "api_identifier": "cf_my_custom_field",
		  "data_type": "STRING",
		  "presentation_type": "COMBO_BOX",
		  "validation_rules": {
			"valid_options": [
			  {
				"value": "opcao_1",
				"label": {
				  "pt-BR": "opcao_1"
				}
			  },
			  {
				"value": "opcao_2",
				"label": {
				  "pt-BR": "opcao_2"
				}
			  }
			]
		  }
		}
		:return: json response
		{
 		 "uuid": "fdeba6ec-f1cf-4b13-b2ea-e93d47c0d828"
		}
		"""
		RDInsertFieldCurrentAccount.path = \
			"/".join((RDInsertFieldCurrentAccount.path, "fields"))
		return self._post(self, fields, **kwargs)

	def _post(self, data, **kwargs):
		return self.send_response("POST", data=fields, **kwargs)


class RDUpdateFieldCurrentAccount(RDFieldsResource):
	"""
	Updates a Field for the current account. It supports partial updates.
	ref: https://developers.rdstation.com/en/reference/fields#methodGetDetails
	"""

	path = "/".join((RDFieldsResource.path, "contacts"))

	def __call__(self, uuid, **kwargs):
		"""
		:param field: type: dict : Request Body
		Update all attributes:
		{
		  "name": {
			"pt-BR": "Meu campo customizado"
		  },
		  "label": {
			"pt-BR": "Selecione uma das opções"
		  },
		  "data_type": "STRING",
		  "presentation_type": "COMBO_BOX",
		  "validation_rules": {
			"valid_options": [
			  {
				"value": "opcao_1",
				"label": {
				  "pt-BR": "opcao_1"
				}
			  },
			  {
				"value": "opcao_2",
				"label": {
				  "pt-BR": "opcao_2"
				}
			  }
			]
		  }
		}

		Update a single attribute
		{
  			"name": { "pt-BR": "Meu campo customizado atualizado" }
		}

		:return: json response * No response body
        {}
		"""
		RDUpdateFieldCurrentAccount.path = \
			"/".join((RDUpdateFieldCurrentAccount.path, "fields", uuid))
		return self._patch(self, fields, **kwargs)

	def _patch(self, data, **kwargs):
		return self.send_response("PATCH", data=fields, **kwargs)


class RDDeleteFieldCurrentAccount(RDFieldsResource):
	"""
	Deletes a Field from the current account.
	ref: https://developers.rdstation.com/en/reference/fields#methodGetDetails
	"""

	path = "/".join((RDFieldsResource.path, "fields"))

	def __call__(self, uuid, **kwargs):
		"""
		:param uuid: type: dict : The unique uuid associated to each RD Station field.

		response:
		Success / Code: 204
		"""
		RDDeleteFieldCurrentAccount.path = \
			"/".join((RDDeleteFieldCurrentAccount.path, f"{uuid}"))
		return self._delete(self, **kwargs)

	def _delete(self, data, **kwargs):
		return self.send_response("DELETE", **kwargs)


# end-of-file