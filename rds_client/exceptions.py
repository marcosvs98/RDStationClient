""" We use conventional HTTP response codes to indicate the success or failure
of an API request. In general, codes in the 2xx range indicate success, codes
in the 4xx range indicate an error that failed given the information provided
(e.g., a required parameter was omitted, a charge failed, etc.), and codes
in the 5xx range indicate an error with our servers (these are rare). """


class RDStationException(Exception):
	""" ref: https://developers.rdstation.com/en/error-states """
	pass


class RDUnauthorizedRequest(RDStationException):
	""" If the token or credentials are invalid, or code is expired or the user
	is not authorized. Status 401 Unauthorized. """

	def __init__(self, msg):
		super(RDUnauthorizedRequest, self).__init__(msg)


class RDForbiddenRequest(RDStationException):

	def __init__(self, msg):
		super(RDStationException, self).__init__(msg)


class RDExpiredCodeGrant(RDStationException):
	def __init__(self, msg):
		super(RDExpiredCodeGrant, self).__init__(msg)


class RDResourceNotFound(RDStationException):
	""" If the resource does not exist in RD Station Status 404 not found. """

	def __init__(self, msg):
		super(RDResourceNotFound, self).__init__(msg)


class RDInvalidrefreshToken(RDUnauthorizedRequest):
	def __init__(self, msg):
		super(RDUnauthorizedRequest, self).__init__(msg)


class RDUnsupportedMediaType(RDStationException):
	""" If the Content-Type is not set properly Status 415 Unsupported Media Type. """

	def __init__(self, msg):
		super(RDUnsupportedMediaType, self).__init__(msg)


class RDBadRequestException(RDStationException):
	def __init__(self, msg):
		super(RDMalformedBodyRequest, self).__init__(msg)


class RDMalformedBodyRequest(RDBadRequestException):
	""" If the body request is malformed accordingly to the Content-Type
	header Status 400 Bad Request. """

	def __init__(self, msg):
		super(RDMalformedBodyRequest, self).__init__(msg)


class RDInvalidFormat(RDBadRequestException):
	""" If an invalid format for an attribute is sent Status 400 Bad Request. """

	def __init__(self, msg):
		super(RDMalformedBodyRequest, self).__init__(msg)


class RDUpperCaseTagsException(RDBadRequestException):
	""" If the tags contain uppercase characters: """

	def __init__(self, msg):
		super(RDUpperCaseTagsException, self).__init__(msg)


class RDInvalidDataType(RDStationException):
	""" If an invalid data type is sent Status 422 Unprocessable Entity. """

	def __init__(self, msg):
		super(RDInvalidDataType, self).__init__(msg)


class RDReadOnlyFieldsException(RDStationException):
	""" When trying to update a read only attribute Status 400 Bad Request. """

	def __init__(self, msg):
		super(RDReadOnlyFieldsException, self).__init__(msg)


class RDInexistentFields(RDStationException):
	""" When trying to update an attribute that does not exist Status 400 Bad Request. """

	def __init__(self, msg):
		super(RDInexistentFields, self).__init__(msg)


class RDConflictingField(RDStationException):
	""" When using the UPSERT like PATCH endpoint, and a field that was used  to identify
	the lead appears again in the request payload Status 400 Bad Request. """

	def __init__(self, msg):
		super(RDInexistentFields, self).__init__(msg)


class RDEmailAlreadyInUse(RDStationException):
	""" When using the PATCH by uuid Contact endpoint and an e-mail
	that already is used Status 400 Bad Request. """

	def __init__(self, msg):
		super(RDEmailAlreadyInUse, self).__init__(msg)


class RDValidationRelatedException(RDStationException):
	""" Validation related error types """

	def __init__(self, msg):
		super(RDValidationRelatedException, self).__init__(msg)


# end-of-file
