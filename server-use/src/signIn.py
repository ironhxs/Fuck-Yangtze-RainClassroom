from datetime import datetime

import requests

from api import url, api, headers, log_file_name
from file import write_log, read_log


def get_user_info():
    response = requests.get(url + api["user_info"], headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        # 提取 `data` 列表中的第一个元素信息
        if "data" in response_data and response_data["data"]:
            return response_data["data"][0].get("name")
    else:
        return "错误"


def check_and_sign(check_num=1):
    data = {
        "size": check_num,
        "type": [],
        "beginTime": None,
        "endTime": None
    }

    sign_data = {
        "source": 23,
        "lessonId": "",
        "joinIfNotIn": True
    }
    name = get_user_info()
    # 检查收到消息
    response = requests.post(url + api["get_received"], headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        # 提取 `data` 列表中的第一个元素信息
        if "data" in response_data and response_data["data"]:
            courseware_info = response_data["data"][0]
            courseware_id = courseware_info.get("coursewareId")
            courseware_title = courseware_info.get("coursewareTitle")
            course_name = courseware_info.get("courseName")
            course_url = courseware_info.get("url",None)
            
            logs = read_log(log_file_name)
            if logs and logs[-1]["id"] == courseware_id:
                print("已签过")
                return

            print("标题:", courseware_title)
            print("名称:", course_name)
           

            sign_data["lessonId"] = str(courseware_id)
            response_sign = requests.post(url + api["sign_in_class"], headers=headers, json=sign_data)

            if response_sign.status_code == 200:
                status = "签到成功"
                
                print(name,status)

                sign_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("时间:", sign_time)
                # 将签到信息写入文件顶部
                new_log = {
                    "id": courseware_id,
                    "title": courseware_title,
                    "name": course_name,
                    "time": sign_time,
                    "student" : name,
                    "status": status,
                    "url" : "https://changjiang.yuketang.cn/m/v2/lesson/student/"+str(courseware_id)
                }
                write_log(log_file_name, new_log)
            else:
                print("失败", response_sign.status_code, response_sign.text)
        else:
            print("没有找到数据")
    else:
        print("请求失败:", response.status_code, response.text)
