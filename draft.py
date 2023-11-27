import requests

url = "https://us.sobot.com/callservice/v6/cc-config/summary-classifies?planType=1"

payload = {}
headers = {
  'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHAiOiIiLCJybG0iOiJjb25zb2xlIiwibmJmIjowLCJpc3MiOiJzb2JvdCIsImV4cCI6MTcwMTEzOTUyOTc5MiwiaWF0IjoxNzAxMDUzMTI5NzkyLCJhaWQiOiIyODg2YWE0MzhmZjI0YmVkOGM4Njk1ZGJhMmM4MGYyYyIsImNpZCI6IjM4MzdjY2EzYmRhNDRmODhiNWEwNjVjNzJjMGJhNjJkIn0.7Z92g1ul3eoZut-7SMjE9Ej2pZppnt_uSeTNiASnpc8',
  # 'bno': '3837cca3bda44f88b5a065c72c0ba62d',
  # 'temp-id': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55SWQiOiIzODM3Y2NhM2JkYTQ0Zjg4YjVhMDY1YzcyYzBiYTYyZCIsImFnZW50SWQiOiIyODg2YWE0MzhmZjI0YmVkOGM4Njk1ZGJhMmM4MGYyYyIsInNlcnZpY2VFbWFpbCI6ImxlaXlwQHNvYm90LmNvbSIsInpvbmUiOjIsImlzcyI6ImxlaXlwQHNvYm90LmNvbSIsImV4cCI6MTcwMTEzOTUyNCwidHlwZSI6ImNvbnNvbGUifQ.IZ3EsoxXQYRLYQO1gwEUy5m1UfOvZFbJfiuJR6D3jN4',
}
response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)
