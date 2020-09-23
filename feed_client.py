import requests

def get_bls_feed():
    url = 'http://127.0.0.1:5000/feed/bls'
    response = requests.get(url)
    with open('bls.csv', 'w') as f:
        f.write(response.text)
