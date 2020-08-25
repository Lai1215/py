# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 21:26:57 2020

@author: Hank Lai
"""
'''

x = input("c or f")  #c=1 f=2
t = eval(input("溫度= "))
f = t * 9 / 5 + 32
c = (t - 32) * 5 / 9
if (int(x) == 1):
    print(float(c))
else:
    print(float(f))



y = input("請輸入出生年分 :")
if (int(y) % 4) == 0:
    if (int(y) % 100) == 0:
        if (int(y) % 400) == 0:
            print("%s是閏年" % y)
        else:
            print("%s不是閏年" % y)
    else:
        print("%s是閏年" % y)
else:
    print("%s不是閏年" % y)



a = eval(input("a :"))
b = eval(input("b :"))
c = eval(input("c :"))
x = a - b
y = b - c
z = a - c
if (x > 0 and y > 0 and z > 0):
    print("a > b > c")
elif (x > 0 and y < 0 and z > 0):
    print("a > c > b")
elif (x < 0 and y > 0 and z > 0):
    print("b > a > c")
elif (x < 0 and y > 0 and z < 0):
    print("b > c > a")
elif (x > 0 and y < 0 and z < 0):
    print("c > a > b")
else:
    print("c > b > a")



a = eval(input("a :"))
b = eval(input("b :"))
c = eval(input("c :"))
x = a + b - c
y = b + c - a
z = a + c - b
p = a + b + c
if (x > 0 and y > 0 and z > 0):
    print(int(p))
else:
    print("無法組成triangle")
    
str = "THIS IS STRING EXAMPLE....WOW!!!"                 #大寫字符轉小寫lower( )
print(str.lower( ))

str = "this is string example....wow!!!"                 #小寫字符轉大寫upper( )
print(str.upper( ))

str = "this is string example....wow!!!"                 #第一個字符轉大寫title( )
print(str.title( ))

str = "this is string example....wow!!!"                 #返回大小寫swapcase( )
print(str.swapcase( ))  
str = "THIS IS STRING EXAMPLE....WOW!!!"                 #返回大小寫swapcase( )
print(str.swapcase( ))  

str = "     this is string example....wow!!!     "       #去除後面不要的字串
print(str.rstrip( ))
str = "88888888this is string example....wow!!!8888888"  #去除後面不要的字串
print(str.rstrip('8'))

str = "     this is string example....wow!!!     "       #去除前面不要的字串
print(str.lstrip( ))
str = "88888888this is string example....wow!!!8888888"  #去除前面不要的字串
print(str.lstrip('8'))

str = "88888888this is string example....wow!!!8888888"  #去除前後不要的字串
print(str.strip('8'))

str = "this is string example....wow!!!"                 #字串置中
print("str.center(40, 'a') : ", str.center(40, 'a'))

str = "this is string example....wow!!!"                 #字串置前
print(str.rjust(50, '0'))

str = "this is string example....wow!!!"                 #字串置後
print(str.ljust(50, '0'))

str = "this is string example....wow!!!"                 #填滿字串
print(str.zfill(40))
print(str.zfill(50))
'''


e = int(input("數字: "))
num_list = []
for x in range(1,int(e + 1)):
    if x % 2 == 0:
        num_list.append(x)
        x += 1
    else:
        x += 1
print(num_list)

w = int(input("數字: "))
num_list2 = []
y = 1
while y <= int(w):
    if y %2 == 0:
        num_list2.append(y)
        y += 1
    else:
        y += 1
print(num_list2)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    













































































    
    
    
    
    
    
    
    
    
    
    