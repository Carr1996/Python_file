products=[['Iphone8',6888],['MacPro',14000],['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799]]
Shopping_box=[]
run_flag=True
while run_flag:
    print('---------商品列表---------')    #显示商品列表
    for index,p in enumerate(products):
        print('%s .  %s   %s'%(index,p[0],p[1]))

    choice=input('choose what you want:')
    if choice.isdigit():
        choice = int(choice)
        if choice>=0 and choice<6:
            Shopping_box.append(products[choice])
            print('you have added this: %s'%products[choice])
        else:
            print('this goods not exits')
    elif choice=='q':
        if len(Shopping_box)>0:
            print('your all added things:')
            for index,p in enumerate(Shopping_box):
                print('%s .  %s   %s' % (index, p[0], p[1]))
        else:
            print('you dont buy anything')
        run_flag=False



