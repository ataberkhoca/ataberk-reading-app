# -*- coding: utf-8 -*-
"""
Butun uygulama (18 tema dosyasi, Y2-Y4) icin checker.py'deki ayni sema/JSON kontrollerini
her dosyaya uygular. Salt-okunur.
Cikti: denetim/checker_all_output.json + stdout ozeti.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FILES = [
    ('grade2', 'school-life',            'Y2-T1 School Life'),
    ('grade2', 'classroom-life',          'Y2-T2 Classroom Life'),
    ('grade2', 'personal-life',           'Y2-T3 Personal Life'),
    ('grade2', 'family-life',             'Y2-T4 Family Life'),
    ('grade2', 'homes-houses',            'Y2-T5 Homes & Houses'),
    ('grade2', 'life-in-city',            'Y2-T6 Life in the City'),
    ('grade3', 'school-life-y3',          'Y3-T1 School Life'),
    ('grade3', 'classroom-life-y3',       'Y3-T2 Classroom Life'),
    ('grade3', 'personal-life-y3',        'Y3-T3 Personal Life'),
    ('grade3', 'family-life-y3',          'Y3-T4 Family Life'),
    ('grade3', 'homes-houses-y3',         'Y3-T5 Homes & Houses'),
    ('grade3', 'life-in-the-city-y3',     'Y3-T6 Life in the City'),
    ('grade4', 'school-life-y4',          'Y4-T1 School Life'),
    ('grade4', 'classroom-life-y4',       'Y4-T2 Classroom Life'),
    ('grade4', 'personal-life-y4',        'Y4-T3 Personal Life'),
    ('grade4', 'family-life-y4',          'Y4-T4 Family Life'),
    ('grade4', 'homes-houses-y4',         'Y4-T5 Homes & Houses'),
    ('grade4', 'life-in-the-city-y4',     'Y4-T6 Life in the City'),
]

REQUIRED_TEXT_FIELDS = [
    "id", "title", "subtitle", "icon", "hlMode", "hintMode",
    "choices", "cast", "sentences", "translations", "questions",
]
REQUIRED_QUESTION_FIELDS = ["q", "qTr", "correct", "wrong", "hint", "hl"]
REQUIRED_CAST_FIELDS = ["e", "n"]
GROUPS = ["scan", "skim", "int", "inf"]


def check_text(group, idx, item, all_ids, issues):
    loc = f"{group}[{idx}]"
    tid = item.get("id", f"<no-id:{loc}>")

    missing = [k for k in REQUIRED_TEXT_FIELDS if k not in item]
    if missing:
        issues.append(dict(sev="KRITIK", cat="sema", id=tid, field="-",
                            msg=f"Zorunlu alan(lar) eksik: {missing}"))
        return

    if tid in all_ids:
        issues.append(dict(sev="KRITIK", cat="sema", id=tid, field="id",
                            msg=f"id cakismasi: '{tid}' birden fazla kez kullanilmis"))
    all_ids.add(tid)

    if tid != f"{group}-{idx+1}":
        issues.append(dict(sev="KUCUK", cat="sema", id=tid, field="id",
                            msg=f"id sirasi/adlandirmasi beklenenden farkli: beklenen '{group}-{idx+1}', bulunan '{tid}'"))

    sentences = item.get("sentences") or []
    translations = item.get("translations") or []

    if len(sentences) != len(translations):
        issues.append(dict(sev="KRITIK", cat="sema", id=tid, field="sentences/translations",
                            msg=f"sentences ({len(sentences)}) != translations ({len(translations)})"))

    for i, s in enumerate(sentences):
        if not isinstance(s, str) or not s.strip():
            issues.append(dict(sev="CIDDI", cat="sema", id=tid, field=f"sentences[{i}]",
                                msg="Bos veya gecersiz cumle"))
    for i, t in enumerate(translations):
        if not isinstance(t, str) or not t.strip():
            issues.append(dict(sev="CIDDI", cat="sema", id=tid, field=f"translations[{i}]",
                                msg="Bos veya gecersiz ceviri"))

    for i, c in enumerate(item.get("cast", [])):
        miss = [k for k in REQUIRED_CAST_FIELDS if k not in c]
        if miss:
            issues.append(dict(sev="CIDDI", cat="sema", id=tid, field=f"cast[{i}]",
                                msg=f"cast objesinde eksik alan: {miss}"))

    choices_n = item.get("choices")
    questions = item.get("questions") or []
    if not isinstance(questions, list) or len(questions) == 0:
        issues.append(dict(sev="KRITIK", cat="sema", id=tid, field="questions",
                            msg="questions listesi bos veya yok"))

    for qi, q in enumerate(questions):
        qloc = f"questions[{qi}]"
        miss = [k for k in REQUIRED_QUESTION_FIELDS if k not in q]
        if miss:
            issues.append(dict(sev="KRITIK", cat="sema", id=tid, field=qloc,
                                msg=f"Zorunlu soru alani eksik: {miss}"))
            continue

        correct = q.get("correct")
        wrong = q.get("wrong") or []
        hl = q.get("hl") or []

        if correct in wrong:
            issues.append(dict(sev="KRITIK", cat="sema", id=tid, field=f"{qloc}.correct/wrong",
                                msg=f"correct ('{correct}') ayni zamanda wrong listesinde -> iki gecerli dogru sik"))

        if len(wrong) != len(set(wrong)):
            issues.append(dict(sev="CIDDI", cat="sema", id=tid, field=f"{qloc}.wrong",
                                msg=f"wrong listesinde tekrar eden sik: {wrong}"))

        if choices_n is not None:
            actual = 1 + len(wrong)
            if actual != choices_n:
                issues.append(dict(sev="CIDDI", cat="sema", id=tid, field=f"{qloc}.wrong",
                                    msg=f"choices alani {choices_n} ama fiili sik sayisi (correct+wrong)={actual}"))

        n_sent = len(sentences)
        for h in hl:
            if not isinstance(h, int) or h < 0:
                issues.append(dict(sev="KRITIK", cat="sema", id=tid, field=f"{qloc}.hl",
                                    msg=f"Negatif/gecersiz hl indeksi: {h}"))
            elif h >= n_sent:
                issues.append(dict(sev="KRITIK", cat="sema", id=tid, field=f"{qloc}.hl",
                                    msg=f"hl indeksi ({h}) sentences uzunlugunu ({n_sent}) asiyor"))

        if not hl:
            issues.append(dict(sev="CIDDI", cat="sema", id=tid, field=f"{qloc}.hl",
                                msg="hl listesi bos -> hangi cumleye dayandigi belirsiz"))

        for field in ("q", "correct", "hint"):
            v = q.get(field)
            if not isinstance(v, str) or not v.strip():
                issues.append(dict(sev="CIDDI", cat="sema", id=tid, field=f"{qloc}.{field}",
                                    msg=f"{field} bos veya gecersiz"))


def check_file(grade, key, label):
    path = ROOT / "data" / grade / f"{key}.json"
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return {"label": label, "error": f"JSON gecersiz: {e}"}
    except FileNotFoundError as e:
        return {"label": label, "error": f"Dosya bulunamadi: {e}"}

    issues = []
    counts = {}
    all_ids = set()
    for group in GROUPS:
        items = data.get(group, [])
        counts[group] = len(items)
        for idx, item in enumerate(items):
            check_text(group, idx, item, all_ids, issues)

    total = sum(counts.values())
    sev_count = {}
    for iss in issues:
        sev_count[iss["sev"]] = sev_count.get(iss["sev"], 0) + 1

    return {
        "label": label, "grade": grade, "key": key,
        "theme": data.get("theme"), "themeNumber": data.get("themeNumber"),
        "counts": counts, "total": total,
        "issue_count": len(issues), "severity": sev_count, "issues": issues,
    }


def main():
    all_results = []
    for grade, key, label in FILES:
        r = check_file(grade, key, label)
        all_results.append(r)

    out_path = Path(__file__).resolve().parent / "checker_all_output.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    grand_total_texts = 0
    grand_total_issues = 0
    for r in all_results:
        if "error" in r:
            print(f"{r['label']}: HATA -> {r['error']}")
            continue
        grand_total_texts += r["total"]
        grand_total_issues += r["issue_count"]
        flag = "OK" if r["issue_count"] == 0 else "BULGU VAR"
        print(f"{r['label']}: {r['total']} metin, {r['issue_count']} bulgu [{flag}] {r['severity']}")

    print()
    print(f"TOPLAM: {grand_total_texts} metin, {grand_total_issues} bulgu")
    print(f"Detay: {out_path}")


if __name__ == "__main__":
    main()
