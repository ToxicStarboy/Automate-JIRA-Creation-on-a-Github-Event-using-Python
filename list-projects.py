import requests
import os
from requests.auth import HTTPBasicAuth
import json

url = "https://aadeshdinkargupta2003.atlassian.net/rest/api/3/project/search"

API_TOKEN = os.getenv("JIRA_API_TOKEN")

auth = HTTPBasicAuth("aadeshdinkargupta.com", API_TOKEN)

headers = {
    "Accept": "application/json"
}

response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
