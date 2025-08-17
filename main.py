import requests
import hashlib
import time

sess=hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()
headers = {
  'Cookie': 'PHPSESSID='+sess
}
url = "https://auth.watchgeek.cn/login.php"

user = {'username_or_qq': '3322073603',
         'password': 'ccw123456'
  }
shuchu = requests.request("POST", url, headers=headers, data=user)

print("今日构造cookie：",sess)
print("发送登录！开始签到！")

qd = {'signin': '签到'}
sin = requests.request("POST", "https://auth.watchgeek.cn/signin.php", headers=headers, data=qd)

print(sin.text)
print("完成！")


