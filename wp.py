import requests
import json

url = "https://api.ultramsg.com/instance../messages/document"

payload = {
    "token": "ultramsg token",
    "to": "enter number(target number)",
    "document": "your host(ex:https://08f8-185-177-126-102.ngrok-free.app/up/test.apk.)",
    "filename": "Test.PDF",
    "content_type": "application/vnd.android.package-archive",
    "priority": "10",
    "referenceId": "",
    "msgId": "",
    "mentions": ""
}

headers = {'Content-Type': 'application/json'}

response = requests.request("POST", url, data=json.dumps(payload), headers=headers)


print(response.text)
