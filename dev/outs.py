s = open('moves3d.html').read()
H = "const HYBRID = /[?&]hybrid\\b/.test(location.search);"; P = "const PAPER = HYBRID || /[?&]paper\\b/.test(location.search);"; R = "const READER = HYBRID || /[?&]reader\\b/.test(location.search);"
for x in (H, P, R): assert s.count(x) == 1, x
def out(name, h, p, r, title=None):
    t = s.replace(H, f"const HYBRID = {h};").replace(P, f"const PAPER = {p};").replace(R, f"const READER = {r};")
    if title: t = t.replace("<title>움직임 교과서</title>", f"<title>{title}</title>", 1)
    open(name, 'w').write(t)
out('paper.html', 'false', 'true', 'false')
out('reader.html', 'false', 'false', 'true', '움직임 교과서 · 글로 읽기')
out('hybrid.html', 'true', 'true', 'true')
L = "const LAB = /[?&]lab\\b/.test(location.search);"; assert s.count(L) == 1
open('lab.html', 'w').write(s.replace(L, 'const LAB = true;').replace('<title>움직임 교과서</title>', '<title>움직임 실험실</title>', 1))
print('outs ok')
