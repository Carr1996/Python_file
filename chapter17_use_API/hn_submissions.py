import requests
from operator import itemgetter

# 执行API调用并存储响应
url='https://hacker-news.firebaseio.com/v0/topstories.json'
r=requests.get(url).content
html = content.decode("utf8", "ignore")
print('Status_Code',r.status_code)

# 处理有关每篇文章的信息
submission_ids=r.json()
submission_dicts=[]
for submission_id in submission_ids[:30]:
    # 对于每篇文章都调用一个API
    url=('https://hacker-news.firebaseio.com/v0/item/'+str(submission_id)+'.json')
    submission_r=requests.get(url)
    print(submission_r.status_code)
    response_dict=submission_r.json()

    submission_dict={
        'title':response_dict['title'],
        'link':'http://news.ycombinator.com/item?id='+str(submission_id),
        'comments':response_dict.get('descendants',0)
        }
    submission_dicts.append(submission_dict)

submission_dicts.sort(submission_dicts,key.itemgetter('comments'),reverse=True)

for submission_dict in submission_dicts:
    print('\ntitle:',submission_dict['title'])
    print('Discussion link:',submission_dict['link'])
    print('Comments:',submission_dict['comments'])

names=[]
plot_dicts=[]
for submission_dict in submission_dicts:
    names.append(submission_dict['title'])
    plot_dict={
        'value':submission_dict['comments'],
        'xlink':submission_dict['link']
        }
    plot_dicts.append(plot_dict)

# 可视化
my_style=LS('#333366',base_style=LCS)
my_config=pygal.Config()
my_config.x_label_rotation=45 #x轴旋转45°
my_config.show_legend=False #隐藏图例
my_config.title_font_size=24  #标题字体
my_config.label_font_size=14  #副标题字体，x轴上的项目名以及y轴上大部分数字
my_config.major_label_font_size=18  #主标题字体y轴上5000整数倍的刻度
my_config.truncate_label=15  #讲较长的项目名缩短为15个字符
my_config.show_y_guides=False  #隐藏图表中的水平线
my_config.width=1000

chart=pygal.Bar(my_config,style=my_style)
chart.title='Hacker_News_API'
chart.x_labels=names
chart.add('',plot_dicts)
chart.render_to_file('Hacker_News_API.svg')