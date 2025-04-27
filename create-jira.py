from flask import Flask, request, jsonify
import requests
import os
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route("/createJIRA", methods=['POST'])
def createJIRA():
    data = request.get_json()
    body = data.get("body", "")

    if body != "/jira":
        return "", 204

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

    response = requests.post(
        url,
        headers=headers,
        auth=auth,
        data=payload
    )

    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
