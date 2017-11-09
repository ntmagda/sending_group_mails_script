import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time


def prepare_msg(title, data, sender, attachment_files):
    msg = MIMEMultipart()
    msg.attach(MIMEText(data))
    msg['Subject'] = title
    msg['From'] = sender
    for file in attachment_files:
        part = MIMEApplication(open(file, 'rb').read())
        part['Content-Disposition'] = 'attachment; filename="%s"' % file
        msg.attach(part)
    return msg

# title - mail title
# data- mail body
# mail-list = list of mails
# sender- sender email address
# attachment_files - list of attachmed file names
def send_message_m(title, data, mails_list, attachment_files, sender, password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)

    msg = prepare_msg(title, data, sender, attachment_files)
    for mail in mails_list:
        msg['Bcc'] = mail
        server.send_message(msg)
    server.quit()


def parse(raw_data):
    mail_list = [x.strip() for x in raw_data.split(',')]
    return mail_list

#check if all mails in the list are in a proper format, if not delete the mails and print out
def check_regex(mail_list):
    email_regex = "[^@]+@[^@]+\.[^@]+"
    wrong_mails = []
    for mail in mail_list:
        pattern = re.compile(email_regex)
        if pattern.match(mail) is None:
            print('wrong one:')
            print(mail)
            wrong_mails.append(mail)
            mail_list.remove(mail)
        else:
            pass
    return wrong_mails

def get_mail_list(file):
    with open(file) as all:
        raw_mail_list_r = all.read()
    return raw_mail_list_r

def get_msg_text(file):
    with open(file) as text_file:
        msg_text = text_file.read()
    return msg_text


def send_mails(title, text_file, mails_file, attachment_files, sender, password):
    start_time = time.time()
    raw_mail_list = get_mail_list(mails_file)
    mail_list = parse(raw_mail_list)

    text = get_msg_text(text_file)
    wrong_mails = check_regex(mail_list)
    if wrong_mails is not []:
        print("Not correct email adresses detected: ")
        print(wrong_mails)
    print("Sending %d mails: " % mail_list.__len__())
    print(mail_list)
    send_message_m(title, text, mail_list, attachment_files, sender, password)
    print("--- %s seconds ---" % (time.time() - start_time))
