import requests

query = input("Enter the topic you are interested in : ")
api = "1278b923ae2f4e8d9ceb9fd161e9f22b"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-09-15&sortBy=publishedAt&apiKey={api}"

print(url)
r = requests.get(url)
data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index+1, article["title"], article["url"])
    print("\n*********************************************\n")
