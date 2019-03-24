import smtplib
import datetime
import random
import string
import base64
import time

_from = 'qingshanyouyou1@gmail.com'
_to = '37628372@qq.com'

_host = 'smtp.gmail.com'
_port = 587
_user = 'qingshanyouyou1@gmail.com'
_passwd = 'a3200781'

def gene_recv():
    return str(random.randint(10000, 10000000))+'@qq.com'


def msg_generate():
    rnd = ''.join(random.choice(string.letters) for _ in range(int(3000 * random.random())))
    msg = "From: " + _from + "\r\n" \
          + "To: " + _to + "\r\n" \
          + "Subject: PyTgen " + str(datetime.datetime.now()) + "\r\n\r\n" \
          + rnd + "\r\n"
    return msg

cnt = 0
while True:
    try:
        sender = smtplib.SMTP(_host, _port)
        try:

            sender.starttls()

        except:
            pass

        try:
            sender.login(_user, _passwd)

        except smtplib.SMTPAuthenticationError:
            sender.docmd("AUTH LOGIN", base64.b64encode(_user))
            sender.docmd(base64.b64encode(_passwd), "")

        msg = msg_generate()
        print(msg)
        _to = gene_recv()
        sender.sendmail(_from, _to, msg)
        print("Email sent successful")

    except:
        raise

    else:
        sender.quit()

    sleepTime = random.uniform(1, 2)
    time.sleep(sleepTime)
    cnt += 1
    if cnt == 10:
        cnt = 0
        time.sleep(random.uniform(5,10))
