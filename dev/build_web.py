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
    s = s.replace('https://claude.ai/artifact/EeGvg8K49sdJwxZ39vaAwu', 'classic.html')
    s = s.replace(' target="_blank" rel="noopener"><b>실험실 열기 →</b><span>새 창에서 열려요</span>', '><b>실험실 열기 →</b><span>트레이닝 원리 실험</span>')
    s = s.replace('학교 망에서 jsdelivr.net이 막혀 있는지 확인해 주세요.', '페이지를 새로고침해 주세요.')
    for a, b in extra: assert a in s, a; s = s.replace(a, b)
    assert 'jsdelivr' not in s.split('<script type="importmap">')[1][:300]
    open(dst, 'w').write(HEAD + s + SW)
conv('moves3d.html', OUT + '/classic.html')
shutil.copy('app.html', OUT + '/index.html')
conv('book3d.html', OUT + '/book.html')
conv('principles.html', OUT + '/principles.html', [('target="_blank" rel="noopener">움직임 교과서로 돌아가기', '>움직임 교과서로 돌아가기')])
print('ok')
