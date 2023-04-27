#Muallif: Abrorbek Mahmudov
#sana: 11.04.2023
#shart operatorlari bilan ishlash

#1-misol
#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car=='gm':
#         print(car.upper())
#     else:
#         print(car.title())


# 2-misol    
# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
# for car in cars:
#     if car!='gm':
#         print(car.title())
#     else:
#         print(car.upper())


#3-misol
# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
# login=input("Salom hurmatli foydalanuvchi loginingizni kiriting--")
# if login=='admin':
#     print(f"Xush kelibsiz {login} foydalanuvchi")
# else:
#     login.title()
#     print(f"Xush kelibsiz {login}")


# 4-misol
# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# a=float(input("Biror ixtiyoriy son kiriting ---"))
# b=float(input("Ikkinchi sonni kiriting      ---"))
# if a==b:
#     print("Siz teng sonlar kiritdingiz")
# else:
#     print("Siz kiritgan sonlar yig'indisi",a+b)


# 5-misol
# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
# a=float(input("Ixtiyoriy son kiriting>>>"))
# if a>0:
#     print("Siz musbat son kiritdingiz")
# else:
#     print("Siz kiritgan son manfiy")


# 6-misol
# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
# b=float(input("Ixtiyoriy biror son kiriting>>>"))
# if b>0:
#     print("Siz kiritgan sonning kvadrat ildizi>> ",b**(1/2))
# else:
#     print("Siz manfiy son kiritdingiz boshqason kiriting")

