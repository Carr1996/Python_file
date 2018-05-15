import matplotlib.pyplot as plt
x_value=list(range(1,5001))
y_value=[x**3 for x in x_value]
plt.scatter(x_value,y_value,s=20,c=y_value,cmap=plt.cm.Reds,edgecolors=None)

# 定义相关样式
plt.title('x**3',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Squares of Value',fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()
# plt.savefig('.png',bbox_inches='tight')