from tavily import TavilyClient

client = TavilyClient(api_key="YOUR_KEY")

def web_search(query):
    results = client.search(query)
    return results["results"]