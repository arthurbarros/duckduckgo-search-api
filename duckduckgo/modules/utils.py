import requests


def _get_search_url(query):
    return "https://duckduckgo.com/html/?q={}".format(query)

def get_html(url, connection_manager=None):
    header = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/10.10 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11"
    }
    try:
        request = requests.get(url, headers=header)
        html = request.text
        return html
    except Exception as e:
        print("Error accessing:", url)
        raise e
