import requests
from bs4 import BeautifulSoup
import smtplib
import datetime
import time

def send_email(hs300, zz500):
    # 邮件服务器地址
    smtp_server = "smtp.gmail.com"
    # 邮件服务器端口
    smtp_port = 587
    # 发件人邮箱地址
    from_email = "your_email@gmail.com"
    # 发件人邮箱密码
    from_email_password = "your_email_password"
    # 收件人邮箱地址
    to_email = "2818343657@qq.com"
    # 邮件主题
    subject = "China Stock Market Index"
    # 邮件内容
    body = "Shanghai & Shenzhen 300 Index: " + hs300 + "\n" + "China CSI 500 Index: " + zz500
    
    # 创建SMTP对象
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(from_email, from_email_password)
    message = f"Subject: {subject}\n\n{body}"
    smtp.sendmail(from_email, to_email, message)
    smtp.quit()
    print("Email sent successfully!")

while True:
    now = datetime.datetime.now()
    if now.hour == 14 and now.minute == 0:
        # 获取沪深300指数
        res = requests.get("https://finance.yahoo.com/quote/%5ESZ399300?p=%5ESZ399300")
        soup = BeautifulSoup(res.text, "html.parser")
        hs300 = soup.find("span", {"data-reactid": "14"}).text
        
        # 获取中证500指数
        res = requests.get("https://finance.yahoo.com/quote/000905.SS?p=000905.SS")
        soup = BeautifulSoup(res.text, "html.parser")
        zz500 = soup.find("span", {"data-reactid": "14"}).text
        
        send_email(hs300, zz500)
    time.sleep(60)

