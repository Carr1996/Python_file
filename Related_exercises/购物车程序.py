products=[['Iphone8',6888],['MacPro',14000],['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799]]
Shopping_box=[]
 #工资需求
while True:
    wages = input('请输入你的工资：')
    if wages.isdigit():
        wages=int(wages)
        print('您当前工资总额为 %d'%wages)
        break
    else:
        print('请重新输入整数数字')

i=wages
while True:
    print('---------商品列表----------')
    for index, p in enumerate(products):
        print('%d . %s  %s' % (index, p[0], p[1]))
    want=input('请输入想要购买的商品的编号（想要退出请输入q）:')
    if want.isdigit():
        want=int(want)
        if i>=products[want][1]:
            print('你已经购买 %s'%products[want][0])
            Shopping_box.append(products[want])
            i=i-products[want][1]
            print('你当前的余额为 %d'%i)
        else:
            print('你的余额不足')
    elif want=='q':
        if len(Shopping_box)>0:
            print('你已经购买的商品为：')
            for p in Shopping_box:
                print(p[0])
            print('你当前剩余的工资为%d'%i)
        else:
            print('你未购买任何商品')
            print('你当前剩余的工资为%d' % i)
        break
    else:
        print('请正确输入')


