import smtplib
from email.message import EmailMessage
from typing import List


class SmtpSender:
    def __init__(self, login: str, password: str, smtp_server: str = "smtp.gmail.com", smtp_port: int = 465) -> None:
        self.server = smtp_server
        self.port = smtp_port
        self.login = login
        self.password = password

    def send(self, receivers: List[str], subject: str, message: str) -> None:
        msg = EmailMessage()
        msg["From"] = self.login
        msg["To"] = receivers
        msg["Subject"] = subject

        try:
            if isinstance(message, str):
                msg.set_content(message, subtype="plain")
            else:
                raise Exception("wrong message format: expected str")

            server = smtplib.SMTP_SSL(self.server, self.port)
            server.ehlo()
            server.login(self.login, self.password)
            server.send_message(msg)
            server.quit()
        except Exception as er:
            print(er)
