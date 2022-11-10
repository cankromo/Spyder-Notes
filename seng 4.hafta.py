"""
d = 0
b = 0
c = 0
cıft=0
tek=0
summon=0
avr=0
for a in range(0,10,1):
    n = int(input("Lütfen hesaplama için sayı giriniz: "))
    
    if n % 2 == 0:
        cıft=cıft+1
    
    else:
        tek=tek+1
        
        
    summon=summon+n
    avr=summon/(cıft+tek)
print("Tek sayı adetiniz ",tek, "çift sayı adetiniz " ,cıft)
print("Toplam değer ", summon ,)
print("Ortalama değer " , avr)

"""
"""
a = "lütfenaf"

print(a)
print(a[2:8:2])

name="Can"
age=0
surname="Kankılıç"
#print("My name is {} my ag is {} and my surname is{}".format(name,age,surname))
print(f"My name is {name}")

"""


"""
website = "http://www.sadikturan.com"
length = len(website)
result = website[7:10]
print(result)
"""
#sonuç = website[22:25]
course="asdadjadkjasdkasdkadsakjdkajdajakd"

#lenght = len(course)


#result = course[0:15]
#result2 = course[lenght-15:lenght+1]
#print(result)
#print(result2)

result = course[::-1]
print(result)
























    