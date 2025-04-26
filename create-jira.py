import requests
import os
from requests.auth import HTTPBasicAuth
import json

url = "https://aadeshdinkargupta2003.atlassian.net/rest/api/3/issue"

API_TOKEN = os.getenv("JIRA_API_TOKEN")

auth = HTTPBasicAuth("aadeshdinkargupta.com", API_TOKEN)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = json.dumps({
    "fields": {
        "project": {
            "key": "ADG"
        },
        "summary": "First JIRA ticket",
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "My first JIRA ticket"
                        }
                    ]
                }
            ]
        },
        "issuetype": {
            "id": "10009" 
        }
    }
})

response = requests.request(
    "POST",
    url,
    headers=headers,
    auth=auth,
    data=payload
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
