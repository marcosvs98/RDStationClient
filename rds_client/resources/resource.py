
class RDStationResource(object):
	"""
	Class responsible for implementing an Abstract Factory.
	"""
	def __init__(self, client):
		"""
		:param api: The instance of :class:`RDStationClient
		<rest_client.resource.RDStationResource>`.
		"""
		self.client = client

	def send_request(self, method, data=None, *args, **kwargs):
		return self.client.send_request(self, method, data=data, *args, **kwargs)

# end-of-file