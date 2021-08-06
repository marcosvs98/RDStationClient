import json

class RDSJsonResponse():

	def __init__(self, response, status_code, raise_status=False, safe=False):

		if safe and isinstance(json_response, dict):
			raise TypeError(
				'In order to allow non-dict objects to be serialized set the '
				'safe parameter to False.')

		for key, value in json_response.items():
			setattr(self, key, value)

		if self.errors:
			for r in self.errors:
				rd_code, message = r['error_message'].split(': ')

				log.warning(f"code: {rd_code} message: {message}")

				raise self.throw_exactly_matched_exception(
					status_code, r['error_type'], int(rd_code), message))
		try:
			post_data = {}
			for data in self.post_data.split("&"):
				key, value = data.split('=')
				post_data[key] = value
		except AttributeError:
			post_data = ''

		setattr(self, 'post_data', post_data)

	def throw_exactly_matched_exception(self, exact, string, message):
		if string in exact:
			raise RD_STATION_EXCEPTIONS[string](message)