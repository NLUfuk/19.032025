import random

class Otomat:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def secim_yap(self):
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

class Raporlama:
    def __init__(self):
        self.gurultu = random.randint(30, 100)  # Desibel cinsinden gürültü seviyesi
        self.doluluk_orani = random.randint(0, 100)  # Oyun alanı doluluk oranı (%)
        self.elektrik_kullanimi = random.randint(50, 500)  # kWh cinsinden elektrik kullanımı
        self.isı_olcumu = random.randint(15, 35)  # Derece cinsinden ısı ölçümü

    def raporla(self):
        return (f"Gürültü Seviyesi: {self.gurultu} dB\n"
                f"Oyun Alanı Doluluk Oranı: {self.doluluk_orani}%\n"
                f"Elektrik Kullanımı: {self.elektrik_kullanimi} kWh\n"
                f"Isı Ölçümü: {self.isı_olcumu}°C")

# Kullanıcıdan bilgi al
isim = input("Adınızı girin: ")
yas = int(input("Yaşınızı girin: "))

# Otomatı oluştur ve seçim yap
otomat = Otomat(isim, yas)
print(otomat.secim_yap())

# Raporlama sınıfını oluştur ve raporu göster
rapor = Raporlama()
print("\nOyun Alanı Raporu:")
print(rapor.raporla())