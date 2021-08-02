from abc import ABC, abstractmethod
from resources.resource import RDStationResource


class RDMarketingResource(RDStationResource):
	"""
	Classe responsável por implementar o recurso de api ´Marketing´.
	"""
	path = 'marketing'

	@abstractmethod
	def __call__(self):
		pass


class RDMarketingAccountInfo(RDMarketingResource):
	"""
	The use of API Key makes it possible to send conversion events to
	RD Station Marketing. API key is a token that must be sent via
	Query String using the api_key parameter.

	ref: https://developers.rdstation.com/pt-BR/reference/account_infos#methodGetDetails
	"""

	path = "/".join((RDMarketingResource.path, "account_info"))

	def __call__(self, **kwargs):
		"""
		:param kwargs: type: dict args
		:return: json response
		{
		  "name": "Account Name"
		}
		"""
		return self._get(self, **kwargs)

	def _get(self, **kwargs):
		return self.send_response("GET", **kwargs)


class RDMarketingTrackingCode(RDMarketingResource):
	"""
	The use of API Key makes it possible to send conversion events to
	RD Station Marketing. API key is a token that must be sent via
	Query String using the api_key parameter.

	ref: https://developers.rdstation.com/pt-BR/reference/account_infos#methodGetDetails
	"""

	path = "/".join((RDMarketingResource.path, "tracking_code"))

	def __call__(self, **kwargs):
		"""
		:param kwargs: type: dict args
		:return: json response
		{
		   "path": "https://d335luupugsy2.cloudfront.net/js/loader-scripts/8d2892c6-b15a-36916776e5e7-loader.js"
		}
		"""
		return self._get(self, **kwargs)

	def _get(self, **kwargs):
		return self.send_response("GET", **kwargs)


# end-of-file