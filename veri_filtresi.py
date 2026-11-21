
def veri_filtresi(veri_listesi, esik_deger):
    filtrelenmis = [
        veri for veri in veri_listesi
        if veri > esik_deger
    ]
    return filtrelenmis


# Test 1: Sıcaklık verileri
sicakliklar = [35, 42, 55, 48, 62, 30]

kritik_veriler = veri_filtresi(sicakliklar, 50)

print("Kritik Sıcaklıklar:", kritik_veriler)


# Test 2: Filtrelenen verilerin ortalaması
if kritik_veriler:
    ortalama = sum(kritik_veriler) / len(kritik_veriler)
    print("Kritik Verilerin Ortalaması:", ortalama)
else:
    print("Kritik veri bulunamadı.")


# Test 3: Boş liste kontrolü
print("Boş Liste Testi:", veri_filtresi([], 50))
