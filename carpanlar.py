
import math
i=1                                    
while i==1:
    #i = i - 1
    denklem = input("ax²+bx+c: ")
    if denklem == "stop" :
        break
        
    say = denklem.count('-') #b ve c katsayılarından kaçının negatif olduğunu ögreniyoruz.
    if say > 0:#eğer negatif bir katsayı varsa,
        index1 = int(denklem.find('²-'))#daha sonra katsayıları bulmamıza yarayacak indexleri belirliyoruz.
        index2 = int(denklem.find('x-')) #eğer denklemde 'x-' bulunmazsa index - değerli olacaktır
        if index1 < 0:#index - ise bunu düzeltmek için '²-'elemanı bulunmadığı için '²+' elemanını arıyoruz
                index1 = int(denklem.find('²+'))
        if index2 < 0:#aynı işlemi ikinci indexe uyarladık
            index2 = int(denklem.find('x+'))
    if say == 0:#eğer negatif katsayı yoksa indexleri kontrol etmemize gerek yok direk tanımlıyoruz
        index1 = int(denklem.find('²+'))
        index2 = int(denklem.find('x+'))

    a = str(denklem[:index1 -1 ])            
    b = int(denklem[index1 + 1 : index2 ])  #daha önce tanımladığımız indexlerle katsayıları buluyoruz.
    c = int(denklem[index2 + 1:])            
    if a == '': a = int(1)                                  # eger x² in önünde bir sayı girilmemiş   
    elif a == '-': a = int(-1)                              # yada - varsa 
    elif a != '' or a != '-': a = int(denklem[:index1 -1 ]) # a katsayısının 1 yada -1 olarak tanımlıyoruz       

    d = b**2 - 4*a*c  #denklemin discriminantını hesapladık

    def tek_kok1() :#  d = 0, a != 1
        x1 = b / (2*a) 
        if x1 % int(x1) == 0:
            x1 = int(x1)
        ###################
        if x1 < 0:
            x1 = x1 * -1
            print("{1}(x - {0})²".format(x1 , a))
        else : print("{1}(x + {0})²".format(x1 , a))         
        
    def cift_kok1() : #  d > 0, a != 1
        x1 = (b - math.sqrt(d)) / 2
        x2 = (b + math.sqrt(d)) / (2*a)
        if x1 % int(x1) == 0:
            x1 = int(x1)
        if x2 % int(x2) == 0:
            x2 = int(x2)
        ############################
        if x1 < 0 and x2 > 0:
            x1 = x1 * -1
            print("({2}x - {0})(x + {1})".format(x1 , x2 , a))
        if x2 < 0 and x1 > 0:
            x2 = x2 * -1
            print("({2}x + {0})(x - {1})".format(x1 , x2 , a))
        if x2 < 0 and x1 < 0:
            x1 = x1 * -1
            x2 = x2 * -1
            print("({2}x - {0})(x - {1})".format(x1 , x2 , a))
        else: print("({2}x + {0})(x + {1})".format(x1 , x2 , a))

    def tek_kok() : # d = 0, a = 0
        x1 = b / (2*a)
        if x1 % int(x1) == 0:
            x1 = int(x1)
        #################
        if x1 < 0:
            x1 = x1 * -1
            print("(x - {})²".format(x1))
        else : print("(x + {})²".format(x1)) 

    def cift_kok():# d > 0, a = 0
        x1 = (b - math.sqrt(d)) / 2
        x2 = (b + math.sqrt(d)) / 2
        if x1 % int(x1) == 0:
            x1 = int(x1)
        if x2 % int(x2) == 0:
            x2 = int(x2)
        #########################
        if x1 < 0 and x2 > 0:
            x1 = x1 * -1
            print("(x - {0})(x + {1})".format(x1 , x2))
        elif x2 < 0 and x1 > 0:
            x2 = x2 * -1
            print("(x + {0})(x - {1})".format(x1 , x2))
        elif x2 < 0 and x1 < 0:
            x1 = x1 * -1
            x2 = x2 * -1
            print("(x - {0})(x - {1})".format(x1 , x2))
        else: print("(x + {0})(x + {1})".format(x1 , x2))
    #  discriminant ve bas katsayının(a) durumlarına göre carpanları yazdıracak fonksiyonları tanınmladım                   
    if d == 0 and a != 1 : tek_kok1()                                            
    elif d > 0 and a != 1 : cift_kok1()                                                                                               
    elif d == 0 and a == 1: tek_kok()                                            
    elif d > 0 and a == 1 : cift_kok()                                            
    elif d < 0 : print("Denklemin reel kökü yoktur.")                                         
    # uygun durumlara göre tanımladığımız  fonksiyonları çağırıyoruz

'''eksiklikler:
    1) a katsayısı asal değilse sonuçlar  küsüratlı çıkıyor bas katsayının carpanlarını dagıtmak yerine tek bir çarpanı genişletiyor 
        örn: 12x²+7x-10 için :
        (3x + -2.0)(4x + 5.0) yerine (12x + -8.0)(x + 1.25) 
    2)eger float sonucları yuvarlamak istersem int olan kokü tekrar float a ceviriyor
        yani ya tam sayı olmayan (x + 3.33333333333334)seklindekileri, (x + 3.333) 'e yuvarlayamıyorum 
        yada (x + 3) seklindekileride  (x + 3.000) seklinde gosteriliyor yani ikisi aynı anda olmuyor
    3) girdi ax²+bx+c seklinde değilse print ile hata mesajı gonderip while döngüsünü kırmadan sürdürmenin bir yolu varmı?
        (değilse direk hata veriyor)
    '''

# ² sembolünün klavye kombinasyonu: Alt + 0178
