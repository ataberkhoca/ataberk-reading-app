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
fs.cpSync(path.join(ROOT, 'data'), path.join(WWW, 'data'), {
  recursive: true,
  // .claude/ is Claude Code tooling config, not app content — never ship it.
  filter: (src) => !src.split(path.sep).includes('.claude'),
});
fs.copyFileSync(path.join(ROOT, 'manifest.json'), path.join(WWW, 'manifest.json'));

// sw.js'in CACHE_NAME'ini her build'de tazeler — aksi halde dosya byte-byte aynı
// kaldığı için tarayıcı yeni bir service worker sürümü olduğunu hiç fark etmez ve
// eski önbellek (dolayısıyla eski reading-skills.html) sonsuza kadar sunulmaya devam eder.
const swSrc = fs.readFileSync(path.join(ROOT, 'sw.js'), 'utf8');
const buildId = new Date().toISOString().replace(/[:.]/g, '-');
const swOut = swSrc.replace(/const CACHE_NAME = '[^']*';/, `const CACHE_NAME = 'ataberk-hoca-${buildId}';`);
fs.writeFileSync(path.join(WWW, 'sw.js'), swOut);

fs.copyFileSync(path.join(ROOT, 'icon-512.png'), path.join(WWW, 'icon-512.png'));

console.log('www/ senkronize edildi: index.html + data/ + manifest.json + sw.js (yeni cache sürümü) + icon-512.png');
