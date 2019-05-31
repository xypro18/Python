from urllib.request import urlopen

def get_data(url):
    with urlopen(url) as response:
        source = response.read()
    
    return source