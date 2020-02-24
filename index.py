#https://myaccount.google.com/lesssecureapps?pli=1
#goto this url and turn on to allow less secure app can send gmail
import smtplib


def hamGuiMail(username, password, mail_receive, title, content):
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login(username, password)
    conn.sendmail(username, mail_receive,
                  'Subject: '+title+'\n\n'+content)

import io
import time
f=io.open('data.txt',encoding='utf8')
ndung=f.read()

list_lines = ndung.split('\n')
dem=0
for line in list_lines:
    dem+=1
    print(line)
    username, password, mail_receive, title, content = line.split('|')
    time.sleep(5)
    
    try:
        hamGuiMail(username, password, mail_receive, title, content)
        print('---success--%s' % dem)
    except:
        print('---error--%s' % dem)
        pass
