

RDSTATION = {
    # https://developers.rdstation.com/en/request-limit
	
	"endpoints": {
		"base_domain": "https://api.rd.services",
		"socket": "wss://api.rd.services/echo/websocket"
	},
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
    },
	"default_headers":{
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
		'Content-Type': 'application/json'
	}
}

# end-of-file