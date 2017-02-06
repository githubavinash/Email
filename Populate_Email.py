#pip install names
#Generates random names


#import names
import datetime
import smtplib
import argparse
import time
import os


sender_username = "qastability.ind04@gmail.com"
sender_password = "Iambuild"

parser = argparse.ArgumentParser(description="Enter valid To addr and mail count")
parser.add_argument('-r', '--recipient', required = True, type = str, help = "Enter recipient's email ID")
parser.add_argument('-c', '--count', required = True, type = int, help = "Enter the number of mails to be sent")
args = parser.parse_args()


To = args.recipient
mail_count = args.count
get_email_provider_name = To.split('@')[1].split('.')[0]
count = 0

def populateInbox(subject):
#    print "11111111111"
    FROM = sender_username
    TO = [To]
    SUBJECT = subject
    TEXT = "randon name generated from the names lib. "
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(str(x) for x in TO), SUBJECT, TEXT)
#    print FROM
#    print TO
#    print SUBJECT
#    print message
    try:
#        print"inside try"
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(sender_username,sender_password )
        server.sendmail(FROM, TO, message)
        server.close()
        print "Successfully sent email - "
        time.sleep(2)
    except smtplib.SMTPException:
        print "Error: unable to send email"

#if os.path.isfile("phrasesToSearch"+get_email_provider_name.capitalize()+".txt"):
#    with open("phrasesToSearch"+get_email_provider_name.capitalize()+".txt") as fp:
#        count = sum(1 for line in fp)

#with open("phrasesToSearch"+get_email_provider_name.capitalize()+".txt","a") as fp:
#    for line in range((count+1),(count+mail_count+1)):
#        rand_name_gen = names.get_full_name()
#        fp.write(rand_name_gen+"\n")
#        populateInbox("PopulatingMailsWithSearchString - " + (datetime.date.today().strftime("%d/%m/%Y")) + " LoopNum - " + str(line), str(line))
populateInbox("Jenkins Mail")





