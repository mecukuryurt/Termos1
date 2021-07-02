while True:
    exitt=0
    try:
        komutlarr = """- Termos 1.0 - Komutları
temizle -------------------- : Ekranı temizler
çıkış ---------------------- : Sanal makineyi kapatır
dizin ---------------------- : Etkin olunan dizini gösterir
makedir (klasör adı) ------- : makedir komutu klasör adıyla verilmelidir. makedir komutundan sonra oluşturulacak klasörün adı girilir: Örnek: makedir denemekalsörü
dirlist -------------------- : Etkin olduğunuz dizinin içinde bulunan dosya ve klasörleri listeler.
restart -------------------- : Sanal makineyi yeniden başlatır
cdir (klasör adı veya bfdir) : cdir komutu bfdir ile kullanıldığında bir alt klasöre geçer. Örnek: cdir bfdir
                               bfdir yerine o klasörde bulunan başka bir klasöre geçer.
termos --------------------- : Termos giriş ekranını gösterir
benkimim ------------------- : Kullanıcı adını verir
hesapmak ------------------- : Hesap Makinesi uygulamasını açar.
komutlar ------------------- : Termos'ta kullanılabilecek komutları listeler
pythonshell ---------------- : Python terminalini açar.
    """
        while True:
            u="termos"
            p="trm1.0"
            try:
                from os import *
                from sys import *
                from time import sleep
                import apps
                
            except:
                print("Termos Error!")
                print("Modules not found!")
                print("Can't use TermOs")
                print("Enter to exit")
                sleep(0.5)

            system("color 1c")

            while True:
                system("cls")
                print("Termos 1.0")
                username=input("Kullanıcı Adı :")
                password=input("Şifre         :")
                if username == u:
                     if password == p:
                         print("Giriş Başarılı")
                         sleep(1)
                         break
                     else:
                         print("Şifre Yanlış!")
                         sleep(1)
                else:
                    print("Kullanıcı Adı Yanlış!")
                    sleep(1)
                            
            chdir("C:\\termos\\users\\termos")
            dizin = "/users/termos"
            sistemdizin = "C:\\termos\\users\\termos"
            system("cls")
            print("Termos 1.0")
            print("MEÇ Software Programming")
            print(version)
            print("")
                    
            while True:
                command = input(f">termos@{dizin}?$")
                        
                if command == "temizle":
                    system("cls")
                            
                elif command == "çıkış":
                    exitt = 1
                    quit()
                            
                elif command == "dizin":
                    print(dizin)
                            
                elif "makedir" in command:
                    mkdir = command.split()
                    dirname = mkdir[1]
                    mkdircomm = "mkdir " + dirname
                    system(mkdircomm)

                elif "dirlist"==command:
                    for i in listdir(sistemdizin):
                        print(i)

                elif "restart"==command:
                        system("cls")
                        break

                elif "cdir" in command:
                           
                    cmdcdir=command.split()
                    _2ndw = cmdcdir[1]
                            
                    if _2ndw == "bfdir":
                        dizn = dizin.split("/")
                        del dizn[len(dizn)-1]
                        del dizn[0]
                        dizin = ""
                        for dr in dizn:
                            dizin += "/" + dr

                        sdzn = sistemdizin.split("\\")
                        del sdzn[len(sdzn)-1]
                        del sdzn[0]
                        sistemdizin = "C:"
                        for sdr in sdzn:
                            sistemdizin += "\\" + sdr

                        chdir(sistemdizin)

                    else:
                        dizin = _2ndw
                        sistemdizin = "C:\\termos" + dizin.replace("/","\\")
                        chdir(sistemdizin)

                elif command=="termos":
                    print("Termos 1.0")
                    print("MEÇ Software Programming")
                    print(version)
                    print("")

                elif command=="benkimim":
                    print(u)

                elif command=="hesapmak":
                    apps.calc()

                elif command=="komutlar":
                    print(komutlarr)

                elif command=="pythonshell":
                    system("python")
                            
                else:
                    print("HATALI GİRİŞ")


    except:
        system("cls")
        if exitt == 0:
            print("Termos Error!")
            print("Your VM is restarting...")
            sleep(0.5)
        else:
            quit()
        
