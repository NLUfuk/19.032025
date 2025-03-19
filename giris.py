from datetime import datetime, timedelta

class Giris:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def giris_yap(self):
        return f"{self.yas} yasinda {self.isim} giriş yaptı."

class AbonmanKart(Giris):
    def __init__(self, isim, yas, bitis_tarihi):
        super().__init__(isim, yas)
        self.bitis_tarihi = datetime.strptime(bitis_tarihi, "%Y-%m-%D")

    def kart_dogrula(self):
        bugun = datetime.today()
        if bugun <= self.bitis_tarihi:
            return f"{self.isim} için giriş başarılı. Kart geçerli!"
        else:
            return f"{self.isim} için giriş reddedildi! Kart süresi dolmuş."

    def sure_hatirlat(self):
        kalan_gun = (self.bitis_tarihi - datetime.today()).days
        if kalan_gun > 0:
            return f"Kart süreniz {kalan_gun} gün sonra dolacak."
        else:
            return "Kart süreniz dolmuştur, yenileyiniz!"

class NakitKart(Giris):
    def __init__(self, isim, yas, bakiye):
        super().__init__(isim, yas)
        self.bakiye = bakiye
        self.ucret = 50  # Giriş ücreti

    def giris_yap(self):
        if self.bakiye >= self.ucret:
            self.bakiye -= self.ucret
            return f"{self.isim} giriş yaptı. Kalan bakiye: {self.bakiye} TL"
        else:
            return "Yetersiz bakiye! Lütfen yükleme yapın."

class GunubirlikBilet(Giris):
    def __init__(self, isim, yas, bilet_kodu):
        super().__init__(isim, yas)
        self.bilet_kodu = bilet_kodu

    def qr_kod_dogrula(self, girilen_kod):
        if girilen_kod == self.bilet_kodu:
            return f"{self.isim} için QR kod doğrulandı, giriş başarılı!"
        else:
            return "Hatalı QR kodu! Giriş reddedildi."

class OkulKurulusGiris(Giris):
    def __init__(self, okul_adi, yas, kisi_sayisi):
        super().__init__(okul_adi, yas)
        self.kisi_sayisi = kisi_sayisi

    def grup_giris(self):
        return f"{self.isim} adına {self.kisi_sayisi} kişi giriş yaptı. (Ortalama yaş: {self.yas})"
