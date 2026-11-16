import shutil, os, re
OUT = '/home/user/squat-coach/textbook'; NT = '../npmthree/node_modules/three'
os.makedirs(OUT + '/lib/addons/controls', exist_ok=True)
shutil.copy(NT + '/build/three.module.js', OUT + '/lib/three.module.js')
shutil.copy(NT + '/examples/jsm/controls/OrbitControls.js', OUT + '/lib/addons/controls/OrbitControls.js')
HEAD = '''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#14191c">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="../icon-192.png">
<link rel="apple-touch-icon" href="../icon-192.png">
'''
SW = '''
<script>
if ('serviceWorker' in navigator && location.protocol === 'https:') navigator.serviceWorker.register('sw.js').catch(() => {});
</script>
'''
def conv(src, dst, extra=()):
    s = open(src).read()
    s = s.replace('https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js', './lib/three.module.js')
    s = s.replace('https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/', './lib/addons/')
    s = s.replace('https://minable17-glitch.github.io/squat-coach/?', '../?')
    s = s.replace('https://claude.ai/artifact/SQSGVFbjwgGwjysAkuDZTQ', 'principles.html')
    s = s.replace('https://claude.ai/artifact/EeGvg8K49sdJwxZ39vaAwu', 'index.html')
    s = s.replace('https://claude.ai/artifact/VTb4fmJvBQxLvQemfLaPjg" target="_blank" rel="noopener"', 'train.html"')
    s = s.replace('https://claude.ai/artifact/F8EST5LxjPCbyUFHZevYqE" target="_blank" rel="noopener"', 'lab.html"')
    s = s.replace(' target="_blank" rel="noopener"><b>실험실 열기 →</b><span>새 창에서 열려요</span>', '><b>실험실 열기 →</b><span>트레이닝 원리 실험</span>')
    s = s.replace('학교 망에서 jsdelivr.net이 막혀 있는지 확인해 주세요.', '페이지를 새로고침해 주세요.')
    for a, b in extra: assert a in s, a; s = s.replace(a, b)
    assert 'jsdelivr' not in s.split('<script type="importmap">')[1][:300]
    open(dst, 'w').write(HEAD + s + SW)
conv('paper.html', OUT + '/paper.html')
conv('reader.html', OUT + '/reader.html')
conv('hybrid.html', OUT + '/hybrid.html')
conv('lab.html', OUT + '/lab.html', [("const BOOKU = /github\\.io$/.test(location.hostname) ? 'hybrid.html' : 'https://claude.ai/artifact/63vdMFpPEtReXDStqeoU7D';", "const BOOKU = 'hybrid.html';")])
conv('throw3d.html', OUT + '/throw.html', [('https://claude.ai/artifact/63vdMFpPEtReXDStqeoU7D" target="_blank" rel="noopener"', 'hybrid.html#throw"')])
t = open('train.html').read().replace("const BOOK = 'https://claude.ai/artifact/63vdMFpPEtReXDStqeoU7D';", "const BOOK = 'hybrid.html';").replace('href="https://claude.ai/artifact/63vdMFpPEtReXDStqeoU7D"', 'href="hybrid.html"')
assert "'hybrid.html'" in t
open(OUT + '/train.html', 'w').write(HEAD + '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>\n' + t + SW)
print('ok')
