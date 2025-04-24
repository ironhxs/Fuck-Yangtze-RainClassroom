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
    # 获取正在处于上课的列表
    "get_listening": "api/v3/classroom/on-lesson-upcoming-exam"
}

log_file_name = "log.json"

# 登录凭证

sessionId = os.environ["SESSION"]
email_user = os.environ["EMAIL_USER"]
email_pass = os.environ["EMAIL_PASS"]
to_email = os.environ["TO_EMAIL"]
email_host = os.environ["EMAIL_HOST"]
email_port = os.environ["EMAIL_PORT"]

headers = {
    "Cookie": "sessionid=" + sessionId
}


question_type = {
    1 : "单选题",
    2 : "",
    3 : "",
    4 : "",

}
