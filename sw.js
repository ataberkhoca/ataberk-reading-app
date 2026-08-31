// İlkokul İngilizce Okuma Becerileri — offline service worker.
// Tüm uygulama (HTML + veri dosyaları) ilk ziyarette önbelleğe alınır,
// sonrasında internet olmadan da çalışır.
const CACHE_NAME = 'ataberk-hoca-v1';

const PRECACHE_URLS = [
  './',
  './index.html',
  './manifest.json',
  './icon-512.png',
  './data/grade2/classroom-life.json',
  './data/grade2/family-life.json',
  './data/grade2/homes-houses.json',
  './data/grade2/life-in-city.json',
  './data/grade2/personal-life.json',
  './data/grade2/school-life.json',
  './data/grade3/classroom-life-y3.json',
  './data/grade3/family-life-y3.json',
  './data/grade3/homes-houses-y3.json',
  './data/grade3/life-in-the-city-y3.json',
  './data/grade3/personal-life-y3.json',
  './data/grade3/school-life-y3.json',
  './data/grade4/classroom-life-y4.json',
  './data/grade4/family-life-y4.json',
  './data/grade4/homes-houses-y4.json',
  './data/grade4/life-in-the-city-y4.json',
  './data/grade4/personal-life-y4.json',
  './data/grade4/school-life-y4.json',
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches
      .open(CACHE_NAME)
      .then((cache) => cache.addAll(PRECACHE_URLS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// Cache-first for same-origin requests (app shell + data), network fallback
// for anything not precached (e.g. Google Fonts on first load). Cross-origin
// font requests are cached too so styling still works offline after that
// first successful load.
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;

  event.respondWith(
    caches.match(event.request).then((cached) => {
      if (cached) return cached;
      return fetch(event.request)
        .then((response) => {
          if (response && response.status === 200) {
            const copy = response.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(event.request, copy));
          }
          return response;
        })
        .catch(() => cached);
    })
  );
});
