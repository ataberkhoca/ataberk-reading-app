# -*- coding: utf-8 -*-
"""
17 dosya (Y2-T2..T6, Y3-T1..T6, Y4-T1..T6) icin mufredat "a) Target Vocabulary" listelerine
gore kelime kapsami taramasi. Y2-T1 zaten 03-kapsam-raporu.md'de ayrintili yapildi, burada
tekrar edilmiyor. Salt-okunur.
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FILES = [
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

# Sadece o temada YENI olan hedef kelimeler (recycled/background haric, mufredattan)
VOCAB = {
    'Y2-T2 Classroom Life': [
        'desk','table','smart board','blackboard','whiteboard','chair','bookcase','clock','door','window','wall',
        'pencil','coloured pencil','rubber','eraser','notebook','book','crayon','pencil case','sharpener','chalk','glue','scissors',
        'computer','tablet',
        'red','white','black','pink','blue','purple','yellow','brown','green','orange',
    ],
    'Y2-T3 Personal Life': [
        'leg','hand','arm','head','face','ear','eye','nose','mouth','hair',
        'big','short','long','small','tall','blond','dark',
        'shirt','t-shirt','trousers','dress','coat','shoes','hat','scarf','glasses','gloves','umbrella',
        'gift','birthday','monday','tuesday','wednesday','thursday','friday','saturday','sunday',
        'cold','hot','raining','snowing',
    ],
    'Y2-T4 Family Life': [
        'father','mother','sister','brother','grandfather','grandmother','baby','son','daughter','mum','dad',
        'nice','beautiful','handsome',
    ],
    'Y2-T5 Homes & Houses': [
        'bedroom','bathroom','sitting-room','sitting room','kitchen','garden','dining room','balcony','doorbell','dollhouse',
        'bed','sofa','coffee table',
        'pet','dog','cat','rabbit','bird','goldfish','fish',
        'tail','whiskers','claw','paw','beak',
        'dance',
    ],
    'Y2-T6 Life in the City': [
        'water','milk','ayran','tea','coffee',
        'tomato','banana','apple','orange','pear','strawberr','grape','cherr',
        'potato','carrot','bean','pepper','lettuce','cucumber','spinach','broccoli','garlic','cauliflower','courgette',
        'chicken','fish','bread','meat','egg',
    ],
    'Y3-T1 School Life': [
        'classmate','librarian','nurse','headteacher','caretaker',
        'art room','music room','meeting room','office','sports field','corridor','gym',
        'birthday party','candle','cake','balloon','surprise',
        'january','february','march','april','may','june','july','august','september','october','november','december',
        'prepare','decorate','write a song','play the guitar',
    ],
    'Y3-T2 Classroom Life': [
        "teacher's desk","student's desk",'bookshelf',"teacher's chair",'locker','basket','lights',
        'pen','ruler','coursebook','workbook','exercise book','map','school bag','paintbrush','bin','duster','flashcard','card',
        'keyboard','mouse','microphone',
        'life study','maths','turkish','music','sports','pe','english',
        'winner','prize',
        'grey','sunny','windy',
    ],
    'Y3-T3 Personal Life': [
        'foot','feet','back','tooth','teeth','chin','eyelash','eyebrow',
        'curly','straight',
        'little','strong','weak','pretty','fat','ugly',
        'happy','sad','lazy','hardworking','young','old',
        'sweatshirt','jumper','jeans','skirt','jacket','uniform','boots','necklace','earring','bag','sunglasses','socks',
    ],
    'Y3-T4 Family Life': [
        'cousin','aunt','uncle','parent','grandparent','grandson','granddaughter','child','children','man','men','woman','women',
        'wake up','wash','brush teeth','put on','have breakfast','go to school','study','have lunch','go home','have dinner','watch tv','read a book','play games','do homework','go to bed',
        'swim','basketball','football','piano','violin','chess',
        'cook','iron','wash the dishes','make the bed','garbage',
    ],
    'Y3-T5 Homes & Houses': [
        'cow','donkey','goat','horse','sheep','duck','turkey',
        'farmhouse','cottage','barn',
        'village','farm','field','tractor','grass','plant',
        'feed','bake','water','milk','garden','grow','collect',
    ],
    'Y3-T6 Life in the City': [
        'breakfast','lunch','dinner',
        'juice','cheese','cake','butter','pasta','soup','rice','salad','sandwich','pancake','toast','olive',
        'fast food','takeaway','restaurant','café','cafe','bill','waiter','waitress',
    ],
    'Y4-T1 School Life': [
        'counsellor',
        'assembly','attend','break','leave school',
        'club meeting','school play','sports day','talent show','parent-teacher meeting','field trip','main hall',
    ],
    'Y4-T2 Classroom Life': [
        'folder','board marker','calculator','highlighter','stapler','poster','chart','worksheet','activity book',
        'projector','speaker','printer','headphone',
        'social sciences','visual arts',
        'summer','autumn','winter','spring',
        'half past','quarter to','quarter past',
    ],
    'Y4-T3 Personal Life': [
        'stomach','moustache','beard','tongue','finger','neck','shoulder','knee','toe',
        'thick','thin','huge','fair','wavy','bright','medium','round',
        'angry','kind','funny','friendly','clever','quiet','brave','careful','naughty','sweet',
        'enjoy','prefer',
        'wardrobe','blouse','hoodie','shorts','leggings','sundress','raincoat','cardigan','sandals','slippers','flip-flops','trainers','flats','pyjamas','bracelet','ring','belt','helmet',
        'cloudy','foggy','cool','stormy','clear','misty','freezing','humid',
    ],
    'Y4-T4 Family Life': [
        'grandpa','grandma','mummy','daddy',
        'doctor','farmer','dentist','imam','police officer','scientist','singer','shop assistant','secretary','chef','writer','artist','cleaner','driver',
        'theatre','hospital','museum','bank','hotel','market','station','cinema','post office',"chemist's","hairdresser's","barber's","greengrocer's",'bakery',"butcher's",
    ],
    'Y4-T5 Homes & Houses': [
        'whale','shark','dolphin','sea turtle','jellyfish','octopus','crab','starfish','seal',
        'ocean','river','lake','sea','lagoon',
        'splash','dive','hide','crawl',
        'plastic','waste','fishing net','pollution','hunting','climate change',
        'beach house','lake house','houseboat',
    ],
    'Y4-T6 Life in the City': [
        'plum','lemon','yogurt','nuts','pea','turkey','brown rice',
        'chips','sweets','biscuit','soda','ice-cream','chocolate','noodles','burger','sausage','pizza','lemonade',
        'kebab','moussaka','taco','falafel',
        'italy','spain','greece','germany','mexico','algeria','azerbaijan',
    ],
}


def all_text(data):
    out = []
    for grp in ['scan', 'skim', 'int', 'inf']:
        for item in data.get(grp, []):
            for s in item.get('sentences', []):
                out.append(s)
            out.append(item.get('title', ''))
            out.append(item.get('subtitle', ''))
            for q in item.get('questions', []):
                out.append(q.get('q', ''))
                out.append(q.get('correct', ''))
                out.append(q.get('hint', ''))
                out.extend(q.get('wrong', []))
    return ' | '.join(out).lower()


def main():
    report = {}
    for grade, key, label in FILES:
        path = ROOT / 'data' / grade / f'{key}.json'
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        corpus = all_text(data)
        words = VOCAB.get(label, [])
        counts = {}
        for w in words:
            n = len(re.findall(re.escape(w.lower()), corpus))
            counts[w] = n
        zero = [w for w, n in counts.items() if n == 0]
        low = [w for w, n in counts.items() if n == 1]
        report[label] = {'counts': counts, 'zero': zero, 'low': low, 'total_words': len(words)}

    out_path = Path(__file__).resolve().parent / 'coverage_scan_output.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    for label, r in report.items():
        print(f"{label}: {r['total_words']} kelime tarandi -> {len(r['zero'])} hic yok, {len(r['low'])} sadece 1 kez")
        if r['zero']:
            print('   HIC YOK:', r['zero'])
        if r['low']:
            print('   1 KEZ:', r['low'])
    print('Detay:', out_path)


if __name__ == '__main__':
    main()
