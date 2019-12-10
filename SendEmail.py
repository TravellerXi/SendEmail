#!/usr/bin/python
#author:https://github.com/TravellerXi
# coding:utf-8

import smtplib

from email.mime.text import MIMEText

import sys

mail_user = 'user@domain.com'

mail_pass = 'passwordHere'


def send_mail(to_list, subject, content):
    me = "EmailTitleHere" + "<" + mail_user + ">"
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = me
    msg['to'] = to_list
    try:
        s = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        #smtp地址以及端口号/SMTP address and port
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print (str(e))
        with open ('error.log','a') as f:
            f.write(str(e))
            f.write('\n')

        return False

if __name__ == "__main__":
    send_mail(sys.argv[1], sys.argv[2], sys.argv[3])
