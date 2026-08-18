#!/usr/bin/env node
// www/ Capacitor'ın kullandığı web varlıkları klasörüdür ve tamamen üretilmiş bir
// çıktıdır — asıl kaynak reading-skills.html + data/'dır. Bu script ikisini www/'a
// kopyalar; git'e alınmaz (bkz. .gitignore), her değişiklikten önce yeniden çalıştırılır.
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const WWW = path.join(ROOT, 'www');

fs.rmSync(WWW, { recursive: true, force: true });
fs.mkdirSync(WWW, { recursive: true });

fs.copyFileSync(path.join(ROOT, 'reading-skills.html'), path.join(WWW, 'index.html'));
fs.cpSync(path.join(ROOT, 'data'), path.join(WWW, 'data'), { recursive: true });

console.log('www/ senkronize edildi: index.html + data/');
