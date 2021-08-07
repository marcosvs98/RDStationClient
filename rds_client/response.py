import json

from exceptions import RDStationException
from exceptions import RDUnauthorizedRequest
from exceptions import RDForbiddenRequest
from exceptions import RDExpiredCodeGrant
from exceptions import RDResourceNotFound
from exceptions import RDInvalidrefreshToken
from exceptions import RDUnsupportedMediaType
from exceptions import RDBadRequestException
from exceptions import RDMalformedBodyRequest
from exceptions import RDInvalidFormat
from exceptions import RDUpperCaseTagsException
from exceptions import RDInvalidDataType
from exceptions import RDReadOnlyFieldsException
from exceptions import RDInexistentFields
from exceptions import RDConflictingField
from exceptions import RDEmailAlreadyInUse
from exceptions import RDValidationRelatedException


RDS_CLIENT_EXCEPTIONS = {
    # Request related error types
    "UNAUTHORIZED": RDUnauthorizedRequest,
    "ACCESS_DENIED": RDForbiddenRequest,
    "EXPIRED_CODE_GRANT": RDExpiredCodeGrant,
    "INVALID_REFRESH_TOKEN": RDInvalidrefreshToken,
    "RESOURCE_NOT_FOUND": RDResourceNotFound,
    "UNSUPPORTED_MEDIA_TYPE": RDUnsupportedMediaType,
    "BAD_REQUEST": RDBadRequestException,
    "INVALID_FORMAT": RDInvalidFormat,
    "VALUES_MUST_BE_LOWERCASE": RDUpperCaseTagsException,
    "MUST_BE_STRING": RDInvalidDataType,
    "INVALID_FIELDS": RDReadOnlyFieldsException,
    "CONFLICTING_FIELD": RDConflictingField,
    "EMAIL_ALREADY_IN_USE": RDEmailAlreadyInUse,
    # Validation related error types
    "CANNOT_BE_NULL": RDValidationRelatedException,
    "CANNOT_BE_BLANK": RDValidationRelatedException,
    "INVALID": RDValidationRelatedException,
    "TAKEN": RDValidationRelatedException,
    "TOO_SHORT": RDValidationRelatedException,
    "TOO_LONG": RDValidationRelatedException,
    "EXCLUSION": RDValidationRelatedException,
    "INCLUSION": RDValidationRelatedException,
}


class RDSResponse():
	""" ."""

	def __init__(self, response, raise_status=False, safe=False):

		json_response = response.json()
		exceptions = []

		if not json_response:
			raise RDStationException("Response body has no return in json.")

		if safe and isinstance(response.json(), dict):
			raise TypeError(
				'In order to allow non-dict objects to be serialized set the '
				'safe parameter to False.')

		for key, value in json_response.items():
			setattr(self, key, value)

		if self.errors:
			for r in self.errors:
				exceptions.append(
					self.throw_exactly_matched_exception(
						r['error_type'], r['error_message']))
			raise RDStationException(exceptions)
		try:
			post_data = {}
			for data in self.post_data.split("&"):
				key, value = data.split('=')
				post_data[key] = value
		except AttributeError:
			post_data = ''
		finally:
			setattr(self, 'post_data', post_data)

	def throw_exactly_matched_exception(self, error_type, error_message):
		exception = RDS_CLIENT_EXCEPTIONS.get(error_type, RDStationException)
		return exception(error_message)


# end-of-file