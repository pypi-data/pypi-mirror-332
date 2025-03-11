import os
import smtplib
from dataclasses import dataclass
from email.mime.text import MIMEText

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


@dataclass
class MailInfo:
  receiver_email: str
  subject: str
  body: str


class MailWorker(object):
  mail_server: str = "smtp.exmail.qq.com"
  port: int = 465

  def __init__(self, mail_info: MailInfo):
    self.mail_info = mail_info
    self.get_credentials()

  def get_credentials(self):
    self.sender_email = os.getenv("EMAIL_HOST_USER")
    self.sender_password = os.getenv("EMAIL_HOST_PASSWORD")
    if self.sender_email is None or self.sender_password is None:
      raise ValueError("EMAIL_HOST_USER and EMAIL_HOST_PASSWORD must be set")

  def send(self):
    message = MIMEText(self.mail_info.body)
    message["Subject"] = self.mail_info.subject
    message["From"] = self.sender_email
    message["To"] = self.mail_info.receiver_email

    try:
      server = smtplib.SMTP_SSL(self.mail_server, self.port)
      server.login(self.sender_email, self.sender_password)
      server.sendmail(
        self.sender_email, self.mail_info.receiver_email, message.as_string()
      )
      server.quit()
      print("Email sent successfully!")
    except Exception as e:
      print(f"Error: {e}")
