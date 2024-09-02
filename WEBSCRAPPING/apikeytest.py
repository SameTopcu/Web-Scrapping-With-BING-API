import requests

def test_bing_search(api_key, query):
    url = f"https://api.bing.microsoft.com/v7.0/search?q={query}&responseFilter=Webpages&count=10"
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None
    data = response.json()
    return data

api_key = "bbc5a773d22843bcba9c917e4257f10b"
query = "laptop"
results = test_bing_search(api_key, query)
if results:
    print("Search results found:")
    for result in results['webPages']['value']:
        print(result['name'], result['url'])
else:
    print("No search results found.")
