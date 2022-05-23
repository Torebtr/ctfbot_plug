# coding:utf-8
import requests
import re
from bs4 import BeautifulSoup
from hub import *
from time import *
from lxml import etree
import requests

def ctf_time():
    url = "https://ctftime.org"
    message = get_ctftime_running(url)  # 正在举行的比赛
    message += get_ctftime_upcoming(url)  # 即将举行的比赛
    return message


def ctf_hub():
    # print("---正在进行的比赛---")
    message = '------正在进行的比赛-------'
    message += getinfo(getrunning_id())
    # print(getinfo(getrunning_id()))

    # print("---即将到来的比赛---")
    message += '------即将到来的比赛-------'
    message += getinfo(getupcoming_id())
    # print(getinfo(getupcoming_id()))
    return message


def tiangou(uid, gid):
    url = 'https://www.nihaowua.com/dog.html'
    response = requests.get(url)
    etree_html = etree.HTML(response.content.decode('utf-8'))

    message = etree_html.xpath('//article/text()')[0]
    # print(message)

    data = {
        "message": message,
        "group_id": gid
    }

    if gid != None:
        requests.post(url='http://127.0.0.1:5700/send_group_msg', data=data)

def Attendance_reminder(uid , gid):
    message1 = ctf_hub()
    data = {
        "message": message1,
        "group_id": gid
    }
    # print('----------------message----------')
    # print(message1)
    if gid != None:
        requests.post(url='http://127.0.0.1:5700/send_group_msg', data=data)
        # requests.get(
        #     url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, message1))

import requests

'下面这个函数用来判断信息开头的几个字是否为关键词'
'如果是关键词则触发对应功能，群号默认为空'


def keyword(message, uid, gid = None):
    if message[0:5] == 'bisai':
        Attendance_reminder(uid, gid)
    elif message == 'tiangou':
        tiangou(uid, gid)

