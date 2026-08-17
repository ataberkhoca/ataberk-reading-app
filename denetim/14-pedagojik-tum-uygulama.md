# Pedagojik Tam Okuma — Bütün Uygulama (710 metin, 17 dosya)

Bu rapor, [04-pedagojik-rapor.md](04-pedagojik-rapor.md)'de Y2-Tema1'in 51 metnine uygulanan
aynı derinlikte (her metnin `sentences`, `questions`, `translations` alanlarının tamamını okuyup
4 eksende değerlendirme + gerçek içerik hatalarını arama) kalan 17 dosyaya genişletiliyor.
**Bu çok büyük bir iş olduğu için rapor parça parça dolduruluyor** — tamamlanan dosyalar
aşağıda, devam eden çalışma [12-genel-ozet.md](12-genel-ozet.md)'de izlenebilir.

## Yöntem notu

Önceki turlarda (07-11) zaten doğrulanmış bulgular (cast eksikliği, ipucu sızıntısı, müfredat
gramer sızıntısı, kelime kapsamı) burada tekrar edilmiyor — yalnızca bu turda satır satır
okumayla ortaya çıkan **yeni** bulgular (özellikle içerik/mantık hataları) ve 4 eksenli genel
değerlendirme raporlanıyor.

---

## Y2-T2 Classroom Life (45 metin) — TAMAMLANDI

### Yeni bulgu — içerik/mantık hatası

**✅ DÜZELTİLDİ** — soru "What does Eda want to do?" olarak yeniden yazıldı, doğru cevap "Go
outside" yapıldı (bkz. `denetim/12-genel-ozet.md` "Uygulanan Düzeltmeler").

```
[KRİTİK] [pedagojik] data/grade2/classroom-life.json:scan-12 → questions[2]
Mevcut : sentences[3]="Eda: Miss Oli, can I go outside?" / sentences[4]="Miss Oli: No, you
         can't, Eda." — soru: "Where is Eda?" → correct: "Outside"
Sorun  : Metin, Eda'nın dışarı çıkma İZNİNİN REDDEDİLDİĞİNİ açıkça söylüyor ("No, you can't").
         Yani Eda dışarıda DEĞİL — sınıfta kalmış olmalı. Ama sorunun "doğru" cevabı "Outside"
         (Dışarıda) olarak işaretlenmiş — bu, metnin kendi anlatısıyla doğrudan çelişen bir
         mantık hatası. Bir öğrenci metni doğru anlayıp "In the classroom" gibi bir şık
         seçseydi (böyle bir şık olsaydı), sistem onu YANLIŞ sayardı.
Öneri  : `correct` alanını "In the classroom" (ya da metne uygun bir başka konum) olarak
         düzelt; `wrong` listesine "Outside"u ekle. Ya da soruyu "What does she want to do?"
         gibi isteği soran bir soruya çevirip "Go outside" olarak cevaplat.
Dayanak: Bu, sızıntı ya da kapsam sorunu değil — doğrudan bir **doğruluk hatası**. Kurul
         karşısında en çabuk fark edilecek türden bulgu (bir öğretmen metni okuyup "Hayır, cevap
         yanlış!" diyebilir).
```

### 4 eksenli genel değerlendirme

| Eksen | Puan (1-5) | Not |
|---|---|---|
| Yapı taşıyıcılığı | 5 | Renk sorma + "how many" + izin "can" (temanın 3 hedef yapısı) doğal diyaloglarla, kural anlatmadan işleniyor — örnek ders kitabı kalitesinde. |
| Geri dönüşüm zenginliği | 4 | Y2-T1'in "Who is X/Where is X/What day" kalıpları düzenli tekrarlanıyor (scan-10/skim-10/int-10 milli gün metinleri, scan-7-9/int-1-11 selamlaşma+izin karışımı). |
| Sızıntı temizliği | 4 | Ordinal-tarih kalıbı 4 metinde tekrarlanıyor (bkz. 08-mufredat-sizinti-tum-uygulama.md) — bu eksende bu yüzden tam puan değil. |
| Köprü farkındalığı | 4 | Renk+sayı+izin, Y2-T3/T6'ya (giysi renkleri, sayılar, izin isteme genişlemesi) iyi zemin hazırlıyor. |

### Diğer gözlemler

- **Karakter tutarlılığı:** Sorun yok — 45 metnin cast listeleri konuşan karakterlerle tutarlı
  (07 raporunda da bu dosya için 0 cast bulgusu çıkmıştı, bu tam okuma onu doğruluyor).
- **"Video mu fotoğraf mı?":** Karışık. Sayma/renk soran metinlerin çoğu (scan-1..6, skim-1..6,
  int-3/7) statik envanter tarzı ("Kaç tane X? Y tane!") — bulgu değil ama STİL notu:
  bu 15+ metin neredeyse aynı kalıbı (Miss Oli sorar, öğrenci sayı/renk söyler, "Aferin")
  tekrarlıyor. İzin isteme metinleri (scan-9/12, int-2/5/11) ve milli gün metinleri (scan-10,
  skim-10, int-10, inf-10) daha "video" — gerçek bir istek/red/onay döngüsü var.
- **Çeviri/dil doğallığı:** Sorun yok, 45 metin boyunca tutarlı ve doğal.
- **Şık makuliyeti:** Yanlış şıklar hep aynı kategoriden (renk sorusuna renk, sayı sorusuna
  sayı) — makul, gülünç derecede elenebilir şık yok.

---

---

## Y2-T3 Personal Life (43 metin) — TAMAMLANDI

### Yeni bulgu deseni — `q` (İngilizce soru) ile `qTr` (Türkçe çevirisi) uyuşmuyor — ✅ DÜZELTİLDİ

Üç `qTr` alanı da gerçek İngilizce soruyla eşleşecek şekilde yeniden çevrildi. Bu dosyada 3 ayrı
metinde aynı garip desen bulunmuştu: `inf` grubunun SON sorusunda İngilizce soru
metni bir şey soruyor, ama Türkçe "çevirisi" (`qTr`) TAMAMEN FARKLI bir soru soruyor —
muhtemelen önceki bir taslaktan kalma, güncellenmemiş bir alan.

```
[CİDDİ] [şema/teknik] data/grade2/personal-life.json:inf-1 → questions[4]
Mevcut : q="What has Tom got?" | qTr="Neden Tom değil?" ("Why not Tom?")
Sorun  : Türkçe metin, İngilizce soruyla hiç örtüşmüyor — biri "Tom'da ne var?" soruyor,
         diğeri "Neden Tom değil?" diyor. Öğrenci "Türkçe" butonuna basarsa soruyla alakasız
         bir çeviri görür.
```
```
[CİDDİ] [şema/teknik] data/grade2/personal-life.json:inf-9 → questions[4]
Mevcut : q="What has Eda got?" | qTr="Neden Eda değil?" ("Why not Eda?")
Sorun  : Aynı desen.
```
```
[CİDDİ] [şema/teknik] data/grade2/personal-life.json:inf-10 → questions[4]
Mevcut : q="What day is it today?" | qTr="Neden Çocuk Bayramı değil?" ("Why not Children's
         Day?") | correct="It is a religious day"
Sorun  : Üçlü bir uyumsuzluk — İngilizce soru "Bugün hangi gün?" diyor, Türkçe çevirisi "Neden
         Çocuk Bayramı değil?" diyor, doğru cevap ise "Bu dini bir gün" (ikisinden de farklı bir
         mantık). Muhtemelen bu soru başta "Why is it not Children's Day?" olarak tasarlanmış,
         sonradan `q` alanı değiştirilmiş ama `qTr` ve `correct` eski hâlde kalmış.
Öneri  : Her üç metinde `qTr` alanını gerçek İngilizce soruya göre yeniden çevirmek (ör. "Tom'da
         ne var?", "Eda'da ne var?", "Bugün günlerden ne?").
Dayanak: Bu üçü tesadüf olamayacak kadar aynı kalıpta — muhtemelen bu dosyanın `inf` grubu bir
         şablon güncellemesinden geçti ve son soru her metinde gözden kaçtı.
```

### 4 eksenli genel değerlendirme

| Eksen | Puan | Not |
|---|---|---|
| Yapı taşıyıcılığı | 5 | Vücut parçaları + giysi renkleri + yaş/doğum günü + hava durumu (temanın 4 ana hedefi) doğal diyaloglarla işleniyor. |
| Geri dönüşüm zenginliği | 4 | Y2-T1'in "What day is it" kalıbı (scan-5/6, skim-3/8, int-3/9) ve Y2-T2'nin renk sorma kalıbı (giysi renklerine taşınmış) iyi kullanılmış. |
| Sızıntı temizliği | 3 | "What kind of day" (Y4-T1 yapısı) 5 kez tekrarlanıyor (bkz. 08 raporu) — bu eksende düşük puan. |
| Köprü farkındalığı | 4 | Yaş/doğum günü + hava durumu, Y2-T4/T5'e (aile, ev) iyi zemin hazırlıyor. |

### Diğer gözlemler

- **Karakter tutarlılığı:** Sorun yok.
- **"Video mu fotoğraf mı?":** Doğum günü metinleri (scan-5/6, skim-3/8, int-3/9) ve "kısa/uzun
  arkadaş" karşılaştırma metinleri (scan-9, skim-6, int-6) gerçek bir sosyal etkileşim içeriyor —
  video. Hava durumu/giysi metinlerinin çoğu (scan-3/4/7/8, skim-4/5/9, int-2/4/5) envanter
  tarzı — fotoğraf, ama tema doğası gereği (kıyafet açıklaması) bu makul.
- **Çeviri/dil doğallığı:** Yukarıdaki 3 bulgu dışında sorun yok.

---

---

## Y2-T4 Family Life (40 metin) — TAMAMLANDI

### Yeni bulgu

Bu dosyada **yeni bir içerik/mantık hatası bulunamadı** — 40 metnin tamamı satır satır okundu,
`q`/`qTr` uyumu, `correct`/hikâye tutarlılığı sorunsuzdu.

### 4 eksenli genel değerlendirme

| Eksen | Puan | Not |
|---|---|---|
| Yapı taşıyıcılığı | 5 | "Who is X? Has X got blue eyes?" + betimleme sıfatları doğal, kural anlatmadan işleniyor. |
| Geri dönüşüm zenginliği | 4 | Y2-T3'ün göz/saç rengi + boy sıfatları (tall/short/beautiful) doğrudan aile üyelerine taşınmış. |
| Sızıntı temizliği | 5 | Bu dosyada 08 raporunda hiçbir ileri-sızıntı bulunmadı — temiz. |
| Köprü farkındalığı | 4 | Aile üyesi betimlemesi Y2-T5'in "kim nerede" ve Y3-T4'ün genişletilmiş aile kelime dağarcığına iyi zemin. |

### Diğer gözlemler

- **Karakter tutarlılığı:** Sorun yok — tekrar eden aile üyeleri (Ela, Mia, Ayşe, Ali, Deniz)
  isim/yaş/özellik bakımından metinler arası tutarlı (ör. Ela hep 4 yaşında ve sarı saçlı,
  Ayşe hep yeşil gözlü büyükanne).
- **İpucu kalitesi:** 10-ipucu-tam-tarama.md'de zaten bulunan 10 sızıntı (yaş/göz rengi doğrudan
  ipucuda verilmesi) bu okumada da doğrulandı, tekrar edilmiyor.
- **"Video mu fotoğraf mı?":** Neredeyse tamamı "bu kişiyi tanıt" formatında statik betimleme —
  fotoğraf ağırlıklı, ama tema doğası (aile tanıtımı) için makul; gerçek bir olay örgüsü yok.

---

## Y2-T5 Homes & Houses (43 metin) — TAMAMLANDI

### Yeni bulgu

Bu dosyada **yeni bir içerik/mantık hatası bulunamadı** — 43 metnin (scan 11, skim 11, int 11,
inf 10) tamamı satır satır okundu, `q`/`qTr` uyumu, `correct`/hikâye tutarlılığı ve `inf`
grubunun ipucu kalitesi sorunsuzdu. `inf` grubu boyunca hep güvenli "değil" (eleme) tarzı ipuçları
kullanılmış (ör. inf-9: "Bu bir kedi değil. Bu bir köpek değil." → cevap "A bird") — doğrudan
cevabı veren tek bir ipucu yok.

### 4 eksenli genel değerlendirme

| Eksen | Puan | Not |
|---|---|---|
| Yapı taşıyıcılığı | 5 | "There is/are" + oda/mobilya/evcil hayvan kelime dağarcığı + konum edatları ("on", "in") doğal diyaloglarla, kural anlatmadan işleniyor. |
| Geri dönüşüm zenginliği | 5 | Y2-T1'in "What day is it" (int-10/inf-10 millî+dinî gün metinleri), Y2-T2'nin renk sorma kalıbı (evcil hayvan/mobilya rengi) ve Y2-T4'ün aile kelime dağarcığı (int-9, inf-8) doğrudan bu temaya taşınmış — 5 farklı evcil hayvan (köpek Maxi, kedi Misho, kuş Cici, tavşan Pamuk, balık Bubble) ve 4 oda üzerinden sistemli tekrar var. |
| Sızıntı temizliği | 4 | Ordinal-tarih kalıbı (int-10 "The 29th of October") burada da tekrarlanıyor (bkz. 08 raporu) — bu eksende bu yüzden tam puan değil. |
| Köprü farkındalığı | 4 | Oda/mobilya konumu + evcil hayvan betimlemesi, Y2-T6'nın "nerede/nasıl gidilir" şehir teması ve Y3-T5'in genişletilmiş ev kelime dağarcığına iyi zemin. |

### Diğer gözlemler

- **Karakter tutarlılığı:** Sorun yok — 5 evcil hayvan (Maxi/Misho/Cici/Pamuk/Bubble) ve
  sahipleri (Eda/Can/Lila/Tom) metinler arası tutarlı; cast listeleri konuşan karakterlerle
  eşleşiyor.
- **"Video mu fotoğraf mı?":** Karışık. Ev turu ve evcil hayvan betimleme metinlerinin çoğu
  (scan-1..8, skim-1..7, int-1..9) statik envanter tarzı ("X odasında ne var? Y var!") —
  bulgu değil ama STİL notu: bu desen dosya boyunca sık tekrarlanıyor. Millî/dinî gün metinleri
  (scan-10, skim-10, int-10, inf-10) ve "kimin evcil hayvanı" bulmaca metni (inf-5) daha "video" —
  gerçek bir sosyal bağlam/bulmaca var.
- **Çeviri/dil doğallığı:** Sorun yok, 43 metin boyunca tutarlı ve doğal.
- **Şık makuliyeti:** Yanlış şıklar hep aynı kategoriden (oda sorusuna oda, hayvan sorusuna
  hayvan) — makul, gülünç derecede elenebilir şık yok.

---

## Y2-T6 Life in the City & the World (43 metin) — TAMAMLANDI

### Yeni bulgu

Bu dosyada **yeni bir içerik/mantık hatası bulunamadı** — 43 metnin (scan 11, skim 11, int 11,
inf 10) tamamı satır satır okundu. `inf` grubunun ipucu kalitesi de sorunsuz: tüm ipuçları
"değil" (eleme, ör. "Yeşil değil. Sarı değil.") veya "dikkat et" (yönlendirme, ör. "Eda'nın
sözlerine dikkat et.") tarzında — hiçbiri cevabı doğrudan söylemiyor.

**Not (müfredat doğrulaması):** Dosya adı "life-in-city" olsa da, içerik neredeyse tamamen
yiyecek/içecek/öğün kelime dağarcığı üzerine kurulu (meyve, sebze, içecek, "Do you like...?",
"I have got some...", izin isteme "Can I have...?"). Bu, 03-kapsam-raporu.md'de kullanılan
müfredat VOCAB listesiyle karşılaştırıldı — Y2-Tema6'nın resmî adı "Life in the City & the
World" olup, MEB müfredatında bu temada hedeflenen kelimeler tam olarak yiyecek/içecek/sebze/
meyve kategorisinde (bkz. coverage_scan.py). Yani bu bir **hata değil** — temanın adı
"şehir hayatı" çağrıştırsa da müfredatın kendisi bu temayı beslenme/yemek kültürü etrafında
tanımlıyor. Yalnızca STİL notu: ebeveyn/öğretmen gözünden dosya adı ile içerik arasındaki bu
isim uyumsuzluğu ilk bakışta kafa karıştırıcı olabilir.

### 4 eksenli genel değerlendirme

| Eksen | Puan | Not |
|---|---|---|
| Yapı taşıyıcılığı | 5 | "Do you like...? Yes/No, I do/don't" + "I have got some..." + izin isteme "Can I have some...?" doğal diyaloglarla, kural anlatmadan işleniyor. |
| Geri dönüşüm zenginliği | 5 | Y2-T5'in izin kalıbı ("Can I...? Yes, you can!") ve Y2-T1'in millî/dinî gün kalıbı (int-10/inf-10 23 Nisan, skim-10 Ramazan Bayramı) doğrudan bu temaya taşınmış; "yummy" sıfatı üzerinden sistemli beğeni/beğenmeme karşılaştırması (int-1/2/5, inf-5) iyi bir tekrar örüntüsü oluşturuyor. |
| Sızıntı temizliği | 5 | Bu dosyada 08 raporunda ileri-sızıntı bulunmadı — temiz. |
| Köprü farkındalığı | 4 | Yiyecek/içecek kelime dağarcığı + izin kalıbı, Y3-T1'in genişletilmiş okul/sosyal kelime dağarcığına ve ileriki temalardaki "would like" gibi yapılara iyi zemin. |

### Diğer gözlemler

- **Karakter tutarlılığı:** Sorun yok — Eda/Tom/Can/Lila'nın besin tercihleri (ör. Can'ın
  brokoliyi sevmemesi hem scan-4 hem int-2'de tutarlı) metinler arası korunuyor.
- **"Video mu fotoğraf mı?":** Çoğunlukla "video" — bu dosyanın en güçlü yanı. Neredeyse her
  metin gerçek bir karşılıklı konuşma/istek-onay döngüsü içeriyor (beğeni sorma, izin isteme),
  Y2-T2/T4/T5'teki envanter-tarzı metinlerden daha az statik.
- **Çeviri/dil doğallığı:** Sorun yok, 43 metin boyunca tutarlı ve doğal.
- **Şık makuliyeti:** Yanlış şıklar hep aynı kategoriden (yiyecek sorusuna yiyecek, içecek
  sorusuna içecek) — makul, gülünç derecede elenebilir şık yok.

---

## Y2 ÖZETİ — 6/6 tema tamamlandı

Y2'nin 6 temasının tamamı (251 metin: T1'in 51'i [04-pedagojik-rapor.md'de], T2-T6'nın 200'ü
[bu raporda]) satır satır okunarak 4 eksende değerlendirildi. Bu turda **3 yeni bulgu** ortaya
çıktı (T2'de 1 KRİTİK mantık hatası, T3'te 3 CİDDİ q/qTr uyumsuzluğu) — T1, T4, T5, T6'da yeni
bulgu yok. Şimdi Y3'ün 6 temasına geçiliyor.

---

## Y3-T1 School Life (40 metin) — TAMAMLANDI

### Yeni bulgu

Bu dosyada **yeni bir içerik/mantık hatası bulunamadı** — 40 metnin (scan 10, skim 10, int 10,
inf 10) tamamı satır satır okundu. `inf` grubunun ipucu kalitesi sorunsuz: ipuçları hep "değil"
(eleme) veya genel-bilgi çıkarımı tarzında (ör. inf-2: "Resim odasında boya var." → cevap
"There is no paint" — cevabı değil, çıkarım yapmak için gereken arka plan bilgisini veriyor).

### 4 eksenli genel değerlendirme

| Eksen | Puan | Not |
|---|---|---|
| Yapı taşıyıcılığı | 5 | Okul personeli/mekânları + "must/mustn't" kuralları + 12 ay/4 mevsim + selamlaşma ifadeleri (temanın 4 hedefi) doğal diyaloglarla, kural anlatmadan işleniyor. |
| Geri dönüşüm zenginliği | 5 | Y2'nin "Who is X? Where is X?" kalıpları ve doğum günü/millî-dinî gün kalıbı (int-6, inf-5/6 doğum günü; scan-9/10, int-9/10, inf-9/10 millî/dinî günler) sistemli şekilde bu temaya taşınmış — 5 farklı millî/dinî gün (23 Nisan, 10 Kasım, 19 Mayıs, 30 Ağustos, Kurban Bayramı) tek dosyada işleniyor. |
| Sızıntı temizliği | 4 | Bu dosyada 08 raporunda bazı ileri-sızıntı bulguları var (bkz. 08-mufredat-sizinti-tum-uygulama.md) — bu eksende tam puan değil. |
| Köprü farkındalığı | 5 | Okul kuralları ("must/mustn't") + ay/mevsim + selamlaşma, Y3-T2'nin sınıf kuralları ve Y4'ün ileri zaman ifadelerine çok iyi zemin hazırlıyor — bu dosyanın en güçlü yanı. |

### Diğer gözlemler

- **Karakter tutarlılığı:** Sorun yok — okul personeli (Ms. Hart öğretmen, Mr. Blake müdür,
  Mrs. Pine hemşire, Mr. Cole hizmetli, Ms. Shaw kütüphaneci) ve öğrenciler (Maya, Leo, Ada,
  Zara, Deniz, Kerem) isim/rol/doğum ayı bakımından metinler arası tutarlı (ör. Leo'nun doğum
  günü hem skim-6 hem int-6'da Ocak; Mr. Blake'in doğum günü hem scan-6 hem skim-6'da Haziran).
- **"Video mu fotoğraf mı?":** Ağırlıklı "video" — okul turu, kayıp öğrenci (int-2), yeni
  öğrenci (skim-8), doğum günü sürprizi (int-6) gibi metinlerin çoğu gerçek bir olay örgüsü
  içeriyor. Ay/mevsim envanteri (scan-4/5/6, skim-4/5) ve kural listeleri (scan-3, int-3)
  nispeten daha statik ama tema doğası gereği makul.
- **Çeviri/dil doğallığı:** Sorun yok, 40 metin boyunca tutarlı ve doğal.
- **Şık makuliyeti:** Yanlış şıklar hep aynı kategoriden (ay sorusuna ay, kişi sorusuna kişi)
  — makul, gülünç derecede elenebilir şık yok.

---

## Y3-T2 Classroom Life (44 metin) — TAMAMLANDI

### Yeni bulgu

Bu dosyada **yeni bir içerik/mantık hatası bulunamadı** — 44 metnin (scan 11, skim 11, int 11,
inf 11) tamamı satır satır okundu. `inf` grubunun ipucu kalitesi sorunsuz: tüm ipuçları "değil"
(eleme) veya sözel-referans ("X'e bak") tarzında, cevabı doğrudan vermiyor.

**Küçük stil notu (bulgu değil):** skim-11'de Ada "How many chairs are there in **our class**?"
diye soruyor ama Kerem "There are forty chairs in **our school**!" diye cevaplıyor — soru sınıfı
sorarken cevap okulu konu alıyor. Sorunun kendisi ("How many chairs are there in the school?")
ve doğru cevabı ("Forty") tutarlı olduğu için bu bir hata değil, yalnızca diyalogdaki ufak bir
doğallık pürüzü.

### 4 eksenli genel değerlendirme

| Eksen | Puan | Not |
|---|---|---|
| Yapı taşıyıcılığı | 5 | Sınıf eşyaları/renkleri + saat/ders programı + mevsimler/hava durumu + sınıf yönergeleri (temanın 4 hedefi) doğal diyaloglarla, kural anlatmadan işleniyor. |
| Geri dönüşüm zenginliği | 5 | Y3-T1'in ay/mevsim ve millî/dinî gün kalıpları (scan-10, skim-9, int-10, inf-10 — 23 Nisan; 29 Ekim) ve Y2'nin "how many" sayma kalıbı sistemli şekilde bu temaya taşınmış. |
| Sızıntı temizliği | 4 | Bu dosyada 08 raporunda bazı ileri-sızıntı bulguları var (bkz. 08-mufredat-sizinti-tum-uygulama.md) — bu eksende tam puan değil. |
| Köprü farkındalığı | 4 | Sınıf yönergeleri + saat/program, Y3-T3'ün kişisel rutinleri ve Y4'ün ileri zaman ifadelerine iyi zemin hazırlıyor. |

### Diğer gözlemler

- **Karakter tutarlılığı:** Sorun yok — Maya/Leo ikilisi ve yan karakterler (Ada, Zara, Kerem,
  Mert, Deniz) metinler arası tutarlı kullanılmış.
- **"Video mu fotoğraf mı?":** Karışık. Yönerge/ders-programı metinleri (scan-3/8/9, int-1/7)
  gerçek bir "video" — sınıf içi gerçek zamanlı etkileşim var. Eşya sayma/renk metinleri
  (scan-1/6/7/11, skim-2/5/8/11, int-3/5/6) daha statik envanter tarzı — tema doğası gereği
  makul ama bu STİL örüntüsü Y2'den beri sık tekrarlanıyor.
- **Çeviri/dil doğallığı:** skim-11 notu dışında sorun yok, 44 metin boyunca tutarlı ve doğal.
- **Şık makuliyeti:** Yanlış şıklar hep aynı kategoriden (ders sorusuna ders, sayı sorusuna
  sayı) — makul, gülünç derecede elenebilir şık yok.

---

## Y3-T3 Personal Life (44 metin) — TAMAMLANDI

### Yeni bulgu

Bu dosyada **yeni bir içerik/mantık hatası bulunamadı** — 44 metnin (scan 11, skim 11, int 12,
inf 10) tamamı satır satır okundu. `inf` grubunun ipucu kalitesi sorunsuz: tüm ipuçları "değil"
(eleme) veya sözel-referans tarzında, cevabı doğrudan vermiyor.

### 4 eksenli genel değerlendirme

| Eksen | Puan | Not |
|---|---|---|
| Yapı taşıyıcılığı | 5 | Görünüş/vücut betimlemesi + karakter sıfatları + kıyafet/aksesuar + hava durumuna göre giyinme (temanın 4 hedefi) doğal diyaloglarla, kural anlatmadan işleniyor. |
| Geri dönüşüm zenginliği | 5 | Y2-T3/T1'in göz/saç rengi + mevsim/hava durumu kalıpları ve Y3-T1/T2'nin millî gün kalıpları (scan-10, skim-10, int-10, inf-10 — 23 Nisan, 29 Ekim, 19 Mayıs, Ramazan Bayramı) sistemli şekilde bu temaya taşınmış. |
| Sızıntı temizliği | 4 | Bu dosyada 08 raporunda bazı ileri-sızıntı bulguları var (bkz. 08-mufredat-sizinti-tum-uygulama.md) — bu eksende tam puan değil. |
| Köprü farkındalığı | 4 | Kıyafet/aksesuar + karakter sıfatları, Y3-T4'ün genişletilmiş aile/kişi betimlemesine ve Y4'ün "would like/should" gibi yapılarına iyi zemin hazırlıyor. |

### Diğer gözlemler

- **Karakter tutarlılığı:** Sorun yok — tekrar eden karakterlerin (Maya, Leo, Ada, Zara, Kerem,
  Mert, Deniz) fiziksel özellikleri (Maya: uzun kıvırcık kahverengi saç + mavi göz; Zara: uzun
  sarı saç; Ada: sarı saç + mavi göz) ve karakter özellikleri (Mert: tembel ama kibar; Kerem:
  çalışkan) metinler arası tutarlı.
- **"Video mu fotoğraf mı?":** Karışık. "Kimin eşyası" bulmaca metinleri (scan-3/9, skim-7,
  int-2/6, inf-3/6/7/8) ve tanışma/yeni-arkadaş metinleri (skim-8) gerçek bir "video" — bulmaca
  ya da sosyal etkileşim var. Görünüş betimleme metinlerinin çoğu (scan-1/2/6, skim-1/2, int-1/9)
  daha statik "tanıtım" formatı — tema doğası gereği makul.
- **Çeviri/dil doğallığı:** Sorun yok, 44 metin boyunca tutarlı ve doğal.
- **Şık makuliyeti:** Yanlış şıklar hep aynı kategoriden (renk sorusuna renk, kıyafet sorusuna
  kıyafet) — makul, gülünç derecede elenebilir şık yok.

---

## Y3-T4 Family Life (43 metin) — TAMAMLANDI

### Yeni bulgu

Bu dosyada **yeni bir içerik/mantık hatası bulunamadı** — 43 metnin (scan 11, skim 11, int 11,
inf 10) tamamı satır satır okundu. `inf` grubunun ipucu kalitesi sorunsuz: tüm ipuçları "değil"
(eleme) veya sözel-referans tarzında, cevabı doğrudan vermiyor. Bu dosya 11-kapsam-tum-
uygulama.md'de en zayıf kelime-kapsamı puanına sahip dosya olarak işaretlenmişti (8 hedef
kelime hiç geçmiyor) — o bulgu burada tekrarlanmıyor, ama bu tam okuma sırasında ek bir
içerik/mantık hatası da bulunmadı.

### 4 eksenli genel değerlendirme

| Eksen | Puan | Not |
|---|---|---|
| Yapı taşıyıcılığı | 4 | Aile yaşları + "can/can't" yetenek + günlük rutin/ev işleri + "could you...?" nazik istek (temanın 4 hedefi) doğal diyaloglarla işleniyor, ama 11 raporundaki kelime kapsamı eksiklikleri (torun, kadın/kadınlar, giyinme, ders çalışma, ödev yapma gibi kelimelerin hiç geçmemesi) bu eksende tam puanı engelliyor. |
| Geri dönüşüm zenginliği | 5 | Y3-T1'in millî/dinî gün kalıbı (scan-10, int-10, inf-10 — Ramazan/Kurban Bayramı) ve Y3-T3'ün "could you...?" nazik istek kalıbı sistemli şekilde bu temaya taşınmış; "can/can't" yetenek karşılaştırması (scan-5/6/11, int-3/7) zengin bir tekrar örüntüsü oluşturuyor. |
| Sızıntı temizliği | 5 | Bu dosyada 08 raporunda ileri-sızıntı bulunmadı — temiz. |
| Köprü farkındalığı | 4 | Aile yaşları + günlük rutin + ev işleri, Y3-T5'in ev/oda kelime dağarcığına ve Y4'ün "should/have to" gibi yapılarına iyi zemin hazırlıyor. |

### Diğer gözlemler

- **Karakter tutarlılığı:** Sorun yok — aile üyelerinin yaşları (ör. Maya'nın büyükannesi hep
  65, büyükbabası hep 70; Zara'nın büyükannesi hep 70) ve yetenekleri (ör. Kerem'in gitar
  çalabilmesi ama piyano çalamaması) metinler arası tutarlı.
- **"Video mu fotoğraf mı?":** Karışık. "Kim bu aile üyesi" bulmaca metinleri (inf grubunun
  tamamı, 10/10) gerçek bir "video" — ipucu zinciri ve çıkarım var. Yaş/yetenek karşılaştırma
  metinlerinin çoğu (scan-1/2/5/6/11, skim-6/10) daha statik envanter tarzı — tema doğası
  gereği makul.
- **Çeviri/dil doğallığı:** Sorun yok, 43 metin boyunca tutarlı ve doğal.
- **Şık makuliyeti:** Yanlış şıklar hep aynı kategoriden (yaş sorusuna yaş, yetenek sorusuna
  yetenek) — makul, gülünç derecede elenebilir şık yok.

---

## Y3-T5 Homes & Houses (43 metin) — TAMAMLANDI

### Yeni bulgu

Bu dosyada **yeni bir içerik/mantık hatası bulunamadı** — 43 metnin (scan 11, skim 11, int 11,
inf 10) tamamı satır satır okundu. `inf` grubunun ipucu kalitesi sorunsuz: tüm ipuçları "değil"
(eleme) veya "X mi, Y mi?" (seçenek daraltma) tarzında, cevabı doğrudan vermiyor.

**Not (müfredat doğrulaması):** Bu tema "Homes & Houses" adını taşısa da içerik köy/çiftlik
hayatı (çiftlik evi, kulübe, ahır, hayvanlar) ve şimdiki zaman ("what is X doing now/at
present?") etrafında kurulu — Y2-T5'in oda/mobilya odaklı içeriğinden farklı. Bu, MEB
müfredatının Y3-Tema5'i "köy evleri ve şimdiki zaman" olarak tanımlamasıyla tutarlı (bkz.
coverage_scan.py VOCAB listesi) — hata değil, temanın doğal genişlemesi.

### 4 eksenli genel değerlendirme

| Eksen | Puan | Not |
|---|---|---|
| Yapı taşıyıcılığı | 5 | Şimdiki zaman ("is/are + -ing", "now/at present") + çiftlik hayvanları + köy evi türleri (çiftlik evi/kulübe/ahır) doğal diyaloglarla, kural anlatmadan işleniyor — örnek ders kitabı kalitesinde. |
| Geri dönüşüm zenginliği | 5 | Y2/Y3'ün "how many" sayma kalıbı ve millî/dinî gün kalıbı (scan-10, skim-10, int-5/10, inf-10 — Kurban Bayramı, Cumhuriyet Bayramı, 23 Nisan) sistemli şekilde bu temaya taşınmış. |
| Sızıntı temizliği | 5 | Bu dosyada 08 raporunda ileri-sızıntı bulunmadı — temiz. |
| Köprü farkındalığı | 4 | Şimdiki zaman + köy/çiftlik yaşamı, Y3-T6'nın şehir yaşamı karşılaştırmasına ve Y4'ün geçmiş zaman/gelecek zaman yapılarına iyi zemin hazırlıyor. |

### Diğer gözlemler

- **Karakter tutarlılığı:** Sorun yok — Mr. Tarık'ın çiftçi kimliği ve hayvanları (inek/tavuk/
  koyun sayıları metinler arası farklı olsa da tutarlı bir şekilde "many" ifadesiyle uyumlu),
  Selma büyükannenin köy evi ve ekmek pişirme rutini metinler arası tutarlı.
- **"Video mu fotoğraf mı?":** Ağırlıklı "video" — bu dosyanın en güçlü yanı. Şimdiki zaman
  odaklı olması nedeniyle neredeyse her metin gerçek bir "şu anda kim ne yapıyor" anlık kesiti
  sunuyor, statik envanter metni çok az (yalnızca scan-2/5/11 gibi sayma metinleri daha statik).
- **Çeviri/dil doğallığı:** Sorun yok, 43 metin boyunca tutarlı ve doğal.
- **Şık makuliyeti:** Yanlış şıklar hep aynı kategoriden (eylem sorusuna eylem, sayı sorusuna
  sayı) — makul, gülünç derecede elenebilir şık yok.

---

## Y3-T6 Life in the City (42 metin) — TAMAMLANDI

### Yeni bulgu

Bu dosyada **yeni bir içerik/mantık hatası bulunamadı** — 42 metnin (scan 11, skim 11, int 10,
inf 10) tamamı satır satır okundu. `inf` grubunun ipucu kalitesi sorunsuz: tüm ipuçları "değil"
(eleme) veya sözel-referans tarzında, cevabı doğrudan vermiyor.

### 4 eksenli genel değerlendirme

| Eksen | Puan | Not |
|---|---|---|
| Yapı taşıyıcılığı | 5 | "will" gelecek zaman ("I will take...") + restoran/kafe/paket-servis diyaloğu + "have got any...?" + nazik istek kalıpları (temanın hedefleri) doğal diyaloglarla, kural anlatmadan işleniyor. |
| Geri dönüşüm zenginliği | 5 | Y2-T6'nın "Do you like/want" yiyecek kalıbı ve millî/dinî gün kalıbı (scan-10, skim-10, int-10, inf-10 — 23 Nisan, Ramazan Bayramı) sistemli şekilde bu temaya taşınmış; Mr. Cem/Ms. Lale garson karakterleri restoran/kafe/paket-servis metinlerinde tutarlı tekrarlanıyor. |
| Sızıntı temizliği | 4 | Bu dosyada 08 raporunda bazı ileri-sızıntı bulguları var (bkz. 08-mufredat-sizinti-tum-uygulama.md) — bu eksende tam puan değil. |
| Köprü farkındalığı | 4 | "will" gelecek zaman + dışarıda yemek kültürü, Y4'ün ileri zaman yapıları ve şehir hayatı temalarına iyi zemin hazırlıyor. |

### Diğer gözlemler

- **Karakter tutarlılığı:** Sorun yok — Mr. Cem hep erkek garson, Ms. Lale hep kadın garson
  rolünde tutarlı (inf-4'te bu ayrım doğrudan bir çıkarım sorusuna dönüştürülmüş: "Is it a man
  or a woman?").
- **"Video mu fotoğraf mı?":** Ağırlıklı "video" — bu dosyanın güçlü yanı. Restoran/kafe/paket-
  servis sipariş diyalogları neredeyse tamamen gerçek zamanlı etkileşim (garson-müşteri
  soru-cevap döngüsü), envanter-tarzı statik metin çok az.
- **Çeviri/dil doğallığı:** Sorun yok, 42 metin boyunca tutarlı ve doğal.
- **Şık makuliyeti:** Yanlış şıklar hep aynı kategoriden (yemek sorusuna yemek, mekân sorusuna
  mekân) — makul, gülünç derecede elenebilir şık yok.

---

## Y3 ÖZETİ — 6/6 tema tamamlandı

Y3'ün 6 temasının tamamı (259 metin) satır satır okunarak 4 eksende değerlendirildi. Bu turda
**hiçbir yeni içerik/mantık hatası bulunmadı** — Y3'ün tamamı, Y2'den farklı olarak, satır satır
okumada herhangi bir KRİTİK/CİDDİ bulguya rastlanmadı (yalnızca zaten bilinen sızıntı/kapsam
bulguları teyit edildi). Şimdi Y4'ün 6 temasına geçiliyor — bu, denetimin son 6 dosyası.

---

## Y4-T1 School Life (40 metin) — TAMAMLANDI

### Yeni bulgu

Bu dosyada **yeni bir içerik/mantık hatası bulunamadı** — 40 metnin (scan 10, skim 10, int 10,
inf 10) tamamı satır satır okundu. `inf` grubunun ipucu kalitesi genel olarak sağlam: ipuçları
"değil" (eleme) veya sözel-referans tarzında. inf-6'daki "Sam is moving to the music during the
practice" ifadesi zaten 10-ipucu-tam-tarama.md'de "dans etme"ye çok yakın bir çıkarım-öncesi
sızıntı olarak belgelenmişti — burada tekrar edilmiyor, sadece teyit ediliyor.

### 4 eksenli genel değerlendirme

| Eksen | Puan | Not |
|---|---|---|
| Yapı taşıyıcılığı | 5 | Okul personeli (rehber öğretmen, müdür, müzik/beden eğitimi öğretmeni) + saat aralıkları ("between X and Y") + üstünlük sıfatları ("the busiest/quietest/fastest") + "always...but today" karşıtlığı (temanın 4 hedefi) doğal diyaloglarla işleniyor — Y4 seviyesinin dilbilgisel karmaşıklığı iyi yönetiliyor. |
| Geri dönüşüm zenginliği | 5 | Y3'ün millî/dinî gün kalıbı (scan-3/10, int-1/7, inf-9/10 — 23 Nisan, 29 Ekim, 19 Mayıs, 30 Ağustos, 15 Temmuz, Ramazan/Kurban Bayramı) ve ay/mevsim kalıbı zengin biçimde genişletilerek kullanılmış; Mr. Tan/Mrs. Yıldız/Mr. Demir/Ms. Çelik gibi personel karakterleri dosya boyunca tutarlı. |
| Sızıntı temizliği | 4 | Bu dosyada 08 raporunda bazı ileri-sızıntı bulguları var (bkz. 08-mufredat-sizinti-tum-uygulama.md) — bu eksende tam puan değil. |
| Köprü farkındalığı | 5 | Üstünlük sıfatları + saat aralıkları + kulüp/gezi organizasyonu, Y4'ün kalan temalarındaki daha karmaşık zaman/karşılaştırma yapılarına çok iyi zemin hazırlıyor — bu dosyanın en güçlü yanı. |

### Diğer gözlemler

- **Karakter tutarlılığı:** Sorun yok — okul personeli (Ms. Reed sınıf öğretmeni, Mr. Tan
  müdür, Mrs. Yıldız rehber öğretmen, Mr. Demir beden eğitimi, Ms. Çelik müzik) ve öğrenciler
  (Nora, Sam, Leyla) rol/isim bakımından metinler arası tutarlı.
- **"Video mu fotoğraf mı?":** Ağırlıklı "video" — bu dosyanın güçlü yanı. Gezi, spor günü,
  yetenek gösterisi, veli-öğretmen toplantısı gibi metinlerin çoğu gerçek zamanlı olay örgüsü
  içeriyor; yalnızca ay/gün karşılaştırma metinleri (scan-4/7, skim-5/6) daha statik.
- **Çeviri/dil doğallığı:** Sorun yok, 40 metin boyunca tutarlı ve doğal.
- **Şık makuliyeti:** Yanlış şıklar hep aynı kategoriden (okul sorusuna okul, ay sorusuna ay)
  — makul, gülünç derecede elenebilir şık yok.

---

## Y4-T2 Classroom Life (40 metin) — TAMAMLANDI

### Yeni bulgu

Bu dosyada **yeni bir içerik/mantık hatası bulunamadı** — 40 metnin (scan 10, skim 10, int 10,
inf 10) tamamı satır satır okundu. `inf` grubunun ipucu kalitesi sağlam: ipuçları "değil"
(eleme) tarzında, cevabı doğrudan vermiyor. Bu dosyada 09-teknik-tum-uygulama.md'de zaten
belgelenmiş olan **qTr alanının tamamen eksik olması** (200 soru) burada da doğrulandı —
tekrar raporlanmıyor.

**Küçük stil notu — ✅ DÜZELTİLDİ:** inf-10'da Ms. Çelik'in cast emoji'si (👩‍💼) Y4-T1'deki
(👩‍🎤, müzik öğretmeni) ile farklıydı — aynı karaktere ait iki dosyada farklı emoji kullanılmıştı.
İçerik/mantık hatası değil, yalnızca görsel kimlik tutarsızlığıydı; artık 👩‍🎤 üzerinde birleştirildi.

### 4 eksenli genel değerlendirme

| Eksen | Puan | Not |
|---|---|---|
| Yapı taşıyıcılığı | 5 | İyelik zamirleri (mine/yours/ours) + saat ifadeleri (quarter past/to, twenty to/past) + geçmiş zaman ("was/were") + mevsim karşılaştırması (temanın 4 hedefi) doğal diyaloglarla işleniyor. |
| Geri dönüşüm zenginliği | 5 | Y4-T1'in saat aralıkları ve büyük sayılar kalıbı zengin biçimde genişletilerek kullanılmış; İngilizce deyimler ("raining cats and dogs", "break the ice", "one in a million") sistemli tekrarla pekiştirilmiş. |
| Sızıntı temizliği | 4 | Bu dosyada 08 raporunda bazı ileri-sızıntı bulguları var (bkz. 08-mufredat-sizinti-tum-uygulama.md) — bu eksende tam puan değil. |
| Köprü farkındalığı | 5 | Geçmiş zaman ("was/were") + iyelik zamirleri, Y4'ün kalan temalarındaki daha karmaşık zaman yapılarına çok iyi zemin hazırlıyor. |

### Diğer gözlemler

- **Karakter tutarlılığı:** Sorun yok (yukarıdaki emoji notu dışında) — Ms. Reed, Nora, Sam,
  Leyla rol ve kişilik özellikleri bakımından metinler arası tutarlı.
- **"Video mu fotoğraf mı?":** Karışık. Yardımlaşma ve deyim-öğretme metinleri (scan-7/8,
  skim-7/9, int-1/5/9) gerçek zamanlı etkileşim içeriyor. Sayı/saat/mevsim metinlerinin çoğu
  (scan-2/3/4/10, skim-3/4/6/10) daha statik soru-cevap envanteri — tema doğası gereği makul.
- **Çeviri/dil doğallığı:** Sorun yok, 40 metin boyunca tutarlı ve doğal (qTr eksikliği dışında,
  zaten belgelenmiş bir şema sorunu).
- **Şık makuliyeti:** Yanlış şıklar hep aynı kategoriden (saat sorusuna saat, sayı sorusuna
  sayı) — makul, gülünç derecede elenebilir şık yok.

---

## Y4-T3 Personal Life (40 metin) — TAMAMLANDI

### Yeni bulgu

Bu dosyada **yeni bir içerik/mantık hatası bulunamadı** — 40 metnin (scan 10, skim 10, int 10,
inf 10) tamamı satır satır okundu. `inf` grubunun ipucu kalitesi sağlam: ipuçları eleme/karşılaştırma
tarzında akıl yürütme gerektiriyor, cevabı doğrudan vermiyor — bu dosyanın çıkarım grubu, tüm
dosyalar arasında en karmaşık mantıksal zincirlere sahip (ör. inf-9 "en uzun/en kısa" 3 kişilik
sıralama problemi).

**Küçük stil notu — ✅ DÜZELTİLDİ:** Ms. Çelik'in cast emoji'si burada üçüncü kez farklıydı (👩‍🎨,
"sanatçı") — Y4-T1'de 👩‍🎤, Y4-T2'de 👩‍💼, burada 👩‍🎨. Aynı karakter üç dosyada üç farklı emoji
ile temsil edilmişti. İçerik hatası değil, yalnızca görsel kimlik tutarsızlığıydı — üç dosya da
artık 👩‍🎤 üzerinde birleştirildi.

### 4 eksenli genel değerlendirme

| Eksen | Puan | Not |
|---|---|---|
| Yapı taşıyıcılığı | 5 | Karşılaştırma sıfatları (comparative/superlative) + "could/couldn't" geçmiş yetenek + "enjoy/prefer/dislike + -ing" + "is there anything/there isn't any" (temanın 4 hedefi) doğal diyaloglarla, kural anlatmadan işleniyor — Y4 seviyesinin en yoğun dilbilgisel içeriği. |
| Geri dönüşüm zenginliği | 5 | Y3-T3'ün görünüş betimlemesi ve Y2-T4'ün "boy/saç" karşılaştırması ileri düzeyde genişletilmiş; millî gün kalıbı (scan-3, skim-1, int-7 — 23 Nisan, 19 Mayıs, 29 Ekim) sistemli tekrarla korunmuş. |
| Sızıntı temizliği | 4 | Bu dosyada 08 raporunda bazı ileri-sızıntı bulguları var (bkz. 08-mufredat-sizinti-tum-uygulama.md) — bu eksende tam puan değil. |
| Köprü farkındalığı | 5 | Karşılaştırma yapıları + geçmiş yetenek ifadeleri, Y4'ün kalan temalarındaki en karmaşık dilbilgisi yapılarına (would/should/karma zamanlar) mükemmel zemin hazırlıyor. |

### Diğer gözlemler

- **Karakter tutarlılığı:** Sorun yok (emoji notu dışında) — Nora/Sam/Leyla'nın fiziksel
  özellikleri ve altı-yaşındaki-yetenekleri (ör. Sam'in altı yaşında yüzebilmesi ama
  bisiklet süremeyip sonra binebilmesi) metinler arası tutarlı ayrıntılarla anlatılıyor.
  scan-1/skim-2/int-2 üçlüsünde "altı yaşında kim daha uzundu" bilgisi tutarlı.
- **"Video mu fotoğraf mı?":** Ağırlıklı "video" — geçmiş-şimdi karşılaştırması ve tahmin
  oyunları (özellikle tüm inf grubu) gerçek bir anlatı akışı içeriyor; yalnızca hava durumu
  çizelgesi metinleri (scan-7, int-9/10) daha statik envanter tarzı.
- **Çeviri/dil doğallığı:** Sorun yok, 40 metin boyunca tutarlı ve doğal.
- **Şık makuliyeti:** Yanlış şıklar hep aynı kategoriden (kıyafet sorusuna kıyafet, tarih
  sorusuna tarih) — makul, gülünç derecede elenebilir şık yok.

---

## Y4-T4 Family Life (40 metin) — TAMAMLANDI

### Yeni bulgu

Bu dosyada **yeni bir içerik/mantık hatası bulunamadı** — 40 metnin (scan 10, skim 10, int 10,
inf 10) tamamı satır satır okundu. `inf` grubu bu denetimde okunan en güçlü çıkarım-bulmacası
kümelerinden biri: her metin "değil çünkü..." tarzında çok adımlı bir eleme zinciri kuruyor
(ör. inf-9 "hangi gün" bulmacası okul çantası/alışveriş poşeti/çöp kutusu/çorba tenceresi/fırın
poşeti gibi 5 ayrı ipucunu sırayla eleyerek Cuma'ya ulaşıyor) — hiçbirinde cevabı ele veren bir
sızıntı yok.

**Küçük stil notu (bulgu değil):** Bu dosyada "Nora's daddy", "Sam's mummy" gibi isimsiz aile
büyükleri sıkça doğrudan konuşuyor ama resmi `cast` listesine girmiyorlar (yalnızca Nora/Sam/
Leyla/Ms. Reed listeleniyor). Bu, önceki cast-eksikliği bulgularından farklı bir örüntü — burada
tekrarlayan *isimli* bir karakterin eksikliği değil, tek-seferlik *rolsel* konuşmacıların (anne/
baba/büyükanne) baştan beri cast dışı tutulması söz konusu; muhtemelen kasıtlı bir tasarım
tercihi (aile büyükleri için ayrı portre çizmemek). İçerik hatası değil, gözlem notu.

### 4 eksenli genel değerlendirme

| Eksen | Puan | Not |
|---|---|---|
| Yapı taşıyıcılığı | 5 | Meslek adları (doktor/hemşire/aşçı/polis/berber vb.) + mahalle/dükkân kelime dağarcığı + "usually/but today" alışkanlık-istisna karşıtlığı + üstünlük sıfatları (temanın 4 hedefi) doğal diyaloglarla, kural anlatmadan işleniyor. |
| Geri dönüşüm zenginliği | 5 | Y4-T1/T2/T3'ün karşılaştırma yapıları ve millî gün kalıbı zengin biçimde bu temaya taşınmış; şehir/mahalle kelime dağarcığı (eczane, fırın, berber, kuaför, postane) sistemli tekrarla pekiştirilmiş. |
| Sızıntı temizliği | 4 | Bu dosyada 08 raporunda bazı ileri-sızıntı bulguları var (bkz. 08-mufredat-sizinti-tum-uygulama.md) — bu eksende tam puan değil. |
| Köprü farkındalığı | 5 | Meslek/mahalle kelime dağarcığı + çok adımlı çıkarım metinleri, Y4'ün son iki temasındaki (Homes & Houses, Life in the City) şehir yaşamı ve karmaşık anlatılara mükemmel zemin hazırlıyor. |

### Diğer gözlemler

- **Karakter tutarlılığı:** Sorun yok (yukarıdaki cast notu dışında) — Nora/Sam/Leyla'nın aile
  üyeleri (meslekleri, alışkanlıkları) metinler arası tutarlı bir şekilde genişletiliyor (ör.
  Nora'nın büyükannesinin hastane kafesinde aşçı olması scan-1, scan-9, inf-1, inf-7'de tutarlı).
- **"Video mu fotoğraf mı?":** Ağırlıklı "video" — bu dosyanın en güçlü yanı. Meslek Günü,
  aile işleri, hafta sonu ziyaretleri gibi neredeyse her metin gerçek bir olay örgüsü içeriyor;
  bulmaca tarzı `inf` grubu metinleri özellikle güçlü bir anlatı yapısına sahip.
- **Çeviri/dil doğallığı:** Sorun yok, 40 metin boyunca tutarlı ve doğal.
- **Şık makuliyeti:** Yanlış şıklar hep aynı kategoriden (meslek sorusuna meslek, yer sorusuna
  yer) — makul, gülünç derecede elenebilir şık yok.

---

## Y4-T5 Homes & Houses (40 metin) — TAMAMLANDI

### Yeni bulgu

Bu dosyada **yeni bir içerik/mantık hatası bulunamadı** — 40 metnin (scan 10, skim 10, int 10,
inf 10) tamamı satır satır okundu. `inf` grubunun 10 çıkarım-bulmacası (deniz kaplumbağası,
ahtapot, fok gibi hayvan bilmeceleri; nehir/göl/lagün su-türü bilmecesi; fırtına tahmini; sayım
defteri trend analizi) her biri çok adımlı, biyolojik/mantıksal olarak tutarlı eleme zincirleri
kuruyor (ör. inf-1: "en iyi yüzücü değil ama uzun yüzer" → yunus elenir; "dişi yok, deniz bitkisi
yer" → köpekbalığı elenir; "haziranda kuma yumurta bırakır" → fok elenir → deniz kaplumbağası).
Tüm ipuçları "değil" (eleme) veya sözel-referans ("X'e bak", "Y'yi ele/düşün") tarzında, cevabı
doğrudan vermiyor — bu dosyanın çıkarım grubu, denetimde okunan en sağlam bilmece kümelerinden
biri.

**Not (müfredat doğrulaması):** Dosya adı "Homes & Houses" olsa da içerik artık literal ev/oda
konusundan tamamen uzaklaşıp deniz canlıları habitatlarına (balina, fok, ahtapot, yunus,
denizanası, yengeç, denizyıldızı, deniz kaplumbağası), plastik kirliliğine, balıkçı ağlarına,
iklim değişikliğine ve tekne-ev/plaj-evi/göl-evi karşılaştırmasına odaklanıyor. Bu,
`coverage_scan.py`'deki VOCAB listesiyle karşılaştırıldı ve Y4-Tema5'in müfredatta "habitatlar
ve çevre bilinci" olarak tanımlanan ileri-seviye genişlemesiyle tutarlı — hata değil, temanın
kasıtlı bir üst-seviye uzantısı. (09-teknik-tum-uygulama.md'de bu dosyanın 200 sorusunun tamamında
`qTr` alanının eksik olduğu zaten belgelenmişti — burada tekrar raporlanmıyor.)

### 4 eksenli genel değerlendirme

| Eksen | Puan | Not |
|---|---|---|
| Yapı taşıyıcılığı | 5 | "mustn't/shouldn't" çevresel kurallar + üstünlük sıfatları ("the worst danger", "the best hider") + çok-ipuçlu çıkarım zincirleri (temanın ileri-seviye hedefleri) doğal diyaloglarla, kural anlatmadan işleniyor. |
| Geri dönüşüm zenginliği | 5 | Y4-T1-T4'ün üstünlük sıfatları ve karşılaştırma yapıları zengin biçimde bu temaya taşınmış; "mustn't" kuralı Y3-T1'in okul kurallarından genişletilerek çevre bilincine uygulanmış. |
| Sızıntı temizliği | 5 | `inf` grubunun tamamı sağlam eleme/sözel-referans ipuçları kullanıyor; 08 raporunda bu dosya için ek bir ileri-sızıntı bulgusu yok. |
| Köprü farkındalığı | 4 | Habitat/çevre kelime dağarcığı + çok adımlı çıkarım, Y4-T6'nın (Life in the City) şehir/çevre temasına iyi zemin hazırlıyor; ancak temanın adıyla içeriği arasındaki büyük sapma (ev → deniz habitatı) bir sonraki temaya "köprü" kurarken biraz kopuk hissettiriyor. |

### Diğer gözlemler

- **Karakter tutarlılığı:** Sorun yok — Nora/Sam/Leyla ve Ms. Reed (öğretmen, tüm gruplarda
  👩‍🏫 emoji ile tutarlı — Y4-T1/T2/T3'teki Ms. Çelik emoji tutarsızlığının aksine burada sorun
  yok) rol ve kişilik özellikleri bakımından metinler arası tutarlı; Grandpa (inf-6) tek-seferlik
  bir karakter olarak cast listesine doğru şekilde eklenmiş.
- **"Video mu fotoğraf mı?":** Ağırlıklı "video" — bu dosyanın güçlü yanı. Akvaryum ziyareti,
  plaj temizliği kulübü, fotoğraf karşılaştırmaları ve bilmece-çözme metinlerinin neredeyse
  tamamı gerçek bir keşif/tartışma anlatısı içeriyor; yalnızca birkaç istatistik/harita metni
  (scan/skim grubundaki bazı envanter metinleri) daha statik.
- **Çeviri/dil doğallığı:** Sorun yok, 40 metin boyunca tutarlı ve doğal (qTr şema eksikliği
  dışında, zaten belgelenmiş bir sorun).
- **Şık makuliyeti:** Yanlış şıklar hep aynı kategoriden (hayvan sorusuna hayvan, su-türü
  sorusuna su-türü) — makul, gülünç derecede elenebilir şık yok.

---

## Y4-T6 Life in the City (40 metin) — TAMAMLANDI

### Doğrulama ve detaylandırma — cast eksikliği (07 raporunda zaten bilinen bulgu) — ✅ DÜZELTİLDİ

Aşağıdaki 7 metnin tamamında Leyla artık `cast` dizisine eklendi (👧🏽 emoji ile, dosyanın geri
kalanıyla tutarlı).

[07-tum-uygulama-oynanis-raporu.md](07-tum-uygulama-oynanis-raporu.md) bu dosyada Leyla'nın
avatar'ı olmadan konuştuğu **6** metin bulmuştu (Sonuç 2, genel özette de "6 ayrı metin" olarak
kayıtlı). Bu turdaki tam satır satır okuma aynı bulguyu doğruladı ve **7 metin** tespit etti — 07
raporunun ilk taramasından bir eksik (muhtemelen tek satırlık kısa bir konuşma daha kolay
gözden kaçıyor). Yeni bir bulgu değil, mevcut bulgunun **tam listesi ve sayı düzeltmesi**:

Etkilenen 7 metinde, `cast` listesi yalnızca 3 kişi (Ms. Reed, Nora, Sam) olarak tanımlı ama
resmî cast listesine dahil edilmemiş olan Leyla — dosyanın 4 çekirdek karakterinden biri, 33
diğer metinde kendi emoji'siyle (👧🏽) düzenli listelenen isimli, tekrarlayan bir karakter —
konuşma satırlarıyla doğrudan diyaloğa katılıyor. Bu, Y4-T4'te gözlemlenen "isimsiz tek-seferlik
rol konuşmacısı" (ör. "Nora's daddy") örüntüsünden farklı: orada bulgu sayılmamıştı çünkü o
karakterler zaten cast'e hiç girmeyen bir tasarım kategorisiydi. Burada ise Leyla tam tersi —
dosyanın geri kalanında cast'in daimi bir üyesi — ama bu 7 metinde unutulmuş.

```
[CİDDİ] [şema/görsel] data/grade4/life-in-the-city-y4.json:scan-6 → cast
Mevcut : cast=[Ms. Reed, Nora, Sam] ama sentences[8]="Leyla: Few people eat healthy food every
         day. But it is important!"
Sorun  : Leyla konuşuyor ama cast listesinde yok — uygulama muhtemelen bu satırı boş/varsayılan
         bir avatarla veya hatayla gösterecek.
```
```
[CİDDİ] [şema/görsel] data/grade4/life-in-the-city-y4.json:scan-10 → cast
Mevcut : cast=[Ms. Reed, Nora, Sam] ama sentences[4]="Leyla: Moussaka is the most special dish in
         Greece." ve sentences[7]="Leyla: Brown rice with chicken is delicious in Azerbaijan."
Sorun  : Aynı desen — Leyla iki kez konuşuyor, cast'te yok.
```
```
[CİDDİ] [şema/görsel] data/grade4/life-in-the-city-y4.json:skim-4 → cast
Mevcut : cast=[Ms. Reed, Nora, Sam] ama sentences[8]="Leyla: We should eat the healthy plate
         every day."
Sorun  : Aynı desen.
```
```
[CİDDİ] [şema/görsel] data/grade4/life-in-the-city-y4.json:skim-8 → cast
Mevcut : cast=[Ms. Reed, Nora, Sam] ama Leyla sentences[7], [8] ve [15]'te üç kez konuşuyor
         ("Wow!", "It tastes good with the sauce!", "Every dish from every country tastes good
         in its own way.").
Sorun  : Aynı desen — bu dosyada en sık tekrarlanan örnek (3 konuşma satırı).
```
```
[CİDDİ] [şema/görsel] data/grade4/life-in-the-city-y4.json:skim-10 → cast
Mevcut : cast=[Ms. Reed, Nora, Sam] ama sentences[4]="Leyla: I think the soup will be the best
         part of the meal." ve sentences[7]="Leyla: We are going to learn about Turkish food
         traditions."
Sorun  : Aynı desen. Ayrıca questions[2]'nin ipucu "Leyla'yı bul." diyerek doğrudan cast'te
         olmayan bir karaktere yönlendiriyor.
```
```
[CİDDİ] [şema/görsel] data/grade4/life-in-the-city-y4.json:int-10 → cast
Mevcut : cast=[Ms. Reed, Nora, Sam] ama sentences[3]="Leyla: For Wednesday, we can have a few
         pears and a little yogurt." ve sentences[6]="Leyla: For Friday, we can eat a little
         plum jam on toast."
Sorun  : Aynı desen. questions[1] ve questions[3]'ün ipuçları da "Leyla'ya bak." diyor.
```
```
[CİDDİ] [şema/görsel] data/grade4/life-in-the-city-y4.json:inf-9 → cast
Mevcut : cast=[Nora, Sam, Ms. Reed] ama sentences[2]="Leyla tastes tacos. Leyla: These are good,
         too!"
Sorun  : Aynı desen — çıkarım grubunda da tekrarlanıyor.
Öneri  : Bu 7 metnin tamamında `cast` dizisine {"e": "👧🏽", "n": "Leyla"} eklenmesi (dosyanın
         diğer 33 metninde kullanılan aynı emoji ile).
Dayanak: Bu, tek bir metnin izole hatası değil — dosya boyunca "3 kişilik cast" şablonunun
         kopyalanıp Leyla'nın satırlarının silinmesi unutulduğu sistematik bir üretim hatası
         gibi görünüyor (07 raporundaki cast-eksikliği kategorisiyle aynı, ama bu dosyada normalin
         çok üzerinde bir sıklıkla — 40 metnin 7'sinde, yani %17.5'inde — tekrarlanıyor).
```

`inf` grubunun ipucu kalitesi ayrıca kontrol edildi: tüm ipuçları "değil" (eleme) tarzında veya
doğrudan referans ("X'e bak") — sağlam, cevabı sızdırmıyor.

### 4 eksenli genel değerlendirme

| Eksen | Puan | Not |
|---|---|---|
| Yapı taşıyıcılığı | 5 | "going to" planlı gelecek + "will" tahmin + sayılamayan isimler (little/a little vs few/a few) + tatlar/ülke mutfakları (temanın 4 hedefi) doğal diyaloglarla, kural anlatmadan işleniyor. |
| Geri dönüşüm zenginliği | 5 | Y4-T1-T5'in üstünlük sıfatları ve karşılaştırma yapıları zengin biçimde bu temaya taşınmış; 10 farklı ülke mutfağı (Türkiye, İtalya, İngiltere, Yunanistan, Meksika, Cezayir, ABD, Almanya, Azerbaycan, KKTC) sistemli tekrarla pekiştirilmiş. |
| Sızıntı temizliği | 4 | `inf` grubu sağlam, ancak cast bulgusu bu eksenin dışında (görsel/şema kategorisi) — 08 raporunda bu dosya için ayrı bir ileri-sızıntı bulgusu yok. |
| Köprü farkındalığı | 4 | "going to" + "will" karşılaştırması ve dünya mutfağı kelime dağarcığı, Y4 müfredatının kapanışı için iyi bir sentez sağlıyor; ancak cast tutarsızlığı sıklığı, dosyanın teknik cilası açısından köprü kalitesini biraz düşürüyor. |

### Diğer gözlemler

- **Karakter tutarlılığı:** Yukarıdaki cast bulgusu dışında sorun yok — Nora/Sam/Leyla/Ms. Reed'in
  yemek tercihleri (ör. Sam'in hep "I'm starving!" demesi, Leyla'nın hep "Thanks for everything!"
  demesi) metinler arası tutarlı birer replik imzası gibi kullanılmış.
- **"Video mu fotoğraf mı?":** Ağırlıklı "video" — tatil planları, dünya yemek turu, doğum günü
  sürprizi bulmacası (inf-2) gibi metinlerin çoğu gerçek bir anlatı/diyalog akışı içeriyor;
  yalnızca ülke-yemek eşleştirme envanterleri (scan-2, scan-10, skim-6) daha statik.
- **Çeviri/dil doğallığı:** Sorun yok, 40 metin boyunca tutarlı ve doğal.
- **Şık makuliyeti:** Yanlış şıklar hep aynı kategoriden (ülke sorusuna ülke, yemek sorusuna
  yemek) — makul, gülünç derecede elenebilir şık yok.

---

## Y4 ÖZETİ — 6/6 tema tamamlandı

Y4'ün 6 temasının tamamı (240 metin) satır satır okunarak 4 eksende değerlendirildi. Bu turda
**yeni bir içerik/mantık hatası bulunmadı** — T1-T6'nın hiçbirinde. Y4-T6'da (Life in the City)
07 raporunun cast-eksikliği bulgusu doğrulandı ve tam listesiyle detaylandırıldı (6→7 metin,
yeni bir bulgu değil, sayı düzeltmesi). Ayrıca Ms. Çelik'in emoji'sinin T1/T2/T3 arasında 3
farklı hâlde kullanılması gibi küçük STİL notları kaydedildi (konsolide özette tekilleştirilecek).

---

## TÜM UYGULAMA ÖZETİ — 17/17 dosya, 710/710 metin TAMAMLANDI

Bu raporla birlikte, [04-pedagojik-rapor.md](04-pedagojik-rapor.md)'deki Y2-T1'in 51 metniyle
birlikte uygulamanın **tamamı** (761 metin, 18 dosya) satır satır okunarak 4 eksende
değerlendirildi. Bu son turda (Y2-T2'den Y4-T6'ya kadar 17 dosya, 710 metin) toplam **4 yeni
bulgu** ortaya çıktı:

- **1 KRİTİK** mantık hatası (Y2-T2 scan-12, "Outside" cevap hatası)
- **3 CİDDİ** q/qTr uyumsuzluğu (Y2-T3 inf-1/9/10)

Ayrıca Y4-T6'da (Life in the City) 07 raporunun cast-eksikliği bulgusu tam listeyle doğrulandı ve
sayısı düzeltildi (6→7 metin — yeni bir bulgu değil, mevcut bulgunun netleştirilmesi).

Y2-T4, T5, T6 ve Y3'ün tamamı (6/6 tema) ile Y4'ün 6 temasının tamamında satır satır okumada
**hiçbir yeni KRİTİK/CİDDİ içerik/mantık bulgusuna rastlanmadı**. Konsolide final rapor ve genel
özet güncellemesi [12-genel-ozet.md](12-genel-ozet.md)'de yapılacak.
