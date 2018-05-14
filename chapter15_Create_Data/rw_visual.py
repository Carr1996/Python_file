import matplotlib.pyplot as plt

from random_walk import RandomWalk
# 创建一个random_walk实例，并将其包含的点都绘制出来
while True:  #模拟多次漫步随机
    rw = RandomWalk(50000)
    rw.fill_walk()
    # 调整尺寸以适合屏幕
    plt.figure(figsize=(10,6))

    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,s=1,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none')
    # 突出起点和终点
    plt.scatter(0,0,edgecolors='none',s=100,c='green')
    plt.scatter(rw.x_values[-1],rw.y_values[-1],edgecolors='none',c='red',s=100)
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running=input('Make another walk(y/n):')
    if keep_running=='n':
        break
