from die import Die
import pygal
# 创建一个D6
die=Die()

# 掷几次骰子，并把结果存储在一个列表中
results=[]
for roll_num in range(1,1001):
    result=die.roll()
    results.append(result)
# print(results)

# 分析结果 各个点数每次出现的次数
# frequencies=[]
for value in range(1,die.num_side+1):
    frequency=results.count(value)
    frequencies.append(frequency)
# print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()

hist.title='Result of Rolling one D6 1000 times'
hist.x_labels=[x for x in range(2,die_1.num_side+die_2.num_side+1)]
hist.x_title='Result'
hist.y_title='Frequency of Result'

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')