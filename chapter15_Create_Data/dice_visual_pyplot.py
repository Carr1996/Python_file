import matplotlib.pyplot as plt
from die import Die

# 创建两个D6
die_1=Die()
die_2=Die()

# 投掷骰子多次，将结果存储到列表中
results=[]
for roll_mun in range(1000):
    result=die_1.roll()+die_2.roll()
    results.append(result)
# 分析结果
frequencies=[]
for value in range(2,die_1.num_side+die_2.num_side+1):
    frequency=results.count(value)
    frequencies.append(frequency)
# print(frequencies)

# 可视化图表
x_values=[x for x in range(2,die_1.num_side+die_2.num_side+1)]
plt.scatter(x_values,frequencies,edgecolors='none',c=x_values,cmap=plt.cm.Blues,s=40)
plt.title('Result of Rolling two D6 1000 times',fontsize=24)
plt.xlabel('Results',fontsize=14)
plt.ylabel('Frequencies of Result',fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()