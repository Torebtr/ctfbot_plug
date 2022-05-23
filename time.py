'''
author:C1yas0
time:2021-8-28
'''
import requests
import re
from bs4 import BeautifulSoup

def get_ctftime_running(url):
    url_event = "https://ctftime.org/event/"
    ctf = {} # 写入字典用
    print('---------running--------')
    try:
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
        r = requests.get(url, headers=headers)
        bs_url = BeautifulSoup(r.text, 'html.parser')
        ctf_today = bs_url.find_all('table', width='100%')
        for today1 in ctf_today:
            today_td = today1.find_all('td')
            for today2 in today_td:
                today_a = today2.find('a')
                if today_a:
                    # list = [] # 写入字典用
                    today_a_str = str(today_a)
                    today_url = re.sub('<a href="/event/|" style="color: #000000">|<img alt="Jeopardy" border="0" rel="tooltip" src="/static/images/ct/1.png" title="Jeopardy"/></a>|\n', '', today_a_str)
                    new_url = url_event + today_url
                    list.append([get_time(new_url, today_url), get_url(new_url)]) # 写入字典用
                    ctf[get_name(new_url)] = list # 写入字典用
                    # print(get_name(new_url)+" "+get_time(new_url, today_url)+" " + get_url(new_url))
        print(ctf) # 写入字典用
    except:
        print("请求失败")

def get_ctftime_upcoming(url):
    print('---------upcoming--------')
    try:
        url_event = "https://ctftime.org/event/"
        ctf = {} # 写入字典用
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
        r = requests.get(url, headers=headers)
        bs_url = BeautifulSoup(r.text, 'html.parser')
        ctf_come = bs_url.find_all('table', class_='table table-striped upcoming-events')
        for come1 in ctf_come:
            come_tr = come1.find_all('a')
            for come2 in come_tr:
                list = [] # 写入字典用
                come3 = str(come2)
                come4 = come3[0:20]
                come_url = re.sub('<a href="/event/', '', come4)
                new_url = url_event + come_url
                list.append([get_time(new_url, come_url), get_url(new_url)]) # 写入字典用
                ctf[get_name(new_url)] = list # 写入字典用
                # print(get_name(new_url)+" "+get_time(new_url, come_url)+" "+get_url(new_url))
        print(ctf) # 写入字典用
    except:
        print("请求失败")

def get_name(url): # 获取比赛名称
    try:
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
        r = requests.get(url, headers=headers)
        bs_url = BeautifulSoup(r.text, 'html.parser')
        name = bs_url.find_all('h2')
        final_name = re.sub('<h2>|<i class="icon-play-circle" id="progress" rel="tooltip"></i></h2>|</h2>', '',str(name)) # 比赛名称
        return final_name
    except:
        print("比赛名称获取失败")

def get_time(url,num): # 获取比赛时间
    try:
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
        r = requests.get(url, headers=headers)
        bs_url = BeautifulSoup(r.text, 'html.parser')
        times = bs_url.find('div', class_='span10')
        time = times.find('p')
        time_str = str(time)
        final_time = re.sub('<p>|<a href="/event/|.ics|" id="calendar" rel="tooltip">|<img class="svg_icon" id="icon_calendar" src="/static/img/icon_cal.svg"/>|</a>|</p>|\xa0|\n', '', time_str)
        final_time = re.sub(num, '', final_time) # 比赛时间
        return final_time
    except:
        print("比赛时间获取失败")

def get_url(url): # 获取比赛网址
    try:
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
        r = requests.get(url, headers=headers)
        bs_url = BeautifulSoup(r.text, 'html.parser')
        url = bs_url.find('a', rel='nofollow')
        final_url = re.sub('<a href="|" rel="nofollow">|</a>|\n', '', str(url))
        final_url = final_url[0:int(len(final_url) / 2)]  # 比赛网址
        return final_url
    except:
        print("比赛时间获取失败")

if __name__ == '__main__':
    url = "https://ctftime.org"
    get_ctftime_running(url) # 正在举行的比赛
    get_ctftime_upcoming(url) # 即将举行的比赛

