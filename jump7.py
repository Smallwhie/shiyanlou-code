a=0                           #定义了一个变量a
while a<100:
    a+=1        #利用range函数输出1_100的整数
    if a%7==0 or a/10==7 or a//10==7:          #设置“逢7就过”的条件
        continue                                     
    print(a)                                     #打印输出
