import requests

back = requests.post(url="http://127.0.0.1:7788/api", json={"key": "azhesleep", "status": "清醒"})		
back.encoding = 'utf-8'
print(back.text)  # 这将打印出解码后的字符串