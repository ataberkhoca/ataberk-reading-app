# Müfredat Haritası — Yıl 2 / Tema 1: School Life

> Aşama 1 çıktısı. Onay bekliyor — Aşama 3'e (içerik denetimi) geçilmedi.

## 0. Önemli konum notu (Aşama 0 bulgusu)

Oturumun çalışma dizini `data/grade4` idi, ama görev "Yıl 2 / Tema 1" istiyor. Proje içinde
klasör-yıl eşlemesi `reading-skills.html` içinde açıkça tanımlı (`GRADE_LABELS`: grade2 = "2. Sınıf",
grade3 = "3. Sınıf", grade4 = "4. Sınıf"; dosya adı sonekleri de bunu doğruluyor: grade3/4 dosyaları
`-y3`/`-y4` soneki taşırken grade2 dosyaları taşımıyor). Yani **Yıl 2 / Tema 1 = `data/grade2/school-life.json`**,
şu anki çalışma dizini olan `data/grade4` değil. Denetimin geri kalanı bu dosyayı hedef alıyor.
Bu eşlemeyi onaylıyor musun, yoksa kastettiğin başka bir dosya mı vardı?

## 1. Aşama 0 — Keşif sonucu

Tema 1 için tek içerik dosyası var (ayrı HTML/JS/CSS/oyun dosyası yok — uygulama tek parça
`reading-skills.html` üzerinden `fetch('data/' + grade + '/' + topic + '.json')` ile yüklüyor):

| Dosya | Boyut | Yapı |
|---|---|---|
| `data/grade2/school-life.json` | 5.893 satır / ~116 KB | `{ theme, themeNumber, scan[13], skim[13], int[13], inf[12], pre{stickers}, post{supporting,standard,expansion} }` |

Metin sayısı: **scan 13 · skim 13 · int 13 · inf 12 → toplam 51 metin.** Bu, denetim şablonunun
varsaydığı "10'luk grup → 40 toplam" hedefiyle **uyuşmuyor**; aşağıda not edildi (bkz. §5).

Her metin objesi şu alanları taşıyor: `id, title, subtitle, icon, hlMode, hintMode, choices, cast,
sentences, translations, questions` — şemadaki zorunlu alan listesiyle birebir eşleşiyor.

## 2. Temanın adı ve kapsamı

**THEME 1: SCHOOL LIFE**
Alt temalar: Greetings and introductions at school; people and places at school; days of the week;
national and religious days and celebrations.

## 3. Yıldızlar — `[NEW]` (bu temada ilk kez öğretilen yapılar)

Dil yapıları:
1. `What's/is it/this? It's/is a/an…` — nesne/yer sorma
2. `Who's she/he? She's Mr Aras. He's my English teacher. This is Mr/Mrs/Miss Hopkins. She/He is a teacher/headmaster.` — tanıtma, isim söyleme
3. `Where is she? She is in the garden.` — edat: **in**
4. `What's your name? I'm/am… / My name is…` — isim sorma/söyleme
5. `Come here, please.` (Emir kipi) — komut/rica/yönerge
6. `What day of the week is it? What day is it today? It's/is Monday today.` — haftanın günü sorma
7. Kişi zamirleri: I, he, she, it, we, you, they
8. İşaret zamiri: **this**
9. Soru sözcükleri: what, who, where
10. Selamlaşma: `Good morning! Hello! Hi! How are you? I'm fine, thanks! And you?`

Hedef kelime grupları (bunlar da bu temada ilk kez geliyor, dolayısıyla "yıldız" statüsünde):
- **Okuldaki kişiler:** a teacher, a pupil, a headmaster/headmistress, a friend, a boy, a girl, a kid
- **Okuldaki yerler:** a classroom, a lunch hall (lunchroom), a canteen, a library, a sports hall, a garden, a playground, a teacher's room
- **Milli/dini gün ve bayramlar [TR-CULTURE]:** 29 October Republic Day; 23 April National Sovereignty and Children's Day; 19 May Commemoration of Atatürk, Youth and Sports Day; 15 July Democracy and National Unity Day; 30 August Victory Day; Eid al-Fitr; Festival of Sacrifice (Eid-al-Adha)

Sosyal dil ifadeleri (Tema 1'e özgü, ilk kez): Excuse me!, Sorry!, That's OK!, Sure!, Goodbye!, Bye!,
See you tomorrow!, Hurray!, Welcome!, Well done!, Thank you!, Nice!, Really!, That's great!, Let's start!,
Look!, Good morning everybody!, Can I sit here?, Nice to meet you!

**Dikkat — belirsizlik:** "Days of the week" alt tema olarak sayılıyor ve dilbilgisi kalıbında
("It's Monday today") örnek gün adı geçiyor, ama Tema 1'in **a) Target Vocabulary** bölümünde günlerin
tam listesi (Monday…Sunday) açıkça verilmiyor — tam liste ilk kez Tema 3'ün kelime listesinde çıkıyor.
Yani müfredat metni Tema 1'de yalnızca "Monday" örneğini mi hedefliyor, yoksa yedi günün tümünü mü
bekliyor, açık değil. Bunu onayında netleştirmeni istiyorum çünkü kapsam kontrolü (§ eksik kelime
tespiti) bu karara göre değişir.

## 4. Dekor — `[BACKGROUND]` / geri dönen yapılar

**Yok.** Tema 1, Yıl 2'nin ilk temasıdır; müfredat metninde Tema 1 için hiçbir `[BACKGROUND]` veya
`[RECYCLED from …]` etiketi geçmiyor (geriye dönülecek önceki bir tema yok). Görevin kendi notuyla
tutarlı: bu temada tek risk ileri sızıntıdır.

## 5. Alt temalar ve 10'luk dağılım

Müfredat metni Tema 1 için **4 alt tema** listeliyor:
1. Greetings and introductions at school
2. People and places at school (kişi/yer olarak ayrılabilir)
3. Days of the week
4. National and religious days and celebrations

**Belirsizlik / dayanaksız varsayım:** Müfredat dosyası, bu 4 alt temanın 10 metinlik bir sete (ya da
51 metinlik gerçek sete) nasıl sayısal olarak dağıtılması gerektiğini **belirtmiyor**. Denetim
şablonundaki "hedef: 10 → toplam 40" ve "10'luk sete dağılım" maddeleri müfredattan değil, şablonun
kendi varsayımından geliyor — yani bu haliyle **"iç kural, müfredat dayanağı yok."** Gerçek uygulamada
grup başına metin sayısı 13/13/13/12 (toplam 51). Onayında bu sayıyı temel alıp alt tema dağılımını
oransal olarak mı değerlendireyim, yoksa senin belirleyeceğin başka bir hedef sayı mı var?

## 6. İleri-sızıntı sınırı — Y2 Tema 2-6'da `[NEW]` olan ve Tema 1'de YASAK olan yapılar

**Tema 2'den:**
- "What colour is it? It's/is blue." — renk sorma/söyleme
- "How many chairs? Five chairs." — sayı sorma
- İyelik sıfatları: my, his, her, its, our, your, their
- "Can I go outside? Can I go to the bathroom please? Yes, you can." — izin isteme/verme (`can`)

**Tema 3'ten:**
- "How old are you? I'm/am 7." — yaş sorma
- "Is it your birthday today? Yes, it is." — doğum günü
- "Is she tall? Yes, she is. No, she isn't/is not." — evet/hayır sıfat sorusu
- "How's the weather? It's cold." — hava durumu
- "What have you got? I've got a nose. How many ears have you got? I've got two ears." — have got/has got (vücut)
- "I've got blue trousers. I've got a purple shirt." — have got (giysi)
- Belirteçler a/an'in **açık öğretim konusu** olarak ele alınması (bkz. not aşağıda)
- Edat: **on**

**Tema 4'ten:**
- "What colour eyes has your mother got? My mother's/has got blue eyes." — 3. tekil şahısla has got

**Tema 5'ten:**
- "We've/have got a house. We've got two pets." — we + have got
- "There are five cats in the sitting room." — there is/there are

**Tema 6'dan:**
- "Do you like bread? Yes, I do. Do you like beans? No, I don't." — Simple Present (do/does ile tercih sorma)
- "I've/have got some beans." — quantifier "some" + have got

**Yıl 2'de hiç yer almayan, dolayısıyla iki kat yasak (yıl dışı) yapılar** (denetim şablonunun genel
listesinden, müfredatla doğrulanmış): geniş zamanda 3. tekil şahıs **-s** (Y2'de hiç `[NEW]` olarak
geçmiyor — ilk kez Y3-T4'te), **present progressive/şimdiki zaman** (Y2'de hiç yok — ilk kez Y3-T3/T5'te),
**could** (ilk kez Y3-T4'te), **karşılaştırma dereceleri/comparatives-superlatives** (ilk kez Y4-T1/T3'te),
**will** (ilk kez Y3-T6'da), **be going to** (ilk kez Y4-T6'da), **düzenli/düzensiz geçmiş zaman**
(ilk kez Y4-T3/T4'te).

**Metodolojik not (sızıntı taramasına yön verir):** "a/an" ve "some" gibi öğeler müfredatta bilinçli
olarak **örtük/otomatik kullanım** olarak tanımlanıyor ("taught without its logic; automatic use is
expected" — Tema 3 ve Tema 6). Yani Tema 1 metinlerinde "a teacher", "a classroom" gibi kaçınılmaz
tekil isim önekleri geçmesi **sızıntı sayılmaz** — bunlar kelime düzeyinde zaten kaçınılmaz. Asıl
sızıntı: yukarıdaki listedeki **üretken soru-cevap kalıplarının** (renk sorma, sayı sorma, izin isteme,
yaş sorma, hava durumu, have got, there is/are, do you like) Tema 1 metinlerinde **soru, cevap, ipucu
veya şık** olarak üretici biçimde kullanılmasıdır. Taramada bunu ayırt edeceğim.

## 7. Müfredatın belirttiği temalar arası bağlantılar (köprüler)

Kaynak metinde açıkça işaretlenmiş, Tema 1'i temel alan geri dönüşler:
- **Y2-T3:** `"What's/is it? It/This is a nose/a shirt."` — [RECYCLED from Theme 1]
- **Y2-T3:** `"What day is it today? It's/is Monday today."` — [RECYCLED from Theme 1]
- **Y2-T4:** `"Who is he? Who is she?"` — [RECYCLED "who" from Theme 1, yeni bağlam: aile]
- **Y2-T5:** `"Where's/is the bed? The bed is in the bedroom."` — [RECYCLED "where" from Theme 1, yeni bağlam: ev]
- **Y3-T1:** `"Who's/is this/she/he? This is Mr. Blue."` — [BACKGROUND from Y2-T1]
- **Y3-T1:** `"Where is Daphne? She's/is in the library."` — [BACKGROUND from Y2-T1]
- **Y3-T1:** Selamlaşma temeli (Good morning, Hello, Hi) [RECYCLED], milli/dini günler seti aynen [RECYCLED], okul kişi/yer kelimeleri revizyon kelimesi olarak [RECYCLED]

Yani Tema 1, ileriye doğru en az 5 ayrı noktada (Y2-T3 ×2, Y2-T4, Y2-T5, Y3-T1 ×2+) köprü kuruyor.
Pedagojik denetimde "köprü farkındalığı" ekseni bunları arayacak — ama Tema 1 kendisi ilk tema olduğu
için **kendi içine gelen** bir köprü yok, sadece **çıkan** köprüler var.

---

## Onay bekleyen 3 nokta
1. Hedef dosya `data/grade2/school-life.json` mi (yukarıdaki §0)?
2. "Days of the week" için tam 7 gün mü hedefleniyor, yoksa yalnızca "Monday" örneği mi (§3 dikkat notu)?
3. 10'luk dağılım şablon varsayımı mı kalsın (yoksayıp gerçek 13/13/13/12 üzerinden mi değerlendireyim), yoksa senin verdiğin başka bir hedef sayı mı var (§5)?

**Onayını/düzeltmeni bekliyorum — Aşama 3'e (içerik denetimi) onay gelmeden geçmiyorum.**
