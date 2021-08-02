""" The event's endpoint is responsible for receiving different event types
in which RD Station Contacts take part in. It is possible to send default events
to RD Station such as conversion events, opportunity marking events and won
and lost events. Also, RD Station supports the possibility of receiving different
event types, for instance, chat events, e-commerce ones and others.

ref: https://developers.rdstation.com/en/reference/events
"""
# pylint: disable=unused-import
# pylint: disable=R0902

from abc import ABC
from dataclasses import dataclass, field


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

	event_type: str
	event_family: str
	conversion_identifier: str
	name: str = field(default=None)
	email: str  # req
	job_title: str = field(default=None)
	state: str = field(default=None)
	city: str = field(default=None)
	country: str = field(default=None)
	personal_phone: str = field(default=None)
	mobile_phone: str = field(default=None)
	twitter: str = field(default=None)
	facebook: str = field(default=None)
	linkedin: str = field(default=None)
	website: str = field(default=None)
	cf_custom_field_api_identifier: str = field(default=None)
	company_name: str = field(default=None)
	company_site: str = field(default=None)
	company_address: str = field(default=None)
	client_tracking_id: str = field(default=None)
	traffic_source: str = field(default=None)
	traffic_medium: str = field(default=None)
	traffic_campaign: str = field(default=None)
	traffic_value: str = field(default=None)
	tags: list = field(default=[])
	available_for_mailing: bool = field(default=False)
	legal_bases: list = field(default=[])



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
	value: float = field(default=None)


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
	reason: str = field(default=None)


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
	name: str = field(default=None)
	email: str  # req: true
	cf_order_id: str  # req: true
	cf_order_total_items: int  # req: true
	cf_order_status: str  # req: true
	cf_order_payment_method: str  # req: true
	cf_order_payment_amount: float  # req: true
	legal_bases: list = field(default=[])


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
	name: str = field(default=None)
	email: str  # req: true
	cf_order_id: str  # req: true
	cf_order_product_id: str  # req: true
	cf_order_product_sku: str  # req: true
	legal_bases: list = field(default=[])


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
	name: str = field(default=None)
	email: str  # req: true
	cf_cart_id: str  # req: true
	cf_cart_total_items: int  # req: true
	cf_cart_status: str  # req: true
	legal_bases: list = field(default=[])


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
	name: str = field(default=None)
	email: str  # req: true
	cf_cart_id: str  # req: true
	cf_cart_total_items: int  # req: true
	cf_cart_status: str  # req: true
	legal_bases: list = field(default=[])


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
	cf_chat_type: str = field(default=None)
	cf_birthdate: str = field(default=None)
	cf_gender: str = field(default=None)
	name: str = field(default=None)
	email: str  # req: true
	job_title: str = field(default=None)
	personal_phone: str = field(default=None)
	mobile_phone: str = field(default=None)
	twitter: str = field(default=None)
	facebook: str = field(default=None)
	linkedin: str = field(default=None)
	website: str = field(default=None)
	company_name: str = field(default=None)
	company_site: str = field(default=None)
	legal_bases: list = field(default=[])


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
	cf_chat_type: str = field(default=None)
	cf_birthdate: str = field(default=None)
	cf_gender: str = field(default=None)
	name: str = field(default=None)
	email: str  # req: true
	job_title: str = field(default=None)
	personal_phone: str = field(default=None)
	mobile_phone: str = field(default=None)
	twitter: str = field(default=None)
	facebook: str = field(default=None)
	linkedin: str = field(default=None)
	website: str = field(default=None)
	company_name: str = field(default=None)
	company_site: str = field(default=None)
	legal_bases: list = field(default=[])


@dataclass
class RDCallFinishedEvent(RDRequestBody):
	""" RD Station Marketing considers the value of the event_type
	CALL_FINISHED attribute as the identifier of the custom event.
	This event is recorded whenever a call is ended. """

	def __init__(self):
		super(RDCallFinishedEvent).__init__()

	event_tye: str  # req: true
	event_family: str  # req: true
	name: str = field(default=None)
	email: str  # req: true
	company_name: str = field(default=None)
	company_site: str = field(default=None)
	job_title: str = field(default=None)
	personal_phone: str = field(default=None)
	call_user_email: str = field(default=None)
	call_from_number: str  # req: true
	call_started_at: int = field(default=0)
	call_duration: str = field(default=None)
	call_type: str = field(default=None)
	call_status: str  # req: true
	call_status_description: str = field(default=None)
	call_phone_type: str = field(default=None)
	call_carrier: str = field(default=None)
	call_record: str = field(default=None)
	legal_bases: list = field(default=[])


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
	name: str = field(default=None)
	company_name: str = field(default=None)
	company_site: str = field(default=None)
	job_title: str = field(default=None)
	personal_phone: str = field(default=None)
	mobile_phone: str = field(default=None)
	twitter: str = field(default=None)
	facebook: str = field(default=None)
	linkedin: str = field(default=None)
	website: str = field(default=None)
	media_type: str  # req: true
	media_metadata: str = field(default=None)
	media_recorded_content: bool = field(default=False)
	media_identifier: str  # req: true
	media_category: str = field(default=None)
	media_duration: int = field(default=0)
	media_published_date_timestamp: int = field(default=0)
	legal_bases: list = field(default=[])


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
	name: str = field(default=None)
	company_name: str = field(default=None)
	company_site: str = field(default=None)
	job_title: str = field(default=None)
	personal_phone: str = field(default=None)
	mobile_phone: str = field(default=None)
	twitter: str = field(default=None)
	facebook: str = field(default=None)
	linkedin: str = field(default=None)
	website: str = field(default=None)
	media_type: str  # req: true
	media_metadata: str = field(default=None)
	media_recorded_content: bool = field(default=False)
	media_identifier: str  # req: true
	media_category: str = field(default=None)
	media_duration: int = field(default=0)
	media_published_date_timestamp: int = field(default=0)
	media_finished: bool = field(default=False)
	media_user_interaction_duration: int = field(default=0)
	media_user_interaction_percentage: int = field(default=0)
	media_user_interaction_date_timestamp: str = field(default=None)
	legal_bases: list = field(default=[])


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
