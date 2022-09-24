import json
import requests
import re


def get_html(url):
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    try:
        r = requests.get(url, headers=head)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("这条评论爬取失败")


def trans_html(ulist, html):
    jd = json.loads(html.lstrip('fetchJSON_comment98(').rstrip(');'))
    datas = jd['comments']
    for data in datas:
        ID = data['id']
        content = data['content']
        time = data['creationTime']
        ulist.append([ID, content, time])


def print_html(ulist,count,path):
    for u in ulist:
        count += 1
        print("序号：{0:<4}用户名：{1:<15}\n".format(count, u[0]))
        print("评论：{:<}\n".format(u[1]))
        print("时间：{:<}\n".format(u[2]))
        with open(path,'a',encoding="utf-8") as f:
            f.write("序号：{0:<4}用户名：{1:<15}\n".format(count, u[0]))
            f.write("评论：{:<}\n".format(u[1]))
            f.write("时间：{:<}\n".format(u[2]))

def main():
    ulist = []
    count = 0
    path = 'D://JINGDONG.txt'
    for i in range(0, 50 + 1):
        url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100019125569&score=0&sortType=5&page=' + str(i) + '&pageSize=10&isShadowSku=0&rid=0&fold=1'
        html = get_html(url)
        trans_html(ulist, html)
        print_html(ulist,count,path)

main()