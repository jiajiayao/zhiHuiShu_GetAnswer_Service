import requests
import json
import config
import time
import random
import re

def test():
    #await asyncio.sleep(3)
   
    res = requests.get('https://www.baidu.com')
    print(res)


#爬虫主要
def getAnswer(question, course_name):
    
    try:
        re.sub('\s', ' ', question)
    except:
        print('去除失败')

    print(question)
    params_url={
        #'question':question,
        'key':"6months352805399",
        'ti':question,
    }

    try:
        res = requests.get(config.Set['targetUrl'], params=params_url, headers=config.Set['headers_url'], timeout=6)
        #time.sleep(random.random() * 0.5)
        
        res=res.json()

        res['course_name'] = course_name

        # 前面省略，从下面直奔主题，举个代码例子：
        result2txt=str(res)          # data是前面运行出的数据，先将其转为字符串才能写入
        with open('answer.txt','a') as file_handle:   # .txt可以不自己新建,代码会自动新建
            file_handle.write(result2txt)     # 写入
            file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
    except:
        res = {"question":"233","answer":"搜题接口异常请到issue反馈，或者稍后在尝试搜题"}
    print(res)

    return res

def handleData(problems,course_name):
    res=[]
    for i in problems:
        res.append(getAnswer(i,course_name))

    
    return res

