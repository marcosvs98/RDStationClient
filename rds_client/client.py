# https://developers.rdstation.com/en/overview

# EXCEPTIONS

class RDStationException(Exception):
    """
    ref: https://developers.rdstation.com/en/error-states
    """
    pass

class RDUserIsNotExists(RDStationException):
	def __init__(self, msg):
		super(RDUserIsNotExists, self).__init__(msg)


class RDUnauthorizedRequest(RDStationException):
    """
    If the token or credentials are invalid, or code is expired
    or the user is not authorized. Status 401 Unauthorized.
    """
    def __init__(self, msg):
        super(RDUnauthorizedRequest, self).__init__(msg)


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
    """
    If the resource does not exist in RD Station Status 404 not found.
    """
    def __init__(self, msg):
        super(RDResourceNotFound, self).__init__(msg, status=404)


class RDUnsupportedMediaType(RDStationException):
    """
    If the Content-Type is not set properly Status 415 Unsupported Media Type.
    """
    def __init__(self, msg):
        super(RDUnsupportedMediaType, self).__init__(msg, status=415)


class RDMalformedBodyRequest(RDStationException):
    """
    If the body request is malformed accordingly to the Content-Type 
    header Status 400 Bad Request.
    """
    def __init__(self, msg):
        super(RDMalformedBodyRequest, self).__init__(msg, status=400)


class RDInvalidFormat(RDStationException):
    """
    If an invalid format for an attribute is sent Status 400 Bad Request.
    """
    def __init__(self, msg):
        super(RDMalformedBodyRequest, self).__init__(msg, status=400)

    
class RDUpperCaseTagsException(RDStationException):
    """
    If the tags contain uppercase characters:
    """
    def __init__(self, msg):
        super(RDUpperCaseTagsException, self).__init__(msg, status=400)


class RDInvalidDataType(RDStationException):
    """
    If an invalid data type is sent Status 422 Unprocessable Entity.
    """
    def __init__(self, msg):
        super(RDInvalidDataType, self).__init__(msg, status=422)


class RDReadOnlyFieldsException(RDStationException):
    """
    When trying to update a read only attribute Status 400 Bad Request.
    """
    def __init__(self, msg):
        super(RDReadOnlyFieldsException, self).__init__(msg, status=400)


class RDInexistentFields(RDStationException):
    """
    When trying to update an attribute that does not exist Status 400 Bad Request.
    """
    def __init__(self, msg):
        super(RDInexistentFields, self).__init__(msg, status=400)


class RDConflictingField(RDStationException):
    """
    When using the UPSERT like PATCH endpoint, and a field that was 
    used  to identify the lead appears again in the request payload 
    Status 400 Bad Request.
    """
    def __init__(self, msg):
        super(RDInexistentFields, self).__init__(msg, status=400)


class RDEmailAlreadyInUse(RDStationException):
    """
    When using the PATCH by uuid Contact endpoint and an e-mail 
    that already is used Status 400 Bad Request.
    """
    def __init__(self, msg):
        super(RDEmailAlreadyInUse, self).__init__(msg, status=400)


# SETTINGS

RDSTATION_REQUEST_LIMIT = {
    # https://developers.rdstation.com/en/request-limit

    "contacts": {
        "max_requests": 24,
        "period": 24,
        "supported_methods": (
            "POST", "GET", "HEAD", "PUT", "DELETE"
        )
    },
    "events": {
        "lead":{
            "max_requests": 24,
            "period": 24,
            "supported_methods": (
                "POST", "GET", "HEAD", "PUT", "DELETE"
            )
        },
        "account": {
            "max_requests": 24,
            "period": 24,
            "supported_methods": (
                "POST", "GET", "HEAD", "PUT", "DELETE"
            )
        }
    }
}

# STRUCTS 

@dataclasses
class RDStationClient:
    client_id      : str
    access_token   : str
    client_secret  : str
    code           : str
    redirect_url   : str
    refresh_token  : str


# RESOURCES

# https://developers.rdstation.com/en/data-enrichment

from abc import ABC, abstractclassmethod


class RDStationResource(ABC):
    """
    Representam os recursos disponivéis na api
    """
    @abstractclassmethod
    def __call__(self):
        pass


class RDAuth(RDStationResource):
    def __call__(self):
        pass
        
class RDAPIKey(RDStationResource):
    """
    The use of API Key makes it possible to send conversion 
    events to RD Station Marketing. API key is a token that must 
    be sent via Query String using the api_key parameter
    """
    def __call__(self):
        pass


class RDLead(RDStationResource):
    def __call__(self):
        pass
    

class RDWebhook(RDStationResource):
    def __call__(self):
        pass


class RDContacts(RDStationResource):
    """
    Returns data about a specific Contact
    
    ref: https://developers.rdstation.com/en/reference/contacts
    """
    def __call__(self):
        pass


class RDMarketing(RDStationResource):
    def __call__(self):
        pass


class RDURLCallback(RDStationResource):
    def __call__(self):
        pass


class RDRevokingAcessToken(RDStationResource):
    """
    Client access with OAuth authentication type can be revoked whenever needed.
    This can be done using access_token or refresh_token.
    """
    def __call__(self):
        pass


class RDRefreshExpiredToken(RDStationResource):
    """
    Every access_token is temporary, and its expiration 
    time is defined by the expires_in attribute in seconds,
    which is 86400 seconds (24 hours).
    """
    def __call__(self):
        pass
        

class RDGettingAcessToken(RDStationResource):
    """
    Once you have the code parameter, you just need the 
    access_token. To do this, simply make a request to 
    obtain the.
    """
    def __call__(self):
        pass


class RDConversionEvent(RDStationResource):
    """
    RD Station Marketing considers the value of the 
    conversion_identifier attribute as the conversion identifier.
    This event is recorded whenever a conversion occurs.
    """
    def __call__(self):

        event = {
            "event_type": "CONVERSION",
            "event_family":"CDP",
            "payload": {
                "conversion_identifier": "Name of the conversion event",
                "name": "name of the contact",
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
                "company_name": "company name",
                "company_site": "company website",
                "company_address": "company address",
                "client_tracking_id": "lead tracking client_id",
                "traffic_source": "Google",
                "traffic_medium": "cpc",
                "traffic_campaign": "easter-50-off",
                "traffic_value": "easter eggs",
                "tags": ["mql", "2019"],
                "available_for_mailing": True,
                "legal_bases": [
                        {
                            "category": "communications",
                            "type": "consent",
                            "status": "granted"
                        }
                ],
                "cf_my_custom_field": "custom field value"
            }
        }
        pass

# API CLIENT


class RDStationRestClient():
    """    
    ref: https://developers.rdstation.com/en/overview

    """
    def __init__(self, *args, **kwargs):
        self.client = RDStationClient(**kwargs)
        
    def connect(self):
        pass

    def login(self):
        pass

    def get_lead(self):
        pass

    def update_lead(self):
        pass

    def create_app(self):
        pass

    def get_access_token(self):
        pass

    def refresh_token(self):
        pass

    def redirct_uri(self):
        pass

    def revoke_access_token(self):
        pass

    def conversion_identifier(self):
        pass

    def get_contact(self):
        pass

    def send_request(self):
        # get - post - put- delete
        pass

    #https://developers.rdstation.com/en/reference/account_infos

    def get_account_information(self):
        pass

    def get_tracking_code(self):
        pass

    # https://developers.rdstation.com/en/reference/contacts

    def get_by_uiid(self):
        pass

    def get_by_email(self):
        pass

    # https://developers.rdstation.com/en/reference/contacts/funnels

    def get_by_contact_uuid(self):
        pass

    def get_by_contact_email(self):
        pass

    # https://developers.rdstation.com/en/reference/fields

    def fields(self):
        pass

    # https://developers.rdstation.com/en/reference/webhooks

    def webhooks(self):
        pass

    # https://developers.rdstation.com/en/reference/events
    def get_events(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self):
        pass

    def __delete__(self):
        pass
    

# end-of-file

rdclient = RDStationRestClient(
    client_id="adadada", 
    access_token=""
)

rdclient.connect()

rdclient.get_account_information()

rdclient.get_by_contact_email("xpto@protonmail.com")
