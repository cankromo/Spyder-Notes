# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 13:41:09 2022

@author: CAN KANKILIÇ
"""
"""
a=-1
b=1

max_v=0
while a!=97 and b!=99:
   
    
   
    
   
    a=a+2
    b=b+2
    sum_v=a/b
    max_v=sum_v+max_v
    
print(max_v)
   
    """
"""    
x = 41

if x > 10:
  print("Sayı ondan büyük")
  if x > 20:
    print("Sayı yirmiden büyük")
  else:
    print("Sayı yirmiden küçük")    
"""

"""
m=1000
a=5
b=10
n=30
x=4
y=4
z=3

if x<z:
    print("1 doğru")
elif x<y:
    print("2 doğru")
    
elif a<b:
    print("2.elif sağlandı")

if m<n:
    print("ikinci if doğru")

    
else:
    print("yanlış")
    
"""    
"""
ilk if doğruysa eliflere bakılmaz, if yanlışsa sırayla eliflere bakılır ilk doğru olan eliften
sonrası kontrol edilmez. Eliflerden biri sağlarsa sondaki else kontrol edilmez. Sona yazılan elif 
kendinden önceki ifin kontrolüdür. 
"""



max1=0
max2=0
max3=0
value=0





while value!=-1:
    
    value=int(input("Lütfen değer giriniz çıkmak için -1: "))
    if value==-1:
        break
    if value>max1:
        max3=max2
        max2=max1
        max1=value
        
    elif value>max2:
        max3=max2
        max2=value
        
        
    elif value>max3:
        max3=value
        
print(max3,max2,max1)        
              
        
         
         

#max1=10 max2=5 max3=3
#max1=10 max2=7 max3=5









































