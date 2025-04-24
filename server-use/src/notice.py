import smtplib
from email.mime.text import MIMEText
from email.header import Header
from api import email_user, email_pass,to_email,email_port,email_host


# 发送邮件提醒 标题、内容、发给谁
def email_notice(subject: str, content: str):
    if not all([email_user, email_pass, to_email]):
        print("邮件配置不完整，请检查环境变量或参数")
        return

    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = email_user
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL(host=email_host, port=email_port) as server:
            server.login(email_user, email_pass)
            server.sendmail(email_user, [to_email], msg.as_string())
    except Exception as e:
        return
