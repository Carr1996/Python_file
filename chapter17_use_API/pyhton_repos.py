import requests
import pygal
from pygal.style import LightColorizedStyle as LCS ,LightenStyle as LS

# 执行API调用并存储响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print('Status_Code：',r.status_code)
# 将API响应存储在一个变量中
response_dict=r.json()
# 处理结果
print(response_dict.keys())

print('Total_repositories:',response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts=response_dict['items']
print('Repositories returned',len(repo_dicts))

    # # 研究第一个仓库
    # repo_dict=repo_dicts[0]
    # print('\nkeys:',len(repo_dict))
    # for key in repo_dict.keys():
    #     print(key)

    # # 返回每个仓库的特定信息
    # print('\nSelected information about each repository:')
    # for repo_dict in repo_dicts:
    #     print('\nName:',repo_dict['name'])
    #     print('Owner:',repo_dict['owner']['login'])
    #     print('Stars:',repo_dict['stargazers_count'])
    #     print('Repository:',repo_dict['html_url'])
    #     print('Description:',repo_dict['description'])

names=[]
plot_dicts=[]
for repo_dict in repo_dicts:
    if repo_dict['description']:
        names.append(repo_dict['name'])
        plot_dict={
            'value':repo_dict['stargazers_count'],
            'label':repo_dict['description'],
            'xlink':repo_dict['html_url']
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
chart.title='Most_starred Python Projects on GitHUb'
chart.x_labels=names
chart.add('',plot_dicts)
chart.render_to_file('python_repo.svg')