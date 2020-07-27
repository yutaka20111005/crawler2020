import requests as req

try:
  res = req.get("http or https URL")
  res.raise_for_status()
  res.encoding = res.apparent_encoding
  print(res.text)

except requests.exceptions.RequestException:
  print('エラーが出ましたよ！')
