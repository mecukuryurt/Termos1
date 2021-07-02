def calc():
    izinli_karakterler = "0123456789+-/*= "

    print(""" Termos Hesap Makinesi v1.0
İşleçler:

    +   toplama
    -   çıkarma
    *   çarpma
    /   bölme

    Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23 * 46 yazdıktan sonra
ENTER tuşuna basın.)

(Çıkmak için q) 
    """)

    while True:
        veri = input("İşleminiz: ")
        if(veri == "q") or (veri == "Q"):
            print("Çıkılıyor...")
            break

        for s in veri:
            if s not in izinli_karakterler:
                print("Yanlış Giriş!!")

        hesap = eval(veri)

        print(hesap)
