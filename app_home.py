email="asdasd@gmail.com"
passw="12341234"
tryagain=True
anamenu=True
while anamenu:
    s=input("\n1: Destek ekibi giriş/kayıt\n2: Lojistik desteği başvurusu\n3: Enkaz altındayım\n")
    if s=="1":
        giris=input("1: Üye ol\n2: Giriş yap\n3: Şifremi unuttum\n")
        if giris=="1":
            email=input("Kaydolmak istediğiniz eposta: ")
            passw=input("Şifre: ")
            print("\nKaydınız başarıyla yapıldı")
        elif giris=="2":
            while tryagain:
                emailtry=input("Eposta: ")
                passwtry=input("Şifre: ")
                if emailtry==email and passwtry==passw:
                    print("\nGiriş başarılı, hoşgeldiniz")
                    tryagain=False
                    anamenu=False
                else:
                    print("\nGiriş bilgileri uyuşmamaktadır!")
        elif giris=="3":
            resetpassw=input("Lütfen şifresini unuttuğunuz hesabın epostasını giriniz\n")
            if resetpassw==email:
                print("\nŞifre sıfırlama linkiniz epostanıza gönderilmiştir")
            else:
                print("\nGirdiğiniz eposta sistemde bulunmamaktadır")
    elif s=="2":
        print(".::Lojistik desteği başvuru formu::.\nLütfen istenen bilgileri hatasız giriniz\n")
        anamenu=False
    elif s=="3":
        print(".::Enkaz altındayım bildiri formu::.\nLütfen harita üzerinden en doğru konumu işaretleyin ve doğrulama için istenen bilgileri girin\n")
        anamenu=False