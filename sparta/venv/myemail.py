import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
emails = ['m']

# 보내는 사람 정보
me = "dlalsrns4064@gmail.com"
my_password = "se4064064"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
you = "minkyun@kakao.com"

# 메일 기본 정보 설정
msg = MIMEMultipart('alternative')
msg['Subject'] = "파이썬으로 이메일 보내기 #1"
msg['From'] = me
msg['To'] = you

# 메일 내용 쓰기
content = "메일 내용"
part2 = MIMEText(content, 'plain')
msg.attach(part2)



# 메일 보내고 서버 끄기
s.sendmail(me, you, msg.as_string())
s.quit()