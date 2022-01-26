import requests
def url_to_html(url):
    r = requests.get(url)
    return r.text