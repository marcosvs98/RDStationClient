from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class RDRequestBody(ABC):
	"""
	Classe responsável por representar um  objeto
	de entidade, podendo ter diversas referências.
	"""
	def update(cls, dic):
		for k, v in dic.items():
			setattr(cls, k, v)

	def get(self, key, NaN=None):
		return self.__dict__.get(key, NaN)

	def __str__(self):
		res = {k: v for k, v in self.__dict__.items()}
		return str(res)

	def __repr__(self):
		return self.__str__()

	def __getitem__(cls, x):
		return getattr(cls, x)

	def __setitem__(cls, key, value):
		return setattr(cls, key, value)

	def __enter__(cls):
		return cls

	def __exit__(cls, typ, value, tb):
		pass

	def __del__(self):
		pass

	def __len__(self):
		return len(self.__dict__)


@dataclass
class RDConversionEvent(RDBodyEvent):
	event_type: str  # req
	event_family 	: str  # req
	conversion_identifier 	: str  # req
	name 	                : str
	email 	                : str  # req
	job_title 	            : str
	state 	                : str
	city 	                : str
	country 	            : str
	personal_phone 	        : str
	mobile_phone 	        : str
	twitter 	            : str
	facebook 	            : str
	linkedin 	            : str
	website 	            : str
	cf_custom_field_api_identifier 	: str
	company_name 	        : str
	company_site 	        : str
	company_address 	    : str
	client_tracking_id 	    : str
	traffic_source 	        : str
	traffic_medium 	        : str
	traffic_campaign 	    : str
	traffic_value 	        : str
	tags 	                : list
	available_for_mailing 	: bool
	legal_bases 	        : list



@dataclass
class RDMarkOpportunityEvent(RDBodyEvent):
	event_type      : str  # req: true
	event_family 	: str  # req: true
	funnel_name 	: str  # req: true
	email 	        : str  # req: true
	value 	        : float  # req: false


@dataclass
class RDMarkOpportunityLostEvent(RDBodyEvent):
	event_type    : str  # req: true
	event_family  : str  # req: true
	email 	      : str  # req: true
	funnel_name   : str  # req: true
	reason 	      : str  # req: false


@dataclass
class RDPlacedOrderEvent(RDBodyEvent):
	event_tye : str  # req: true
	event_family 	: str  # req: true
	name 	: str  # req: false
	email 	: str  # req: true
	cf_order_id 	: str  # req: true
	cf_order_total_items 	: int  # req: true
	cf_order_status 	: str  # req: true
	cf_order_payment_method 	: str  # req: true
	cf_order_payment_amount 	: float  # req: true
	legal_bases 	: list  # req: false


@dataclass
class RDPlacedOrderEventWithItem(RDBodyEvent):
	event_tye : str  # req: true
	event_family 	: str  # req: true
	name 	: str  # req: false
	email 	: str  # req: true
	cf_order_id 	: str  # req: true
	cf_order_product_id 	: str  # req: true
	cf_order_product_sku 	: str  # req: true
	legal_bases 	: list  # req: false



@dataclass
class RDAbandonedCartEvent(RDBodyEvent):
	event_tye : str  # req: true
	event_family 	: str  # req: true
	name 	: str  # req: false
	email 	: str  # req: true
	cf_cart_id 	: str  # req: true
	cf_cart_total_items 	: int  # req: true
	cf_cart_status 	: str  # req: true
	legal_bases 	: list  # req: false


@dataclass
class RDAbandonedCartEventWithItem(RDBodyEvent):
	event_tye : str  # req: true
	event_family 	: str  # req: true
	name 	: str  # req: false
	email 	: str  # req: true
	cf_cart_id 	: str  # req: true
	cf_cart_total_items 	: int  # req: true
	cf_cart_status 	: str  # req: true
	legal_bases 	: list  # req: false


@dataclass
class RDChatStartedEvent(RDBodyEvent):
	event_tye : str  # req: true
	event_family 	: str  # req: true
	chat_subject 	: str  # req: true
	cf_chat_status 	: str  # req: true
	cf_chat_type 	: str  # req: false
	cf_birthdate 	: str  # req: false
	cf_gender 	: str  # req: false
	name 	: str  # req: false
	email 	: str  # req: true
	job_title 	: str  # req: false
	personal_phone 	: str  # req: false
	mobile_phone 	: str  # req: false
	twitter 	: str  # req: false
	facebook 	: str  # req: false
	linkedin 	: str  # req: false
	website 	: str  # req: false
	company_name 	: str  # req: false
	company_site 	: str  # req: false
	legal_bases 	: list  # req: false


@dataclass
class RDChatFinishedEvent(RDBodyEvent):
	event_tye : str  # req: true
	event_family 	: str  # req: true
	chat_subject 	: str  # req: true
	cf_chat_status 	: str  # req: true
	cf_chat_transcript_message 	: str  # req: true
	cf_chat_type 	: str  # req: false
	cf_birthdate 	: str  # req: false
	cf_gender 	: str  # req: false
	name 	: str  # req: false
	email 	: str  # req: true
	job_title 	: str  # req: false
	personal_phone 	: str  # req: false
	mobile_phone 	: str  # req: false
	twitter 	: str  # req: false
	facebook 	: str  # req: false
	linkedin 	: str  # req: false
	website 	: str  # req: false
	company_name 	: str  # req: false
	company_site 	: str  # req: false
	legal_bases 	: list  # req: false


@dataclass
class RDCallFinishedEvent(RDBodyEvent):
	"""  """
	event_tye : str  # req: true
	event_family 	: str  # req: true
	name 	: str  # req: false
	email 	: str  # req: true
	company_name 	: str  # req: false
	company_site 	: str  # req: false
	job_title 	: str  # req: false
	personal_phone 	: str  # req: false
	call_user_email 	: str  # req: false
	call_from_number 	: str  # req: true
	call_started_at 	: int  # req: false
	call_duration 	: str  # req: false
	call_type 	: str  # req: false
	call_status 	: str  # req: true
	call_status_description 	: str  # req: false
	call_phone_type 	: str  # req: false
	call_carrier 	: str  # req: false
	call_record 	: str  # req: false
	legal_bases 	: list  # req: false


@dataclass
class RDMediaEvents(RDBodyEvent):
	"""
	RD Station Marketing always considers the value of the event_type
	MEDIA_PLAYBACK_STARTED attribute as the identifier of the custom event.
	This event is recorded whenever a media playback is initiated.
	"""
	event_tye : str  # req: true
	event_family 	: str  # req: true
	email 	: str  # req: true
	name 	: str  # req: false
	company_name 	: str  # req: false
	company_site 	: str  # req: false
	job_title 	: str  # req: false
	personal_phone 	: str  # req: false
	mobile_phone 	: str  # req: false
	twitter 	: str  # req: false
	facebook 	: str  # req: false
	linkedin 	: str  # req: false
	website 	: str  # req: false
	media_type 	: str  # req: true
	media_metadata 	: str  # req: false
	media_recorded_content 	: bool  # req: false
	media_identifier 	: str  # req: true
	media_category 	: str  # req: false
	media_duration 	: int  # req: false
	media_published_date_timestamp 	: int  # req: false
	legal_bases 	: list  # req: false


@dataclass
class RDMediaPlaybackStoppedEvent(RDBodyEvent):
	"""
	RD Station Marketing always considers the value of the event_type
	MEDIA_PLAYBACK_STOPPED attribute as the identifier of the custom
	event. This event is recorded whenever a media playback ends.
	"""
	event_tye : str  # req: true
	event_family 	: str  # req: true
	email 	: str  # req: true
	name 	: str  # req: false
	company_name 	: str  # req: false
	company_site 	: str  # req: false
	job_title 	: str  # req: false
	personal_phone 	: str  # req: false
	mobile_phone 	: str  # req: false
	twitter 	: str  # req: false
	facebook 	: str  # req: false
	linkedin 	: str  # req: false
	website 	: str  # req: false
	media_type 	: str  # req: true
	media_metadata 	: str  # req: false
	media_recorded_content 	: bool  # req: false
	media_identifier 	: str  # req: true
	media_category 	: str  # req: false
	media_duration 	: int  # req: false
	media_published_date_timestamp 	: int  # req: false
	media_finished 	: bool  # req: false
	media_user_interaction_duration 	: int  # req: false
	media_user_interaction_percentage 	: int  # req: false
	media_user_interaction_date_timestamp 	: str  # req: false
	legal_bases 	: list  # req: false


@dataclass
class RDEventsBatch(RDBodyEvent):
	""" The events batch endpoint allows RD Station to receive more than
	one event at once. Thus allowing events of order placed and order placed
	items to be sent without the need of multiple requests. """

	event_tye : str  # req: true
	event_family 	: str  # req: true
	payload 	: object  # req: true


# end-of-file