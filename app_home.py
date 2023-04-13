kullanicilist=[
    ["gemiciahmet@gmail.com", "Richardbut200lbs", "user"],
    ["deryayuzuguzel@gmail.com", "EngDealer34", "user"],
    ["mustafaoz@gmail.com", "OREOisnice_NY", "user"],
    ["albinatricube@gmail.com","femCoder_2x0", "admin"]
]
tryagain=True
anamenu=True

while anamenu:
    s=input("\n1: Destek ekibi giriş/kayıt\n2: Lojistik desteği başvurusu\n3: Enkaz altındayım\n")
    if s=="1":
        giris=input("1: Üye ol\n2: Giriş yap\n3: Şifremi unuttum\n")
        if giris=="1":
            regemail=input("Kaydolmak istediğiniz eposta: ")
            regpassw=input("Şifre: ")
            kullanicilist.append([regemail,regpassw,"user"])
            print("\nKaydınız başarıyla yapıldı")
        elif giris=="2":
            while tryagain:
                emailtry=input("Eposta: ")
                passwtry=input("Şifre: ")
                for i in range(0,len(kullanicilist)):
                    if emailtry==kullanicilist[i][0] and passwtry==kullanicilist[i][1]:
                        if kullanicilist[i][2]=="admin":
                            print("\nAdmin olarak giriş yaptınız, hoş geldiniz")
                        else:
                            print("\nGiriş başarılı, hoş geldiniz")
                        tryagain=False
                        anamenu=False
        elif giris=="3":
            matchtrysuccess=False
            resetpassw=input("Lütfen şifresini unuttuğunuz hesabın epostasını giriniz\n")
            for i in range(0,len(kullanicilist)):
                if resetpassw==kullanicilist[i][0]:
                    matchtrysuccess=True
            if matchtrysuccess==True:
                print("\nSıfırlama linkiniz epostanıza gönderilmiştir")
                matchtrysuccess=False
            else:
                print("\nGirdiğiniz eposta kayıtlarda bulunamadı")
    elif s=="2":
        print(".::Lojistik desteği başvuru formu::.\nLütfen istenen bilgileri hatasız giriniz\n")
        anamenu=False
    elif s=="3":
        print(".::Enkaz altındayım bildiri formu::.\nLütfen harita üzerinden en doğru konumu işaretleyin ve doğrulama için istenen bilgileri girin\n")
        anamenu=False
        