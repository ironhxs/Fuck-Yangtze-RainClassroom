from datetime import datetime
import time


# 时间戳 用于提交答案
def get_date_time():
    return int(time.time() * 1000)


# 写入日志用
def get_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
