'''
Barig algoritmi fractal sumon
@author Adxajon97 <adxamjon97@umail.uz>
'''
# TODO: bunda birma bir kod yozganman keyinroq L-systemani qo'lleman
from turtle import *
from math import sqrt

uzunlik = 400  # Uzunligi
oraliq  = 5    # bo'g'ini
foiz    = (200 / oraliq) + 4  # foyizi
#foiz    = ((sqrt(5)+1)/2)*oraliq*6 # zalatoy sichenyani qo'llemiz keyin
#print(foiz)
ildiz   = 8   # usish jarayoni
burum   = 20  # barglar yoyiladi kichrayadi
ay      = 73  # zaruriy foyiz

title('Barg')
#ht()
#speed(0)
tracer(0, 0) # birdaniga chizilib qoladi barchasi
width(3)
bgcolor('white')


def start():
    ''' qalamni boshlang'ich pozitsyaga keltiradi '''
    up()
    lt(-90)
    fd(300)
    lt(180)
    down()


#TODO: ozma oz rivojlantirishkere
    # masalan: rangbarang
    # va birdaniga barcha shoxlari bo'yalishini qilish
def func(a, b=1):
    ''' Asosiy algoritm barg uchun '''
    fd(a)
    bk(a)
    if b < ildiz:
        lt(burum)
        func((a * foiz) / ay, b + 1)
        lt(-burum * 2)
        func((a * foiz) / ay, b + 1)
        lt(burum)

        fd((a * foiz) / ay)
        func((a * foiz) / ay, b + 1)
        bk((a * foiz) / ay)

# start
start()
fd(50)
func(uzunlik)
mainloop()
