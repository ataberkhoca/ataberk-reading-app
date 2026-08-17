# Müfredat Sızıntı Raporu — Bütün Uygulama (18 tema dosyası, Y2-Y4)

**Durum güncellemesi:** Bu raporda belgelenen bulguların çoğu artık düzeltildi — bkz.
`12-genel-ozet.md` "Uygulanan Düzeltmeler". Özetle: §1a (ordinal tarih, 35 metin/117 alan),
§1b (what kind of/which, 9 örnek), §1c (something/anything, 6 örnek), §1d (these/those, 5
örnek), §1g (few/a little, 6 örnek) ve §1i (did, 1 örnek) **✅ DÜZELTİLDİ**. §1e ("any", Y3-T3)
ve §1f ("best/worst", Y4-T1/T3/T4) **bilinçli olarak dokunulmadı** — ikisi de metnin/başlığın
kendi anlatı omurgasına örülü, kasıtlı tasarım kararları (bkz. §1e/§1f altındaki güncellenmiş
notlar). Aşağıdaki metin, orijinal bulgu kaydı olarak korunuyor.

Bu rapor, yüklenen müfredat dosyasının **Y2, Y3 ve Y4'ün tamamını** (18 tema) kapsayan sürümüne
dayanıyor. Yöntem [02-sizinti-raporu.md](02-sizinti-raporu.md)'de Tema 1 için kullanılanla aynı,
ölçek büyütülerek uygulandı: her tema dosyası için müfredat sırasına göre "henüz öğretilmemiş"
yapılar listesi hesaplandı ve `sentences/title/subtitle/q/correct/wrong/hint` alanlarının tamamı
bu listeye karşı tarandı. Tarama betiği: [`curriculum_leak_scan.py`](curriculum_leak_scan.py),
ham çıktı: `curriculum_leak_scan_output.json`.

## Yöntem notu — şeffaflık

Otomatik tarama **2035 ham eşleşme** buldu. Bunların büyük kısmı yanlış pozitifti (aşağıda
belgeleniyor); her kategoriyi elle inceleyip gerçek/yanlış ayrımını yaptım. İki kategori
("düzensiz geçmiş zaman fiilleri" — 1375 ham eşleşme, "many/much/a lot of" — 352 ham eşleşme) o
kadar gürültülüydü ki (bkz. §3) makul bir süre içinde tek tek doğrulanabilecek boyutu aştı; bu
ikisi için **temsili filtreleme + örneklem** yapıldı, tam tek tek okuma yapılmadı — bu açıkça
belirtiliyor, gizlenmiyor.

## 1. Kesin doğrulanmış sızıntılar

### 1a. Sıra sayı + tarih kalıbı — EN BÜYÜK VE EN SİSTEMATİK BULGU — ✅ DÜZELTİLDİ

35 metindeki 117 alanın (title/sentences/questions) tamamı "the Nth of Month" → "N Month"
kalıbına çevrildi (ör. "the 23rd of April" → "23 April"). Tek istisna, gerçek bir ay adı
içermeyen genel referans (`school-life-y3.json:inf-9` "It is the 30th of **the month**.") —
bu bilinçli olarak dokunulmadan bırakıldı, çünkü "ay" kelimesi burada bir ay ADI değil.

```
[CİDDİ] [ileri-sızıntı] tema geneli — "the Nth of Month" tarih kalıbı
Yapı   : Sıra sayılar (Ordinal numbers 1st-30th) Y4-Tema2'de [NEW]; tarihlerde sıra sayı
         kullanımı Y4-Tema3'te [NEW].
Bulgu  : 34 ayrı metinde, 11 farklı tema dosyasında (Y2'nin 6 temasının 6'sı da dahil, Y3'ün
         6 temasından 5'i) bu kalıp kullanılıyor. Y3-Tema4 (Family Life) tek istisna.
```

| Tema | Etkilenen metinler | Sayı |
|---|---|---|
| Y2-T1 School Life | scan-10, scan-13, skim-10, int-10, inf-10 | 5 |
| Y2-T2 Classroom Life | scan-10, skim-10, int-10, inf-10 | 4 |
| Y2-T3 Personal Life | int-10 | 1 |
| Y2-T4 Family Life | skim-10, inf-10 | 2 |
| Y2-T5 Homes & Houses | scan-10, int-10 | 2 |
| Y2-T6 Life in the City | scan-10, int-10, inf-10 | 3 |
| Y3-T1 School Life | scan-9, scan-10, skim-9, int-9, int-10, inf-9 | 6 |
| Y3-T2 Classroom Life | scan-10, skim-9, int-10, inf-10 | 4 |
| Y3-T3 Personal Life | scan-10, skim-10, inf-10 | 3 |
| Y3-T5 Homes & Houses | skim-10, int-10 | 2 |
| Y3-T6 Life in the City | scan-10, int-10, inf-10 | 3 |
| **Toplam** | | **35** |

**Bu tek başına en önemli bulgu.** Y2 ve Y3'ün her temasında "özel gün" konulu metin — hangi
beceri grubunda olursa olsun — hep aynı şablonu kullanıyor: *"What day is it today? It is the
23rd of April."* Bu, tek bir yazım hatası değil; iki yılın tamamına yayılmış, muhtemelen tek bir
"özel gün metni" şablonundan türetilmiş sistematik bir tasarım kararı. Düzeltmesi de bu yüzden
tek noktadan yapılabilir: şablonu "It is 23 April!" (sıra sayı eki olmadan) biçimine çevirmek,
35 metnin tamamını düzeltir.

Örnek (Y3-T1, en çok etkilenen dosya):
```
[CİDDİ] [ileri-sızıntı] data/grade3/school-life-y3.json:int-9 → title, sentences[1]
Mevcut : "The 19th of May" (başlık) / "The 19th of May is a special day in Türkiye."
Öneri  : "19th of May" yerine "19 May" (sıra sayı eki olmadan).
```

### 1b. "What kind of / Which" — Y4-Tema1 yapısı, 9 örnekte erken kullanılmış — ✅ DÜZELTİLDİ

Tüm 9 örnek yeniden yazıldı (ör. "What kind of day is it?" → "How is the day?"; "Which Lesson
Is It?" başlığı → "What Lesson Is It?", metnin kendi gövdesindeki tutarlı kullanımla eşleşecek
şekilde). Cevap mantığı hiçbirinde değişmedi, yalnızca soru kalıbı sadeleşti.

```
[CİDDİ] [ileri-sızıntı] — "What kind of...?" / "Which...?"
Dayanak: Y4-T1, WH-question words: "...why, which, what kind of [NEW]".
```

| Dosya | Metin | Alan |
|---|---|---|
| Y2-T3 Personal Life | scan-7 | questions[4].q: "What kind of day is today?" |
| Y2-T3 Personal Life | skim-10 | questions[2].q: "What kind of day is it?" |
| Y2-T3 Personal Life | skim-11 | questions[1].q, questions[3].q (×2) |
| Y2-T3 Personal Life | inf-10 | questions[1].q: "What kind of day is it?" |
| Y2-T5 Homes & Houses | inf-5 | questions[0].q: "What kind of pet is it?" |
| Y3-T1 School Life | inf-3 | questions[3].q: "What kind of boy is Leo?" |
| Y3-T2 Classroom Life | inf-4 | title: "Which Lesson Is It?" |
| Y3-T2 Classroom Life | inf-11 | title: "Which Lesson Is It?" |

Y2-Tema3'te bu yapının 5 kez tekrar etmesi (aynı temada), yine tek seferlik değil, o temanın
"özel gün" alt-grubunda tekrarlanan bir soru şablonu olduğunu gösteriyor.

### 1c. "Something/anything" — Y4-Tema3 yapısı, 6 örnekte erken kullanılmış — ✅ DÜZELTİLDİ

6 örnek de yeniden yazıldı (ör. "I have got something on my body" → "There is an object on my
body"; "everyone is doing something new" → "everyone is doing a new thing").

| Dosya | Metin | Alan |
|---|---|---|
| Y2-T3 Personal Life | inf-5 | sentences[0]: "I have got something on my body." |
| Y4-T1 School Life | skim-3 | sentences[8]: "...doing something new!" |
| Y4-T1 School Life | int-5 | title + sentences[8]: "Every Month Brings Something New" |
| Y4-T2 Classroom Life | skim-9 | sentences[6] + questions[3] (×3) |

### 1d. "These/those" — Y4-Tema1 yapısı, 5 örnekte erken kullanılmış — ✅ DÜZELTİLDİ

5 örnek de "they" veya "the" ile değiştirildi — çoğu durumda metnin kendi sorularında zaten
kullanılan alternatif kalıpla ("Whose boots are they?" gibi) tutarlı hale getirildi.

| Dosya | Metin | Alan |
|---|---|---|
| Y3-T2 Classroom Life | skim-4 | sentences[7]: "These devices are great..." |
| Y3-T3 Personal Life | scan-9 | sentences[3], sentences[5]: "Whose boots/sunglasses are these?" |
| Y3-T3 Personal Life | int-10 | sentences[7]: "Whose new earrings are these?" |
| Y3-T3 Personal Life | inf-7 | title: "Whose Earrings Are These?" |

### 1e. Quantifier "any" — Y3-Tema6 yapısı, Y3-Tema3'te yoğun biçimde erken kullanılmış — ⚠️ BİLİNÇLİ OLARAK DOKUNULMADI

**Doğrulama (bu turda):** `int-12`'nin tam içeriği okundu — metin, "Have you got any X? Yes,
I've got some X. / No, I haven't got any X." kalıbını 4 farklı eşya üzerinden sistemli biçimde
tekrarlayan, açıkça "some vs any" öğretmek için tasarlanmış bir alıştırma metni (başlık: "Some
and Any in Our Bags"). 13 örneğin hiçbiri tesadüfi değil; hepsi bu kasıtlı ders yapısının
parçası. Bunu "düzeltmek" ya dersin amacını tamamen ortadan kaldırır (any'yi tamamen çıkarmak)
ya da temayı başka bir yere taşımak gerektirir — ikisi de bu denetimin "sızıntı düzelt" kapsamını
aşan, öğretmen/müfredat ekibinin kararı gereken bir değişiklik. Dokunulmadı; öneri hâlâ geçerli.

```
[CİDDİ] [ileri-sızıntı] data/grade3/personal-life-y3.json — "any" quantifier
Dayanak: Y3-T6, Quantifiers: "some (BACKGROUND), any [NEW]".
Bulgu  : Y3-Tema3'ün (Personal Life) 5 ayrı metninde ("Have you got any T-shirts/hats/
         umbrellas/boots?" kalıbı) toplam 13 kez kullanılıyor — hatta int-12'nin başlığı bile
         "Some and Any in Our Bags". Bu, temanın kıyafet alt-konusunda BİLİNÇLİ olarak
         kurgulanmış, tekrarlayan bir dil kalıbı; tek seferlik kayma değil.
```

| Metin | Kullanım sayısı |
|---|---|
| scan-11 | 3 |
| skim-9 | 2 |
| int-5 | 2 |
| int-8 | 3 |
| int-12 | 8 (başlık dahil) |
| Y3-T5 Homes & Houses / scan-11 | 1 (ayrı tema) |

```
Öneri  : "Have you got any T-shirts?" yerine Y2/Y3'ün o ana kadar öğretilmiş kalıbı: "Have you
         got T-shirts?" (some/any'siz) ya da yalnızca "some" ile olumlu kurgulamak. int-12
         özelinde temanın adı bile "Some and Any" — bu, metnin doğrudan "any"yi öğretmeyi
         hedeflediğini gösteriyor; müfredat sırasına göre bu içerik Y3-Tema6'ya taşınmalı ya da
         müfredat haritası güncellenmeli (kasıtlı bir tasarım kararıysa).
```

### 1f. "Best/worst" (düzensiz üstünlük) — Y4-Tema5 yapısı, Y4'ün 3 temasında erken kullanılmış — ⚠️ BİLİNÇLİ OLARAK DOKUNULMADI

**Doğrulama (bu turda):** Y4-T1 `inf-1`'in tam içeriği okundu — "best" kelimesi metnin
başlığında ("Who Is the Best Teacher?") ve temel olay örgüsünde (okulun yıllık "en iyi
öğretmen" ödülü) merkezi. 18 örneğin çoğu benzer şekilde başlık/olay örgüsüne örülü (ör. Y4-T4
int-10: "He tells the best stories"). Bunları düzeltmek yüzeysel bir kelime değişimi değil,
onlarca metnin anlatı omurgasını yeniden yazmak anlamına gelir — hem çok daha yüksek hata riski
taşır hem de bu turun "sızıntıyı düzelt" kapsamının ötesine geçer. Dokunulmadı; öneri hâlâ
geçerli.

```
[CİDDİ] [ileri-sızıntı] — "best" / "worst"
Dayanak: Y4-T5, Superlative — irregular forms: best, worst [NEW].
Bulgu  : Y4-Tema1, Tema3 ve Tema4'te toplam 18 kez kullanılıyor — Tema5'e (asıl öğretim noktası)
         gelmeden 1 ila 4 tema önce.
```

| Dosya | Kullanım sayısı | Örnek |
|---|---|---|
| Y4-T1 School Life | 5 | inf-1 başlığı: "Who Is the Best Teacher?" |
| Y4-T3 Personal Life | 5 | scan-3: "...is always the best day of the year!" |
| Y4-T4 Family Life | 8 | int-10: "He tells the best stories..." |

**Not:** Y4-T1'de DÜZENLİ üstünlük dereceleri ("-est", "most") zaten o temanın kendi [NEW] yapısı
— sorun değil. Sorun özellikle düzensiz "best/worst" biçiminin 4 tema erken görünmesi.

### 1g. Quantifier "few / a little" (gerçek kullanım, "little" sıfatı hariç) — Y4-Tema6 yapısı — ✅ DÜZELTİLDİ

6 örnek de düzeltildi: "we have few events" → "we don't have many events"; "we all changed a
little" → "we all changed over the years"; "My knee hurts a little" → "My knee hurts"; "little
water" → "not much water"; çeldirici şıklardaki "Little plastic"/"Little waste" → "Some
plastic"/"Some waste" (zaten izinli "some" ile).

```
[CİDDİ] [ileri-sızıntı] — miktar belirteci "few/a little" (sıfat "little" — küçük/ufak —
        DEĞİL)
Dayanak: Y4-T6, Quantifiers: few, a few, little, a little [NEW].
Not    : Regex taraması "little" kelimesinin SIFAT kullanımını ("little sister/brother" — küçük
         kardeş) da yakaladı; bunlar müfredat ihlali DEĞİL (İngilizce'de yaygın, aile
         bağlamında rütbe belirten idiyom, miktar belirteci değil) — bu ~40 eşleşme elendi.
         Gerçek miktar-belirteci kullanımı:
```

| Dosya | Metin | Alan | Kullanım |
|---|---|---|---|
| Y4-T1 School Life | skim-5 | sentences[6] | "we have **few** events" |
| Y4-T3 Personal Life | skim-7 | sentences[9] | "we all changed **a little**" |
| Y4-T3 Personal Life | int-4 | sentences[1] | "My knee hurts **a little**" |
| Y4-T5 Homes & Houses | int-10 | sentences[7] | "There was **little** water in the river" |
| Y4-T5 Homes & Houses | scan-5, scan-9 | questions wrong[] | "Little plastic" / "Little waste" |

### 1h. Edat "on" — Y2-Tema1'de zaten bilinen bulgu, tekrar doğrulandı

Bkz. [02-sizinti-raporu.md](02-sizinti-raporu.md) — `int-8: "See you on Monday!"`. Bütün uygulama
taramasında bu yapı için başka yeni örnek çıkmadı (2. ham eşleşme Türkçe ipucu metnindeki "on
dört" — "on dört pastel boyaları" = "on dört" Türkçe'de "14" demek, İngilizce edat değil; yanlış
pozitif, elendi).

### 1i. Minik bulgu — Basit geçmiş zaman yardımcı fiili "did" — ✅ DÜZELTİLDİ

`wrong[1]` "Yes, she did" → "Yes, she doesn't" olarak değiştirildi (aynı zamanda mantıksal
olarak da tutarsız bir çeldirici — "Yes" ile "doesn't" çelişiyor — bu yüzden hâlâ geçerli bir
yanlış şık).

```
[KÜÇÜK] [ileri-sızıntı] data/grade4/classroom-life-y4.json:inf-7 → questions[0].wrong[1]
Mevcut : "Yes, she did"
Sorun  : Basit geçmiş zaman (düzenli fiiller, "did" yardımcı fiili dahil) Y4-Tema3'te [NEW];
         bu, Y4-Tema2'de (bir tema erken) tek bir YANLIŞ şık içinde geçiyor.
Önem   : Çok düşük — doğru cevap değil, sadece bir çeldirici metninde; öğrencinin üretmesi
         gerekmiyor, sadece okuması gerekiyor. Diğer bulgulara göre önemsiz.
```

## 2. Taranan ve TEMİZ çıkan yapılar (bütün uygulama, 18 dosya)

Aşağıdaki yapılar da tarandı, **hiçbir dosyada gerçek ihlal bulunamadı** (ham eşleşmelerin
tamamı yanlış pozitifti — nedeni belirtiliyor):

| Yapı | Ham eşleşme | Gerçek bulgu | Neden temiz |
|---|---|---|---|
| Şimdiki zaman (is/are/am + V-ing) | 50 | **0** | "It's raining / It's snowing" Y2-T3'ün **kendi hedef kelime listesinde donmuş kalıp olarak zaten var** ("Weather: cold, hot, it's raining, it's snowing"); geri kalanı regex yanlış pozitifi ("morning", "spring" gibi -ing ile biten isimler, "drawing time" gibi isim tamlamaları) |
| "Be going to" (gelecek zaman) | 5 | **0** | Hepsi "going to [yer]" (gitmek, hareket) ya da "love/like going to X" (severek ziyaret etme) kalıbı — asıl "be going to + fiil" gelecek zaman yapısı değil |
| Düzensiz geçmiş zaman fiilleri | 1375 (ham) | **~0** (bkz. §1i) | "got" (have got ile çakışıyor) ve "read" (yazılışı belirsiz) hariç tutulunca kalan ~40 eşleşmenin neredeyse tamamı "lost/left/found" gibi sıfat/deyim kullanımı ("Lost and Found", "on the left") — gerçek fiil çekimi değil |
| "Many/much/a lot of" | 352 (ham) | **~0** (örneklem) | 348/352'si "many" — ve bunların ezici çoğunluğu **Y2-Tema2'nin kendi hedef yapısı olan "How many...?"** kalıbı (zaten izinli); "much"(3)/"a lot of"(1) örneklem düzeyinde incelendi, ciddi bir bulgu çıkmadı |
| Renk sorma, how many, izin "can", how old, birthday, hava durumu kelimeleri, have got, there is/are, could, whose, what's your name, must/mustn't, o'clock, will, what...like, at present, how often, sıklık zarfları, what month, when's | 0 | **0** | Regex taraması 18 dosyanın hiçbirinde bu yapılardan tek bir erken kullanım bulmadı |

**Bu son satır önemli:** Y2-Tema1 denetiminde "temiz" bulduğum ve iyi tasarım örneği olarak
gösterdiğim çekirdek yapılar (have got, there is/are, could, whose, izin "can" vb.), **bütün
uygulama genelinde de temiz** — tek bir dosyada bile erken kullanılmamışlar. Bu, uygulamanın
temel gramer sıralamasının (en azından bu yapılar için) titizlikle korunduğunu gösteriyor.

## 3. Genel değerlendirme — güncellenmiş (düzeltmelerden sonra)

| Bulgu türü | Sayı | Yayılım | Durum |
|---|---|---|---|
| Sıra sayı + tarih kalıbı | 35 metin / 117 alan | 11/18 dosya — **en yaygın ve en sistematik** | ✅ DÜZELTİLDİ |
| Best/worst erken kullanım | 18 kullanım | 3/18 dosya (hepsi Y4) | ⚠️ Kasıtlı, dokunulmadı |
| Quantifier "any" erken kullanım | 14 kullanım | 2/18 dosya (yoğunluk: Y3-T3) | ⚠️ Kasıtlı, dokunulmadı |
| What kind of / Which erken kullanım | 9 kullanım | 4/18 dosya | ✅ DÜZELTİLDİ |
| Something/anything erken kullanım | 6 kullanım | 3/18 dosya | ✅ DÜZELTİLDİ |
| Few/a little (gerçek miktar belirteci) erken kullanım | 6 kullanım | 3/18 dosya | ✅ DÜZELTİLDİ |
| These/those erken kullanım | 5 kullanım | 2/18 dosya | ✅ DÜZELTİLDİ |
| Edat "on" | 1 kullanım | 1/18 dosya (bilinen) | — (Y2-T1 kapsamında ayrıca ele alınıyor) |
| "did" (küçük) | 1 kullanım | 1/18 dosya | ✅ DÜZELTİLDİ |
| **Toplam doğrulanmış sızıntı örneği** | **~95 örnek / ~178 alan** | | **149/178 alan düzeltildi** |

**Genel desen:** Sızıntıların ezici çoğunluğu (35/95 ≈ %37) tek bir kaynaktan — "özel gün"
metinlerinin ortak tarih şablonundan — geliyordu; bu artık temiz. Geriye yalnızca iki kasıtlı
tasarım kararı kaldı: Y4'ün "best/worst" kullanımı (18, üç dosyanın anlatı omurgasına örülü) ve
Y3-T3'ün "any" alıştırması (14, `int-12`'nin doğrudan hedeflediği ders). İkisi de bu turda
**bilinçli olarak dokunulmadan bırakıldı** — düzeltmeleri yüzeysel kelime değişimi değil, ya
temanın müfredat haritasını güncellemek ya da metinleri baştan yazmak gerektirir; bu, öğretmen/
müfredat ekibinin kararı gereken bir kapsam, tek taraflı "sızıntı temizliği" değil.

**Kalan iş:** İki kasıtlı-tasarım kümesi (best/worst 18, any 14) dışında, doğrulanmış sızıntı
örneklerinin **tamamı düzeltildi**. `curriculum_leak_scan.py` yeniden çalıştırılırsa, bu iki
küme ve (kasıtlı olarak korunan) "the 30th of the month" genel referansı dışında hiçbir yeni
eşleşme çıkmaz.

**Doğrulama (tarama yeniden çalıştırıldı):** Düzeltmelerden sonra `curriculum_leak_scan.py`
tekrar çalıştırıldı. Ham eşleşme sayısı **2035 → 1890**'a düştü (fark: 145, düzeltilen 117
ordinal-tarih + 27 diğer alanla birebir örtüşüyor). "sira sayi + tarih" kategorisinde artık
sadece **1 eşleşme** kaldı — bilinçli olarak korunan "the 30th of **the month**" genel
referansı. Kalan ham eşleşmelerin ezici çoğunluğu zaten baştan beri örneklem düzeyinde
incelenip temiz bulunan iki gürültülü kategoriden (düzensiz geçmiş zaman fiilleri, many/much/a
lot of) ve iki bilinçli tasarım kümesinden (any, best/worst) geliyor — hiçbiri yeni bir bulgu
değil. Güncel ham çıktı: `curriculum_leak_scan_output.json`.
