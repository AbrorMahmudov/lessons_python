# -*- coding: utf-8 -*-
"""
dars:  list bilan ishlash
author: Mahmudov Abrorbek
sana:  01.04.2023

"""
#1-misol
#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
#ismlar=["Abrorbek", 'Ikromjon', 'Xusniddin']
#print(ismlar)


#2-misol
#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
#print("Assalomu alaykum do'stim ",ismlar[0])
#print(ismlar[0], ' sen do\'stimiz', ismlar[1],'ni bazmga chaqirdingmi')
#print(ismlar[1],'ga ayt kelishida', ismlar[2],'ni chaqirib kelsin')
#print('Hamma', ismlar,'ertaroq kelsin')


#3-misol
#friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
friends=[]
friends.append('Anvar')
friends.append('Solijon')
friends.append('Nabijon')
friends.append('Qurbonali')
friends.append('Salovat')


#4-misol
#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
friends.remove('Anvar')
print(friends)
friends.remove('Nabijon')
print(friends)


#5-misol
#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing
friends.append('oxiriga qo\'shildi')
friends.insert(0, 'boshiga qo\'shildi')
friends.insert(3, 'o\'rtaga qo\'shildi')
print(friends)

#Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar=[]
mehmonlar=friends.pop(1)
mehmonlar=friends.pop(1)
mehmonlar=friends.pop(2)
print(friends)
print(mehmonlar)

