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
    "class_info" : "m/v2/lesson/student/"
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
time = int(re.search(r'\"(.*?)\"', list[1]).group(1))

headers = {
    "Cookie": "sessionid=" + sessionId
}
