import os

url = "https://changjiang.yuketang.cn/"

api = {
    # 获取收到的消息
    "get_received": "api/v3/activities/received/",
    # 获取我发布的信息
    "get_published": "api/v3/activities/published/",
    # 进入课堂
    "sign_in_class": "api/v3/lesson/checkin",
    # 个人信息
    "user_info" : "v2/api/web/userinfo",
}

log_file_name = "log.json"


def read(filename):
    with open(filename, 'r') as file:
        strings = file.readlines()
        return strings


# 登录凭证

sessionId = os.environ["SESSION"]

headers = {
    "Cookie": "sessionid=" + sessionId
}
