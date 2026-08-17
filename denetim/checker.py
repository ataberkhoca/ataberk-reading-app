# -*- coding: utf-8 -*-
"""
Y2-Tema1 (School Life) otomatik teknik denetim betiği.
Salt-okunur: data/grade2/school-life.json dosyasini okur, hicbir dosyayi degistirmez.
Cikti: denetim/checker_output.json (makine-okunur) + stdout ozet (insan-okunur, ASCII-guvenli).
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "data" / "grade2" / "school-life.json"

REQUIRED_TEXT_FIELDS = [
    "id", "title", "subtitle", "icon", "hlMode", "hintMode",
    "choices", "cast", "sentences", "translations", "questions",
]
REQUIRED_QUESTION_FIELDS = ["q", "qTr", "correct", "wrong", "hint", "hl"]
REQUIRED_CAST_FIELDS = ["e", "n"]

GROUPS = ["scan", "skim", "int", "inf"]


def load():
    with open(TARGET, encoding="utf-8") as f:
        return json.load(f)


def check_text(group, idx, item, all_ids, issues):
    loc = f"{group}[{idx}]"
    tid = item.get("id", f"<no-id:{loc}>")

    # 5. zorunlu alanlar
    missing = [k for k in REQUIRED_TEXT_FIELDS if k not in item]
    if missing:
        issues.append(dict(sev="KRITIK", cat="sema", id=tid, field="-",
                            msg=f"Zorunlu alan(lar) eksik: {missing}"))
        return  # devamini kontrol etmenin anlami yok

    # 6. id cakismasi
    if tid in all_ids:
        issues.append(dict(sev="KRITIK", cat="sema", id=tid, field="id",
                            msg=f"id cakismasi: '{tid}' birden fazla kez kullanilmis"))
    all_ids.add(tid)

    if tid != f"{group}-{idx+1}":
        issues.append(dict(sev="KUCUK", cat="sema", id=tid, field="id",
                            msg=f"id sirasi/adlandirmasi beklenenden farkli: beklenen '{group}-{idx+1}', bulunan '{tid}'"))

    sentences = item.get("sentences") or []
    translations = item.get("translations") or []

    # 2. sentences == translations sayisi
    if len(sentences) != len(translations):
        issues.append(dict(sev="KRITIK", cat="sema", id=tid, field="sentences/translations",
                            msg=f"sentences ({len(sentences)}) != translations ({len(translations)})"))

    # bos cumle kontrolu
    for i, s in enumerate(sentences):
        if not isinstance(s, str) or not s.strip():
            issues.append(dict(sev="CIDDI", cat="sema", id=tid, field=f"sentences[{i}]",
                                msg="Bos veya gecersiz cumle"))
    for i, t in enumerate(translations):
        if not isinstance(t, str) or not t.strip():
            issues.append(dict(sev="CIDDI", cat="sema", id=tid, field=f"translations[{i}]",
                                msg="Bos veya gecersiz ceviri"))

    # cast alan kontrolu
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

        # 4. correct, wrong icinde tekrar ediyor mu
        if correct in wrong:
            issues.append(dict(sev="KRITIK", cat="sema", id=tid, field=f"{qloc}.correct/wrong",
                                msg=f"correct ('{correct}') ayni zamanda wrong listesinde -> iki gecerli dogru sik"))

        # wrong icinde kendi icinde tekrar var mi
        if len(wrong) != len(set(wrong)):
            issues.append(dict(sev="CIDDI", cat="sema", id=tid, field=f"{qloc}.wrong",
                                msg=f"wrong listesinde tekrar eden sik: {wrong}"))

        # 7. soru sayisi / choices sema uyumu: choices = 1(correct) + len(wrong)
        if choices_n is not None:
            actual = 1 + len(wrong)
            if actual != choices_n:
                issues.append(dict(sev="CIDDI", cat="sema", id=tid, field=f"{qloc}.wrong",
                                    msg=f"choices alani {choices_n} ama fiili sik sayisi (correct+wrong)={actual}"))

        # 3. hl indeksleri sinir icinde mi
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


def main():
    issues = []
    counts = {}
    hlmode_values = {}
    hintmode_values = {}
    choices_values = {}

    try:
        data = load()
    except json.JSONDecodeError as e:
        print(f"KRITIK: JSON gecersiz -> {e}")
        sys.exit(1)

    all_ids = set()
    for group in GROUPS:
        items = data.get(group, [])
        counts[group] = len(items)
        for idx, item in enumerate(items):
            check_text(group, idx, item, all_ids, issues)
            hlmode_values.setdefault(item.get("hlMode"), 0)
            hlmode_values[item.get("hlMode")] += 1
            hintmode_values.setdefault(item.get("hintMode"), 0)
            hintmode_values[item.get("hintMode")] += 1
            choices_values.setdefault(item.get("choices"), 0)
            choices_values[item.get("choices")] += 1

    total = sum(counts.values())

    result = {
        "theme": data.get("theme"),
        "themeNumber": data.get("themeNumber"),
        "counts": counts,
        "total": total,
        "hlMode_dagilimi": hlmode_values,
        "hintMode_dagilimi": hintmode_values,
        "choices_dagilimi": choices_values,
        "issue_count": len(issues),
        "issues": issues,
    }

    out_path = Path(__file__).resolve().parent / "checker_output.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    # ASCII-guvenli stdout ozeti (Windows cp1254 konsollari icin)
    print(f"Tema: {result['theme']} (themeNumber={result['themeNumber']})")
    print(f"Grup sayilari: {counts} -> toplam {total}")
    print(f"hlMode dagilimi: {hlmode_values}")
    print(f"hintMode dagilimi: {hintmode_values}")
    print(f"choices dagilimi: {choices_values}")
    print(f"Toplam bulgu: {len(issues)}")
    sev_count = {}
    for iss in issues:
        sev_count[iss["sev"]] = sev_count.get(iss["sev"], 0) + 1
    print(f"Ciddiyet dagilimi: {sev_count}")
    print(f"Detay: {out_path}")


if __name__ == "__main__":
    main()
