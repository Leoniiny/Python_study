import requests

url = "https://api-c.soboten.com/text/chat-set/rest/selectConfigInfo/4"
params = {
  "channelType": 1,
  "current": 1,
  "pageSize": 100,
  "pageNo": 1
}
headers = {
  'bno': '5105b359aa37444284f5b0660a6fed24',
  'temp-id': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55SWQiOiI1MTA1YjM1OWFhMzc0NDQyODRmNWIwNjYwYTZmZWQyNCIsImFnZW50SWQiOiI1YTRkMjA2NTkzNjY0Y2Y2ODUwMjdkZGQzMTkzZWY1NiIsInNlcnZpY2VFbWFpbCI6InpoaWNoaTIwQDE2My5jb20iLCJ6b25lIjoxLCJpc3MiOiJ6aGljaGkyMEAxNjMuY29tIiwiZXhwIjoxNzAzMDQxOTEyLCJ0eXBlIjoiY29uc29sZSJ9.sbpT7yToXcqsxmZLiSy8_hZY-1hrATebj0-nt5IyH4M'
}
response = requests.request("GET", url, headers=headers,params=params)
print(response.text)
