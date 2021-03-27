# 开发团队:个人
# 开发时间:2021/3/27 下午 1:21
# 开发人员:Erhecy
# 开发名称:konachanVer-2.py
# 开发格式:PyCharm
import requests
import re
import os

def kogetli(page):
    print("开始获取图片")
    print('开始获取第', page, '页的图片')
    url = 'https://konachan.net/post?page=' + str(page)
    body = requests.get(url)
    imgulstart = body.text.find('''<ul id="post-list-posts">''')
    imgulendbody = body.text[imgulstart:9999999]
    imgulend = imgulendbody.find('''</ul>''')
    # 获取li
    imglistli = body.text[imgulstart + 25:imgulend + imgulstart]
    # print(imglistli)
    return imglistli

def get_konachanpic():
    page = 1
    picnum = 1
    html = kogetli(page)
    while True:
        pic_url = re.findall('class="directlink largeimg" href="(.*?)"', html, re.S)
        for key in pic_url:
            # print(key+'\n')
            print('开始获取第',picnum,'个图片')
            picname_ = str(key)[26:999999].replace('/','')
            picname = picname_[0:picname_.find('Konachan')]
            if os.path.exists(os.getcwd()+'\\'+picname+'.jpg') == False:
                seve_img(key,picname)
            else:
                print("文件已存已跳过下载")
            picnum = picnum + 1
        page = page + 1
        html = kogetli(page)

def seve_img(img_url,file_name):
    img = requests.get(img_url)
    f = open(file_name+'.jpg', 'ab')  # 存储图片，多媒体文件需要参数b（二进制文件）
    f.write(img.content)
    f.close()


if __name__ == '__main__':
    get_konachanpic()