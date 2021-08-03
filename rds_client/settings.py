

RDSTATION = {
	# https://developers.rdstation.com/en/reference/webhooks#webhooks-retries
	"endpoints": {
		"base_domain": "https://api.rd.services",
		"max_retries": 5,
		"time_sleep": 10
	},
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
    },
	"default_headers":{
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
		'Content-Type': 'application/json'
	}
}

# end-of-file