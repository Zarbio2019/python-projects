# To send an email
import yagmail

email = yagmail.SMTP(user="pythonprocourse1@gmail.com", password="python_pro_course_1")
email.send(to="ypddjuio@yomail.info",
           subject="Hi there!",
           contents="Hi, this is the body of the email!\nArdit",
           attachments="design.txt")
