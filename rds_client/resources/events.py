
from abc import abstractmethod
from resources.resource import RDStationResource

class RDEventResource(ABC, RDStationResource):
	"""
		The event's endpoint is responsible for receiving different event
		types in which RD Station Contacts take part in.
		"""
	path = "/".join((RDFieldsResource.path, "plataform"))

	@abstractmethod
	def __call__(self):
		pass


class RDConversionEvent(RDEventResource):
	"""
	The event's endpoint is responsible for receiving different event
	types in which RD Station Contacts take part in.
	"""
	path = "/".join((RDEventResource.path, "events"))

	def __call__(self, event_type, event_family, conversion_identifier, **kwargs):
		"""
		:param event_type: The event type that diferentiates the event.
			For the conversion event it should be sent as "CONVERSION".
		:param event_family: The family of the event for processing purposes.
			It currently accepts only "CDP" as valid option.
		:param conversion_identifier: The name of the conversion event.
		example request body:
		{
		  "event_type": "CONVERSION",
		  "event_family":"CDP",
		  "payload": {
			"conversion_identifier": "Name of the conversion event",
			"name": "Nome",
			"email": "email@email.com",
			"job_title": "job title value",
			"state": "state of the contact",
			"city": "city of the contact",
			"country": "country of the contact",
			"personal_phone": "phone of the contact",
			"mobile_phone": "mobile_phone of the contact",
			"twitter": "twitter handler of the contact",
			"facebook": "facebook name of the contact",
			"linkedin": "linkedin user name of the contact",
			"website": "website of the contact",
			"cf_custom_field_api_identifier": "custom field value",
			"company_name": "company name",
			"company_site": "company website",
			"company_address": "company address",
			"client_tracking_id": "lead tracking client_id",
			"traffic_source": "Google",
			"traffic_medium": "cpc",
			"traffic_campaign": "easter-50-off",
			"traffic_value": "easter eggs",
			"tags": ["mql", "2019"],
			"available_for_mailing": true,
			"legal_bases": [
			  {
				"category": "communications",
				"type": "consent",
				"status": "granted"
			  }
			]
		  }
		}
		:param kwargs: Other's params
		:return: JsonResponse
			Success | Code: 200
		{
		  "event_uuid": "5408c5a3-4711-4f2e-8d0b-13407a3e30f3"
		}
		"""
		payload = {
			"conversion_identifier": conversion_identifier
		}
		payload.updade(kwargs)

		data = {
			"event_type": event_type
			"event_family": event_family
			"payload": payload
		}
		return self._post(self, data, **kwargs)

	def _post(self, data, **kwargs):
		return self.send_response("POST", data=data, **kwargs)


class RDMarkOpportunityEvent(RDEventResource):
	"""
	The Mark Opportunity event records contacts marked as an
	opportunity in RD Station Marketing.
	"""
	path = "/".join((RDEventResource.path, "events"))

	def __call__(self, event_type, event_family, funnel_name, email, **kwargs):
		"""
		:param event_type:  The event type that diferentiates the event. For the opportunity
		 		event it should be sent as "OPPORTUNITY".
		:param event_family: The family of the event for processing purposes.
		 		It currently accepts only "CDP" as valid option.
		:param funnel_name: Name of the funnel to which the Contact should be marked as opportunity.
		:param email: Email of the contact.
		:param kwargs: Other's params

		Request body example
		{
		  "event_type": "OPPORTUNITY",
		  "event_family":"CDP",
		  "payload": {
			"email": "email@email.com",
			"funnel_name": "default"
		  }
		}

		* Obs: This event does not create a new contact and requires
		an existing contact to be processed.

		:return: JsonResponse
			Success | Code: 200
		{
		  "event_uuid": "5408c5a3-4711-4f2e-8d0b-13407a3e30f3"
		}
		"""
		data = {
			"event_type": event_type
			"event_family": event_family
			"payload": {
				"email": email,
				"funnel_name": funnel_name
			}
		}
		return self._post(self, data, **kwargs)

	def _post(self, data, **kwargs):
		return self.send_response("POST", data=data, **kwargs)


class RDMarkOpportunityWonEvent(RDEventResource):
	"""
	The Mark Opportunity Won event records a contact
	as an opportunity won in RD Station Marketing.
	"""
	path = "/".join((RDEventResource.path, "events"))

	def __call__(self, event_type, event_family, funnel_name, email, value, **kwargs):
		"""
		:param event_type:  The event type that diferentiates the event. For the opportunity
		 		event it should be sent as "OPPORTUNITY".
		:param event_family: The family of the event for processing purposes.
		 		It currently accepts only "CDP" as valid option.
		:param funnel_name: Name of the funnel to which the Contact should be marked as opportunity.
		:param email: Email of the contact.
		:param value: Value of the won opportunity..
		:param kwargs: Other's params

		Request body example
		{
		  "event_type": "SALE",
		  "event_family":"CDP",
		  "payload": {
			"email": "email@email.com",
			"funnel_name": "default",
			"value": 200.0
		  }
		}

		* Obs: This event does not create a new contact
		and requires an existing contact to be processed.

		:return: JsonResponse
			Success | Code: 200
		{
		  "event_uuid": "5408c5a3-4711-4f2e-8d0b-13407a3e30f3"
		}
		"""
		data = {
			"event_type": event_type
			"event_family": event_family
			"payload": {
				"email": email,
				"funnel_name": funnel_name,
				"value": value
			}
		}
		return self._post(self, data, **kwargs)

	def _post(self, data, **kwargs):
		return self.send_response("POST", data=data, **kwargs)


class RDMarkOpportunityLostEvent(RDEventResource):
	"""
	The Mark Opportunity Lost event records a contact
	as an opportunity lost in RD Station Marketing.
	"""
	path = "/".join((RDEventResource.path, "events"))

	def __call__(self, event_type, event_family, funnel_name, email, reason, **kwargs):
		"""
		:param event_type:  The event type that diferentiates the event. For the opportunity
		 		event it should be sent as "OPPORTUNITY".
		:param event_family: The family of the event for processing purposes.
		 		It currently accepts only "CDP" as valid option.
		:param funnel_name: Name of the funnel to which the Contact should be marked as opportunity.
		:param email: Email of the contact.
		:param reason: Reason for why the Contact was marked as lost.
		:param kwargs: Other's params

		Request body example
		{
		  "event_type": "OPPORTUNITY_LOST",
		  "event_family":"CDP",
		  "payload": {
			"email": "email@email.com",
			"funnel_name": "default",
			"reason":"Lost reason"
		  }
		}

		* Obs: This event does not create a new contact
		and requires an existing contact to be processed.

		:return: JsonResponse
			Success | Code: 200
		{
		  "event_uuid": "5408c5a3-4711-4f2e-8d0b-13407a3e30f3"
		}
		"""
		data = {
			"event_type": event_type
			"event_family": event_family
			"payload": {
				"email": email,
				"funnel_name": funnel_name,
				"reason": reason
			}
		}
		return self._post(self, data, **kwargs)

	def _post(self, data, **kwargs):
		return self.send_response("POST", data=data, **kwargs)


class RDPlacedOrderEvent(RDEventResource):
	"""
	RD Station Marketing always considers the value of the event_type ORDER_PLACED
	attribute as the identifier of this custom event. This event is recorded whenever
	an order is placed on an e-commerce platform.
	"""
	path = "/".join((RDEventResource.path, "events"))

	def __call__(self, event_type, event_family, email, order, **kwargs):
		"""
		:param event_type:  The event type that diferentiates the event. For the opportunity
		 		event it should be sent as "OPPORTUNITY".
		:param event_family: The family of the event for processing purposes.
		 		It currently accepts only "CDP" as valid option.
		:param funnel_name: Name of the funnel to which the Contact should be marked as opportunity.
		:param email: Email of the contact.
		:param order: order event.
		:param kwargs: Other's params

		Request body example
		{
		  "event_type": "ORDER_PLACED",
		  "event_family":"CDP",
		  "payload": {
			"name": "Contact's Name",
			"email": "email@email.com",
			"cf_order_id": "order identifier",
			"cf_order_total_items": 2,
			"cf_order_status": "pending_payment",
			"cf_order_payment_method": "Credit Card",
			"cf_order_payment_amount": 40.20,
			"legal_bases": [
			  {
				"category": "communications",
				"type":"consent",
				"status":"granted"
			  }
			]
		  }
		}

		* Obs: This event does not create a new contact
		and requires an existing contact to be processed.

		:return: JsonResponse
			Success | Code: 200
		{
		  "event_uuid": "5408c5a3-4711-4f2e-8d0b-13407a3e30f3"
		}
		"""
		payload = {
			"email": email,
		}
		payload.update(order)

		data = {
			"event_type": event_type
			"event_family": event_family
			"payload": payload
		}
		return self._post(self, data, **kwargs)

	def _post(self, data, **kwargs):
		return self.send_response("POST", data=data, **kwargs)


class RDPlacedOrderEventWithItem(RDEventResource):
	"""
	RD Station Marketing always considers the value of the event_type ORDER_PLACED
	attribute as the identifier of this custom event. This event is recorded whenever
	an order is placed on an e-commerce platform.
	"""
	path = "/".join((RDEventResource.path, "events"))

	def __call__(self, event_type, event_family, email, order, **kwargs):
		"""
		:param event_type:  The event type that diferentiates the event. For the opportunity
		 		event it should be sent as "OPPORTUNITY".
		:param event_family: The family of the event for processing purposes.
		 		It currently accepts only "CDP" as valid option.
		:param funnel_name: Name of the funnel to which the Contact should be marked as opportunity.
		:param email: Email of the contact.
		:param order: order event.
		:param kwargs: Other's params

		Request body example
		{
		  "event_type": "ORDER_PLACED_ITEM",
		  "event_family":"CDP",
		  "payload": {
			"name": "Contact's Name",
			"email": "email@email.com",
			"cf_order_id": "Order Identifier",
			"cf_order_product_id": "Product 1",
			"cf_order_product_sku": "SKU 1",
			"legal_bases": [
			  {
				"category": "communications",
				"type": "consent",
				"status": "granted"
			  }
			]
		  }
		}

		* Obs: This event does not create a new contact
		and requires an existing contact to be processed.

		:return: JsonResponse
			Success | Code: 200
		{
		  "event_uuid": "5408c5a3-4711-4f2e-8d0b-13407a3e30f3"
		}
		"""
		payload = {
			"email": email,
		}
		payload.update(order)

		data = {
			"event_type": event_type
			"event_family": event_family
			"payload": payload
		}
		return self._post(self, data, **kwargs)

	def _post(self, data, **kwargs):
		return self.send_response("POST", data=data, **kwargs)


class RDAbandonedCartEvent(RDEventResource):
	"""
	RD Station Marketing always considers the value of the event_type CART_ABANDONED
	attribute as the identifier of the custom event. This event is recorded whenever a
	cart is abandoned on an e-commerce platform.
	"""
	path = "/".join((RDEventResource.path, "events"))

	def __call__(self, event_type, event_family, email, order, **kwargs):
		"""
		:param event_type:  The event type that diferentiates the event. For the opportunity
		 		event it should be sent as "OPPORTUNITY".
		:param event_family: The family of the event for processing purposes.
		 		It currently accepts only "CDP" as valid option.
		:param funnel_name: Name of the funnel to which the Contact should be marked as opportunity.
		:param email: Email of the contact.
		:param order: order event.
		:param kwargs: Other's params

		Request body example
		{
		  "event_type": "ORDER_PLACED_ITEM",
		  "event_family":"CDP",
		  "payload": {
			"name": "Contact's Name",
			"email": "email@email.com",
			"cf_order_id": "Order Identifier",
			"cf_order_product_id": "Product 1",
			"cf_order_product_sku": "SKU 1",
			"legal_bases": [
			  {
				"category": "communications",
				"type": "consent",
				"status": "granted"
			  }
			]
		  }
		}

		* Obs: This event does not create a new contact
		and requires an existing contact to be processed.

		:return: JsonResponse
			Success | Code: 200
		{
		  "event_uuid": "5408c5a3-4711-4f2e-8d0b-13407a3e30f3"
		}
		"""
		payload = {
			"email": email,
		}
		payload.update(order)

		data = {
			"event_type": event_type
			"event_family": event_family
			"payload": payload
		}
		return self._post(self, data, **kwargs)

	def _post(self, data, **kwargs):
		return self.send_response("POST", data=data, **kwargs)

# end-of-file