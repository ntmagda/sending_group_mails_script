
from utils import send_mails

# title - email subject
# text-file - txt file with email body
# mails_file - txt file with emails seperated with commas
# attachment_files - list of filenames to attach ["filename1.pdf, "filename2.pdf"]
# sender - email that emails will be sent from
# password - email password

# all files have to be withing the script directory

title = "Job application"
text_file = "cover_letter.txt"
mails_file = "all_test.txt"
attachment_files = ["CV.pdf", "CV.pdf"]
sender = "ntmagda93@gmail.com"
password = "xxxx"

send_mails(title, text_file, mails_file, attachment_files, sender, password)
