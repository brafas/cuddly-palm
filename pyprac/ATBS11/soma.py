import requests

url = 'http://ice1.somafm.com/groovesalad-128-aac'

def print_url(r, *args, **kwargs):
    print(r.headers)

requests.get(url, hooks=dict(response=print_url))