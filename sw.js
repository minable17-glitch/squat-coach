// 한 번 받은 파일을 기기에 저장해서, 다음부터는 체육관 와이파이가 약해도 빨리 열리게 해요
const CACHE = 'squat-coach-v2';
const FILES = ['./', 'index.html', 'manifest.webmanifest', 'icon-192.png', 'icon-512.png', 'lib/vision_bundle.mjs', 'lib/supabase.js',
  'lib/wasm/vision_wasm_internal.js', 'lib/wasm/vision_wasm_internal.wasm', 'models/pose_landmarker_lite.task'];
self.addEventListener('install', e => e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)).then(() => self.skipWaiting())));
self.addEventListener('activate', e => e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith('squat-coach') && k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())));
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  if (e.request.method !== 'GET' || url.origin !== location.origin) return;
  if (e.request.mode === 'navigate') { e.respondWith(fetch(e.request).catch(() => caches.match('index.html'))); return; } // 화면은 새 버전 먼저
  e.respondWith(caches.match(e.request).then(hit => hit || fetch(e.request).then(res => { const copy = res.clone(); caches.open(CACHE).then(c => c.put(e.request, copy)); return res; })));
});
