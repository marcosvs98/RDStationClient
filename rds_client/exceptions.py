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

	'Order would trigger immediately.': InvalidOrder,
	'Account has insufficient balance for requested action.': InsufficientFunds,
	'Rest API trading is not enabled.': ExchangeNotAvailable,
	"You don't have permission.": PermissionDenied,  # {"msg":"You don't have permission.","success":false}
	'Market is closed.': ExchangeNotAvailable,  # {"code":-1013,"msg":"Market is closed."}
	'-1000': ExchangeNotAvailable,  # {"code":-1000,"msg":"An unknown error occured while processing the request."}
	'-1001': ExchangeNotAvailable,  # 'Internal error; unable to process your request. Please try again.'
	'-1002': AuthenticationError,  # 'You are not authorized to execute self request.'
	'-1003': RateLimitExceeded,
	# {"code":-1003,"msg":"Too much request weight used, current limit is 1200 request weight per 1 MINUTE. Please use the websocket for live updates to avoid polling the API."}
	'-1013': InvalidOrder,  # createOrder -> 'invalid quantity'/'invalid price'/MIN_NOTIONAL
	'-1015': RateLimitExceeded,  # 'Too many new orders; current limit is %s orders per %s.'
	'-1016': ExchangeNotAvailable,  # 'This service is no longer available.',
	'-1020': BadRequest,  # 'This operation is not supported.'
	'-1021': InvalidNonce,  # 'your time is ahead of server'
	'-1022': AuthenticationError,  # {"code":-1022,"msg":"Signature for self request is not valid."}
	'-1100': BadRequest,  # createOrder(symbol, 1, asdf) -> 'Illegal characters found in parameter 'price'
	'-1101': BadRequest,  # Too many parameters; expected %s and received %s.
	'-1102': BadRequest,  # Param %s or %s must be sent, but both were empty
	'-1103': BadRequest,  # An unknown parameter was sent.
	'-1104': BadRequest,  # Not all sent parameters were read, read 8 parameters but was sent 9
	'-1105': BadRequest,  # Parameter %s was empty.
	'-1106': BadRequest,  # Parameter %s sent when not required.
	'-1111': BadRequest,  # Precision is over the maximum defined for self asset.
	'-1112': InvalidOrder,  # No orders on book for symbol.
	'-1114': BadRequest,  # TimeInForce parameter sent when not required.
	'-1115': BadRequest,  # Invalid timeInForce.
	'-1116': BadRequest,  # Invalid orderType.
	'-1117': BadRequest,  # Invalid side.
	'-1118': BadRequest,  # New client order ID was empty.
	'-1119': BadRequest,  # Original client order ID was empty.
	'-1120': BadRequest,  # Invalid interval.
	'-1121': BadSymbol,  # Invalid symbol.
	'-1125': AuthenticationError,  # This listenKey does not exist.
	'-1127': BadRequest,  # More than %s hours between startTime and endTime.
	'-1128': BadRequest,  # {"code":-1128,"msg":"Combination of optional parameters invalid."}
	'-1130': BadRequest,  # Data sent for paramter %s is not valid.
	'-1131': BadRequest,  # recvWindow must be less than 60000
	'-2010': ExchangeError,
	# generic error code for createOrder -> 'Account has insufficient balance for requested action.', {"code":-2010,"msg":"Rest API trading is not enabled."}, etc...
	'-2011': OrderNotFound,  # cancelOrder(1, 'BTC/USDT') -> 'UNKNOWN_ORDER'
	'-2013': OrderNotFound,  # fetchOrder(1, 'BTC/USDT') -> 'Order does not exist'
	'-2014': AuthenticationError,  # {"code":-2014, "msg": "API-key format invalid."}
	'-2015': AuthenticationError,  # "Invalid API-key, IP, or permissions for action."
	'-3005': InsufficientFunds,
	# {"code":-3005,"msg":"Transferring out not allowed. Transfer out amount exceeds max amount."}
	'-3008': InsufficientFunds,
	# {"code":-3008,"msg":"Borrow not allowed. Your borrow amount has exceed maximum borrow amount."}
	'-3010': ExchangeError,  # {"code":-3010,"msg":"Repay not allowed. Repay amount exceeds borrow amount."}
	'-3022': AccountSuspended,  # You account's trading is banned.
},


# end-of-file

