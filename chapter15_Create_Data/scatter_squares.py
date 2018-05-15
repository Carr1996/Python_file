import matplotlib.pyplot as plt
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=20)
# edgecolors='none'删除数据点的轮廓,默认为none
# 可以使用RGB颜色模式自定义颜色c=(0,0,0.8)分别是红色绿色蓝色的分量
# 值越接近0指定的颜色越深，值越接近1指定的颜色越浅

# 添加样式
plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])
plt.show()
# plt.savefig('scatter_squares.png',bbox_inches='tight')
# 第二个实参指定讲图标多余的空白区域裁剪掉