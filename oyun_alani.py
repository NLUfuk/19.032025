import random

class Otomat:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
        print(f"[{self.__class__.__name__}] Sınıfı Başlatıldı: {isim}, {yas} yaşında")
    
    def secim_yap(self):
        print(f"[{self.__class__.__name__}.secim_yap()] Çağrıldı")
        if self.yas >= 65:
            muzik = "Sakin müzik"
            oyun_suresi = "10 dakika"
            hiz = "Düşük"
        elif 20 <= self.yas < 65:
            muzik = "Pop müzik"
            oyun_suresi = "25 dakika"
            hiz = "Orta"
        else:
            muzik = "Death Metal"
            oyun_suresi = "1 saat"
            hiz = "Yüksek"

        return f"{self.isim} için seçimler:\nMüzik: {muzik}\nOyun Süresi: {oyun_suresi}\nHız: {hiz}"
    
    def qr_kod_ile_giris(self, qr_kod, dogrulama_kodu):
        print(f"[{self.__class__.__name__}.qr_kod_ile_giris()] Çağrıldı")
        return "Giriş Başarılı!" if qr_kod == dogrulama_kodu else "Geçersiz QR kodu!"

class Raporlama:
    def __init__(self):
        self.gurultu = random.randint(30, 100)  # Desibel cinsinden gürültü seviyesi
        self.doluluk_orani = random.randint(0, 100)  # Oyun alanı doluluk oranı (%)
        self.elektrik_kullanimi = random.randint(50, 500)  # kWh cinsinden elektrik kullanımı
        self.isi_olcumu = random.randint(15, 35)  # Derece cinsinden ısı ölçümü
        print(f"[{self.__class__.__name__}] Sınıfı Başlatıldı")

    def raporla(self):
        print(f"[{self.__class__.__name__}.raporla()] Çağrıldı")
        return (f"Gürültü Seviyesi: {self.gurultu} dB\n"
                f"Oyun Alanı Doluluk Oranı: {self.doluluk_orani}%\n"
                f"Elektrik Kullanımı: {self.elektrik_kullanimi} kWh\n"
                f"Isı Ölçümü: {self.isi_olcumu}°C")

# Kullanıcıdan bilgi al
isim = input("Adınızı girin: ")
yas = int(input("Yaşınızı girin: "))
qr_kod = input("QR Kodunuzu girin: ")
dogrulama_kodu = "12345"  # Örnek doğrulama kodu

# Otomatı oluştur ve seçim yap
otomat = Otomat(isim, yas)
print(otomat.secim_yap())
print(otomat.qr_kod_ile_giris(qr_kod, dogrulama_kodu))

# Raporlama sınıfını oluştur ve raporu göster
rapor = Raporlama()
print("\nOyun Alanı Raporu:")
print(rapor.raporla())
