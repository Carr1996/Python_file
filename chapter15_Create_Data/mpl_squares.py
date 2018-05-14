import matplotlib.pyplot as plt
input_values=[1,2,3,4,5]  #输入值
squares=[1,4,9,16,25]   #输出值
plt.plot(input_values,squares,linewidth=5)  #更改线条粗细

# 设置图标标题并且为x，y轴加上标题
plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)
plt.show()