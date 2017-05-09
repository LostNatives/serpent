#!/usr/bin/python
# Copyright (c) Cameron Poe 2017
# Python 2

import socket
import sys
import os
import time
try:
    from tld import get_tld
except ImportError:
    print ("No tld Imported!")
try:
    import requests
except ImportError:
    print ("No requests Imported!")

def banner():
    print ("""
 Welcome to Serpent Security Recon Tool
 github.com/initnix/serpent
 """)

# Grabbing ipv4 ip
def ipv4address():
    try:
        host = sys.argv[1]
        domain = get_tld(host)
        ip = str(socket.gethostbyname(domain))
        print ("IPV4 address: " + ip)
    except socket.error as msg:
        print ("Socket Error! No Connection")
        sys.exit(1)
    except NameError:
        sys.exit()
    except IndexError:
        sys.exit()

def url():
    try:
        host = sys.argv[1]
        print ("URL: " + host)
    except NameError:
        sys.exit()
    except IndexError:
        sys.exit()

# Outputting domain
def domain():
    try:
        host = sys.argv[1]
        domain = get_tld(host)
        print ("Domain: " + domain)
    except NameError:
        sys.exit()
    except IndexError:
        sys.exit()

# Setting up Functions for directory creation and .txt file creation.
def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_file(path, data):
    f = open(path, "w")
    f.write(str(data))
    with open(path, 'w') as f:
        sys.stdout = f
        main()
    f.close()

# Information thats outputted to user during scans.
def user():
    host = sys.argv[1]
    domain = get_tld(host)
    banner()
    time.sleep(5)
    print (" Finshed. Check 'targets/" + domain + "'")

# Functions thats going to be written to .txt file
def main():
    print ("Basic Info")
    print ("-----------")
    domain()
    url()
    ipv4address()
    print (" \n### Start Recon Report Here. ###")
    print ("-" * 33)

# 'targets' directory and .txt file creation and results being written to file.
def report():
    try:
        host = sys.argv[1]
        domain = get_tld(host)
        ROOT_DIR = 'targets'
        create_dir(ROOT_DIR)
        project_dir = ROOT_DIR + '/'
        create_dir(project_dir)
        write_file(project_dir + '/' + domain + ".txt", user())
    except (KeyboardInterrupt, SystemExit):
        print ("CTR+C! Exiting...")
    except NameError:
        print ("Error")
        sys.exit()
    except IndexError:
        print ("No URL Specifed!")
        print ("Example: " + sys.argv[0] + " https://zay.li/")
        sys.exit()

if __name__ == "__main__":
    if sys.platform == 'win32' or sys.platform == 'win64':
        os.system('cls')
        report()
    else:
        os.system('clear')
        report()
