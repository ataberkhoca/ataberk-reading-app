# Session Summary — Full App Audit & Fix (2026-08-17)

**Purpose of this file:** a self-contained handoff document. Paste this into a fresh Claude
conversation and it explains everything that happened today without needing the other 15 audit
reports in `denetim/`. Written in English for portability; the underlying audit files and app
content are in Turkish/English (the app teaches English to Turkish-speaking children).

## What the app is

`ataberk-reading-app` is an English-learning reading app for Turkish primary-school children
(Grades 2-4 / "Y2-Y4"). Content lives in 18 JSON files (`data/grade2/*.json`,
`data/grade3/*.json`, `data/grade4/*.json`) — one file per grade × theme (6 themes each). Each
file holds ~40-51 short reading "texts," split into 4 skill groups (`scan`, `skim`, `int`,
`inf` = scanning / skimming / intensive reading / inference), each text with `sentences`
(English), `translations` (Turkish), and `questions` (with `q`/`qTr`, `correct`, `wrong[]`,
`hint`, `hl`). 761 texts total across the whole app.

## What was asked

Two phases, back to back:

1. **Independent audit** — act as an external MEB YEĞİTEK-style reviewer + parent/teacher,
   checking all 761 texts against a supplied curriculum map (`MÜFREDAT DOSYASI.md`) for content
   errors, curriculum-sequencing leaks (grammar/vocabulary used before its official introduction
   point), hint-answer leakage, cast/character consistency, and schema completeness. Read-only —
   never touch the data files, only write findings to `denetim/`.
2. **Fix everything found** — once the audit was complete, the read-only constraint was lifted
   and every concrete, verifiable finding was fixed directly in the data files.

## Methodology

- Automated scripts for the mechanical checks: `checker.py`/`checker_all.py` (JSON schema
  validity, required fields), `curriculum_leak_scan.py` (regex scan for curriculum-order
  violations against the supplied map), `coverage_scan.py` (target-vocabulary coverage per
  theme).
- Every automated hit was **read by hand** and classified real/false-positive — the scripts
  cast a wide net (plain regex), so most raw hits are noise (e.g. "morning" matching an "-ing"
  progressive-tense regex). Two very noisy categories (irregular past tense: 1,375 raw hits;
  many/much/a lot of: 352 raw hits) were sampled rather than individually read — disclosed, not
  hidden.
- All 761 texts (`sentences`, `translations`, `questions`, `hint`) were read line-by-line by a
  human-equivalent full pass, not just scanned — this is how the KRİTİK logic error and the
  cast-consistency bugs were found; scripts can't catch "the story says X but the marked-correct
  answer is the opposite of X."
- Every fix was applied via small Python scripts (never hand-edited JSON), each one asserting
  the *exact* old value before writing the new one — so a script either fixes precisely what it
  claims to, or crashes loudly. Nothing was silently overwritten.
- After every batch of fixes: re-ran `checker_all.py`, re-validated JSON parses, and reviewed
  `git diff --stat` to confirm the diff was minimal (see the indent-mismatch story below).

## What was found and fixed (all confirmed via `checker.py` = 0/761 findings)

| # | Category | Count | What it was | Fix |
|---|---|---|---|---|
| 1 | **KRİTİK logic error** | 1 text | A story explicitly says a character's request was denied ("No, you can't"), but the marked-correct answer to "Where is Eda?" was "Outside" — contradicting the story | Reworded question to "What does Eda want to do?" → "Go outside" |
| 2 | **q/qTr mismatch** | 3 questions | English question and its Turkish "translation" field asked completely different things (leftover from a template edit) | Rewrote the 3 Turkish translations to match the real English question |
| 3 | **Hint answer-leakage** | 37 findings / 40 questions | Hints in the "inference" skill group stated the answer directly instead of guiding elimination (violates the whole point of an inference exercise) | Rewrote every leaking hint to either pure elimination ("not X, not Y") or a redirect-to-text style ("look at the sentence", "remember") |
| 4 | **Missing `qTr` translations** | 403 questions | Two entire files (Y4 Classroom Life, Y4 Homes & Houses = 400 questions) had no Turkish translation field at all — app was silently falling back to showing the *hint* text instead when a student tapped "Turkish." Plus 3 stray gaps in another file. | Wrote a genuine, natural Turkish translation for every one of the 403 questions |
| 5 | **Cast/avatar inconsistency** | 20 texts, 4 files | A character speaks in the story but isn't listed in the `cast` array, so the app can't show their avatar. Includes finding an extra instance (7th) that an earlier automated pass had missed by manually re-reading every text. | Added the missing character (with their emoji, matched from elsewhere in the same file) to `cast` in all 20 texts |
| 6 | **Character emoji inconsistency** | 1 character, 3 files | Same teacher character drawn with 3 different emoji across 3 files | Unified to one emoji everywhere |
| 7 | **Ordinal-date curriculum leak** | 35 texts / 117 fields | "The 23rd of April" — ordinal date format is a Y4-level grammar point, but this exact phrasing appeared in "special day" texts across Y2 and Y3, one shared template copy-pasted 35 times | Rewrote every instance to plain "23 April" format (dropped "the", ordinal suffix, and "of") |
| 8 | **Smaller curriculum-order leaks** | 27 instances | "what kind of / which" (9), "something/anything" (6), "these/those" (5), "few/a little" (6), one stray "did" — all grammar structures used earlier than their official curriculum introduction point | Reworded each to a same-meaning phrasing that doesn't use the not-yet-taught structure |

**Total: ~530 individual field edits across 17 of the 18 data files.**

## What was deliberately NOT touched — and why

Three things were investigated, confirmed real, and then **left alone on purpose**:

1. **"Best/worst" (18 uses, 3 Y4 files)** — Read the actual texts before deciding. This isn't
   scattered vocabulary; it's load-bearing plot content (e.g. a whole text is built around an
   annual "best teacher" school award). "Fixing" it means rewriting narrative content in ~18
   places, not patching a bug — real risk of introducing new errors, and a decision that belongs
   to whoever owns the curriculum, not something to force through mechanically.
2. **"any" quantifier (14 uses, concentrated in one Y3 file)** — One text is *literally titled*
   "Some and Any in Our Bags" and is a deliberate, systematic some/any drill repeated across 4
   items. This is intentional lesson content that happens to be one theme ahead of where the
   curriculum map says it should be — same reasoning as #1.
3. **8 missing target vocabulary words in one Y3 theme** (grandson, granddaughter, men,
   woman/women, put on, study, do homework) — never appear anywhere in that theme's 43 texts.
   This is a content-*addition* task (writing new sentences), qualitatively different from every
   fix above, which were all corrections to existing content.

The honest open question behind #1 and #2: they only count as "wrong" if the curriculum
sequencing is meant to be followed strictly text-by-text. Given how deliberately each is
constructed, it's just as plausible the *curriculum map* should be updated to reflect these as
intentional early-introductions, rather than the app content being rewritten. That's a call for
whoever owns the curriculum design, not something to decide unilaterally by editing story
content.

## Two mistakes I made and caught mid-session (transparency)

1. Twice, when adding fields to already-large files, I used the wrong JSON indent width (1-space
   vs. the file's native 2-space), which would have silently reformatted the entire file on
   write. Caught both times via `git diff --numstat` showing an implausibly large change count
   before anything was left in a bad state; reverted and rewrote correctly.
2. One regex-based bulk fix (the ordinal-date one) had an edge case: "the 30th of **the month**"
   (a generic reference, not an actual month name) got mangled into "30 the month" by a
   substitution that assumed the word after "of" was always a month name. Caught it in a
   post-fix spot-check, reverted just that one line.

Both are recorded here rather than glossed over, per the same "don't inflate, don't hide"
standard applied throughout the audit itself.

## Current status

- `checker.py` (schema/completeness validator): **0 findings across all 761 texts, 18 files**
  (down from 403 at the start of the fixing pass).
- `curriculum_leak_scan.py` (curriculum-order regex scan): raw hit count dropped from 2,034 to
  1,890 after fixes — the difference (144) matches exactly the number of curriculum-leak fields
  fixed (117 ordinal-date + 27 smaller ones). The remaining raw hits are almost entirely the two
  intentionally-preserved clusters (any, best/worst) plus two categories that were sampled-clean
  from the start and never contained real leaks (irregular past tense, many/much/a lot of).
- All 17 touched data files re-validated as parseable JSON with clean, minimal git diffs.
- No data file was ever hand-edited — every change went through a Python script with an
  assertion on the old value, so every edit is exactly traceable.

## Where to look for more detail

Full findings, per-file pedagogical scoring, and the original audit methodology live in
`denetim/`:

- `04-pedagojik-rapor.md` — the original deep-dive template (Y2-T1, 51 texts, done first)
- `07-tum-uygulama-oynanis-raporu.md` — playthrough + cast-consistency scan, all 18 files
- `08-mufredat-sizinti-tum-uygulama.md` — the curriculum-leak findings (this file's fixes are #7
  and #8 above)
- `09-teknik-tum-uygulama.md` — schema/qTr findings (fix #4 above)
- `10-ipucu-tam-tarama.md` — hint-leakage findings (fix #3 above)
- `11-kapsam-tum-uygulama.md` — vocabulary coverage gaps (including the untouched item #3)
- `12-genel-ozet.md` — the master summary tying all reports together, kept up to date with
  ✅ DÜZELTİLDİ (fixed) markers throughout today's session
- `14-pedagojik-tum-uygulama.md` — full line-by-line read of all 710 remaining texts (found
  fixes #1, #2, and part of #5)
