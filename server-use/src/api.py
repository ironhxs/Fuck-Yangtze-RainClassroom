import re

url = "https://changjiang.yuketang.cn/"

api = {
    # 获取收到的消息
    "get_received": "api/v3/activities/received/",
    # 获取我发布的信息
    "get_published": "api/v3/activities/published/",
    # 进入课堂
    "sign_in_class": "api/v3/lesson/checkin",
    # 登录雨课堂账号
    "login_user": "pc/login/verify_pwd_login/",
    # 个人信息
    "user_info" : "v2/api/web/userinfo",
    # 如果是课堂 可以通过此URL进入课堂查看PPT 尾接courseID
    "class_info" : "m/v2/lesson/student/",
    # 获取正在处于上课的列表
    "get_listening": "api/v3/classroom/on-lesson-upcoming-exam"
}

log_file_name = "log.json"
config_file_name = "config.txt"


def read(filename):
    with open(filename, 'r') as file:
        strings = file.readlines()
        return strings


# 登录凭证
list = read(config_file_name)

sessionId = re.search(r'\"(.*?)\"', list[0]).group(1)
email_user = str(re.search(r'\"(.*?)\"', list[1]).group(1))
email_pass = str(re.search(r'\"(.*?)\"', list[2]).group(1))
to_email = str(re.search(r'\"(.*?)\"', list[3]).group(1))
email_host = str(re.search(r'\"(.*?)\"', list[4]).group(1))
email_port = int(re.search(r'\"(.*?)\"', list[5]).group(1))

headers = {
    "Cookie": "sessionid=" + sessionId
}

question_type = {
    1 : "单选题",
    2 : "",
    3 : "",
    4 : "",

}

