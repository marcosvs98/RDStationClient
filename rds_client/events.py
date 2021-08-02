""" The event's endpoint is responsible for receiving different event types
in which RD Station Contacts take part in. It is possible to send default events
to RD Station such as conversion events, opportunity marking events and won
and lost events. Also, RD Station supports the possibility of receiving different
event types, for instance, chat events, e-commerce ones and others.

ref: https://developers.rdstation.com/en/reference/events
"""

from abc import ABC
from dataclasses import dataclass


# pylint: disable=R0902


@dataclass
class RDRequestBody(ABC):
	""" Classe responsável por representar um  objeto
	de entidade, podendo ter diversas referências. """

	def update(self, new_dict):
		""" update representation """
		# pylint: disable=E0213
		for key, value in new_dict.items():
			setattr(self, key, value)

	def get(self, key, value=None):
		""" get dict representation """
		# pylint: disable=E0213
		return self.__dict__.get(key, value)

	def __str__(self):
		# pylint: disable=E0213
		return str(self.__dict__)

	def __repr__(self):
		return self.__str__()

	def __getitem__(self, item):
		return getattr(self, item)

	def __setitem__(self, key, value):
		return setattr(self, key, value)

	def __len__(self):
		return len(self.__dict__)


@dataclass
class RDConversionEvent(RDRequestBody):
	""" RD Station Marketing considers the value of the conversion_identifier
	attribute as the identifier of the custom event. This event is recorded
	whenever a conversion occurs. """

	def __init__(self):
		super(RDConversionEvent).__init__()

	event_type: str  # req
	event_family: str  # req
	conversion_identifier: str  # req
	name: str
	email: str  # req
	job_title: str
	state: str
	city: str
	country: str
	personal_phone: str
	mobile_phone: str
	twitter: str
	facebook: str
	linkedin: str
	website: str
	cf_custom_field_api_identifier: str
	company_name: str
	company_site: str
	company_address: str
	client_tracking_id: str
	traffic_source: str
	traffic_medium: str
	traffic_campaign: str
	traffic_value: str
	tags: list
	available_for_mailing: bool
	legal_bases: list



@dataclass
class RDMarkOpportunityEvent(RDRequestBody):
	""" The Mark Opportunity event records contacts marked as
	 an opportunity in RD Station Marketing. """

	def __init__(self):
		super(RDMarkOpportunityEvent).__init__()

	event_type: str  # req: true
	event_family: str  # req: true
	funnel_name: str  # req: true
	email: str  # req: true
	value: float  # req: false


@dataclass
class RDMarkOpportunityLostEvent(RDRequestBody):
	""" The Mark Opportunity Lost event records a contact as an
	opportunity lost in RD Station Marketing. """

	def __init__(self):
		super(RDMarkOpportunityLostEvent).__init__()

	event_type: str  # req: true
	event_family: str  # req: true
	email: str  # req: true
	funnel_name: str  # req: true
	reason: str  # req: false


@dataclass
class RDPlacedOrderEvent(RDRequestBody):
	""" RD Station Marketing always considers the value of the
	event_type ORDER_PLACED attribute as the identifier of
	this custom event. This event is recorded whenever an order
	is placed on an e-commerce platform. """

	def __init__(self):
		super(RDPlacedOrderEvent).__init__()

	event_tye: str  # req: true
	event_family: str  # req: true
	name: str  # req: false
	email: str  # req: true
	cf_order_id: str  # req: true
	cf_order_total_items: int  # req: true
	cf_order_status: str  # req: true
	cf_order_payment_method: str  # req: true
	cf_order_payment_amount: float  # req: true
	legal_bases: list  # req: false


@dataclass
class RDPlacedOrderEventWithItem(RDRequestBody):
	""" RD Station Marketing always considers the value of the event_type
	ORDER_PLACED_ITEM attribute as the identifier of the custom event.
	This event is recorded whenever an order with a specific item is
	placed on an e-commerce platform. """

	def __init__(self):
		super(RDPlacedOrderEventWithItem).__init__()

	event_tye: str  # req: true
	event_family: str  # req: true
	name: str  # req: false
	email: str  # req: true
	cf_order_id: str  # req: true
	cf_order_product_id: str  # req: true
	cf_order_product_sku: str  # req: true
	legal_bases: list  # req: false


@dataclass
class RDAbandonedCartEvent(RDRequestBody):
	""" RD Station Marketing always considers the value of
	the event_type CART_ABANDONED attribute as the identifier of
	the custom event. This event is recorded whenever a
	cart is abandoned on an e-commerce platform. """

	def __init__(self):
		super(RDAbandonedCartEvent).__init__()

	event_tye: str  # req: true
	event_family: str  # req: true
	name: str  # req: false
	email: str  # req: true
	cf_cart_id: str  # req: true
	cf_cart_total_items: int  # req: true
	cf_cart_status: str  # req: true
	legal_bases: list  # req: false


@dataclass
class RDAbandonedCartEventWithItem(RDRequestBody):
	""" RD Station Marketing always considers the value of the event_type
	CART_ABANDONED_ITEM attribute as the identifier of the custom event.
	This event is recorded whenever a cart is abandoned with a specific
	item on an e-commerce platform. """

	def __init__(self):
		super(RDAbandonedCartEventWithItem).__init__()

	event_tye: str  # req: true
	event_family: str  # req: true
	name: str  # req: false
	email: str  # req: true
	cf_cart_id: str  # req: true
	cf_cart_total_items: int  # req: true
	cf_cart_status: str  # req: true
	legal_bases: list  # req: false


@dataclass
class RDChatStartedEvent(RDRequestBody):
	""" RD Station Marketing always considers the value of the
	event_type CHAT_STARTED attribute as the identifier of the
	custom event. This event is recorded whenever a chat is initiated. """

	def __init__(self):
		super(RDChatStartedEvent).__init__()

	event_tye: str  # req: true
	event_family: str  # req: true
	chat_subject: str  # req: true
	cf_chat_status: str  # req: true
	cf_chat_type: str  # req: false
	cf_birthdate: str  # req: false
	cf_gender: str  # req: false
	name: str  # req: false
	email: str  # req: true
	job_title: str  # req: false
	personal_phone: str  # req: false
	mobile_phone: str  # req: false
	twitter: str  # req: false
	facebook: str  # req: false
	linkedin: str  # req: false
	website: str  # req: false
	company_name: str  # req: false
	company_site: str  # req: false
	legal_bases: list  # req: false


@dataclass
class RDChatFinishedEvent(RDRequestBody):
	""" RD Station Marketing always considers the value of
	the event_type CHAT_FINISHED attribute as the identifier of
	the custom event. This event is recorded whenever a chat is ended. """

	def __init__(self):
		super(RDChatFinishedEvent).__init__()

	event_tye: str  # req: true
	event_family: str  # req: true
	chat_subject: str  # req: true
	cf_chat_status: str  # req: true
	cf_chat_transcript_message: str  # req: true
	cf_chat_type: str  # req: false
	cf_birthdate: str  # req: false
	cf_gender: str  # req: false
	name: str  # req: false
	email: str  # req: true
	job_title: str  # req: false
	personal_phone: str  # req: false
	mobile_phone: str  # req: false
	twitter: str  # req: false
	facebook: str  # req: false
	linkedin: str  # req: false
	website: str  # req: false
	company_name: str  # req: false
	company_site: str  # req: false
	legal_bases: list  # req: false


@dataclass
class RDCallFinishedEvent(RDRequestBody):
	""" RD Station Marketing considers the value of the event_type
	CALL_FINISHED attribute as the identifier of the custom event.
	This event is recorded whenever a call is ended. """

	def __init__(self):
		super(RDCallFinishedEvent).__init__()

	event_tye: str  # req: true
	event_family: str  # req: true
	name: str  # req: false
	email: str  # req: true
	company_name: str  # req: false
	company_site: str  # req: false
	job_title: str  # req: false
	personal_phone: str  # req: false
	call_user_email: str  # req: false
	call_from_number: str  # req: true
	call_started_at: int  # req: false
	call_duration: str  # req: false
	call_type: str  # req: false
	call_status: str  # req: true
	call_status_description: str  # req: false
	call_phone_type: str  # req: false
	call_carrier: str  # req: false
	call_record: str  # req: false
	legal_bases: list  # req: false


@dataclass
class RDMediaEvents(RDRequestBody):
	""" RD Station Marketing always considers the value of the event_type
	MEDIA_PLAYBACK_STARTED attribute as the identifier of the custom event.
	This event is recorded whenever a media playback is initiated. """

	def __init__(self):
		super(RDMediaEvents).__init__()

	event_tye: str  # req: true
	event_family: str  # req: true
	email: str  # req: true
	name: str  # req: false
	company_name: str  # req: false
	company_site: str  # req: false
	job_title: str  # req: false
	personal_phone: str  # req: false
	mobile_phone: str  # req: false
	twitter: str  # req: false
	facebook: str  # req: false
	linkedin: str  # req: false
	website: str  # req: false
	media_type: str  # req: true
	media_metadata: str  # req: false
	media_recorded_content: bool  # req: false
	media_identifier: str  # req: true
	media_category: str  # req: false
	media_duration: int  # req: false
	media_published_date_timestamp: int  # req: false
	legal_bases: list  # req: false


@dataclass
class RDMediaPlaybackStoppedEvent(RDRequestBody):
	""" RD Station Marketing always considers the value of the event_type
	MEDIA_PLAYBACK_STOPPED attribute as the identifier of the custom
	event. This event is recorded whenever a media playback ends. """

	def __init__(self):
		super(RDMediaPlaybackStoppedEvent).__init__()

	event_tye: str  # req: true
	event_family: str  # req: true
	email: str  # req: true
	name: str  # req: false
	company_name: str  # req: false
	company_site: str  # req: false
	job_title: str  # req: false
	personal_phone: str  # req: false
	mobile_phone: str  # req: false
	twitter: str  # req: false
	facebook: str  # req: false
	linkedin: str  # req: false
	website: str  # req: false
	media_type: str  # req: true
	media_metadata: str  # req: false
	media_recorded_content: bool  # req: false
	media_identifier: str  # req: true
	media_category: str  # req: false
	media_duration: int  # req: false
	media_published_date_timestamp: int  # req: false
	media_finished: bool  # req: false
	media_user_interaction_duration: int  # req: false
	media_user_interaction_percentage: int  # req: false
	media_user_interaction_date_timestamp: str  # req: false
	legal_bases: list  # req: false


@dataclass
class RDEventsBatch(RDRequestBody):
	""" The events batch endpoint allows RD Station to receive more than
	one event at once. Thus allowing events of order placed and order placed
	items to be sent without the need of multiple requests. """

	def __init__(self):
		super(RDEventsBatch).__init__()

	event_tye: str  # req: true
	event_family: str  # req: true
	payload: object  # req: true


# end-of-file
