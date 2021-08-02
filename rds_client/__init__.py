import json

class RDSJsonResponse():

	def __init__(self, json_response, status_code, raise_status=False, safe=False):

		if safe and isinstance(json_response, dict):
			raise TypeError(
				'In order to allow non-dict objects to be serialized set the '
				'safe parameter to False.'
			)
		for key, value in json_response.items():
			setattr(self, key, value)

		self.response_errors = []

		if self.errors:
			for r in self.errors:
				rd_code, message = r['error_message'].split(': ')

				self.response_errors.append(
					(status_code, r['error_type'], int(rd_code), message))

		post_data = {}
		for data in self.post_data.split("&"):
			key, value = data.split('=')
			post_data[key] = value

		setattr(self, 'post_data', post_data)
		setattr(self, 'content_type', 'application/json')


c = RDSJsonResponse({
	'query_string': '',
	'request_method': 'POST',
	'request_path': '/api/platform/token',
	'post_data': 'client_id=cc3fbf81-3a32-4591-823e-8cf49d2116ab&client_secret=e52fc0ef6053427ca197c35a494f667b',
	'errors': [{
			'error_type': 'BAD_REQUEST',
			'error_message': "822: unexpected token at 'client_id=cc3fbf81-3a32-4591-823e-8cf49d2116ab&client_secret=e52fc0ef6053427ca197c35a494f667b'",
			'error_class': 'ActionDispatch::Http::Parameters::ParseError'
				},
	]}, 400)

print(c.response_errors)
print(c.post_data)
