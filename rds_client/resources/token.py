from resources.resource import RDStationResource


class RDRevokingAcessToken(RDStationResource):
	"""
	Client access with OAuth authentication type can be revoked whenever needed.
	This can be done using access_token or refresh_token.
	"""
	def __call__(self):
		pass


class RDRefreshExpiredToken(RDStationResource):
	"""
	Every access_token is temporary, and its expiration
	time is defined by the expires_in attribute in seconds,
	which is 86400 seconds (24 hours).
	"""
	def __call__(self):
		pass


class RDGettingAcessToken(RDStationResource):
	"""
	Once you have the code parameter, you just need the
	access_token. To do this, simply make a request to
	obtain the.
	"""
	def __call__(self):
		pass


# end-of-file