import requests

for page in range(0, 201, 20):
    url = f'https://cool.bilibili.com/x/co-create/material/list?material_type=19&ps=20&start_rank={page}&t=1634914151249'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/95.0.4638.54 Safari/537.36 '
    }
    response = requests.get(url=url, headers=headers)
    materials = response.json()['data']['materials']
    for index in materials:
        title = index['title']
        video_url = index['videopre_url']
        video_content = requests.get(url=video_url, headers=headers).content
        with open('video\\' + title + '.mp4', mode='wb') as f:
            f.write(video_content)
            print('已下载视频 ' + title)
