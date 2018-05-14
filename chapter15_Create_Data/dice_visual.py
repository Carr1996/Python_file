import pygal
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
print(frequencies)
# 可视化结果
hist=pygal.Bar()

hist.title='Result of Rolling two D6 1000 times'
hist.x_labels=[x for x in range(2,die_1.num_side+die_2.num_side+1)]
hist.x_title='Result'
hist.y_title='Frequency of Result'

hist.add('D6+D6',frequencies)
hist.render_to_file('dice_visual.svg')