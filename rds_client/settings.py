

RDSTATION = {
	# https://developers.rdstation.com/en/reference/webhooks#webhooks-retries
	"endpoints": {
		"base_domain": "https://api.rd.services",
		"socket": "wss://api.rd.services/echo/websocket",
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
'''

curl -vvv 'https://app.rdstation.com.br/api/platform/auth'
	-H 'content-type: application/x-www-form-urlencoded'
	-H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
	-H 'cookie: __rdsid=22216e1d089dc6592b8273aed57a7bed'
	--data-raw 'authenticity_token=xYhMkncLacpoxN89JMaizY5tael2vrLau8DK%2F3mpUEzOYi28VN5DvVApNquL6wLeiiccGzjKQr%2BJDK78ckI88Q%3D%3D&client_id=cc3fbf81-3a32-4591-823e-8cf49d2116ab&redirect_uri=https%3A%2F%2Fgithub.com%2FMarcosVs98%2F&state=&account_id=359227'   \
	--compressed
'''