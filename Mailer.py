# coding=utf-8
import base64
import codecs
import quopri
import string
import sys
from ConfigParser import SafeConfigParser
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from random import *
from smtplib import SMTP_SSL, SMTP
import string
import random

min_char = 60
max_char = 100

email_indice = "&email&"
rand_indice = "&rand&"
link_indice = "&link&"

domain_enabled = "False"
links_enabled = "False"


def Generate_random():
    allchar = string.ascii_letters + string.digits
    rand = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return rand


reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

Content_Transfer_Encoding = ["7bit",
                             "base64",
                             "8bit",
                             "binary",
                             "quoted-printable"]


def contains_non_ascii_characters(str_in):
    return not all(ord(c) < 128 for c in str_in)


def add_header(message, header_name, header_value):
    if contains_non_ascii_characters(header_value):
        h = Header(header_value, 'utf-8')
        message[header_name] = h
    else:
        message[header_name] = header_value
    return message


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


# noinspection PyShadowingNames
def send_email(sender, recipient, subject, body, mode, Encoding, X_Mailer, random_sender, list_unsubscribe, List_Id,
               List_Help, Message_Id, sender_domain, link):
    header_charset = 'UTF-8'
    sender_name, sender_addr = parseaddr(sender)
    recipient_name, recipient_addr = parseaddr(recipient)

    if random_sender == "True":
        sender_addr = recipient.split('@')[0] + "@" + sender_addr.split('@')[1]
        sender = formataddr((sender_name, sender_addr))

    if sender_domain != "none":
        sender_addr = recipient.split('@')[0] + "@" + sender_domain.rstrip()
        sender = formataddr((sender_name, sender_addr))

    sender_name = str(Header(unicode(sender_name), header_charset))
    recipient_name = str(Header(unicode(recipient_name), header_charset))

    sender_addr = sender_addr.encode('ascii', 'ignore')
    recipient_addr = recipient_addr.encode('ascii', 'ignore')

    if Encoding == "base64":
        body = base64.b64encode(body)

    if Encoding == "quoted-printable":
        body = quopri.encodestring(body)

    if contains_non_ascii_characters(body):
        msg = MIMEText(body, mode)
    else:
        msg = MIMEText(body, mode)

    msg['From'] = formataddr((sender_name, sender_addr)).replace("\n", "").strip("")
    msg['To'] = formataddr((recipient_name, recipient_addr))
    msg['Subject'] = Header(unicode(subject), header_charset)

    if X_Mailer != 'none':
        msg['X-Mailer'] = X_Mailer
    if list_unsubscribe != 'none':
        msg['List-Unsubscribe'] = list_unsubscribe
    if List_Id == 'true':
        msg['List-Id'] = "<" + str(random_with_N_digits(4)) + "." + str(random_with_N_digits(6)) + "." + \
                         recipient_addr.split('@')[0].replace("-", "").replace("_", "").replace(".", "") + ">"
    if List_Help != 'none':
        msg['List-Help'] = List_Help
    if Message_Id == 'true':
        msg['Message-Id'] = "<" + str(random_with_N_digits(13)) + str(
            random.choice(string.ascii_uppercase)) + "." + str(random_with_N_digits(5)) + "@" + sender_addr.split("@")[
                                1] + ">"
    msg.replace_header('content-transfer-encoding', Encoding)
    try:
        print "[+] Sending to", recipient, "...",
        msg = msg.as_string().replace(email_indice.replace("\n", ""), recipient).replace(rand_indice, Generate_random())
        if link != "none":
            msg = msg.replace(link_indice, link)
        smtp.sendmail(sender, recipient, msg)
        print " Ok"
    except:
        print " ERROR while Sending the e-mail !"
        print sys.exc_info()


def Connect_local(ip):
    global smtp
    try:
        print "[+] Connecting To ", ip, " ...",
        smtp = SMTP(ip, 25)
        print " Connected !"

    except:
        print " ERROR { connection attempt failed } while Connecting to server !"
        if "connection attempt failed" in str(sys.exc_info()):
            Connect_local(ip)
        else:
            print "Unknown error Exit ..."
            sys.exit(0)


def Disconnect():
    try:
        print "[+] Disconnecting From server ...",
        smtp.quit()
        print " OK"
    except:
        print ' ERROR while Disconnecting from server !'
        print sys.exc_info()


def get(parser, name):
    if parser.has_option("config", name):
        return parser.get("config", name)
    return None


# -----------------------------------------------------------
msg = str(codecs.open("letter1.html", 'r', 'utf-8').read())
print "[+] Loading Config data ..."
try:
    config = SafeConfigParser()
    config.read('Config.ini')
    if config.has_section('config'):
        sender = config.get('config', 'sender')
        subject = config.get('config', 'subject')
        mode = config.get('config', 'mode')
        Encoding = config.get('config', 'Encoding')
        X_Mailer = config.get('config', 'X_Mailer')
        List_Id = config.get('config', 'List_Id')
        List_Help = config.get('config', 'List_Help')
        Message_Id = config.get('config', 'Message_Id')
        list_unsubscribe = config.get('config', 'list_unsubscribe')

        print "     -sender     : ", sender
        print "     -subject    : ", subject
        print "     -mode       : ", mode
        print "     -Encoding   : ", Encoding
        print "     -X_Mailer   : ", X_Mailer
        print "     -List_Id   : ", List_Id
        print "     -List_Help   : ", List_Help
        print "     -Message_Id   : ", Message_Id
        print "     -list_unsubscribe   : ", list_unsubscribe

    if config.has_section('Mode'):
        random_sender = config.get('Mode', 'random_sender')
    if "True" in random_sender:
        print "Random Sender Mode Activated !!"
    else:
        print "[!] No section \"config\" in Config.ini"
except:
    print sys.exc_info()
    print "[+] Error : Config.ini  "
    exit(0)


def get_data(filename):
    try:
        data = open(filename, "r").readlines()
        print "[+] Imported ", len(data), " from ", filename
        return data
    except IOError:
        print "Error: Check your ", filename, " - Not Found\n"
        exit(0)


domains = get_data("domains.txt")
email_lines = get_data("emails.txt")
links = get_data("Links.txt")

if not len(domains):
    domain = "none"
if not len(links):
    link = "none"

# lines = open(sys.argv[1], "r").readlines()
# ---------------------------
# --------------------
domain_counter = -1
links_counter = -1
Connect_local("127.0.0.1")
for i, email in enumerate(email_lines):
    if i % 2 == 0:
        domain_counter += 1
        links_counter += 1
        Disconnect()
        Connect_local("127.0.0.1")
    email = email.replace("\n", "").strip(" ")
    try:
        domain = domains[domain_counter]
        link = links[links_counter]
    except IndexError:
        domain_counter = 0
        links_counter = 0
    send_email(sender=sender,
               recipient=email,
               subject=subject,
               body=msg,
               mode=mode,
               Encoding=Encoding,
               X_Mailer=X_Mailer,
               list_unsubscribe=list_unsubscribe,
               random_sender=random_sender,
               List_Id=List_Id,
               List_Help=List_Id,
               Message_Id=Message_Id,
               sender_domain=domain,
               link=link
               )

Disconnect()
