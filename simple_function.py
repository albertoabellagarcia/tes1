def json_import(url):
    import json
    import requests
    pointer = requests.get(url)
    content = pointer.content.decode()
    print(content)
