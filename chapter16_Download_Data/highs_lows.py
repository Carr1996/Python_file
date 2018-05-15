import csv
from matplotlib import pyplot as plt
from datetime import datetime
# 从文件中获取日期，最低气温，最高气温
filename ='sitka_weather_2014.csv'
with open(filename,'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)

# 从文件中获取最高气温,并将字符串转化为数字
# 从文件中获取日期，并转化为指定格式
# 从文件中获取最低气温
    highs=[]
    dates=[]
    lows=[]
    for row in reader:
        try:
            high=int(row[1])
            date=datetime.strptime(row[0],'%Y-%m-%d')
            low=int(row[3])
        except ValueError:
            print(date,'missing data')
        else:
            highs.append(high)
            dates.append(date)
            lows.append(low)
    # print(highs)
    # print(dates)

# 根据数据绘制图形
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)   #最高气温
plt.plot(dates,lows,c='blue',alpha=0.5)   #最低气温
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1) #给图表区域着色，alpha表示透明度
# 设置图形的格式
plt.title('Daily high and low temperatures - 2014',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()  #绘制斜的日期标签
plt.ylabel('Temperatures(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()
# plt.savefig('',bbox_inches='tight'裁剪掉多余的空白区域)