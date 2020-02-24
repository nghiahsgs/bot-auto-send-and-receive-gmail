import smtplib
import getpass

class AutoGmail():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def loginGmail(self):
        self.conn = smtplib.SMTP('smtp.gmail.com', 587)
        self.conn.ehlo()
        self.conn.starttls()
        self.conn.login(self.username, self.password)

    def sendEmail(self, mail_receive, title, content):
        self.conn.sendmail(self.username, mail_receive,
                           'Subject: '+title+'\n\n'+content)


username = "nghiahsgs40"
password = getpass.getpass()
mail_receive = "nghiahsgs@gmail.com"

bot = AutoGmail(username, password)
bot.loginGmail()
bot.sendEmail(mail_receive, 'this is a title', 'this is a content')
