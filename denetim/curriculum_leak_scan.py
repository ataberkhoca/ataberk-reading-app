# -*- coding: utf-8 -*-
"""
Butun uygulama (18 tema dosyasi, Y2-Y4) icin mufredat-tabanli ileri-sizinti taramasi.
Mufredat sirasina gore her dosya icin "henuz ogretilmemis" yapilar listesi hesaplanir,
ve sentences+q+correct+wrong+hint+title+subtitle alanlarinda bu yapilar aranir.
Salt-okunur: hicbir veri dosyasini degistirmez.
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Dosya sirasi = mufredat sirasi (Y2T1..Y2T6, Y3T1..Y3T6, Y4T1..Y4T6)
FILES = [
    (1,  'grade2', 'school-life',            'Y2-T1 School Life'),
    (2,  'grade2', 'classroom-life',          'Y2-T2 Classroom Life'),
    (3,  'grade2', 'personal-life',           'Y2-T3 Personal Life'),
    (4,  'grade2', 'family-life',             'Y2-T4 Family Life'),
    (5,  'grade2', 'homes-houses',            'Y2-T5 Homes & Houses'),
    (6,  'grade2', 'life-in-city',            'Y2-T6 Life in the City'),
    (7,  'grade3', 'school-life-y3',          'Y3-T1 School Life'),
    (8,  'grade3', 'classroom-life-y3',       'Y3-T2 Classroom Life'),
    (9,  'grade3', 'personal-life-y3',        'Y3-T3 Personal Life'),
    (10, 'grade3', 'family-life-y3',          'Y3-T4 Family Life'),
    (11, 'grade3', 'homes-houses-y3',         'Y3-T5 Homes & Houses'),
    (12, 'grade3', 'life-in-the-city-y3',     'Y3-T6 Life in the City'),
    (13, 'grade4', 'school-life-y4',          'Y4-T1 School Life'),
    (14, 'grade4', 'classroom-life-y4',       'Y4-T2 Classroom Life'),
    (15, 'grade4', 'personal-life-y4',        'Y4-T3 Personal Life'),
    (16, 'grade4', 'family-life-y4',          'Y4-T4 Family Life'),
    (17, 'grade4', 'homes-houses-y4',         'Y4-T5 Homes & Houses'),
    (18, 'grade4', 'life-in-the-city-y4',     'Y4-T6 Life in the City'),
]

# yapi: (tanitildigi_sira, etiket, regex, notlar)
STRUCTURES = [
    (2,  'renk sorma (what colour)',            r'\bwhat colou?r\b'),
    (2,  'how many',                             r'\bhow many\b'),
    (2,  'izin/modal can (kucuk harf)',           r'(?<![A-Za-z])can\b'),  # case-sensitive asagida ayrica kontrol edilecek
    (3,  'how old',                               r'\bhow old\b'),
    (3,  'birthday',                              r'\bbirthday\b'),
    (3,  'hava durumu kelimeleri',                r'\b(weather|raining|snowing)\b'),
    (3,  'have got / has got',                    r"('ve got|'s got|has got|have got)"),
    (3,  'edat "on"',                             r'(?<![A-Za-z])on\b'),
    (5,  'there is/are',                          r'\bthere (is|are)\b'),
    (6,  'quantifier "some"',                     r'\bsome\b'),
    (6,  'tercih fiilleri (like/love/hate/dislike)', r'\b(like|likes|love|loves|hate|hates|dislike|dislikes)\b'),
    (7,  'what month',                            r'\bwhat month\b'),
    (7,  "when's/when is (dogum gunu sorusu)",    r"\bwhen.?s\b|\bwhen is\b"),
    (7,  'must/mustn\'t',                         r"\bmust\b|\bmustn.?t\b"),
    (8,  "o'clock",                               r"o.?clock"),
    (9,  'whose',                                 r'\bwhose\b'),
    (9,  'what...like sorusu',                    r'what[^.?!]{0,25}\blike\?'),
    (9,  'simdiki zaman (is/are/am + Ving)',      r'\b(is|are|am)\s+\w+ing\b'),
    (10, 'could',                                 r'\bcould\b'),
    (10, 'how often',                             r'\bhow often\b'),
    (10, 'siklik zarflari (always/sometimes/often/never)', r'\b(always|sometimes|often|never)\b'),
    (11, 'at present',                            r'\bat present\b'),
    (12, 'will / \'ll',                           r"\bwill\b|\b[a-z]+'ll\b"),
    (12, 'quantifier "any"',                      r'\bany\b'),
    (13, 'superlative (-est / most)',             r'\b\w{4,}est\b|\bmost\b'),
    (13, 'during/between',                        r'\bduring\b|\bbetween\b'),
    (13, 'why/which/what kind of',                r'\bwhy\b|\bwhich\b|what kind of'),
    (13, 'these/those',                           r'\bthese\b|\bthose\b'),
    (13, 'because',                               r'\bbecause\b'),
    (14, 'was/were',                              r'\bwas\b|\bwere\b'),
    (14, 'yarim/ceyrek saat (half past/quarter to/past)', r'half past|quarter to|quarter past'),
    (14, 'sira sayi + tarih (the Nth of Month / Nth)', r'\bthe \d{1,2}(st|nd|rd|th)\b|\b\d{1,2}(st|nd|rd|th)\b'),
    (15, 'karsilastirma (-er than / more...than)', r'\b\w{3,}er than\b|\bmore \w+ than\b'),
    (15, 'something/anything',                    r'\bsomething\b|\banything\b'),
    (16, 'duzensiz gecmis zaman fiilleri',        r'\b(read|ate|went|saw|did|had|wrote|bought|came|took|gave|found|made|said|told|thought|knew|got|left|felt|kept|spoke|broke|chose|drove|flew|grew|threw|wore|paid|sold|rode|ran|sang|swam|drank|began|stood|understood|slept|met|sat|fell|heard|held|drew|taught|caught|brought|built|sent|spent|lent|bent|dealt|meant|lost|won)\b'),
    (17, 'should/shouldn\'t',                     r"\bshould\b|\bshouldn.?t\b"),
    (17, 'en iyi/en kotu (best/worst)',           r'\bbest\b|\bworst\b'),
    (17, 'many/much/a lot of',                    r'\bmany\b|\bmuch\b|a lot of'),
    (18, 'be going to (gelecek zaman)',           r'going to\b'),
    (18, 'few/a few/little/a little',             r'\ba few\b|\ba little\b|(?<!\w)few\b|(?<!\w)little\b'),
]

def load(grade, key):
    p = ROOT / 'data' / grade / f'{key}.json'
    with open(p, encoding='utf-8') as f:
        return json.load(f)

def all_fields(item):
    out = []
    for i, s in enumerate(item.get('sentences', [])):
        out.append((f'sentences[{i}]', s))
    out.append(('title', item.get('title', '')))
    out.append(('subtitle', item.get('subtitle', '')))
    for qi, q in enumerate(item.get('questions', [])):
        out.append((f'questions[{qi}].q', q.get('q', '')))
        out.append((f'questions[{qi}].correct', q.get('correct', '')))
        out.append((f'questions[{qi}].hint', q.get('hint', '')))
        for wi, w in enumerate(q.get('wrong', [])):
            out.append((f'questions[{qi}].wrong[{wi}]', w))
    return out

def main():
    results = {}
    for order, grade, key, label in FILES:
        try:
            data = load(grade, key)
        except Exception as e:
            results[label] = {'error': str(e)}
            continue
        forbidden = [(lbl, pat) for (intro, lbl, pat) in STRUCTURES if intro > order]
        file_hits = []
        for grp in ['scan', 'skim', 'int', 'inf']:
            for item in data.get(grp, []):
                tid = item.get('id')
                fields = all_fields(item)
                for lbl, pat in forbidden:
                    for fname, ftext in fields:
                        if not ftext:
                            continue
                        for m in re.finditer(pat, ftext, re.IGNORECASE):
                            # 'can' ozel durum: sadece kucuk harfli modal 'can' say (karakter adi "Can" degil)
                            if lbl.startswith('izin/modal can'):
                                # case-sensitive tekrar kontrol
                                if not re.search(r'(?<![A-Za-z])can\b', ftext):
                                    continue
                                # tam eslesen alt-parca buyuk harfle basliyorsa (karakter adi) atla
                                matched = ftext[m.start():m.end()]
                                if matched[:3] == 'Can':
                                    continue
                            file_hits.append({
                                'structure': lbl, 'id': tid, 'field': fname,
                                'text': ftext, 'match': ftext[m.start():m.end()]
                            })
        results[label] = {'hit_count': len(file_hits), 'hits': file_hits}
    out_path = Path(__file__).resolve().parent / 'curriculum_leak_scan_output.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    for label, r in results.items():
        if 'error' in r:
            print(f'{label}: HATA {r["error"]}')
        else:
            print(f'{label}: {r["hit_count"]} ham eslesme')
    print('Detay:', out_path)

if __name__ == '__main__':
    main()
