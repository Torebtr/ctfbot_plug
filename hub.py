# coding=utf-8
# @author : 0uLL
# @software : pycharm
import requests
import re
from bs4 import BeautifulSoup
import time
# 获取即将到来的比赛ID
def getupcoming_id():
    upcoming_url = "https://api.ctfhub.com/User_API/Event/getUpcoming" #获取即将开始的比赛ID
    upcoming_payload = {
        'offset': 0,
        'limit': 5
    } #POST请求参数
    upcoming_request = requests.post(upcoming_url, json=upcoming_payload)
    upcoming_id = []
    for i in range(len(upcoming_request.json()["data"]["items"])):
        upcoming_id.append(upcoming_request.json()["data"]["items"][i]["id"])
    return upcoming_id #返回比赛ID

# 获取正在进行的比赛ID
def getrunning_id():
    running_url = "https://api.ctfhub.com/User_API/Event/getRunning" #获取正在进行的比赛ID
    running_payload = {
        'offset': 0,
        'limit': 5
    } #POST请求参数
    running_request = requests.post(running_url, json=running_payload)
    running_id = []
    for i in range(len(running_request.json()["data"]["items"])):
        running_id.append(running_request.json()["data"]["items"][i]["id"])
    return running_id #返回比赛ID

# 通过比赛ID获取详细信息
def getinfo(id):
    s = ''
    for i in id:
        info_url = "https://api.ctfhub.com/User_API/Event/getInfo"  #获取详细信息的网址
        info_payload = {
            "event_id": i,
        } #POST请求参数
        info_request = requests.post(url=info_url, json=info_payload)
        js = info_request.json() #把返回值转为json格式
        s +="-------------------------\n"\
             + "名称：" + js["data"]["title"] + "\n" \
             + "比赛类型：" + js["data"]["class"] + "\n" \
             + "比赛形式：" + js["data"]["form"]+ "\n" \
             + "开始时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(js["data"]["start_time"])) + "\n" \
             + "结束时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(js["data"]["end_time"])) + "\n" \
             + "官方链接：" + js["data"]["official_url"] + "\n"\
            +"-------------------------\n"
    return s


if __name__ == '__main__':
    print("---正在进行的比赛---")
    print(getinfo(getrunning_id()))
    print("---即将到来的比赛---")
    print(getinfo(getupcoming_id()))



