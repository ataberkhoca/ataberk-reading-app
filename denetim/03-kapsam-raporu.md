# Kapsam Raporu — Y2 Tema 1 (School Life)

Kullanıcı onayı gereği bu rapor **51 metnin tamamı** üzerinden değerlendiriyor (10'luk grup
varsayımı değil — bkz. [00-mufredat-haritasi.md](00-mufredat-haritasi.md) §5).

## 1. Yıldız (`[NEW]`) dil yapısı kapsamı

| Yapı | Eşleşme | Farklı metin sayısı | Değerlendirme |
|---|---|---|---|
| "What is/'s this/it?" (nesne sorma) | 28 | 12/51 | ✅ Sağlam |
| "Who is/'s…?" (kişi sorma) | 60 | 30/51 | ✅ Çok sağlam — temanın en baskın kalıbı |
| "Where is X? …in…" (yer + edat *in*) | 15 (dar regex) | 7/51 (gerçekte çok daha fazla — regex dar yazıldı, elle okumada `Where is`/`in` neredeyse her scan/int metninde var) | ✅ Sağlam |
| "What's your name? / My name is…" | 6 | 5/51 | ⚠️ Zayıf ama var — yalnızca "yeni öğrenci" alt-hikâyesinde (scan-8, skim-5, int-1, inf-4, inf-9) |
| Emir kipi ("Come here/in", "Sit here/down") | 12 | 9/51 | ⚠️ Orta — hiç işlenmemiş değil ama temanın geri kalanına göre ince |
| "What day (of the week) is it?" | 23 | 14/51 | ✅ Sağlam |
| Selamlaşma (Good morning/Hello/Hi/How are you/fine thanks) | 63 | 22/51 | ✅ Çok sağlam |
| Kişi zamirleri (I/he/she/it/we/you/they) | — | ~51/51 | ✅ Her metinde var (temel cümle kurucu) |
| İşaret zamiri "this" | — | ~45+/51 | ✅ Çok sağlam |
| WH- soru sözcükleri (what/who/where) | — | ~51/51 | ✅ Her metinde var |

**Sonuç: 10 yıldızın hiçbiri "hiç işlenmemiş" değil.** İki tanesi ("What's your name?" ve emir kipi)
diğerlerine göre ince kapsamlı — bunlar CİDDİ değil ama not edilmeye değer bir dengesizlik.

```
[STİL] [kapsam-boşluğu] tema geneli
Sorun  : "What's your name? / My name is…" kalıbı yalnızca 5/51 metinde (hepsi "yeni öğrenci"
         alt-örgüsünde) geçiyor; emir kipi 9/51 metinde. Diğer yıldızlar 12-30 metinde tekrarlanırken
         bu iki hedef yapı belirgin şekilde daha az pratik alanı buluyor.
Öneri  : "Days of the week" veya "Places" alt temalarındaki birkaç metne doğal biçimde bir
         "What's your name?" ya da "Come here, please!" repliği eklemek (örn. bir öğretmenin yeni
         bir öğrenciye sınıfta seslenmesi) kapsamı dengeleyebilir.
Dayanak: Pedagojik — her yıldız yapının en az birkaç bağlamda tekrarlanması bekçi metriktir; bu iki
         yapı bir tek "senaryo"ya (yeni öğrenci hikâyesi) hapsolmuş durumda.
```

## 2. Hedef kelime kapsamı

### Kişiler (a) People in school

| Kelime | Eşleşme | Durum |
|---|---|---|
| a teacher | 52 | ✅ |
| a pupil | 71 | ✅ |
| a headmaster | 27 | ✅ |
| **a headmistress** | **0** | ❌ **Hiç geçmiyor** |
| a friend | 37 | ✅ |
| a boy | 14 | ✅ |
| a girl | 8 | ✅ |
| **a kid** | **1** | ⚠️ **Neredeyse hiç geçmiyor** |

```
[CİDDİ] [kapsam-boşluğu] tema geneli → hedef kelime "headmistress"
Sorun  : Müfredat "a headmaster/headmistress (principal-AmE.)" ifadesini tek bir hedef kelime
         çifti olarak veriyor, ama temadaki tek müdür karakteri (Mr. Aras) erkek; 51 metnin
         hiçbirinde "headmistress" kelimesi kullanılmıyor, dişi bir müdür karakteri de hiç
         tanıtılmıyor.
Öneri  : En az bir metinde ikinci bir okul (ör. "Our sister school has a headmistress, Mrs. …")
         ya da mevcut kadrodan birine ("Mrs. Yaz is our headmistress" gibi) atıfla kelimeyi
         en az 2-3 kez üretici biçimde kullanmak. Alternatif: eğer tasarım kasıtlıysa (tek okulda
         tek müdür karakteri yeter, kelime çifti yalnızca sözlükte bilgi amaçlı), bunu bir
         yorum/notla açıkça belgelemek — şu an sessiz bir boşluk olarak duruyor.
Dayanak: Y2-T1 müfredatı a) Target Vocabulary, People in the school: "a headmaster/headmistress".
```

```
[CİDDİ] [kapsam-boşluğu] data/grade2/school-life.json:inf-4 → hedef kelime "kid"
Sorun  : "a kid" müfredatta ayrı bir hedef kelime olarak listeleniyor ama 51 metinde yalnızca
         inf-4/sentences[3]'te bir kez geçiyor ("He is a kid."), hiçbir soruda kullanılmıyor
         (ne `q`, ne `correct`, ne `wrong`, ne `hint` alanında).
Öneri  : "Boy/girl/pupil/friend" ile dönüşümlü kullanılan birkaç metinde "kid" kelimesini de
         eşanlamlı olarak kullanmak (ör. scan/skim'in tekrarlayan "We are pupils/friends!"
         kapanışlarından birini "We are happy kids!" yapmak) kapsamı 1'den en az 4-5'e çıkarır.
Dayanak: Y2-T1 müfredatı a) Target Vocabulary, People in the school: "a kid".
```

### Yerler (a) Places in school

| Kelime | Eşleşme | Durum |
|---|---|---|
| a classroom | 69 | ✅ |
| a lunch hall | 16 | ✅ |
| a canteen | 20 | ✅ |
| a library | 72 | ✅ |
| a sports hall | 21 | ✅ |
| a garden | 78 | ✅ |
| a playground | 33 | ✅ |
| a teacher's room | 18 | ✅ |

**Bulgu yok.** Yerler kategorisi kusursuz kapsanmış, hiçbir kelime eksik veya zayıf değil.

### Haftanın günleri

| Gün | Eşleşme |
|---|---|
| Monday | 31 |
| Tuesday | 13 |
| Wednesday | 10 |
| Thursday | 11 |
| Friday | 25 |
| Saturday | 15 |
| Sunday | 16 |

Kullanıcı onayı gereği (7 günün tamamı hedef) — **bulgu yok, 7 gün de kapsanmış.** Monday (31) ve
Friday (25) diğerlerine (10-16 aralığı) göre belirgin biçimde daha sık; bu, "hafta başı/hafta
sonu eşiği" anlatısal çerçevesinin doğal bir sonucu (Monday = okul haftasının başlangıcı, Friday =
"eğlenceli gün" kalıp cümlesi çoğu metinde tekrarlanıyor). CİDDİ değil, STİL notu:

```
[STİL] [kapsam-boşluğu] tema geneli
Sorun  : Wednesday/Thursday (10-11 eşleşme) diğer günlere göre yarı yarıya daha az tekrarlanıyor.
Öneri  : Gerekirse değil — 10 eşleşme bir 2. sınıf öğrencisi için zaten yeterli tekrar. Bilgi
         amaçlı not.
Dayanak: Pedagojik denge, zorunlu değil.
```

### Milli/dini gün ve bayramlar

| Gün | Eşleşme | Kendine ait metin |
|---|---|---|
| Republic Day (29 Ekim) | 9 | skim-10 |
| Children's Day (23 Nisan) | 7 | scan-10 |
| Victory Day (30 Ağustos) | 10 | int-10 |
| Democracy [and National Unity] Day (15 Temmuz) | 3 | scan-13 |
| Youth [and Sports] Day (19 Mayıs) | 3 | inf-10 |
| Eid al-Fitr | 3 | skim-13 |
| Eid al-Adha | 3 | int-13 |

**Bulgu yok (kelime kapsamı) — ama tasarım deseni notu:**

```
[STİL] [kapsam-boşluğu] tema geneli — milli/dini gün dağılımı
Sorun  : Müfredattaki 7 özel günün her biri yalnızca TEK bir metne (ve TEK bir beceri grubuna)
         atanmış: Children's Day yalnızca scan'de, Republic Day yalnızca skim'de, Victory Day
         yalnızca int'de, Democracy Day yalnızca scan'de (2.), Youth Day yalnızca inf'de,
         Eid al-Fitr yalnızca skim'de (2.), Eid al-Adha yalnızca int'de (2.). Hiçbir özel gün
         scan+skim+int+inf'in tamamında işlenmiyor — bu yüzden ör. yalnızca "scan" pratiği yapan
         bir öğrenci Republic Day'i, Victory Day'i hiç görmeden geçebilir.
Öneri  : Kasıtlı bir "genişlik > derinlik" tasarımıysa sorun değil (7 gün havuzunu 51 metne
         yaymak makul bir strateji). Ama derinlik isteniyorsa, en azından en önemli 2 gün
         (Republic Day, 23 Nisan) her beceri grubunda birer metinle güçlendirilebilir.
Dayanak: Müfredat bunu açıkça belirtmiyor — tasarım tercihi, dayatma değil.
```

## 3. Alt tema dağılımı (51 metin üzerinden, kullanıcı onayı ile)

| Alt tema | scan | skim | int | inf | Toplam | Grup içi % |
|---|---|---|---|---|---|---|
| Greetings/introductions (selamlaşma, tanışma, yeni öğrenci, kibarlık) | 4 (1,7,8,11,12→~5) | 5 | 6 | 4 | ~20 | ~39% |
| People & places at school | 5 | 3 | 3 | 5 | ~16 | ~31% |
| Days of the week | 2 | 2 | 2 | 2 | 8 | ~16% |
| National/religious days | 2 | 2 | 2 | 1 | 7 | ~14% |

*(Sınıflandırma başlık/konu okumasıyla elle yapıldı; bazı metinler birden fazla alt temaya
dokunduğu için —ör. scan-11 hem selamlaşma hem gün— en baskın temaya atandı, kesin sınır yok.)*

**Bulgu:** Dağılım kaba biçimde dengeli — hiçbir alt tema tamamen ihmal edilmemiş, hiçbiri de
%50'yi aşacak kadar baskın değil. "Days of the week" ve "National/religious days" diğer ikisine
göre biraz daha az yer kaplıyor (%14-16 vs %31-39) ama bu, müfredatın kendi kelime listesi
büyüklüğüyle orantılı (günler=7 kelime, milli günler=7 kavram vs. kişi+yer=15 kelime) — CİDDİ bir
dengesizlik değil.

## 4. İleri sızıntı — bkz. ayrı rapor

[02-sizinti-raporu.md](02-sizinti-raporu.md) — 6 doğrulanmış CİDDİ sızıntı bulgusu (ordinal
tarih kalıbı × 5 metin, edat "on" × 1 metin).

## Özet tablo

| Kontrol | Sonuç |
|---|---|
| Yıldız yapı kapsamı (10/10) | ✅ Hepsi işlenmiş, 2'si ince |
| Kişi kelimeleri (8/8) | ⚠️ 1 hiç yok (headmistress), 1 neredeyse yok (kid) |
| Yer kelimeleri (8/8) | ✅ Kusursuz |
| Haftanın günleri (7/7) | ✅ Hepsi var |
| Milli/dini günler (7/7) | ✅ Hepsi var, ama derinlik değil genişlik stratejisiyle |
| Alt tema dağılımı | ✅ Kaba dengeli |
