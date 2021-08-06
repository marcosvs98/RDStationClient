"""
We use conventional HTTP response codes to indicate the success or failure
of an API request. In general, codes in the 2xx range indicate success, codes
in the 4xx range indicate an error that failed given the information provided
(e.g., a required parameter was omitted, a charge failed, etc.), and codes
in the 5xx range indicate an error with our servers (these are rare).
"""

class RDStationException(Exception):
	""" ref: https://developers.rdstation.com/en/error-states """
	pass


class RDUnauthorizedRequest(RDStationException):
	"""
	If the token or credentials are invalid, or code is expired
	or the user is not authorized. Status 401 Unauthorized.
	"""
	def __init__(self, msg, rd_code, status):
		super(RDUnauthorizedRequest, self).__init__(msg, rd_code, status)


class RDForbiddenResponse(RDStationException):
	def __init__(self, msg):
		super(RDStationException, self).__init__(msg, status=403)


class RDPermissionDenied(RDStationException):
	def __init__(self, msg):
		super(RDStationException, self).__init__(msg, status=406)


class RDExpiredCodeGrant(RDStationException):
	def __init__(self, msg):
		super(RDExpiredCodeGrant, self).__init__(msg, status=401)


class RDInvalidrefreshToken(RDStationException):
	def __init__(self, msg):
		super(RDInvalidrefreshToken, self).__init__(msg, status=405)


class RDResourceNotFound(RDStationException):
	""" If the resource does not exist in RD Station Status 404 not found. """

	def __init__(self, msg):
		super(RDResourceNotFound, self).__init__(msg, status=404)


class RDUnsupportedMediaType(RDStationException):
	""" If the Content-Type is not set properly Status 415 Unsupported Media Type. """

	def __init__(self, msg):
		super(RDUnsupportedMediaType, self).__init__(msg, status=415)


class RDMalformedBodyRequest(RDStationException):
	""" If the body request is malformed accordingly to the Content-Type
	header Status 400 Bad Request. """

	def __init__(self, msg):
		super(RDMalformedBodyRequest, self).__init__(msg, status=400)


class RDInvalidFormat(RDStationException):
	""" If an invalid format for an attribute is sent Status 400 Bad Request. """

	def __init__(self, msg):
		super(RDMalformedBodyRequest, self).__init__(msg, status=400)


class RDUpperCaseTagsException(RDStationException):
	""" If the tags contain uppercase characters: """

	def __init__(self, msg):
		super(RDUpperCaseTagsException, self).__init__(msg, status=400)


class RDInvalidDataType(RDStationException):
	""" If an invalid data type is sent Status 422 Unprocessable Entity. """

	def __init__(self, msg):
		super(RDInvalidDataType, self).__init__(msg, status=422)


class RDReadOnlyFieldsException(RDStationException):
	""" When trying to update a read only attribute Status 400 Bad Request. """

	def __init__(self, msg):
		super(RDReadOnlyFieldsException, self).__init__(msg, status=400)


class RDInexistentFields(RDStationException):
	""" When trying to update an attribute that does not exist Status 400 Bad Request. """

	def __init__(self, msg):
		super(RDInexistentFields, self).__init__(msg, status=400)


class RDConflictingField(RDStationException):
	""" When using the UPSERT like PATCH endpoint, and a field that was
	used  to identify the lead appears again in the request payload
	Status 400 Bad Request. """

	def __init__(self, msg):
		super(RDInexistentFields, self).__init__(msg, status=400)


class RDEmailAlreadyInUse(RDStationException):
	""" When using the PATCH by uuid Contact endpoint and an e-mail
	that already is used Status 400 Bad Request. """

	def __init__(self, msg):
		super(RDEmailAlreadyInUse, self).__init__(msg, status=400)



HTTP_EXCEPTIONS = {
	'401': ExchangeError,
	'404': DDoSProtection,
	'429': RateLimitExceeded,
	'44': ExchangeNotAvailable,
	'409': ExchangeNotAvailable,
	'410': ExchangeNotAvailable,
	'500': ExchangeNotAvailable,
	'501': ExchangeNotAvailable,
	'502': ExchangeNotAvailable,
	'520': ExchangeNotAvailable,
	'521': ExchangeNotAvailable,
	'522': ExchangeNotAvailable,
	'525': ExchangeNotAvailable,
	'526': ExchangeNotAvailable,
	'400': ExchangeNotAvailable,
	'403': ExchangeNotAvailable,
	'405': ExchangeNotAvailable,
	'503': ExchangeNotAvailable,
	'530': ExchangeNotAvailable,
	'408': RequestTimeout,
	'504': RequestTimeout,
	'401': AuthenticationError,
	'511': AuthenticationError,
}


RD_STATION_EXCEPTIONS = {
	'-1103': BadRequest,  # An unknown parameter was sent.
	'-1104': BadRequest,  # Not all sent parameters were read, read 8 parameters but was sent 9
	'-1105': BadRequest,  # Parameter %s was empty.
	'-1106': BadRequest,  # Parameter %s sent when not required.
	'-1111': BadRequest,  # Precision is over the maximum defined for self asset.
	'-1112': InvalidOrder,  # No orders on book for symbol.
	'-1114': BadRequest,  # TimeInForce parameter sent when not required.
	'-1115': BadRequest,  # Invalid timeInForce.

},


# end-of-file

