import requests,json
from urllib.parse import urlencode
import requests
import requests

url = "https://api-c-grey.sobot.com/text/chat-kwb/admin/add_blacklist.action"
data =urlencode( {
	"sender": "OumStS1Q9ewDRdx73IY3WutAI8u3dc8Df19PIuYDz4Siaut75ESvtauhPufTnD8g",
	"receiver": "b89d5565235fae5e64de03934fdc2509",
	"reason": "呵呵呵",
	"type": ""})


headers = {
  'bno': 'cfd4681074ce4bed904928fb609fc824',
  'content-type': 'application/x-www-form-urlencoded',
}
response = requests.request("POST", url, headers=headers, data=data)
print(response.text)

