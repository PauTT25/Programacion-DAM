import requests
from lxml import html

url = "https://elpais.com"

response = requests.get(url, timeout=10)
response.raise_for_status()  # raises exception if not 200

tree = html.fromstring(response.content)

h1_elements = tree.xpath("//a")

for i, h1 in enumerate(h1_elements, start=1):
    text = h1.text_content().strip()
    print(f"H1 #{i}: {text}")

