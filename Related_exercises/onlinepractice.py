from random import randint
count = 1
age=randint(1,11)
while count<=3:  #可以连续猜3次
    user_guess=int(input('your guess:'))
    if user_guess==age:
        print('Yes')
        break
    elif user_guess<age:
        print('small')
    else:
        print('big')
    count+=1
    if count==4:
        choice=input('do you want to continue:')
        if choice=='y':
            count=0  #继续玩的话重置为0