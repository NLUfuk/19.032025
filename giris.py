from datetime import datetime, timedelta

class Giris:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
        print(f"[{self.__class__.__name__}] Sınıfı Başlatıldı: {isim}, {yas} yaşında")
    
    def giris_yap(self):
        print(f"[{self.__class__.__name__}.giris_yap()] Çağrıldı")
        return f"{self.yas} yaşında {self.isim} giriş yaptı."

class AbonmanKart(Giris):
    def __init__(self, isim, yas, bitis_tarihi):
        super().__init__(isim, yas)
        self.bitis_tarihi = datetime.strptime(bitis_tarihi, "%Y-%m-%d")

    def kart_dogrula(self):
        print(f"[{self.__class__.__name__}.kart_dogrula()] Çağrıldı")
        bugun = datetime.today()
        if bugun <= self.bitis_tarihi:
            return f"{self.isim} için giriş başarılı. Kart geçerli!"
        else:
            return f"{self.isim} için giriş reddedildi! Kart süresi dolmuş."

    def sure_hatirlat(self):
        print(f"[{self.__class__.__name__}.sure_hatirlat()] Çağrıldı")
        kalan_gun = (self.bitis_tarihi - datetime.today()).days
        return f"Kart süreniz {kalan_gun} gün sonra dolacak." if kalan_gun > 0 else "Kart süreniz dolmuştur, yenileyiniz!"

class NakitKart(Giris):
    def __init__(self, isim, yas, bakiye):
        super().__init__(isim, yas)
        self.bakiye = bakiye
        self.token = 100  # Nakit giriş yapanlara verilen token

    def giris_yap(self):
        print(f"[{self.__class__.__name__}.giris_yap()] Çağrıldı")
        if self.bakiye >= 50:
            self.bakiye -= 50
            return f"{self.isim} giriş yaptı. Kalan bakiye: {self.bakiye} TL, Tokenler: {self.token}"
        else:
            return "Yetersiz bakiye! Lütfen yükleme yapın."
    
    def token_harcama(self, miktar):
        print(f"[{self.__class__.__name__}.token_harcama()] Çağrıldı")
        if self.token >= miktar:
            self.token -= miktar
            return f"{miktar} token harcandı. Kalan token: {self.token}"
        else:
            return "Yetersiz token!"

class GunubirlikBilet(Giris):
    def __init__(self, isim, yas, bilet_kodu):
        super().__init__(isim, yas)
        self.bilet_kodu = bilet_kodu

    def qr_kod_dogrula(self, girilen_kod):
        print(f"[{self.__class__.__name__}.qr_kod_dogrula()] Çağrıldı")
        return f"{self.isim} için QR kod doğrulandı, giriş başarılı!" if girilen_kod == self.bilet_kodu else "Hatalı QR kodu! Giriş reddedildi."

class OkulKurulusGiris(Giris):
    def __init__(self, okul_adi, yas, kisi_sayisi):
        super().__init__(okul_adi, yas)
        self.kisi_sayisi = kisi_sayisi

    def grup_giris(self):
        print(f"[{self.__class__.__name__}.grup_giris()] Çağrıldı")
        return f"{self.isim} adına {self.kisi_sayisi} kişi giriş yaptı. (Ortalama yaş: {self.yas})"
