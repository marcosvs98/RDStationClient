import json

class RDSJsonResponse():

	def __init__(self, json_response, safe=False):

		if safe and isinstance(json_response, dict):
			raise TypeError(
				'In order to allow non-dict objects to be serialized set the '
				'safe parameter to False.'
			)

		for key, value in json_response.items():
			setattr(self, key, value)
		setattr(self, 'content_type', 'application/json')


		if self.errors:
			pass



c = RDSJsonResponse({
	'query_string': '',
	'request_method': 'POST',
	'request_path': '/api/platform/token',
	'post_data': 'client_id=cc3fbf81-3a32-4591-823e-8cf49d2116ab&client_secret=e52fc0ef6053427ca197c35a494f667b',
	'errors': [{
			'error_type': 'BAD_REQUEST',
			'error_message': "822: unexpected token at 'client_id=cc3fbf81-3a32-4591-823e-8cf49d2116ab&client_secret=e52fc0ef6053427ca197c35a494f667b'",
			'error_class': 'ActionDispatch::Http::Parameters::ParseError'
				}]})

print(c.request_method)
