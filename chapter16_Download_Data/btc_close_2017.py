import json
import pygal
import math
# 将数据加载到一个列表中
filename='btc_close_2017_request.json'
with open(filename) as f :
    btc_data=json.load(f)

# 创建五个列表存储信息
dates=[]
months=[]
weeks=[]
weekdays=[]
closes=[]
# 将每一天的信息加入列表
for btc_dict in btc_data:
    date=btc_dict['date']
    dates.append(date)
    month=int(btc_dict['month'])
    months.append(month)
    week=int(btc_dict['week'])
    weeks.append(week)
    weekday=btc_dict['weekday']
    close=int(float(btc_dict['close']))
    closes.append(close)
    print("{} is month {} week {},{},the close price is {} RMB".format(date,month,week,weekday,close))

line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title='收盘价对数变化($)'
line_chart.x_labels=dates
N=20 #坐标轴每隔20天显示一次
line_chart.x_labels_major=dates[::N]
closes_log=[math.log10(_) for _ in closes]
line_chart.add('log收盘价',closes_log)
line_chart.render_to_file('收盘价对数变化折线图.svg')

# 数据仪表盘
with open('收盘价Dashboard.html','w') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title></head><body>\n')
    for svg in ['收盘价对数变化折线图.svg']:
        html_file.write(' <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
    html_file.write('</body></html>')