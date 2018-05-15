#! -*- coding:utf-8 -*-
from random import choice
score=[0,0]
rest=[5,5] #5轮剩余机会
direction=['left','center','right']

def kick():
    print('------you kick------')
    print('choose one side to shoot')
    you=input(str())
    com=choice(direction)
    print('you choose '+you)
    print('com choose '+com)
    if you!=com:
        print('goal!!')
        score[0]+=1
    else:
        print('ohh no')
    print('you:com=%d : %d'%(score[0],score[1]))
    if rest[0]>0:  #如果在5轮之内
        rest[0]-=1  #机会-1
        #如果玩家落后，且加上剩余机会还落后
        if score[0]<score[1]and score[0]+rest[0]<score[1]:
            return True
        #如果电脑落后，且加上剩余机会还落后
        if score[1]<score[0]and score[1]+rest[1]<score[0]:
            return  True

    print('-----you save-------')
    print('choose one side you save')
    you=input(str())
    print('you choose '+you)
    com=choice(direction)
    print('com choose '+com)
    if you==com:
        print('saved')
    else:
        print('ohh no')
        score[1]+=1
    print('you:com=%d : %d' % (score[0], score[1]))
    if rest[1]>0:
        rest[1]-=1
        if score[0]<score[1]and score[0]+rest[0]<score[1]:
            return True
        if score[1]<score[0]and score[1]+rest[1]<score[0]:
            return  True
    return False  #正常情况下返回false，表示比赛未结束

i=0
end=False
while(i<5 and not end):   #如果没到5局，且没有结束
    print('=====Round %d====='%(i+1))
    end=kick()  #kick返回是否提前结束
    i+=1

while(score[0]==score[1]):
    print('=======Round %d====='%(i+1))
    kick()
    i+=1

if score[0]>score[1]:
    print('you win')
else:
    print('you lose')