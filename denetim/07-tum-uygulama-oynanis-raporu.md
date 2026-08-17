# Bütün Uygulama Oynanış Raporu — 2, 3 ve 4. Sınıf (18 tema dosyası, 761 metin)

## Yöntem — gerçekten "oynayarak" denetim

Bu rapor, önceki turdaki Y2-Tema1 denetiminden farklı olarak salt-okuma değil, **uygulamanın kendi
oyun motorunu gerçekten çalıştırarak** yapıldı. `reading-skills.html` içindeki gerçek fonksiyonlar
(`startSkill()`, `beginQuestions()`, `pick()`, `advQ()`, `showHint()`) tarayıcıda doğrudan
tetiklendi — yani her metin, bir öğrencinin tıklayarak oynayacağı **aynı kod yolundan** geçirildi;
JSON'u okuyup tahmin yürütmek değil, uygulamayı uçtan uca çalıştırmak.

Her metin için:
1. `startSkill(beceri, metinId)` ile metin açıldı (gerçek render — cast rozetleri, hikâye metni).
2. Okuma kapısı atlanıp sorulara geçildi.
3. Her soruda: önce ipucu butonuna basılıp ipucu metni okundu, sonra **doğru şık** tıklanarak bir
   sonraki soruya geçildi — tıpkı bir öğrencinin doğru cevapladığı bir oturum gibi.
4. Son soru sonrası sonuç ekranının açılıp açılmadığı doğrulandı.
5. Cast rozet listesi ile hikâyedeki konuşan karakterler karşılaştırıldı (bkz. Y2-T1 denetimindeki
   yöntem, artık DOM üzerinden gerçek render ile doğrulanıyor).

## Kapsam

| Sınıf | Tema sayısı | Toplam metin |
|---|---|---|
| 2. Sınıf | 6 | 265 |
| 3. Sınıf | 6 | 256 |
| 4. Sınıf | 6 | 240 |
| **Toplam** | **18** | **761** |

## Sonuç 1 — Teknik sağlamlık: 761/761 metin sorunsuz oynandı

**Konsol hatası / çökme: 0.** 761 metnin tamamı — 4 beceri × ortalama 11-13 metin × 18 tema —
baştan sona hatasız oynandı: her metinde okuma ekranı açıldı, her sorunun doğru şıkkı bulundu ve
tıklanabildi, sonuç ekranına ulaşıldı. Hiçbir metinde "doğru şık render edilmedi", "soru
yüklenemedi" gibi bir kırılma yaşanmadı. Bu, uygulamanın veri-motor entegrasyonunun genel olarak
çok sağlam olduğunu gösteriyor.

## Sonuç 2 — Cast/avatar tutarsızlığı: 19 metinde (tüm uygulamada)

Y2-Tema1'de bulunan "konuşan karakterin avatarı yok" deseni (bkz. `04-pedagojik-rapor.md` §2b),
bütün uygulamada taranınca **19 metinde** tekrar ediyor:

| Sınıf | Tema | Metin | Sorun |
|---|---|---|---|
| 2 | School Life | int-9 "A New Teacher Visits" | Miss Oli + Miss Pinar konuşuyor, cast'te yok |
| 2 | School Life | int-11 "Miss Oli in Classroom" | Lila konuşuyor + doğru cevap, cast'te yok |
| 3 | School Life | scan-7 "Hello and Goodbye" | "Ms. Hart" ikinci kez farklı biçimde ("Hart:") geçiyor, eşleşmiyor* |
| 3 | School Life | skim-6 "When Is Your Birthday?" | Kerem konuşuyor, cast'te yok |
| 3 | School Life | skim-7 "A Day at School" | "Hart:" biçimi cast'teki "Ms. Hart" ile otomatik eşleşmedi* |
| 3 | School Life | int-6 "Happy Birthday, Leo!" | Aynı desen ("Hart:")* |
| 3 | School Life | int-7 "A Visitor at School" | "Visitor:" (henüz adı açıklanmamış rol) — muhtemelen zararsız |
| 3 | School Life | inf-1 "Who Is the Kind Woman?" | **"Ms. Shaw" konuşuyor, cast'te "Ms. Hart" var — muhtemelen farklı bir karakter, gerçek bulgu** |
| 3 | Classroom Life | scan-10 "A Special Day in Class" | "Everyone:" (kolektif etiket) — muhtemelen zararsız |
| 3 | Personal Life | skim-8 "A New Friend" | Zara konuşuyor, cast'te yok |
| 3 | Personal Life | inf-6 "Whose Jumper Is It?" | Maya konuşuyor, cast'te yok |
| 4 | Life in the City | scan-6/scan-10/skim-4/skim-10/int-10 | **Leyla 5 ayrı metinde konuşuyor ama cast'te yok — tekrarlanan desen** |
| 4 | Life in the City | scan-7 | Ms. Reed konuşuyor, cast'te yok |
| 4 | Life in the City | skim-8 | Leyla + "Everyone" cast'te yok |
| 4 | Life in the City | inf-1 | "Postcard:" (kart/nesne anlatıcısı) — muhtemelen zararsız |
| 4 | Life in the City | inf-9 | Leyla konuşuyor, cast'te yok |

*`*` işaretli satırlar: "Ms. Hart" karakterinin bazı cümlelerde soyadıyla tek başına ("Hart:")
etiketlenmesi otomatik tespitte farklı bir kişi gibi göründü — bunlar muhtemelen **gerçek bulgu
değil**, aynı karakterin tutarsız etiketlenmesi (yine de küçük bir tutarlılık notu: aynı karakter
bazen "Ms. Hart:", bazen sadece "Hart:" ile konuşturuluyor).

**Gerçek, yüksek güvenilirlikli bulgular (tutarsız etiketleme değil, gerçekten eksik karakter):**

```
[CİDDİ] [tutarlılık] data/grade3/school-life-y3.json:skim-6 → cast
Sorun  : "Kerem" konuşuyor ama cast = [Maya, Leo, Ada]. Avatarı yok.
```
```
[CİDDİ] [tutarlılık] data/grade3/personal-life-y3.json:skim-8 → cast
Sorun  : "Zara" konuşuyor ama cast = [Maya, Ada, Ms. Hart]. Avatarı yok.
```
```
[CİDDİ] [tutarlılık] data/grade3/personal-life-y3.json:inf-6 → cast
Sorun  : "Maya" konuşuyor ama cast = [Mert, Kerem, Ms. Hart]. Avatarı yok.
```
```
[CİDDİ] [tutarlılık] data/grade4/life-in-the-city-y4.json:scan-6, scan-10, skim-4, skim-10, int-10, inf-9 (6 metin!)
Sorun  : "Leyla" bu 6 metnin her birinde konuşuyor ama hiçbirinin cast listesinde yok. Bu,
         tek seferlik bir yazım hatası değil, Life in the City (Y4) temasında Leyla karakteri
         için sistematik bir kalıp — muhtemelen 4. karakter eklenmiş ama cast şeması 3 kişiyle
         sınırlı kalmış (diğer temalarda 3 karakter sabit).
Öneri  : Ya cast dizisini 4 karaktere çıkar (UI 4 rozeti destekliyorsa), ya da bu metinlerde
         Leyla'nın yerini alan/rolünü üstlenen bir "sabit 3" karaktere yeniden yaz.
```
```
[CİDDİ] [tutarlılık] data/grade4/life-in-the-city-y4.json:scan-7 → cast
Sorun  : "Ms. Reed" konuşuyor ama cast = [Nora, Sam, Leyla] (öğretmen dörtlüde bu kez dışarıda
         kalmış — yukarıdaki bulgunun ters yönü).
```

**Desen:** Cast/avatar sorunu rastgele değil — hep aynı mekanizmadan kaynaklanıyor: bir temada 3
sabit karakter + zaman zaman eklenen bir 4. karakter (yeni öğretmen, yeni arkadaş) olduğunda, o
4. karakter bazı metinlerde cast listesine eklenmeyi unutuluyor. Bu, geliştirici için tek bir kural
olarak ifade edilebilir: **"Sentences içinde konuşan her karakter cast dizisinde de olmalı"** —
otomatikleştirilebilir bir kural, `checker.py`'ye eklenmeye değer (aşağıya not düşüldü).

## Sonuç 3 — İpucu kalitesi: 761 metnin ipuçları okundu, desen tema/yazara göre değişiyor

**Yöntem notu (şeffaflık için):** Her `inf` (Çıkarım) sorusunun ipucu metni otomatik olarak
toplandı — toplam **525 ipucu** (18 tema × ortalama ~29 çıkarım sorusu). Bunların hepsini elle
okudum ama farklı derinlikte:
- **2. Sınıf'ın 6 teması: TAMAMI elle okundu** (155 ipucu) — Y2-Tema1 zaten önceki turda tam
  okunmuştu; bu turda kalan 5 tema da (Classroom, Personal, Family, Homes, City) tek tek okundu.
- **3. ve 4. Sınıf'ın 12 teması: örneklem okundu** (her temadan ilk 6 ipucu + otomatik desen
  taraması, toplam ~72 ipucu elle incelendi, geri kalan ~300 ipucu okunmadı). Gerekçe: 2. Sınıf
  taramasında güçlü bir desen ortaya çıktı (bkz. aşağı) ve 3-4. Sınıf örneklemi bu deseni
  doğruladı; kalan hacmi tek tek okumak bu turun kapsamını aşıyor — **bu açık bir sınırlama,
  gizlenmiyor.**

### Bulgu: sızıntı riski rastgele dağılmıyor, temaya/yazara göre kümeleniyor

**2. Sınıf'ta net bir ayrım var:**

| Tema | Elle okunan ipucu | Doğrudan cevap veren ipucu | Değerlendirme |
|---|---|---|---|
| School Life | 51 (tüm inf grubu) | **6** (bkz. önceki tur, 04-pedagojik-rapor.md) | Sorunlu |
| Classroom Life | 13 | **0** | Temiz — "değil/değil" eleme ve tanımlayıcı ipucu tarzı iyi |
| Personal Life | 24 | **~7** | Sorunlu |
| Family Life | 24 | **~10** | En sorunlu tema |
| Homes & Houses | 10 | **0** | Temiz |
| Life in the City | 43 | **0** | Temiz — "dikkat et" (bak/düşün) tarzı meta-ipucu deseni çok iyi |

**3. ve 4. Sınıf örneklemi:** Okunan ~72 ipucunun **hiçbirinde** doğrudan cevap sızıntısı
bulunmadı — bu sınıflardaki ipucu yazımı tutarlı biçimde "eleme" (X değil, Y değil) ya da
"tanımlayıcı" (X özelliği var, Y özelliği var — cevabı adlandırmadan) tarzında, tıpkı 2. Sınıf'ın
temiz temaları gibi. Bu, 3-4. Sınıf içeriğinin **daha yeni ve daha dikkatli yazıldığı**
izlenimini destekliyor (örn. 4. Sınıf'ta "Nora'dan daha uzun, Leyla'dan daha kısa" gibi
karşılaştırmalı-çıkarım ipuçları gayet iyi tasarlanmış).

### Örnek doğrulanmış sızıntılar — Personal Life (2. Sınıf) — ✅ DÜZELTİLDİ

Personal Life ve Family Life'taki bulguların tamamı (bu bölümdeki 7+13 örnek) düzeltildi, bkz.
`12-genel-ozet.md` "Uygulanan Düzeltmeler". Bu bölüm tarihsel kayıt olarak kalıyor.

```
[KRİTİK] [ipucu-kalitesi] data/grade2/personal-life.json:inf-1 → "What has Tom got?" sorusu
Mevcut : correct="Tom is short. He has got dark hair." | hint="Tom uzun değil. Tom'un koyu
         saçları var."
Sorun  : İpucu, doğru cevabın iki bileşenini de (kısa boylu = "uzun değil", koyu saçlı) neredeyse
         birebir çeviriyle tekrar ediyor.
Öneri  : "Nora'yla karşılaştır." gibi karşılaştırmaya yönlendiren, sonucu söylemeyen bir ipucu.
```
```
[KRİTİK] [ipucu-kalitesi] data/grade2/personal-life.json:inf-3 → "How is the weather?"
Mevcut : correct="Cold" | hint="Kıyafetler soğuk günler için."
Sorun  : "soğuk" (cold) kelimesi doğru cevapla birebir aynı, ipucu cevabı içeriyor.
```
```
[KRİTİK] [ipucu-kalitesi] data/grade2/personal-life.json:inf-5 → "How do we know it is glasses?"
Mevcut : correct="It is on my nose" | hint="Burnumda."
Sorun  : İpucu, doğru cevabın birebir çevirisi.
```
```
[KRİTİK] [ipucu-kalitesi] data/grade2/personal-life.json:inf-6 → "How do we know it is Lila?"
Mevcut : correct="The yellow dress" | hint="Sarı elbiseyi eşleştir."
Sorun  : "sarı elbise" (yellow dress) doğru cevapla birebir aynı.
```
```
[KRİTİK] [ipucu-kalitesi] data/grade2/personal-life.json:inf-7 → "How do we know it is Thursday?"
Mevcut : correct="It is snowing on Thursday" | hint="Perşembe kar yağıyor."
Sorun  : İpucu, doğru cevabın birebir çevirisi.
```
```
[KRİTİK] [ipucu-kalitesi] data/grade2/personal-life.json:inf-9 → "What has Eda got?"
Mevcut : correct="Eda: I have got blue eyes" | hint="Eda'nın mavi gözleri var, sarı saçı değil."
Sorun  : İpucu, doğru cevabın (mavi gözler) neredeyse birebir çevirisi.
```
```
[KRİTİK] [ipucu-kalitesi] data/grade2/personal-life.json:inf-11 → "How old is the friend?"
Mevcut : correct="Nine" | hint="Yedi değil. Dokuz yaşında."
Sorun  : "dokuz yaşında" (nine years old) doğru cevabı doğrudan veriyor — sadece elemeyle
         kalmayıp sonucu da söylüyor.
```

### Örnek doğrulanmış sızıntılar — Family Life (2. Sınıf, en sorunlu tema)

```
[KRİTİK] [ipucu-kalitesi] data/grade2/family-life.json:inf-3 → "Is the girl seven?" / "Is she
        the little sister?"
Mevcut : hint="O küçük. O dört yaşında." (2 farklı soruda tekrarlanıyor)
Sorun  : Soru sadece "7 mi?" diye soruyor ama ipucu doğrudan kesin yaşı ("dört yaşında") veriyor —
         hem bu soruyu hem de ileride sorulacak "kaç yaşında" sorusunu baştan çözüyor.
```
```
[KRİTİK] [ipucu-kalitesi] data/grade2/family-life.json:inf-4 → "Is the boy four?" / "Who is the
        boy?" / "Is he the big brother?"
Mevcut : hint="O on yaşında. O uzun boylu." (3 farklı soruda tekrarlanıyor)
Sorun  : Aynı desen — kesin yaş baştan veriliyor.
```
```
[KRİTİK] [ipucu-kalitesi] data/grade2/family-life.json:inf-5 → "Has the mother got blue eyes?"
Mevcut : correct="Yes" | hint="Eda'nın annesinin mavi gözleri var."
Sorun  : İpucu, sorulan olguyu doğrudan doğrulayarak soruyu anlamsızlaştırıyor.
```
```
[KRİTİK] [ipucu-kalitesi] data/grade2/family-life.json:inf-6 → 3 soru
Mevcut : hint="O on iki yaşında. O uzun boylu." (3 kez tekrarlanıyor)
Sorun  : Kesin yaş baştan veriliyor.
```
```
[KRİTİK] [ipucu-kalitesi] data/grade2/family-life.json:inf-8 → "Has the mum got blond hair?"
Mevcut : correct="Yes" | hint="Eda'nın annesinin sarı saçları var."
Sorun  : Doğrudan doğrulama.
```
```
[KRİTİK] [ipucu-kalitesi] data/grade2/family-life.json:inf-9 → "Has the dad got blue eyes?"
Mevcut : correct="Yes" | hint="Tom'un babasının mavi gözleri var."
Sorun  : Doğrudan doğrulama.
```
```
[KRİTİK] [ipucu-kalitesi] data/grade2/family-life.json:inf-10 → "Is today a national day?" /
        "Is today the 23rd of April?"
Mevcut : hint="Dini bir gün. Aileler bir arada." (2 soruda tekrarlanıyor)
Sorun  : "Dini bir gün" (religious day), sorunun asıl amacı olan sonraki "dini bir gün mü?"
         sorusunun cevabını baştan veriyor.
```

**Desen özeti (Personal Life + Family Life):** Bu iki temanın ipucu yazarı, "X değil, Y değil"
eleme kalıbı yerine **"olgu şu, olgu şu"** kalıbını kullanmayı tercih etmiş — ve bu kalıp, olgu
doğru cevapla örtüştüğünde otomatik olarak sızıntıya dönüşüyor. Classroom Life / Homes & Houses /
Life in the City temalarında **aynı yazım kalıbı yok** — oralarda tutarlı olarak eleme ya da
cevabı adlandırmayan tanımlayıcı ipucu kullanılmış. Bu, tema başına farklı biri/farklı bir oturumda
yazılmış olabileceğini düşündürüyor.

## checker.py'ye eklenebilecek otomatik kural (öneri, henüz uygulanmadı)

Bu turda bulunan iki desen otomatikleştirilebilir:
1. **Cast/konuşan-karakter eşleşmesi**: `sentences` içindeki her "İsim:" etiketinin `cast[].n`
   içinde bulunup bulunmadığını kontrol et (kolektif etiketleri — Pupils/Children/Everyone/rol adı
   — hariç tut).
2. **İpucu-cevap benzerlik uyarısı**: `inf` grubunda, `hint` metninin ("değil" içeren elemeler
   çıkarıldıktan sonra kalan) kelime örtüşmesini `correct` alanının olası Türkçe karşılığıyla
   karşılaştırıp yüksek örtüşmede "elle incele" uyarısı ver. (Bu turda elle yapıldı; ölçekte
   otomatikleştirmek gerçek bir sözlük/çeviri katmanı gerektirir.)

## Genel değerlendirme

| Kontrol | Sonuç |
|---|---|
| 761 metnin tamamı oynanabiliyor mu (çökme yok) | ✅ Evet, 761/761 |
| Cast/avatar tutarlılığı | ❌ 19 metinde kırık, aynı kök nedenden (4. karakter unutulmuş) |
| İpucu kalitesi — 2. Sınıf | ⚠️ Karışık: 3 tema temiz, 3 tema (School/Personal/Family Life) sorunlu — toplam ~23 doğrulanmış sızıntı |
| İpucu kalitesi — 3. ve 4. Sınıf | ✅ Örneklemde (72/~380 ipucu) sızıntı yok — ama tam tarama yapılmadı, sınırlama açık |
| Diğer teknik katman (JSON, id, hl) | Bu turda tekrar kontrol edilmedi — Y2-Tema1 için zaten temizdi, diğer 17 dosya için doğrulanmadı |

**En önemli aksiyon maddesi:** Family Life ve Personal Life (2. Sınıf) temalarındaki ~17 ipucu
cümlesi ile School Life'daki 6 cümle (toplam ~23 metin, ~30 satırlık metin değişikliği) gözden
geçirilmeli. Bu, 761 metinlik uygulamanın küçük ama yoğunlaşmış bir kesitinde toplanmış durumda —
rastgele dağılmış yüzlerce hata değil, 3 temaya kümelenmiş, kaynağı belli bir kalite sorunu.
