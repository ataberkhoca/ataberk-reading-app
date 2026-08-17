# Şık Uzunluk Dengesi — Bütün Uygulama (3805 soru)

Y2-Tema1'de bu kontrol 255 soruda **sıfır önyargı** bulmuştu (bkz. 01-teknik-rapor.md). Aynı
kontrol, geri kalan 17 dosyanın 3805 sorusuna genişletildi.

## Sonuç

| | Sayı | Oran |
|---|---|---|
| Toplam soru | 3805 | |
| Doğru şık, tüm yanlış şıklardan **kesin daha uzun** | 134 | %3.5 |
| Doğru şık, tüm yanlış şıklardan **kesin daha kısa** | 34 | %0.9 |
| **Toplam önyargılı** | **168** | **%4.4** |

Y2-Tema1'in aksine (0 önyargı), geri kalan uygulamada hafif ama gerçek bir eğilim var. En çok
etkilenen dosya: **Y4-T6 Life in the City — 200 sorunun 44'ünde (%22) doğru şık en uzunu.**

## Ciddiyet değerlendirmesi — abartılmamalı

```
[KÜÇÜK] [soru-kalitesi] data/grade4/life-in-the-city-y4.json → şık uzunluk eğilimi
Örnekler: correct="Brown rice and yogurt" (4 kelime) vs wrong=["Chips and soda","Cake and
          ice-cream"] (3'er kelime) — correct="Ms. Reed" (2 "kelime": "Ms." + "Reed") vs
          wrong=["Nora","Sam"] (1'er kelime).
Değerlendirme: Fark çoğunlukla 1 kelime — göze çarpan, kolayca istismar edilebilir bir uzunluk
          ipucu değil (ör. 8 kelimeye karşı 2 kelime gibi bariz bir durum yok). İstatistiksel
          olarak ölçülebilir ama pratikte bir öğrencinin "en uzun şıkkı seç" stratejisiyle
          güvenilir biçimde kazanabileceği düzeyde değil.
Öneri  : Acil değil. İstenirse, çok kelimeli doğru cevaplı sorularda (ör. "Brown rice and
         yogurt") yanlış şıkları da aynı uzunlukta yazmak (ör. "White rice and cheese") kolay
         bir düzeltme olur.
```

## Diğer dosyalar

Kalan 16 dosyada önyargı oranı %0-6 arasında, dağınık ve düşük — tek bir dosya dışında
(Y4-T6, %22) endişe verici bir yoğunlaşma yok. Detaylı sayılar denetim sürecinde hesaplandı,
ayrı bir dosyaya kaydedilmedi (düşük öncelikli, tek seferlik kontrol).

## Sonuç

Bu, bütün denetim boyunca bulunan **en hafif** bulgu — ciddiyet olarak KÜÇÜK, tek bir dosyada
(Y4-T6) hafif yoğunlaşma dışında acil bir aksiyon gerektirmiyor.
