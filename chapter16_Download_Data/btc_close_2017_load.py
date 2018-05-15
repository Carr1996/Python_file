import requests

json_url='https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.josn'
req=requests.get(json_url)
# 讲数据写入文件
with open('btc_close_2017_request.josn','w') as f:
    f.write(req.text)
