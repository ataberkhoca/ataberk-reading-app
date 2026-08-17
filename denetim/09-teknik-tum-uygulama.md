# Teknik Rapor — Bütün Uygulama (18 dosya, 761 metin)

`checker.py`'deki aynı şema/JSON kontrolleri [`checker_all.py`](checker_all.py) ile 18 dosyanın
tamamına uygulandı. Ham çıktı: `checker_all_output.json`.

## Sonuç özeti

| Dosya | Metin | Bulgu | Durum |
|---|---|---|---|
| Y2-T1 School Life | 51 | 0 | ✅ |
| Y2-T2 Classroom Life | 45 | 0 | ✅ |
| Y2-T3 Personal Life | 43 | 0 | ✅ |
| Y2-T4 Family Life | 40 | 0 | ✅ |
| Y2-T5 Homes & Houses | 43 | 0 | ✅ |
| Y2-T6 Life in the City | 43 | 0 | ✅ |
| Y3-T1 School Life | 40 | 0 | ✅ |
| Y3-T2 Classroom Life | 44 | 0 | ✅ |
| Y3-T3 Personal Life | 44 | 0 | ✅ |
| Y3-T4 Family Life | 43 | 0 | ✅ |
| Y3-T5 Homes & Houses | 43 | 0 | ✅ |
| Y3-T6 Life in the City | 42 | 0 | ✅ |
| Y4-T1 School Life | 40 | 0 | ✅ |
| Y4-T2 Classroom Life | 40 | 0 | ✅ |
| Y4-T3 Personal Life | 40 | 0 | ✅ |
| Y4-T4 Family Life | 40 | 0 | ✅ |
| Y4-T5 Homes & Houses | 40 | 0 | ✅ |
| Y4-T6 Life in the City | 40 | 3 | ⚠️ |
| **TOPLAM** | **761** | **3** | |

17/18 dosya kusursuz. Kalan tek bulgu, Y4-T6'daki 3 izole soru (aşağıda ayrıca açıklanıyor).

## Bulgu — `qTr` alanı sistematik olarak eksikti (2 tam dosya) — ✅ DÜZELTİLDİ

400 sorunun tamamına (`classroom-life-y4.json` 200 + `homes-houses-y4.json` 200) gerçek, sorunun
İngilizce metnine karşılık gelen `qTr` çevirileri elle yazıldı. `checker.py` artık bu iki dosya
için 0 bulgu veriyor. Aşağıdaki bulgu metni, sorunun orijinal hâlinin tarihsel kaydıdır.

```
[CİDDİ] [şema/teknik] data/grade4/classroom-life-y4.json → questions[*].qTr (40 metin × 5 soru = 200 soru)
Mevcut : Sorularda `qTr` alanı yok. Örnek: {"q": "What is on the teacher's desk?", "correct":
         "A stapler", "wrong": [...], "hint": "Öğretmenin masasını bul.", "hl": [1]} — `qTr`
         yok, doğrudan `hint`'e geçiliyor.
Sorun  : Uygulama `renderQuestionTr()` fonksiyonunda "Türkçe" butonuna basılınca
         `q.qTr || q.hint` mantığıyla çalışıyor — `qTr` yoksa sessizce `hint` metnini
         gösteriyor. Bu yüzden oyun ÇÖKMÜYOR (07 raporundaki 0-hata sonucuyla tutarlı), ama
         öğrenci "Türkçe" butonuna bastığında soru cümlesinin gerçek çevirisini değil, ipucu
         cümlesini görüyor — bu ikisi çoğu zaman aynı şey değil (ör. yukarıdaki örnekte soru
         "Öğretmenin masasında ne var?" olması gerekirken kullanıcı "Öğretmenin masasını bul."
         görüyor — bir çeviri değil, bir yönerge).
Öneri  : 400 soruya (`classroom-life-y4.json` + `homes-houses-y4.json`) gerçek `qTr` alanı
         eklenmeli. Muhtemelen bu iki dosya farklı bir şablon/araçla üretildi ve alan atlandı.
Dayanak: Şema tanımı (`checker.py`'nin REQUIRED_QUESTION_FIELDS listesi) `qTr`'yi zorunlu
         sayıyor; 51/51 Y2-Tema1 metninde ve diğer 15 dosyanın tamamında bu alan dolu.
```

```
[KÜÇÜK] [şema/teknik] data/grade4/life-in-the-city-y4.json → skim-5/questions[0], skim-9/questions[0], skim-10/questions[0]
Sorun  : Aynı eksiklik, ama yalnızca 3 izole soruda (her metnin yalnızca ilk sorusunda) —
         sistematik değil, muhtemelen elle düzeltme sırasında 3 satır atlanmış.
Öneri  : Bu 3 soruya `qTr` eklemek yeterli.
```

## Diğer tüm kontroller — 761 metnin tamamında temiz

- JSON geçerliliği: 18/18 dosya geçerli.
- `sentences`/`translations` sayı eşitliği: 761/761 metinde eşit.
- `hl` indeks sınırları: hiçbir soruda sınır dışı/negatif indeks yok.
- `correct` ∈ `wrong` çakışması: 0.
- `id` çakışması / sıralaması: 0 sorun.
- `cast` alan bütünlüğü (`e`, `n`): 0 sorun.
- `choices` / soru şık sayısı uyumu: 0 sorun.
- Boş `sentences`/`translations`/`q`/`correct`/`hint`: yalnızca yukarıdaki `qTr` bulgusu dışında 0.

**Not:** Bu bulgu, [07-tum-uygulama-oynanis-raporu.md](07-tum-uygulama-oynanis-raporu.md)'deki
"761/761 metin çökmeden oynandı" sonucuyla çelişmiyor — tam tersine onu tamamlıyor: uygulama
eksik veriye karşı sessizce (kullanıcıya hata göstermeden) bir yedek davranışla tepki veriyor,
bu yüzden oynanış testi bu veri eksikliğini yakalayamadı. Bu, yalnızca statik şema
kontrolüyle (bu rapor) ortaya çıkan bir bulgu — iki yöntemin (oynayarak test + şema taraması)
neden birbirini tamamladığının iyi bir örneği.
