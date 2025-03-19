from datetime import datetime, timedelta

class Giris:

    def __init__(self,isim):
        self.isim=isim

    def giris_yap(self):
        return f"{sel.isim} giris yapti."

    
class abonman_kartl(Giris): 

    def __init__(self, isim, bitis_tarihi):
        super().__init__(isim)
        self.bitis_tarihi = datetime.strptime(bitis_tarihi, "%Y-%m-%d")   


    def kart_dogrula(self):
        bugun = datetime.today()
        if bugun <= self.bitis_tarihi:
            return f"{self.isim} için giriş basarili. Kart geçerli!"
        else:
            return f"{self.isim} için giriş reddedildi! Kart süresi dolmuş."

    def sure_hatirlat(self):
        kalan_gun = (self.bitis_tarihi - datetime.today()).days
        if kalan_gun > 0:
            return f"Kart süreniz {kalan_gun} gün sonra dolacak."
        else:
            return "Kart süreniz dolmuştur, yenileyiniz!"

class NakitKart(Giris):
    def __init__(self, isim, bakiye):
        super().__init__(isim)
        self.bakiye = bakiye
        self.ucret = 50  # Giriş ücreti

    def giris_yap(self):
        if self.bakiye >= self.ucret:
            self.bakiye -= self.ucret
            return f"{self.isim} giriş yapti. Kalan bakiye: {self.bakiye} TL"
        else:
            return "Yetersiz bakiye! Lütfen yükleme yapın."

class GunubirlikBilet(Giris):
    def __init__(self, isim, bilet_kodu):
        super().__init__(isim)
        self.bilet_kodu = bilet_kodu

    def qr_kod_dogrula(self, girilen_kod):
        if girilen_kod == self.bilet_kodu:
            return f"{self.isim} için QR kod doğrulandi, giriş başarili!"
        else:
            return "Hatali QR kodu! Giriş reddedildi."

class OkulKurulusGiris(Giris):
    def __init__(self, okul_adi, kisi_sayisi):
        super().__init__(okul_adi)
        self.kisi_sayisi = kisi_sayisi

    def grup_giris(self):
        return f"{self.isim} adina {self.kisi_sayisi} kişi giriş yapti."



abonman = AbonmanKart("Ahmet", "2025-05-15")
print(abonman.kart_dogrula())  # Kart süresi kontrolü
print(abonman.sure_hatirlat())  # Kart süresi hatırlatma

nakit = NakitKart("Mehmet", 100)
print(nakit.giris_yap())  # Bakiye kontrolü ve giriş işlemi

gunubirlik = GunubirlikBilet("Zeynep", "QR1234")
print(gunubirlik.qr_kod_dogrula("QR1234"))  # QR kod doğrulama

okul = OkulKurulusGiris("Bilgi Koleji", 30)
print(okul.grup_giris())  # Grup girişi kontrolü