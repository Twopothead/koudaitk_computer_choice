# https://github.com/githubao/xiao-python-cookbook/blob/a5a644501e931c60aee9f47a8337acc82b122e97/xiaocook/chapter11/sec01_http_requets.py
from urllib import request, parse
import requests
import sys
url = 'http://texmath.koudaitiku.com/cgi-bin/mathtex.cgi?sign=2a8025&%5Cdpi%7B350%7Di'
import re
# print(url.replace('http://texmath.koudaitiku.com/cgi-bin/mathtex.cgi?sign=',""))
tex_png_filename = url.replace('http://texmath.koudaitiku.com/cgi-bin/mathtex.cgi?sign=',"")
u = request.urlopen(url)
resp = u.read()
def save_png(file_name, file_content):
    #    注意windows文件命名的禁用符，比如 /
    with open(file_name + ".png", "wb") as f:
        #   写文件用bytes而不是str，所以要转码
        f.write(file_content)
print(resp)
save_png(tex_png_filename,resp)