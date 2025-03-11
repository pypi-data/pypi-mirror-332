from quick_postman import MailInfo, MailWorker


def test_mail():
  mail_info = MailInfo(receiver_email="svtter@qq.com", subject="test", body="test")
  mail_worker = MailWorker(mail_info)
  mail_worker.send()
