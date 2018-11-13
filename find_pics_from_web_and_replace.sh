# var blueurl= 127.0.0.1/1.txt
# var reg = /([/][^/]+)$/;
# var blueurl = blueurl.replace(reg, "");
# var reg2 = /([^/]+)$/;
# var bluefile = blueurl.match(reg2)[1];
# --------------------- 
grep -Po "(?<=http://\\').*(?=\'\))" computer_chapters/*.tex 
# grep -o 'http://' *.tex | wc -l
# # 出现次数
# more *.tex |grep 'http://' -n
# 把来着网络的图片要下载并替换路径
#https://bbs.csdn.net/topics/380032747
#https://blog.csdn.net/a1102086061/article/details/54616877 
t1="http://abc.png"

>>> rule2 = r'http(.*?)png'
>>> re.findall(rule2, t1)
['://abc.']
>>> rule2 = r'http://(.*?).png'
>>> re.findall(rule2, t1)
['abc']
捕获组
.表示任意一个字符
*表示*前面出现的那个字符重复0或任意次
grep -o 'http://.*.png' *.tex | wc -l
more *.tex | grep -o 'http://.*.png' *.tex
