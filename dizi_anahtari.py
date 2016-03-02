# -*- coding: utf-8 -*-

def dizi_anahtari(gelenListe):
    sayimizSplit = sayimiz.split('-')

    sayilarinToplami = 0
    kacTaneSayiVarki = len(sayimizSplit)

    yeniBosDizi = []

    for diziElemanlari in sayimizSplit:
        sayilarinToplami = sayilarinToplami + int(diziElemanlari)
        yeniBosDizi.append( int(diziElemanlari) )

    sayilarinOrtalamasi = a = sayilarinToplami // kacTaneSayiVarki # // ifadesi tam sayı verir.

    yeniBosDizi.sort()

    if ( kacTaneSayiVarki % 2 == 0 ):

        birinciOrtanca = round(kacTaneSayiVarki / 2) # round ile a.0 sayısını a sayısına yuvarladık.
        ikinciiOrtanca = birinciOrtanca + 1

        ortadakiSayi1 = yeniBosDizi[birinciOrtanca - 1]
        ortadakiSayi2 = yeniBosDizi[ikinciiOrtanca - 1]

        isteOrtadakiSayi = b = (ortadakiSayi1 + ortadakiSayi2) // 2

    else:

        tekTwoBol = kacTaneSayiVarki / 2
        tekTwoBol = tekTwoBol - 0.5
        tekTwoBol = round(tekTwoBol)

        isteOrtadakiSayi = b = yeniBosDizi[tekTwoBol] # ortadaki sayıyı bulduk.

    dizi_anahtarimiz = a * b

    return dizi_anahtarimiz

sayimiz = '6-19-4-60-22-7-4'

print('Dizi anahtarı:', dizi_anahtari(sayimiz) )