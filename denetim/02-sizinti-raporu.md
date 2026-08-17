# Sızıntı Raporu — Y2 Tema 1 (School Life)

Yöntem: `sentences`, `q`, `correct`, `wrong`, `hint`, `title`, `subtitle` alanlarının tamamı, Y2 Tema
2-6'da `[NEW]` olan yapılar için hem otomatik regex taramasıyla (colour, how many, possessive'ler,
can, how old, birthday, weather, have got, "on", some/any, tercih fiilleri, will/going to,
comparative, was/were, there is/are, present progressive) hem de 51 metnin tamamının satır satır
okunmasıyla tarandı. Karakter adı "Can" ile modal fiil "can" büyük/küçük harfe duyarlı ayrıştırıldı
(yanlış pozitif riski yüksekti — 120 ham eşleşmenin 120'si de karakter adıydı, gerçek modal "can"
kullanımı **0**).

## Bulgu 1 — Sıra sayı + tarih kalıbı ("the Nth of Month")

```
[CİDDİ] [ileri-sızıntı] data/grade2/school-life.json:scan-10 → sentences[0]
Mevcut : "Miss Oli: What day is it today? It is the 23rd of April."
Sorun  : "the 23rd of April" sıra sayı + tarih kalıbı, Y2'de hiç öğretilmiyor.
Öneri  : "Miss Oli: What day is it today? It is the 23rd of April." yerine müfredatın kendi
         tarih adlandırma biçimini kullan: "Miss Oli: What day is it today? It is 23 April!"
         (Tema 1'in hedef gün kalıbı zaten "It's/is Monday today" biçiminde asıl sayıyı değil,
         adı söylüyor; buradaki "the 23rd of April" hem sıra sayı hem de gereksiz "of" yapısı
         ekliyor.)
Dayanak: Sıra sayılar ("Ordinal numbers: 1st–30th") Y4-Tema2'de [NEW], tarihlerde sıra sayı
         kullanımı ("Dates with ordinal numbers") Y4-Tema3'te [NEW]. Y2 müfredatı milli günleri
         "23 April National Sovereignty and Children's Day" biçiminde, sıra sayı eki olmadan
         adlandırıyor.
```

```
[CİDDİ] [ileri-sızıntı] data/grade2/school-life.json:scan-13 → sentences[0]
Mevcut : "Eda: What day is it today? Can: It is the 15th of July."
Sorun  : Aynı sıra sayı + tarih kalıbı sızıntısı.
Öneri  : "Can: It is 15 July!" — sıra sayı ekini ve "of"u kaldır.
Dayanak: Yukarıdaki gibi (Y4-T2/T3 [NEW]).
```

```
[CİDDİ] [ileri-sızıntı] data/grade2/school-life.json:skim-10 → sentences[0]
Mevcut : "Can: What day is it today? Eda: It is the 29th of October."
Sorun  : Aynı kalıp.
Öneri  : "Eda: It is 29 October!"
Dayanak: Y4-T2/T3 [NEW].
```

```
[CİDDİ] [ileri-sızıntı] data/grade2/school-life.json:int-10 → sentences[0]
Mevcut : "Eda: What day is it today? Can: It is the 30th of August."
Sorun  : Aynı kalıp.
Öneri  : "Can: It is 30 August!"
Dayanak: Y4-T2/T3 [NEW].
```

```
[CİDDİ] [ileri-sızıntı] data/grade2/school-life.json:inf-10 → sentences[1], sentences[2]
Mevcut : "It is not the 23rd of April. It is not the 29th of October." / "It is the 19th of May."
Sorun  : Aynı kalıp, tek metinde 3 kez tekrarlanıyor (inference ipucu cümleleri).
Öneri  : "It is not 23 April. It is not 29 October." / "It is 19 May."
Dayanak: Y4-T2/T3 [NEW].
```

**Not:** Bu 5 metin de tam olarak müfredatın kendi hedef kalıbını ("What day of the week is it?
What day is it today? It's/is Monday today.") tarih sormak için yeniden kullanıyor — ama bu kalıp
müfredatta yalnızca **haftanın günü** için tanımlı, takvim tarihi için değil. Yani sorun yalnızca
sıra sayı sızıntısı değil, temanın kendi hedef cümle kalıbının amacı dışında (gün yerine tarih
sormak için) zorlanması. Düzeltme önerisi bu ikisini birden çözüyor: sıra sayıyı kaldırıp "It is
[gün] today, and it's [tarih]!" gibi iki ayrı, birbirine karışmayan cümleye bölmek daha güvenli
olurdu — ama en düşük müdahaleli çözüm yukarıdaki öneri (sadece sıra sayı ekini kaldırmak).

## Bulgu 2 — Edat "on" (Tema 3 yapısı)

```
[CİDDİ] [ileri-sızıntı] data/grade2/school-life.json:int-8 → sentences[8]
Mevcut : "Now it is end of day. Miss Oli: Goodbye! See you on Monday!"
Sorun  : Edat "on" (gün adıyla) Y2-Tema1'de yasak; Tema1 yalnızca "in" edatını hedefliyor.
         "on" ilk kez Y2-Tema3'te [NEW] olarak geliyor.
Öneri  : "Miss Oli: Goodbye! See you tomorrow!" — Tema 1'in kendi hedef sosyal ifadesi zaten
         "See you tomorrow!" (bkz. müfredat c) Social Language Expressions). Gün adıyla vedalaşma
         ihtiyacı yoksa bu ifadeye dönmek en temiz çözüm.
Dayanak: Y2 Tema 3, b) Target Grammar: "Preposition: on [NEW]." Tema 1'in kendi hedef edatı
         yalnızca "in" (bkz. 00-mufredat-haritasi.md §3, madde 3).
```

## Taranan ve TEMİZ çıkan kategoriler (bulgu yok)

Aşağıdaki yapı grupları hem regex hem elle okuma ile tüm 51 metin + 255 soru üzerinde tarandı,
**hiçbir örnekte ihlal bulunmadı**:

| Yapı | Kaynak tema | Sonuç |
|---|---|---|
| Renk sorma ("What colour…") | Y2-T2 [NEW] | 0 örnek |
| "How many…" | Y2-T2 [NEW] | 0 örnek |
| İzin isteme "Can I…" (modal *can*, küçük harf) | Y2-T2 [NEW] | 0 örnek — büyük/küçük harf ayrımıyla doğrulandı, 120 ham eşleşmenin tamamı karakter adı "Can" |
| "How old are you?" | Y2-T3 [NEW] | 0 örnek |
| "birthday" | Y2-T3 [NEW] | 0 örnek |
| Hava durumu (cold/hot/raining/snowing/weather) | Y2-T3 [NEW] | 0 örnek |
| have got / has got / 've got / 's got | Y2-T3/T4/T5/T6 [NEW] | 0 örnek |
| some / any (miktar belirteci) | Y2-T6 [NEW] | 0 örnek |
| Tercih fiilleri (like/love/hate/want + do you) | Y2-T6 [NEW] | 0 örnek |
| there is / there are | Y2-T5 [NEW] | 0 örnek |
| will / be going to | Y3-T6 / Y4-T6 [NEW] | 0 örnek |
| Karşılaştırma dereceleri (more/most/-er/-est) | Y4-T1/T3 [NEW] | 0 örnek |
| was / were (geçmiş zaman "to be") | Y4-T2 [NEW] | 0 örnek |
| Şimdiki zaman (is/are + V-ing, donmuş "morning" hariç) | Y3-T3/T5 [NEW] | 0 örnek — 6 ham eşleşmenin tamamı "It is morning" (isim, fiil değil) |
| İyelik sıfatları (my/his/her/its/our/their, "your" hariç) | Y2-T2 [NEW] | 0 örnek — 5 ham eşleşmenin tamamı Tema1'in kendi "My name is…" kalıbı |

## Belirsiz / karar gerektiren durum

```
[STİL] [ileri-sızıntı?] data/grade2/school-life.json:int-4 → sentences[2],[3] + questions[1],[2]
Mevcut : "Miss Oli: What day is after Tuesday? Can: It is Wednesday." / "What day is after
         Wednesday?"
Sorun  : Edat/zarf "after" ile gün sıralaması üretici biçimde soruluyor. Bu yapı ne Y2 ne de
         incelediğim Y3/Y4 müfredat dosyasında açık bir [NEW] madde olarak yer almıyor (en yakın
         akraba yapılar "during, between" Y4-Tema1'de [NEW]; "after" bu listede hiç geçmiyor).
Öneri  : Müfredatta "after" için açık bir zamanlama maddesi yoksa, bu tür sıralama sorularını
         "What day is it today?" / "Is Wednesday a school day?" gibi doğrudan hedef kalıplarla
         değiştirmek en güvenli seçenek. Yapı gerçekten kasıtlıysa (günleri sırayla öğretmenin
         doğal bir yolu olarak), bunun bilinçli bir tasarım kararı olduğunu bir yorumla not düşmek
         yeterli olur.
Dayanak: Müfredatta doğrulanamıyor — bu yüzden KRİTİK/CİDDİ değil, STİL/karar gerektiren durum
         olarak işaretliyorum. Sana danışıyorum: "after" kasıtlı bir tasarım kararı mıydı?
```

## Özet

| Ciddiyet | Sayı |
|---|---|
| CİDDİ (kesin ileri-sızıntı) | 6 (5 metinde ordinal-tarih + 1 metinde "on") |
| STİL (belirsiz, karar gerektiren) | 1 ("after") |
| **Toplam sağlam sızıntı** | **6** |

51 metin, 255 soru ve tüm alanlar (title/subtitle/sentences/q/correct/wrong/hint) tarandığında bulunan
sağlam ileri-sızıntı sayısı düşük (6/51 metin = metinlerin ~%12'si), ama tekrar eden aynı kalıp
(ordinal tarih) 5 ayrı metinde ortaya çıktığı için **rastgele bir yazım hatası değil, sistematik bir
tasarım seçimi** görünümünde — muhtemelen tüm milli/dini gün metinleri tek bir şablondan türetildi ve
şablonun kendisi hatalı. Düzeltme tek noktadan (şablon) yapılırsa 5 metin birden düzelir.
