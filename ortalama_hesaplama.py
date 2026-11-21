def liste_ortalamasi(sayilar):
  if len(sayilar) == 0:
    return 0
  return sum(sayilar) / len(sayilar)


# Test:
irtifalar = [100, 120, 115, 130, 125]
print("Ortalama İrtifa:", liste_ortalamasi(irtifalar))def ortalama_analizi(sayilar):
    if not sayilar:
        return None

    ortalama = sum(sayilar) / len(sayilar)

    return {
        "ortalama": ortalama,
        "en_yuksek": max(sayilar),
        "en_dusuk": min(sayilar)
    }


print("İrtifa Analizi:", ortalama_analizi(irtifalar))
