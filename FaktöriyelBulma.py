sayı=int(input("Faktöriyelini Bulmak İstediğiniz Sayıyı Giriniz: "))

def Faktöriyel(sayı):
    Faktöriyel = 1
    if (sayı == 0 or sayı == 1):
          return(Faktöriyel)
    else:
        while(sayı >=1 ):
            Faktöriyel *= sayı
            sayı -= 1

    return(Faktöriyel)

print("Faktöriyel Sonucu:" ,Faktöriyel(sayı))