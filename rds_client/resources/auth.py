from abc import ABC, abstractmethod
from resources.resource import RDStationResource

class RDAuthenticationResource(RDStationResource):
	"""
	In RD Station, eliminated OAuth and API Keys authentication methods.
	ref: https://api.rd.services/auth/token
	"""
	path = 'auth'

	@abstractmethod
	def __call__(self):
		pass


class RDGettingAcessToken(RDAuthenticationResource):
	"""
	The use of API Key makes it possible to send conversion events to
	RD Station Marketing. API key is a token that must be sent via
	Query String using the api_key parameter.

	ref: https://developers.rdstation.com/en/authentication#methodGetDetails
	"""

	path = "/".join((RDAuthenticationResource.path, "token"))

	def __call__(self, **kwargs):
		"""
		:param client_id: type: String Cliente
		:param client_secret: type: String Secret of client
		:param code: type: String Código
		:return: json response
		{
			"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5UZ3hRamM1UWpKR1FUUkNPRVE0UVRZeFJF"
			               "VTBNRFEzUkRGRE9UVXdPVE5FTXpVM09UUXpRUSJ9.eyJpc3MiOiJodHRwczovL3Jkc3RhdGlvbi5hdXRo"
			               "MC5jb20vIiwic3ViIjoidklUYjF2N0NoVmhmUVE2QUFTbDNLVUpYRUJTSVNCR2hAY2xpZW50cyIsImF1Z"
			               "CI6Imh0dHBzOi8vYXBwLnJkc3RhdGlvbi5jb20uYnIvYXBpL3YyLyIsImV4cCI6MTUwNDI5NDQzMSwiaW"
			               "F0IjoxNTA0MjA4MDMxLCJzY29wZSI6IiJ9.k7OSdhOlTgRBZmEhg_uXXaCofEq4iwDdBi6yuD8SxMF06nC"
			               "A834KjIqWkmX-W-u84q8SEzGyhb_KT0zZlMvyGotoGPMry_vABXEIorC25zKCUE9BtMJpHJ_suFwQMqZQ8r"
			               "K6JSnbkOKwLuuDq8_YnrutBURJiBSdSI9325MLw0DZdnw0IgXnNVCHRLdOMl4k_Ovk5Ke3yzESJvMxgJJ3U"
			               "nojL0ckRExVPwxnbLCyJp1W_PsEe-FOcEl0kDEX-8JQ8MGATiB2vZOu5TJi4sbYCLzg3GInegGh9zvZQR1W"
			               "4K3isDtOmlNRSYU9A5ez3dQ8HTZdCj9gT_aGWWskxWi6Cw",
			"expires_in":86400,
			"refresh_token":"9YORmXHgOI32k-Y22tZWm-rsf--oFPr8JDCQIQhBEUY"
		}
		"""
		data = {
			"client_id": self.client.client.client_id,
			"client_secret": self.client.client.client_secret,
			"code": self.client.client.code
		}
		return self._post(data=data, **kwargs)

	def _post(self, data, **kwargs):
		return self.send_request(method="POST", data=data, **kwargs)



class RDRefreshExpiredToken(RDAuthenticationResource):
	"""
	Every access_token is temporary, and its expiration time is defined by
	the expires_in attribute in seconds, which is 86400 seconds (24 hours).
	"""
	path = "/".join((RDAuthenticationResource.path, "revoke"))

	def __call__(self, client_id, client_secret, refresh_token, **kwargs):
		"""
		:param client_id: type: String Cliente
		:param client_secret: type: String Secret of client
		:param refresh_token: type: token para atualização
		:return: json response
		{
			"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5UZ3hRamM1UWpKR1FUUkNPRVE0UVRZeFJF"
			               "VTBNRFEzUkRGRE9UVXdPVE5FTXpVM09UUXpRUSJ9.eyJpc3MiOiJodHRwczovL3Jkc3RhdGlvbi5hdXRo"
			               "MC5jb20vIiwic3ViIjoidklUYjF2N0NoVmhmUVE2QUFTbDNLVUpYRUJTSVNCR2hAY2xpZW50cyIsImF1Z"
			               "CI6Imh0dHBzOi8vYXBwLnJkc3RhdGlvbi5jb20uYnIvYXBpL3YyLyIsImV4cCI6MTUwNDI5NDQzMSwiaW"
			               "F0IjoxNTA0MjA4MDMxLCJzY29wZSI6IiJ9.k7OSdhOlTgRBZmEhg_uXXaCofEq4iwDdBi6yuD8SxMF06nC"
			               "A834KjIqWkmX-W-u84q8SEzGyhb_KT0zZlMvyGotoGPMry_vABXEIorC25zKCUE9BtMJpHJ_suFwQMqZQ8r"
			               "K6JSnbkOKwLuuDq8_YnrutBURJiBSdSI9325MLw0DZdnw0IgXnNVCHRLdOMl4k_Ovk5Ke3yzESJvMxgJJ3U"
			               "nojL0ckRExVPwxnbLCyJp1W_PsEe-FOcEl0kDEX-8JQ8MGATiB2vZOu5TJi4sbYCLzg3GInegGh9zvZQR1W"
			               "4K3isDtOmlNRSYU9A5ez3dQ8HTZdCj9gT_aGWWskxWi6Cw",
			"expires_in":86400,
			"refresh_token":"9YORmXHgOI32k-Y22tZWm-rsf--oFPr8JDCQIQhBEUY"
		}
		"""
		data = {
		    "client_id": client_id,
		    "client_secret": client_secret,
		    "refresh_token": refresh_token
		}
		return self._post(self, data, **kwargs)

	def _post(self, data, **kwargs):
		return self.send_response("POST", data=data, **kwargs)


class RDRevokingAcessToken(RDAuthenticationResource):
	"""
	The use of API Key makes it possible to send conversion events to RD Station Marketing.
	API key is a token that must be sent via Query String using the api_key parameter
	"""

	def __call__(self, client_id, **kwargs):
		"""
		:param client_id: type: String Cliente
		:param client_secret: type: String Secret of client
		:param token_type_hint: type: token para atualização
		:return: json response
		{
			"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5UZ3hRamM1UWpKR1FUUkNPRVE0UVRZeFJF"
			               "VTBNRFEzUkRGRE9UVXdPVE5FTXpVM09UUXpRUSJ9.eyJpc3MiOiJodHRwczovL3Jkc3RhdGlvbi5hdXRo"
			               "MC5jb20vIiwic3ViIjoidklUYjF2N0NoVmhmUVE2QUFTbDNLVUpYRUJTSVNCR2hAY2xpZW50cyIsImF1Z"
			               "CI6Imh0dHBzOi8vYXBwLnJkc3RhdGlvbi5jb20uYnIvYXBpL3YyLyIsImV4cCI6MTUwNDI5NDQzMSwiaW"
			               "F0IjoxNTA0MjA4MDMxLCJzY29wZSI6IiJ9.k7OSdhOlTgRBZmEhg_uXXaCofEq4iwDdBi6yuD8SxMF06nC"
			               "A834KjIqWkmX-W-u84q8SEzGyhb_KT0zZlMvyGotoGPMry_vABXEIorC25zKCUE9BtMJpHJ_suFwQMqZQ8r"
			               "K6JSnbkOKwLuuDq8_YnrutBURJiBSdSI9325MLw0DZdnw0IgXnNVCHRLdOMl4k_Ovk5Ke3yzESJvMxgJJ3U"
			               "nojL0ckRExVPwxnbLCyJp1W_PsEe-FOcEl0kDEX-8JQ8MGATiB2vZOu5TJi4sbYCLzg3GInegGh9zvZQR1W"
			               "4K3isDtOmlNRSYU9A5ez3dQ8HTZdCj9gT_aGWWskxWi6Cw",
			"expires_in":86400,
			"refresh_token":"9YORmXHgOI32k-Y22tZWm-rsf--oFPr8JDCQIQhBEUY"
		}
		"""
		data = {
		    "client_id": client_id,
		    "client_secret": client_secret,
		    "token_type_hint": "refresh_token"
		}
		return self._post(self, data, **kwargs)

	def _post(self, data, **kwargs):
		return self.send_response("POST", data=data, **kwargs)



# end-of-file