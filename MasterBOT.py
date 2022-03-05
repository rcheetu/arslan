import os
import re
import sys
import time
import paramiko
from pssh.clients import ParallelSSHClient


port = 22
username = 'root'
rsa_path = 'rsa'

ssh_session = []


def Connect(hosts, port, username):
    global ssh_session
    out = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi 
    cc
    lient.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    
                for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
   except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    lient.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    lient.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    lient.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    lient.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    lient.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    lient.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    lient.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
    lient.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    lient.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    lient.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    lient.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    lient.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    lient.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    lient.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
    client = ParallelSSHClient(hosts=hosts, user=username, key_filenamefi        out = client.run_command("sudo screen -d -m python2.7 Mailer.py", read_timeout=3)
    except Exception as e:
        print("run_command: {0}".format(e))
        #continue
    for host_out in out:
        if host_out.stderr is not None:
            for line in host_out.stderr:
                print(line)
        if host_out.stdout is not None:
            for line in host_out.stdout:
                print(line)
    # for host in hosts :
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         print ("[+] Connecting To ", host, " ... ",)
    #         # ssh.connect(host, port, username, password)
    #         ssh.connect(host, username=username, key_filename=rsa_path)
    #         print ("Connected")
    #     except paramiko.SSHException:
    #         print ("ERROR\n[!]Connection To ", host, " Failed")
    #     except:
    #         print ("ERROR\n[!!] Unknown error [!!]")
    #     ssh_session += [ssh]

def excecute_cmd(cmd,ssh):
    print ("[+] Excecuting ", cmd, " ...",)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    errors = stderr.readlines()
    if len(errors):
        print ("ERROR\n")
        for err in errors:
            print (err.strip())
        return errors
    msg = stdout.readlines()
    print ("OK")
    if len(msg):
        for m in msg:
            print (m.strip())
        return msg


def write(list, file):
    list.append(check_email)
    for email in list:
        file.write(email)

# --------------------------------------------------------------
if len(sys.argv) < 1:
    print ("Usage: python ",sys.argv[0]," SMTP")
try:
    servers_lines = open("servers.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your servers text file path\n")
try:
    emails_lines = open("emails.txt", "r").readlines()
    # emails_lines = open("emails.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
    print ("Error: Check your emails text file path\n")
# try:
#     smtps_login = open("smtp.txt", "r").readlines()
#     # smtps_login = open("smtp.txt", "r").readlines()
#     # lines = open(sys.argv[2], "r").readlines()
# except(IOError):
#     print "Error: Check your Smtp text file path\n"

try:
    domains = open("domains.txt", "r").readlines()
    # servers_lines = open("servers.txt", "r").readlines()
    # lines = open(sys.argv[2], "r").readlines()
except(IOError):
	print ("No domains file found ! : Check your domains text file path\n")
	print ("Working with default Domain in Config.ini")
	domains = "none"
for text in [servers_lines, emails_lines]:
    for line in text:
        if "\n" == line:
            text.remove(line)

servers = []
for server in servers_lines:
    servers += re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", server)

#-----------------------------------------------------------------------------------------------------

print ("[+] info :")
print ("          - with Login :",username,"/","RSA-file"," on Port ",port)
print ("          - you have ",len(servers)," Server and ",len(emails_lines)," email")
print ("          - So ",(len(emails_lines) / len(servers))," email per server")
if domains != "none" :
    print ("          - And ",(len(domains))," Domain found")
answer = input("[+] Are you okay with that ? (y/n) :")
if "y" in answer.lower():
    Number_of_emails = len(emails_lines) / len(servers)
    pass
else :
    exit(0)
dirs = ["list","result"]
for dir in dirs :
    if not os.path.exists(dir):
        os.mkdir(dir)

localpath = dirs[0]+"/"
remotepath = "/home/root/"

/homelist_file = []
check_email = input("[+] Enter the check email : ")
# smtp = raw_input("[+] Enter the SMTP server :")
smtp = "none"

for i,outfile in enumerate(servers):
    list_file += [localpath + "emails_" + str(i) + ".txt"]
    out = open(localpath+"emails_"+str(i)+".txt","w")
    # write(check_email+"\n",out)
    write(emails_lines[int(Number_of_emails) * int(i):int(Number_of_emails) * int(int(i) + 1)],out)
    out.close()

Connect(servers, port, username)

for  i, session in enumerate(ssh_session):
    try:
        print ("[+] Sending files to server ",servers[i],"  ",i+1,"/",len(servers))

        sftp = session.open_sftp()
        print ("      Sending emails.txt ...",)
        sftp.put(list_file[i], remotepath+"/emails.txt")
        print ("Ok")
        print ("      Sending Config.ini ...",)
        sftp.put("Config.ini", remotepath+"/Config.ini")
        print ("Ok")
        print ("      Sending letter1.html ...",)
        sftp.put("letter1.html", remotepath+"/letter1.html")
        print ("Ok")
        print ("      Sending Mailer.py ...",)
        sftp.put("Mailer.py", remotepath+"/Mailer.py")
        print ("Ok")
        print ("      Sending domains.txt ...",)
        sftp.put("domains.txt", remotepath + "/domains.txt")
        print ("Ok")
        print ("      Sending Links ...",)
        sftp.put("Links.txt", remotepath + "/Links.txt")
        print ("Ok")
        # session.close()
    except Exception as e:
        print ("[+] A Problem Detected  in ",servers[i]," !")
        print ("[+] ",str(e))

# for  i, session in enumerate(ssh_session):
#     try:
#         print ("[+] Excecuting the script on server ",servers[i],"  ",i+1,"/",len(servers))
#         result = excecute_cmd("sudo screen -d -m python2.7 Mailer.py",session)
#         Out = open(dirs[1]+"/"+servers[i]+".txt","w")
#         write(result,Out)
#         Out.close()
#         # session.close()
#     except Exception as e:
#         print ("[+] A Problem Detected  in ",servers[i]," !")
#         print ("[+] ",str(e))
# print ("[+] Done !")

