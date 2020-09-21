import json

json_settings = json.dumps([

		{
			"type":"string",
			"title": "Name",
		    "desc": "Your name as it appears on the google sheet",
		    "section": "general",
		    "key": "name"
		},
		{
			"type": "string",
	        "title": "Google Sheet Url",
	        "desc": "Url of the google sheet",
	        "section": "general",
	        "key": "url" 
		},
		{
			"type": "string",
	        "title": "Worksheet",
	        "desc": "worksheet name eg. Week 1",
	        "section": "general",
	        "key": "worksheet" 
		}
])