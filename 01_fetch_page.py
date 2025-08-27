import requests

url = "https://openlibrary.org/"
response = requests.get(url)


print("status code: ", response.status_code)
print("First 500 hunders of the HTML: ")
print(response.text[:500])


