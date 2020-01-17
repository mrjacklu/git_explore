import requests
import BeautifulSoup as bs

r = requests.get("https://coreyms.com")
print(r.status_code)
print(r.ok)
