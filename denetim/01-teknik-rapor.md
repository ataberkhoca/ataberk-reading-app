# Teknik Rapor — Y2 Tema 1 (School Life)

Kaynak: `data/grade2/school-life.json` · Kontrol betiği: [`checker.py`](checker.py) · Ham çıktı: `checker_output.json`

## Genel sayılar

| Grup | Metin sayısı |
|---|---|
| scan | 13 |
| skim | 13 |
| int | 13 |
| inf | 12 |
| **Toplam** | **51** |

`hlMode` dağılımı: `fade3` → 38 (scan+int+skim'in bir kısmı hariç... bkz. not), `always` → 13
`hintMode` dağılımı: `button` → 39, `always` → 12
`choices` dağılımı: tüm 51 metinde sabit `3` (1 doğru + 2 yanlış şık)

**Not:** `hlMode:"always"` tam olarak skim grubunun 13 metniyle örtüşüyor (skim = ana fikir bulma,
tüm cümleler sürekli vurgulu — mantıklı). `hintMode:"always"` tam olarak inf grubunun 12 metniyle
örtüşüyor (inference = ipucu her zaman açık — tasarım kararı olarak tutarlı, ama bkz.
[02-sizinti-raporu.md](02-sizinti-raporu.md) ve [04-pedagojik-rapor.md](04-pedagojik-rapor.md):
"her zaman açık ipucu" ile "ipucu cevabı doğrudan söylüyor" birleşince ciddi bir kalite sorununa dönüşüyor.

## Otomatik kontrol sonuçları (checker.py)

| # | Kontrol | Sonuç |
|---|---|---|
| 1 | JSON geçerliliği | ✅ Geçerli |
| 2 | `sentences` sayısı = `translations` sayısı | ✅ 51/51 metinde eşit |
| 3 | `hl` indeksleri sınır içinde (negatif yok, cümle sayısını aşmıyor) | ✅ 255/255 soruda geçerli |
| 4 | `correct` değeri `wrong` listesinde tekrar ediyor mu | ✅ Hiçbir soruda çakışma yok (0/255) |
| 5 | Zorunlu alanlar (`id, title, subtitle, icon, hlMode, hintMode, choices, cast, sentences, translations, questions`) | ✅ 51/51 metinde tam |
| 6 | `id` çakışması | ✅ 51 benzersiz id, sıralama da tutarlı (`scan-1..13` vb.) |
| 7 | Soru sayısı / `choices` şema uyumu | ✅ Her soruda `1 + len(wrong) == choices (3)` |
| — | `wrong` listesi içinde kendi içinde tekrar | ✅ Yok |
| — | Boş cümle/çeviri/soru/ipucu alanı | ✅ Yok |
| — | `cast` objelerinde `e`/`n` eksikliği | ✅ Yok |
| — | `hl` boş liste (dayanaksız soru) | ✅ Yok, her sorunun en az bir `hl` referansı var |

**Sonuç: 0 teknik bulgu.** Şema ve JSON bütünlüğü açısından bu tema temiz. Otomatik taramanın
bulamayacağı sorunlar (karakter tutarlılığı, ipucu kalitesi, dil doğallığı, sızıntı) diğer raporlarda.

## Ek istatistiksel kontrol (madde 12 — şık uzunluk dengesi)

255 sorunun tamamı üzerinde kelime-sayısı bazlı uzunluk karşılaştırması yapıldı:

- Doğru şık, tüm yanlış şıklardan **kesin olarak daha uzun**: 0/255 (%0)
- Doğru şık, tüm yanlış şıklardan **kesin olarak daha kısa**: 0/255 (%0)
- Karışık/eşit: 255/255 (%100)
- Ortalama doğru şık uzunluğu: 1.58 kelime · ortalama yanlış şık uzunluğu: 1.59 kelime

**Bulgu yok.** Doğru şık sistematik olarak en uzun ya da en kısa değil — uzunluktan cevap tahmin
edilemiyor. Bu eksende tema temiz.

## Madde 13 (karakter tutarlılığı) hakkında not

Bu kontrol yapısal/istatistiksel değil, okuma gerektiren bir kontrol — bulgular
[04-pedagojik-rapor.md](04-pedagojik-rapor.md) içinde "tutarlılık" kategorisiyle raporlanıyor.
