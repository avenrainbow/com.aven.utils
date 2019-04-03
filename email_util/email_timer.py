#coding:utf-8

from apscheduler.schedulers.blocking import BlockingScheduler
import time

def scheduler_joner():
    # 实例化一个调度器
    scheduler = BlockingScheduler()

    def email_send_job():
        print("Email Send Job Start!")
        loadhostStatus()
        sender()

    # 定时每周五 17:30:00秒执行任务
    scheduler.add_job(email_send_job,'cron',day_of_week ='4',hour = 17,minute = 30,second = 00)

    # 开始运行调度器
    scheduler.start()


import requests
import urllib3
from vmware.vapi.vsphere.client import create_vsphere_client

host_info = ""

def loadhostStatus():
    try:
        session = requests.session()

        # Disable cert verification for demo purpose.
        # This is not recommended in a production environment.
        session.verify = False

        # Disable the secure connection warning for demo purpose.
        # This is not recommended in a production environment.
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        # Connect to a vCenter Server using username and password
        vsphere_client = create_vsphere_client(server='192.168.214.245', username='administrator@vsphere.local', password='Admin@123', session=session)

        # List all VMs inside the vCenter Server
        # print vsphere_client.vcenter.Host.list()

        hosts = vsphere_client.vcenter.Host.list()

        for host in hosts:
            global host_info
            host_info = host_info + str(host) + "\n"
    except Exception,e:
        print e

import smtplib
from email.mime.text import MIMEText


def sender():
    _user = "525868012@qq.com"
    _pwd  = "xxxxxxxx"
    # "uxtbviubdgoubhib"
    _to   = "xxx@xx.com"

    global host_info

    msg = MIMEText("周五下班时请关闭以下服务器：\n 192.168.103.50 \n 192.168.103.86 \n 192.168.103.98 \n vCenter平台192.168.214.245主机状态如下：\n " + host_info)
    msg["Subject"] = "云宏-服务器闲时关机节能提醒"
    msg["From"]    = _user
    msg["To"]      = _to

    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(_user, _pwd)
        s.sendmail(_user, _to, msg.as_string())
        s.quit()
        print("Email Send Success!")
    except smtplib.SMTPException,e:
        print ("Falied,%s" %e)

def main():
    scheduler_joner()

if __name__ == '__main__':
    main()
