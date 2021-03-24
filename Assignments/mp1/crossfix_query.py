import requests
url = 'http://lab3.sustech.pub:5000/crossfix'
repo_url = "https://github.com/json-path/JsonPath/issues/"
issue_list = {"628","526","620","395","356","273","174","629","623"}
for i in issue_list:
    issue_url = repo_url+i
    payload = {
    'url': issue_url,
    'email': 'chaoyiwang00@gmail.com'
    }
    r = requests.post(url, data=payload)
    print(i, r.status_code, r.text)