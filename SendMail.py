import smtplib
import argparse

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List


def send_mail(
        sender,
        receivers: List[str],
        subject,
        body,
        username,
        password,
        server_address
):
    """Sends an email to the specified receivers using an Exchange server."""
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = ",".join(receivers)
    message["Subject"] = subject
    message.attach(MIMEText(body))

    server = smtplib.SMTP(server_address, 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(sender, receivers, message.as_string())
    server.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sends an email to the specified receivers using the Sykehuspartner Exchange server.")
    parser.add_argument("sender", type=str, help="Sender's email address.")
    parser.add_argument("receivers", type=str, help="Comma-seperated list of email addresses.")
    parser.add_argument("subject", type=str, help="Subject of the email.")
    parser.add_argument("body", type=str, help="Body text of the email. Can be plain text or a file path when -f is passed.")
    parser.add_argument("username", type=str, help="The username to authenticate with on mail server.")
    parser.add_argument("password", type=str, help="The password to authenticate with on mail server.")
    parser.add_argument("server", type=str, help="The address of the mail server.")
    parser.add_argument("-f", "--file", action="store_true", help="Specifies that the body argument contains a file path instead of plain text")
    args = parser.parse_args()

    if args.file:
        with open(args.body) as file:
            args.body = file.read()

    send_mail(args.sender, args.receivers.split(","), args.subject, args.body, args.username, args.password, args.server)