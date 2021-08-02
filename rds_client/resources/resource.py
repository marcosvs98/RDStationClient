from abc import ABC


class RDStationResource(object):
	"""
	Classe responsável por implementar uma Abstract Factory.
	"""
	def __init__(self, client):
		"""
		:param api: The instance of :class:`IQOptionAPI
		<iqoptionapi.api.IQOptionAPI>`.
		"""
		self.client = client

	def send_request(self, method, data=None, *args, **kwargs):
		return self.client.send_request(self, method, data=data, *args, **kwargs)

# end-of-file