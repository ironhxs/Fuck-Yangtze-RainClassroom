from datetime import datetime

import requests

from api import url, api, headers, log_file_name, question_type
from file import write_log, read_log
from notice import email_notice


# 获取用户名字 用于核实
def get_user_info():
    response = requests.get(url + api["user_info"], headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        # 提取 `data` 列表中的第一个元素信息
        if "data" in response_data and response_data["data"]:
            return response_data["data"][0].get("name")
    else:
        return "错误"


# 获取正在进行的
def get_listening():
    response = requests.get(url + api["get_listening"], headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        return response_data["data"]
    else:
        return None


def get_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 获取正在进行的课堂并且签到、写日志
def get_listening_classes_and_sign():
    response = get_listening()
    name = get_user_info()

    if response is None:
        return None
    else:
        classes = list(response["onLessonClassrooms"])
        if len(classes) == 0:
            print("无课")
            return
        else:
            print("发现上课")
            for item in classes:
                course_name = item["courseName"]
                lesson_id = item["lessonId"]
                response_sign = sign(lesson_id)

                if response_sign.status_code == 200:
                    status = "签到成功"

                    print(course_name, status)

                    email_notice(subject="雨课堂课程签到成功", content=course_name)

                    # 将签到信息写入文件顶部
                    new_log = {
                        "id": lesson_id,
                        "title": course_name,
                        "name": course_name,
                        "time": get_now(),
                        "student": name,
                        "status": status,
                        "url": "https://changjiang.yuketang.cn/m/v2/lesson/student/" + str(lesson_id)
                    }
                    write_log(log_file_name, new_log)
                else:
                    print("失败", response_sign.status_code, response_sign.text)

            # 发邮件提醒
            # TODO
            return


# 获取正在进行的考试
def get_exam():
    response = get_listening()
    if response is None:
        return None
    else:
        exams = list(response["upcomingExam"])
        if len(exams) == 0:
            print("无考试")
            return
        else:
            print("发现考试")
            print(exams)
            # 发邮件提醒
            email_notice(subject="雨课堂考试提醒", content="请打开雨课堂")
            return


# 传入lessonId 签到
def sign(lesson_id):
    sign_data = {
        "source": 23,
        "lessonId": str(lesson_id),
        "joinIfNotIn": True
    }

    response_sign = requests.post(url + api["sign_in_class"], headers=headers, json=sign_data)
    return response_sign


# 是否已经签过（写入日志）
def has_signed(lesson_id):
    logs = read_log(log_file_name)
    if logs and logs[-1]["id"] == lesson_id:
        print("已签过")
        return True
    else:
        return False


# 收到的课程列表前check_num个全部进行签到、写日志
def check_and_sign(check_num=1):
    data = {
        "size": check_num,
        "type": [],
        "beginTime": None,
        "endTime": None
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

            if has_signed(courseware_id):
                return

            print("标题:", courseware_title)
            print("名称:", course_name)

            response_sign = sign(courseware_id)

            if response_sign.status_code == 200:
                status = "签到成功"

                print(name, status)

                # 将签到信息写入文件顶部
                new_log = {
                    "id": courseware_id,
                    "title": courseware_title,
                    "name": course_name,
                    "time": get_now(),
                    "student": name,
                    "status": status,
                    "url": "https://changjiang.yuketang.cn/m/v2/lesson/student/" + str(courseware_id)
                }
                write_log(log_file_name, new_log)
            else:
                print("失败", response_sign.status_code, response_sign.text)
        else:
            print("没有找到数据")
    else:
        print("请求失败:", response.status_code, response.text)


# 获取PPT的内容 包括题目
def get_ppt_content():
    return None


# 检查是否有题目出现

# 解析出题目
def parse_question(slide):
    question = slide["problem"]
    id = question["problemId"]
    type = question_type[question["problemType"]]
    limit_time_second = question["limit"]
    score = question["score"]
    content = question["body"]
    options = question["options"]


if __name__ == '__main__':
    # email_notice(subject="测试", content="雨课堂")
    # get_exam()
    get_listening_classes_and_sign()
    check_and_sign()
