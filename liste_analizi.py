# -*- coding: utf-8 -*-

listemiz = [15,94,'Metin Bilim',0.5,True,1.8,'fatih',[18,'Ahmet'],[89,41],'Mehmet',4,False,7,87.6,'Melek',[8],[1],1]

def liste_analizi(gelenListe):

    kacTane_karakterDizisi = 0
    kacTane_tamSayiDisizii = 0
    kacTane_ondalikSayiDiz = 0
    kacTane_mantiksalDeger = 0
    kacTane_listeSekilDizi = 0

    for diziElemanlari in gelenListe:
        elemanTuru = type(diziElemanlari)
        if ( elemanTuru == str ):
            kacTane_karakterDizisi += 1
        elif ( elemanTuru == int ):
            kacTane_tamSayiDisizii += 1
        elif ( elemanTuru == float ):
            kacTane_ondalikSayiDiz += 1
        elif ( elemanTuru == bool ):
            kacTane_mantiksalDeger += 1
        elif ( elemanTuru == list ):
            kacTane_listeSekilDizi += 1

    print('Toplam Karakter Dizisi:', kacTane_karakterDizisi)
    print('Toplam TamSayıı Dizisi:', kacTane_tamSayiDisizii)
    print('Toplam OndalıkS Dizisi:', kacTane_ondalikSayiDiz)
    print('Toplam Mantıksa Dizisi:', kacTane_mantiksalDeger)
    print('Toplam ListeOla Dizisi:', kacTane_listeSekilDizi)

liste_analizi(listemiz)