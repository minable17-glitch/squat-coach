import json, os
from PIL import Image
B='/tmp/claude-0/-home-user/56e6871c-77e2-5c3b-9252-55406b04879c/scratchpad/squat3d/bk/'; O='/home/user/squat-coach/textbook/'
d=json.load(open(B+'data.json'))
VERB={'squat':'앉기','lunge':'한 발 딛기','hinge':'숙이기','pushup':'밀기','pull':'당기기','plank':'버티기','throw':'던지기'}
img={}
for f in sorted(os.listdir(B+'shots')):
    k=f[:-4]; im=Image.open(B+'shots/'+f).convert('RGB'); w,h=im.size
    im=im.crop((int(w*.14),int(h*.06),int(w*.86),int(h*.9))); im.thumbnail((420,420)); im.save(O+'bookdemo/s/'+k+'.webp',quality=72); img[k]='bookdemo/s/'+k+'.webp'
img['squat-base-good']='bookdemo/g_squat.webp'; img['squat-base-valgus']='bookdemo/g_valgus.webp'; img['hinge-base-round']='bookdemo/g_lift.webp'
units=[]
for u in d['units']:
    u['verb']=VERB[u['m']]; u['sec']='Ⅰ. 몸의 움직임과 건강'
    for s in u['scenes']:
        if s['sc'].startswith('a_'): s['name']='양궁 '+s['name']
        for v in s['vars']: v['checks']=v['checks'][:5]
    units.append(u)
units.append({'m':'fitness','kind':'theory','verb':'체력 요소','name':'건강과 운동 체력','sec':'Ⅱ. 체력과 트레이닝','intro':'체력은 몸을 움직이는 힘이에요. 오래 달리는 힘, 무거운 것을 드는 힘, 몸을 잘 굽히는 힘처럼 여러 가지로 나뉘어요. 어떤 체력을 기르고 싶은지에 따라 운동 방법이 달라져요.','items':[
 {'name':'심폐지구력','scene':'s-fitness-base','img':'bookdemo/ill_cardio.webp','text':'심장과 폐가 산소를 온몸에 오래 보내는 힘이에요. 오래달리기·줄넘기·수영처럼 숨이 차는 운동을 꾸준히 하면 길러져요.'},
 {'name':'근력','scene':'s-fitness-strength','img':'bookdemo/ill_strength.webp','text':'근육이 한 번에 낼 수 있는 가장 큰 힘이에요. 조금 무거운 무게를 적은 횟수로 들어 기르고, 스쿼트·푸시업이 대표 운동이에요.'},
 {'name':'근지구력','scene':'s-fitness-endur','img':'bookdemo/ill_endur.webp','text':'근육이 같은 힘을 오래, 여러 번 낼 수 있는 힘이에요. 가벼운 무게를 여러 번 반복하거나 플랭크처럼 오래 버티며 길러요.'},
 {'name':'유연성','scene':'s-fitness-flex','img':'bookdemo/ill_flex.webp','text':'관절이 넓게 움직이는 능력이에요. 몸이 따뜻할 때 천천히 늘이는 스트레칭으로 길러요. 반동을 주지 않아요.'},
 {'name':'순발력','scene':'s-fitness-power','img':'bookdemo/ill_power.webp','text':'짧은 순간에 큰 힘을 내는 능력이에요. 제자리멀리뛰기·점프 스쿼트·공 던지기처럼 빠르고 힘찬 동작으로 길러요.'}]})
units.append({'m':'train','kind':'theory','lab':True,'verb':'트레이닝 원리','name':'트레이닝 원리','sec':'Ⅱ. 체력과 트레이닝','intro':'운동을 해도 체력이 늘지 않는다면 방법을 점검해 봐요. 다섯 가지 원리를 지키면 다치지 않고 꾸준히 좋아져요.','items':[
 {'name':'과부하의 원리','scene':'s-train-base','img':'bookdemo/ill_overload.webp','text':'평소보다 조금 더 무거운 무게나 많은 횟수로 운동해야 몸이 좋아져요. 바른 자세가 무너지지 않는 범위 안에서요.'},
 {'name':'점진성의 원리','scene':'s-train-prog','img':'bookdemo/ill_prog.webp','text':'몸이 좋아진 만큼 조금씩 강도를 올려요. 한꺼번에 많이 올리면 다치기 쉬워요.'},
 {'name':'반복성의 원리','scene':'s-train-repeat','img':'bookdemo/ill_repeat.webp','text':'꾸준히 되풀이해야 효과가 쌓여요. 운동을 멈추면 늘었던 체력도 다시 줄어요.'},
 {'name':'개별성의 원리','scene':'s-train-indiv','img':'bookdemo/ill_indiv.webp','text':'사람마다 체력과 몸이 달라서 알맞은 무게와 횟수도 달라요. 친구와 비교하지 말고 내 몸에 맞춰요.'},
 {'name':'특이성의 원리','scene':'s-train-speci','img':'bookdemo/ill_speci.webp','text':'운동한 부위와 체력만 좋아져요. 달리기를 잘하고 싶으면 달리기를, 팔 힘을 기르고 싶으면 팔 운동을 해요.'}]})
for u in units:
    if u['m'] in d.get('theory',{}): u['spread']=d['theory'][u['m']]
data={'units':units,'img':img,'lv':d['lv']}
t=open(B+'tpl.html').read().replace('/*STYLE*/',open(B+'style.css').read()).replace('/*DATA*/',json.dumps(data,ensure_ascii=False))
open(O+'book_demo.html','w').write(t); print('ok', len(img), len(t)//1024,'KB')
