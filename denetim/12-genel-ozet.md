# Genel Özet — Bütün Uygulama Denetimi (2, 3, 4. Sınıf, 18 tema, 761 metin)

Bu, denetimin tamamını bağlayan son özet. Alttaki raporlar üç dalga hâlinde üretildi:
**1. dalga** (00-06) yalnızca Y2-Tema1'i (51 metin) en yüksek derinlikte inceledi — müfredat
haritası, teknik, sızıntı, kapsam, 4 eksenli pedagojik puanlama, canlı UX testi. **2. dalga**
(07-11) aynı kontrolleri **bütün uygulamaya** (18 dosya, 761 metin) genişletti — oynanış testi,
şema taraması, ipucu tam okuması, müfredat-tabanlı gramer sızıntı taraması, kelime kapsamı.
**3. dalga** (14) Y2-T1'e 04'te uygulanan en yüksek derinlikli yöntemi (`sentences`/`questions`/
`translations` alanlarının tamamının satır satır okunması + 4 eksenli pedagojik puanlama) kalan
**710 metnin tamamına** genişletti — bu, denetimin en kapsamlı ve son turu.

## Nereden bakılırsa bakılsın sabit kalan sonuçlar

- **761/761 metin, çökmeden oynanabiliyor.** Konsol hatası: 0. Uygulamanın motor katmanı
  (soru render, doğru/yanlış geri bildirimi, ilerleme, rozet sistemi) tüm uygulama genelinde
  sağlam.
- **Çekirdek gramer sıralaması genel olarak korunuyor.** "Have got", "there is/are", "could",
  "whose", "izin can", "renk sorma", "how many" gibi merkezi yapılar 18 dosyanın hiçbirinde
  erken kullanılmamış.
- **4. Sınıf, içerik kalitesi açısından en disiplinli sınıf.** Kelime kapsamında 6 temanın 6'sı
  da kusursuz; ipucu kalitesinde 6 temanın 5'i sıfır sızıntı.
- **761 metnin tamamı artık en az bir kez satır satır okundu.** 51'i (Y2-T1) en yüksek derinlikte
  (00-06), kalan 710'u da aynı derinlikte (14) — uygulamanın tamamında yalnızca 1 KRİTİK ve 3
  CİDDİ saf içerik/mantık hatası bulundu (bkz. §0 aşağıda).

## Kök neden kümeleri (ciddiyet sırasına göre)

### 0. Doğrudan mantık/doğruluk hataları — 1 KRİTİK + 3 CİDDİ, 2 dosyada

710 metnin satır satır tam okumasında ([14-pedagojik-tum-uygulama.md](14-pedagojik-tum-uygulama.md))
ortaya çıkan, önceki taramaların (07-11, şema/oynanış/sızıntı odaklı) yakalayamayacağı türden
saf **içerik doğruluğu** hataları:

- **[KRİTİK] ✅ DÜZELTİLDİ** Y2-T2 `classroom-life.json:scan-12` — metin Eda'nın dışarı çıkma
  izninin reddedildiğini açıkça söylüyordu ("No, you can't, Eda.") ama sorunun doğru cevabı
  "Outside" (Dışarıda) olarak işaretliydi — metnin kendi anlatısıyla doğrudan çelişen bir
  doğruluk hatası. Soru "What does Eda want to do?" olarak yeniden yazıldı, doğru cevap "Go
  outside" yapıldı — artık metinle tutarlı.
- **[CİDDİ] × 3 ✅ DÜZELTİLDİ** Y2-T3 `personal-life.json:inf-1/9/10` — `inf` grubunun son
  sorusunda İngilizce soru (`q`) ile Türkçe "çevirisi" (`qTr`) tamamen farklı şeyler soruyordu
  (ör. `q`="What has Tom got?" ama `qTr`="Neden Tom değil?"). Üç `qTr` alanı da gerçek soruyla
  eşleşecek şekilde yeniden çevrildi.

Bu 4 bulgu **tüm uygulamada bu türden bulunan tek örnekler** — geri kalan 706 metinde (Y2-T4/T5/T6,
Y3'ün 6/6 teması, Y4'ün 6/6 teması) satır satır okumada hiçbir yeni içerik/mantık hatası
bulunmadı. Bu, uygulamanın dil/anlatı iskeletinin genel olarak çok sağlam olduğunu, ama bu 4
noktanın **doğrudan görünür, öğretmen/veli gözüyle en çabuk fark edilecek** hatalar olduğunu
gösteriyor.

### 1. İpucu cevap sızıntısı — 37 doğrulanmış örnek, 18 dosyanın 9'unda — ✅ DÜZELTİLDİ

Aşağıda belgelenen tüm örneklerin `hint` alanları, cevabı doğrudan veya neredeyse birebir
tekrarlamayan; bunun yerine ya saf eleme ("X değil, Y değil") ya da metne geri yönlendiren
("cümleye bak", "hatırla") bir versiyonla değiştirildi. Toplam 40 soru düzeltildi (bazı metinlerde
aynı sızıntı birden fazla soruda tekrarlandığı için 37 "bulgu"dan fazla soru etkilendi).
`checker.py` düzeltmelerden sonra da aynı 403 şema bulgusunu (ipucu içeriğiyle ilgisiz, ayrı bir
kategori) veriyor — hiçbir şey bozulmadı. Aşağıdaki tablo ve örnekler artık tarihsel kayıt.

Tüm `inf` (Çıkarım) grubu ipuçları (18 dosya × ortalama ~29 ipucu ≈ 525 ipucu) tek tek okundu.
37 tanesi, cevabı doğrudan ya da neredeyse birebir veriyor. Dağılım son derece eşitsiz:

| Tema | Sayı |
|---|---|
| Y2-T4 Family Life | ~10 |
| Y2-T3 Personal Life | ~7 |
| Y2-T1 School Life | 6 |
| Y4-T6 Life in the City | 5 |
| Y3-T1 School Life | 4 |
| Y3-T4 Family Life, Y3-T6 Life in the City | 2'şer |
| Y4-T1 School Life | 1 |
| Kalan 9 tema | 0 |

Bkz. [04-pedagojik-rapor.md](04-pedagojik-rapor.md) §2a ve [10-ipucu-tam-tarama.md](10-ipucu-tam-tarama.md).
**Bu, kurul önünde çıkma ihtimali en yüksek tek bulgu kümesi** — çünkü "Çıkarım" becerisinin
tanımıyla doğrudan çelişiyor.

### 2. Sıra sayı + tarih kalıbı — 35 metin, 11/18 dosya — ✅ DÜZELTİLDİ

"The 23rd of April" gibi ifadeler Y4-Tema2/3 yapısı ama Y2'nin 6 temasının 6'sında ve Y3'ün 6
temasından 5'inde kullanılıyordu. Tek bir şablon kaynaklıydı, tek noktadan düzeltildi: 35
metindeki 117 alanın tamamı "N Month" biçimine (ör. "23 April") çevrildi. Tek istisna —
`school-life-y3.json:inf-9`'daki gerçek bir ay adı içermeyen "the 30th of **the month**" genel
referansı — bilinçli olarak korundu. Bkz.
[08-mufredat-sizinti-tum-uygulama.md](08-mufredat-sizinti-tum-uygulama.md) §1a.

### 3. `qTr` alanı eksikliği — 403 soru, 2 tam dosya + 3 soru — ✅ 400/403 DÜZELTİLDİ

Y4-Tema2 (Classroom Life) ve Y4-Tema5 (Homes & Houses) dosyalarının **tamamında** (400 soru),
soru cümlesinin Türkçe çevirisi (`qTr`) hiç girilmemişti. Uygulama sessizce ipucu metnine
düşüyordu (çökmüyor, ama "Türkçe" butonu yanlış içerik gösteriyordu). **Bu 400 soruya gerçek,
soruya karşılık gelen Türkçe çeviri elle yazıldı** — `checker.py` artık bu iki dosya için 0
bulgu veriyor. Geriye yalnızca Y4-T6 Life in the City'deki 3 izole soru (skim-5/9/10'un ilk
sorusu) kaldı — sistematik değil, düzeltilmedi. Bkz. [09-teknik-tum-uygulama.md](09-teknik-tum-uygulama.md).

### 4. Cast/avatar-konuşmacı tutarsızlığı — 18 dosyanın 4'ünde — ✅ DÜZELTİLDİ

Konuşan bir karakterin `cast` dizisinde avatarı yoktu. En çarpıcı örnek: 4. Sınıf Life in the
City'de "Leyla" konuşuyor ama avatarı yoktu — 07 raporunun ilk taramasında 6 metin bulunmuştu,
[14-pedagojik-tum-uygulama.md](14-pedagojik-tum-uygulama.md)'nin tam satır satır okuması bunu
**7 metne** düzeltti (scan-6/10, skim-4/8/10, int-10, inf-9 — hepsi düzeltildi). Ayrıca 07
raporunun tam listesindeki kalan adaylar tek tek doğrulandı: **7 tanesi gerçek bulguydu**
(Y2-T1 `int-9`/`int-11`, Y3-T1 `school-life-y3.json:skim-6`/`inf-1`, Y3-T3
`personal-life-y3.json:skim-8`/`inf-6`, Y4-T6 `scan-7`) ve düzeltildi; **6 tanesi yanlış
pozitifti** (3× "Ms. Hart" farklı biçimde etiketlenmesi şüphesi — okumada tamamen tutarlı
çıktı; "Visitor" ve iki "Everyone" — kasıtlı isimsiz/kolektif anlatıcı; "Postcard" — cansız
nesne anlatıcısı) ve dokunulmadı, çünkü gerçekten eksik bir karakter yoktu. Toplam: 18 dosyanın
tamamında artık konuşan her karakterin `cast` dizisinde bir karşılığı var. Bkz.
[07-tum-uygulama-oynanis-raporu.md](07-tum-uygulama-oynanis-raporu.md) §Sonuç 2.

### 4a. Karakter emoji tutarsızlığı — 1 karakter, 3 dosyada (küçük/stil) — ✅ DÜZELTİLDİ

4. Sınıf'ta müzik öğretmeni Ms. Çelik, üç ayrı dosyada üç farklı emoji ile temsil ediliyordu:
Y4-T1'de 👩‍🎤 (müzik öğretmeni rolüyle uyumlu), Y4-T2'de 👩‍💼 ve Y4-T3'te 👩‍🎨. İçerik/mantık
hatası değildi, yalnızca görsel kimlik tutarsızlığıydı. Üç dosya da 👩‍🎤 üzerinde birleştirildi.
Bkz. [14-pedagojik-tum-uygulama.md](14-pedagojik-tum-uygulama.md) Y4-T2/T3 notları.

### 5. Best/worst ve "any" — Y4 ve Y3-Tema3'te yoğunlaşan ileri-sızıntı — ⚠️ İncelendi, bilinçli olarak dokunulmadı

Düzensiz üstünlük ("best/worst") Y4'ün 3 temasında 18 kez, "any" nicelik belirteci Y3-Tema3'te
14 kez erken kullanılıyor. Bu turda ikisi de doğrulandı: `int-12`'nin (Y3-T3) tam içeriği
okundu — metin, "Have you got any X? Yes, I've got some X." kalıbını 4 eşya üzerinden sistemli
tekrarlayan, doğrudan "some vs any" öğretmek için tasarlanmış bir alıştırma (başlık: "Some and
Any in Our Bags"). Y4-T1 `inf-1`'in tam içeriği de okundu — "best" kelimesi başlıkta ve olay
örgüsünün merkezinde (okulun yıllık "en iyi öğretmen" ödülü). İkisi de **kasıtlı tasarım
kararı**, tesadüfi sızıntı değil — düzeltmek yüzeysel kelime değişimi değil, ya müfredat
haritasını güncellemeyi ya da metinleri baştan yazmayı gerektirir. Bu turda **bilinçli olarak
dokunulmadı**; bu, denetimde geriye kalan en büyük açık karar kalemidir. Bkz.
[08-mufredat-sizinti-tum-uygulama.md](08-mufredat-sizinti-tum-uygulama.md) §1e-1f.

### 6. Y3-Tema4 (Family Life) kelime kapsamı boşluğu — 8 hedef kelime hiç yok

"Grandson, granddaughter, men, woman, women, put on, study, do homework" — bu temanın kendi
hedef kelime listesinden 8 öğe 43 metnin hiçbirinde geçmiyor. İlginç biçimde bu tema aynı
zamanda ileri-sızıntısı EN AZ olan dosyalardan biri (yalnızca 4 ham eşleşme) — yani "fazla ileri
gitmiyor" ama "yeterince kapsamıyor" da. Bkz. [11-kapsam-tum-uygulama.md](11-kapsam-tum-uygulama.md).

### 7. Küçük/dağınık bulgular — ✅ İleri-sızıntı kısmı DÜZELTİLDİ, kapsam boşlukları açık

"What kind of/which" (9, 4 dosya), "something/anything" (6, 3 dosya), "these/those" (5, 2
dosya), "few/a little" (6, 3 dosya) ve "did" (1) — bu 27 ileri-sızıntı örneğinin **tamamı bu
turda düzeltildi** (bkz. §1b-1d, 1g, 1i yukarıda). "Headmistress" hiç yok + "kid" 1 kez (Y2-T1)
ve birkaç ince kapsamlı kelime (Y2-T2, Y3-T1, Y3-T2) ise kapsam **boşluğu** (eksik kelime, içerik
eklemesi gerektirir) — ileri-sızıntı (fazladan yazılmış kelime, silinmesi/değiştirilmesi
yeterli) ile farklı bir düzeltme kategorisi; bu turda dokunulmadı. Tümü ayrı ayrı raporlarda
listelendi.

## Kurul kararı — güncellenmiş (710 metnin tam okuması + düzeltmelerden sonra)

**Bu tema/uygulama bugün jüri önüne çıksa hangi bulgu yüzünden eleme yer?**

710 metnin tam satır satır okuması ([14-pedagojik-tum-uygulama.md](14-pedagojik-tum-uygulama.md))
üç görünür/ağır bulgu kümesi ortaya çıkardı — **üçü de artık düzeltildi**:

1. Y2-T2 `scan-12`'deki **KRİTİK doğruluk hatası** — metin Eda'nın izninin reddedildiğini açıkça
   söylerken sistem "Dışarıda"yı doğru cevap sayıyordu. **✅ Düzeltildi.**
2. **İpucu cevap sızıntısı** (37 bulgu / 40 soru, 9 farklı tema) — "Çıkarım" becerisinin amacıyla
   doğrudan çelişen, tek temaya özgü olmayan sistematik bir kalite sorunuydu. **✅ Düzeltildi** —
   tüm ipuçları artık eleme ("X değil, Y değil") veya metne yönlendirme ("cümleye bak", "hatırla")
   tarzında, cevabı vermiyor.
3. Y2-T3'ün 3 metninde `q`/`qTr` uyumsuzluğu ve 18 dosyanın tamamında cast eksiklikleri
   (20 metin, 4 dosya). **✅ Düzeltildi.**
4. **`qTr` alanının 2 tam temada toptan eksik olması** (400 soru, Y4-T2 Classroom Life + Y4-T5
   Homes & Houses) + Y4-T6'daki 3 izole `qTr` eksikliği. **✅ Düzeltildi** — 403 sorunun tamamına
   gerçek, soruya karşılık gelen Türkçe çeviri elle yazıldı; `checker.py` artık **761 metnin
   tamamında 0 bulgu** veriyor.
5. **Sıra sayı + tarih kalıbı** (35 metin, 117 alan, 11/18 dosya) — tek bir şablondan kaynaklanan
   en yaygın ileri-sızıntı. **✅ Düzeltildi** — "the 23rd of April" → "23 April" biçimine
   çevrildi.
6. **Küçük/dağınık ileri-sızıntılar** — "what kind of/which" (9), "something/anything" (6),
   "these/those" (5), "few/a little" (6), "did" (1) = 27 örnek. **✅ Düzeltildi.**

**Kasıtlı olarak dokunulmayan tek küme:** "Best/worst" (18 kullanım, Y4'ün 3 dosyası) ve "any"
(14 kullanım, Y3-T3) — ikisi de doğrulandı ve gerçekten metnin/başlığın anlatı omurgasına örülü
kasıtlı tasarım kararları olduğu tek tek okunarak teyit edildi (bkz. §5 yukarıda). Bunları
düzeltmek yüzeysel kelime değişimi değil, ya müfredat haritasını güncellemeyi ya da metinleri
baştan yazmayı gerektirir — bu, tek taraflı bir "sızıntı temizliği" turunun kapsamını aşan,
öğretmen/müfredat ekibinin onayını gerektiren bir karar. Y3-T4'ün 8 kelimelik kapsam boşluğu da
benzer bir nedenle dokunulmadı: bu bir *ekleme* işi (yeni cümle/içerik üretmek), var olan bir
hatayı düzeltmek değil.

**Olumlu taraf:** 710 metnin tam okumasından sonra sorunların ezici çoğunluğu düzeltildi. 761
metnin dil/gramer iskeleti (yıldız kapsamı, JSON bütünlüğü, uygulama motoru, pedagojik yapı)
genel olarak çok sağlam; 706 metinde (Y2-T4/T5/T6, Y3'ün 6/6'sı, Y4'ün 6/6'sı) satır satır
okumada hiç yeni içerik hatası çıkmadı.

- ~~1 doğru cevap düzeltmesi~~ **✅ DÜZELTİLDİ**
- ~~3 qTr çeviri düzeltmesi~~ **✅ DÜZELTİLDİ**
- ~~20 cast dizisi (18 dosyanın tamamı)~~ **✅ DÜZELTİLDİ**
- ~~1 emoji tutarsızlığı~~ **✅ DÜZELTİLDİ**
- ~~~37 ipucu cümlesi (ipucu sızıntısı, 40 soru)~~ **✅ DÜZELTİLDİ**
- ~~403 qTr alanı (Y4-T2/T5/T6)~~ **✅ DÜZELTİLDİ**
- ~~35 tarih ifadesi / 117 alan (tek şablon)~~ **✅ DÜZELTİLDİ**
- ~~27 dağınık ileri-sızıntı (what kind of, something, these/those, few, did)~~ **✅ DÜZELTİLDİ**
- 32 kasıtlı tasarım kararı (best/worst 18 + any 14) — **bilinçli olarak dokunulmadı**, müfredat
  ekibinin kararı gerekiyor
- 8 kelimelik Y3-T4 kapsam boşluğu — **içerik ekleme** işi, bu turun kapsamı dışında

**Kalan işin durumu:** `checker.py` artık **761 metnin tamamında 0 bulgu** veriyor (403'ten
düştü). Denetimde saptanan tüm somut hatalar ve mekanik/format sızıntıları düzeltildi. Geriye
yalnızca iki kategori kaldı, ikisi de bilinçli olarak: (1) müfredat sırasını bilerek çiğneyen
2 tasarım kararı (best/worst, any) ve (2) 1 kelime kapsamı boşluğu — ikisi de "hata düzeltme"
değil, ayrı bir karar/içerik-üretim süreci gerektiriyor.

## Tüm rapor dosyaları

| # | Dosya | Kapsam |
|---|---|---|
| 00 | mufredat-haritasi.md | Y2-T1 müfredat haritası |
| 01 | teknik-rapor.md | Y2-T1 şema kontrolü |
| 02 | sizinti-raporu.md | Y2-T1 ileri-sızıntı |
| 03 | kapsam-raporu.md | Y2-T1 kelime/yapı kapsamı |
| 04 | pedagojik-rapor.md | Y2-T1, 51 metin, 4 eksen |
| 05 | kullanici-deneyimi.md | Y2-T1 canlı UX testi |
| 06 | ozet.md | Y2-T1 kurul özeti |
| 07 | tum-uygulama-oynanis-raporu.md | 18 dosya, oynanış + cast + ipucu (ilk tur) |
| 08 | mufredat-sizinti-tum-uygulama.md | 18 dosya, müfredat gramer sızıntısı |
| 09 | teknik-tum-uygulama.md | 18 dosya, şema kontrolü |
| 10 | ipucu-tam-tarama.md | 18 dosya, `inf` ipucu tam okuması |
| 11 | kapsam-tum-uygulama.md | 17 dosya, kelime kapsamı |
| 12 | genel-ozet.md | Bu dosya — hepsini bağlayan özet |
| 14 | pedagojik-tum-uygulama.md | 17 dosya (710 metin), tam satır satır okuma + 4 eksen |

## Betikler

`checker.py` / `checker_all.py` (şema), `curriculum_leak_scan.py` (gramer sızıntısı),
`coverage_scan.py` (kelime kapsamı) — hepsi salt-okunur, `denetim/` klasöründe.
