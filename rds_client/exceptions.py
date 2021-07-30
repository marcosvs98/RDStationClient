class RDStationException(Exception):
	"""
	ref: https://developers.rdstation.com/en/error-states
	"""
	pass


class RDUnauthorizedRequest(RDStationException):
	"""
	If the token or credentials are invalid, or code is expired
	or the user is not authorized. Status 401 Unauthorized.
	"""

	def __init__(self, msg):
		super(RDUnauthorizedRequest, self).__init__(msg)


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
	"""
	If the resource does not exist in RD Station Status 404 not found.
	"""

	def __init__(self, msg):
		super(RDResourceNotFound, self).__init__(msg, status=404)


class RDUnsupportedMediaType(RDStationException):
	"""
	If the Content-Type is not set properly Status 415 Unsupported Media Type.
	"""

	def __init__(self, msg):
		super(RDUnsupportedMediaType, self).__init__(msg, status=415)


class RDMalformedBodyRequest(RDStationException):
	"""
	If the body request is malformed accordingly to the Content-Type
	header Status 400 Bad Request.
	"""

	def __init__(self, msg):
		super(RDMalformedBodyRequest, self).__init__(msg, status=400)


class RDInvalidFormat(RDStationException):
	"""
	If an invalid format for an attribute is sent Status 400 Bad Request.
	"""

	def __init__(self, msg):
		super(RDMalformedBodyRequest, self).__init__(msg, status=400)


class RDUpperCaseTagsException(RDStationException):
	"""
	If the tags contain uppercase characters:
	"""

	def __init__(self, msg):
		super(RDUpperCaseTagsException, self).__init__(msg, status=400)


class RDInvalidDataType(RDStationException):
	"""
	If an invalid data type is sent Status 422 Unprocessable Entity.
	"""

	def __init__(self, msg):
		super(RDInvalidDataType, self).__init__(msg, status=422)


class RDReadOnlyFieldsException(RDStationException):
	"""
	When trying to update a read only attribute Status 400 Bad Request.
	"""

	def __init__(self, msg):
		super(RDReadOnlyFieldsException, self).__init__(msg, status=400)


class RDInexistentFields(RDStationException):
	"""
	When trying to update an attribute that does not exist Status 400 Bad Request.
	"""

	def __init__(self, msg):
		super(RDInexistentFields, self).__init__(msg, status=400)


class RDConflictingField(RDStationException):
	"""
	When using the UPSERT like PATCH endpoint, and a field that was
	used  to identify the lead appears again in the request payload
	Status 400 Bad Request.
	"""

	def __init__(self, msg):
		super(RDInexistentFields, self).__init__(msg, status=400)


class RDEmailAlreadyInUse(RDStationException):
	"""
	When using the PATCH by uuid Contact endpoint and an e-mail
	that already is used Status 400 Bad Request.
	"""

	def __init__(self, msg):
		super(RDEmailAlreadyInUse, self).__init__(msg, status=400)


# end-of-file
