import email
import smtplib
import imaplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"

class Email:

    def __init__(self, login, password, subject, recipients, message, header=None):
        self.login = login
        self.password = password
        self.subject = subject
        self.recipients = recipients
        self.message = message
        self.header = header


    def send_message(self):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))
        smtpObj = smtplib.SMTP(GMAIL_SMTP, 587) # identify ourselves to smtp gmail client
        smtpObj.ehlo()
        smtpObj.starttls() # secure our email with tls encryption
        smtpObj.ehlo()# re-identify ourselves as an encrypted connection
        smtpObj.login(self.login, self.password)
        smtpObj.sendmail(self.login, smtpObj, msg.as_string())
        smtpObj.quit() #send end


    def recieve(self):
        mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        return email_message


if __name__ == '__main__':
    send_mail = Email(
        login='login@gmail.com',
        password='qwerty',subject='Subject',
        recipients=['vasya@email.com', 'petya@email.com'],
        message='Message',
        header=None
    )

