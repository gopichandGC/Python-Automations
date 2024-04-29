# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os



url = "https://gopichand-vadlamudi.atlassian.net/rest/api/3/issue"
api_token=os.getenv("api_token")
auth = HTTPBasicAuth("vadlamudigchand@gmail.com",api_token)


headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}
payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "AUT"
    },
    "issuetype": {
      "id": "10008"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))