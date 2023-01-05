import requests
import re
import json
from pprint import pprint

# 导入数据包
# 请求url链接
url = 'https://www.bilibili.com/video/BV1Jg411A7Se/?spm_id_from=333.337.search-card.all.click&vd_source' \
      '=a6ae9902d6deca105abb7f09164cbe81 '
# 把Python伪装成浏览器
headers = {
    # 防盗链
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 '
                  'Safari/537.36 '
}
# 发送请求  <Response [200]>200是状态码，表示请求成功
response = requests.get(url=url, headers=headers)
# 获取数据，返回响应数据 -->文本数据
print(response.text)
# 正则表达式 --->对于字符串数据类型进行解析/提取
title = re.findall('"title":"(.*?)","pubdate"', response.text)[0]
html_data = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]
json_data = json.loads(html_data)
print(title)
print(html_data)
# print打印字典数据，输出一行内容
print(json_data)
# pprint 打印字典数据，格式化输出 展开效果
pprint(json_data)
audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
video_url = json_data['data']['dash']['video'][0]['baseUrl']
print(audio_url)
print(video_url)
audio_content = requests.get(url=audio_url, headers=headers).content
video_content = requests.get(url=video_url, headers=headers).content
with open('video//' + title + '.mp4', mode='wb') as video:
    video.write(video_content)
with open('video//' + title + '.mp3', mode='wb') as audio:
    audio.write(audio_content)
