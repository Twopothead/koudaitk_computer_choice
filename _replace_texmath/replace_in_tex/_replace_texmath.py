f = open('raw_texmath_url.txt',"r")
lines = f.readlines()#读取全部内容
list = []  ## 空列表, 将第i行数据存入list中
for i in range(0,lines.__len__(),1): #(开始/左边界, 结束/右边界, 步长)
    for word in lines[i].split():
         word=word.strip(" ")
         list.append(word)
    # print(list)
foldername = "texmath/"
for url in list:
    url_ok = url.replace("\\","")
    url_lll = url.replace("\&","\\\\\\&").replace("\%","\\\\\\%")
    # \& 换成 \\\&
    # \%换成\\\%
    # url_ok_lll = url_ok.replace("\&","\\\\\\&").replace("\%","\\\\\\%")
    texmath_png = url_ok.replace("http://texmath.koudaitiku.com/cgi-bin/mathtex.cgi?sign=","").replace("&","").replace("%","")
    # 还要吧文件名中的&和%换成\\＆和\\%
    # print(url+" "+url_ok)
    
    print("sed  -i \"s#"+url_lll+"#"+foldername+texmath_png+"#"+"g\""+" *.tex")
    # url_slash = url.replace("\#",'\\\#').replace("\%","\\\%")
    # url_ok_slash = url_ok.replace("http://texmath.koudaitiku.com/cgi-bin/mathtex.cgi?sign=","").replace("\\","")
    # print("sed -i \"s/"+url_slash+"/"+url_ok_slash+"/g\""+" laji.txt")
    # sed "s/甲/乙/g" hello.txt
    # sed "s#甲#乙#g" hello.txt 避免/
#  sed -i "s:\\\:\/:g"  /home/pp/install.sql
#        将/home/pp/install.sql 文件中的 \ 替换为 /  
# \　要写成　\\\
# \\\正确sed "s#http://texmath.koudaitiku.com/cgi-bin/mathtex.cgi?sign=2f67ff\\\#laji#g" test.txt 
# \\错误sed "s#http://texmath.koudaitiku.com/cgi-bin/mathtex.cgi?sign=2f67ff\\#laji#g" test.txt 
