import requests

print("hello world!")

response = requests.get("http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=3")

print(response.json())