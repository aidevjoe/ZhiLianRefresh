#!/bin/python3

import requests
import argparse
import json
from bs4  import BeautifulSoup
import time

class ZlAccount:
    def __init__(self):
        self.loginname=''
        self.password=''
        self.loggedin=False
        self.session=requests.Session()
        self.session.headers.update({'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'})
        #self.session.headers.update({'host':'i.zhaopin.com'})

    def __del__(self):
        if self.session:
            self.session.close()

    def set_cookie(self,cookie):
        # cookies can be obtained  from your Chrome console by the following command: 'document.cookie'
        # pass the raw string to this method.
        self.session.headers.update({'Cookie':cookie})

    def refresh_resumes(self):
        s=self.session
        resp=s.get('https://i.zhaopin.com')
        soup=BeautifulSoup(resp.content,'html.parser')
        #print(soup.prettify())
        search_result=soup.find_all('a',class_='myLinkA linkRefresh')
        if search_result:
            link=search_result[0].attrs['url']
            params=link.split('?')[1]
            kvpairs=params.split('&')
            resume={}
            resume['resumeId']=kvpairs[1].split('=')[1]
            resume['resumenum']=kvpairs[2].split('=')[1]
            self.refresh(resume)
        else:
            print('no resume found.')
        #print(resp.content)

    def refresh(self,resume):
        # resume should be a dict contains two keys:resumeId,resumenum
        url='https://i.zhaopin.com/ResumeCenter/MyCenter/RefreshResume'
        resume['version']='1'
        resume['language']='1'
        resume['t']=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) #str(time.time())
        print('resume dict: %s'%resume)
        r=self.session.get(url,data=resume)
        soup=BeautifulSoup(r.content,'html.parser')
        #print(soup.prettify())
        sr=soup.find_all('h3',class_='entH setH')
        review=soup.find_all("p",class_='saleP')
        if sr:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ": " + sr[0].text + "，" + review[0].text)
        else:
            print('failed..')


def main():
    parser = argparse.ArgumentParser(description='refresh resume on zl')
    parser.add_argument('cookiefile',type=str,help='path/to/your/cookie/file')
    args = parser.parse_args()
    za=ZlAccount()
    f=open(args.cookiefile,'r')
    cookie=f.readline()
    #print(cookie)
    f.close()
    za.set_cookie(cookie.replace('\n',''))
    za.refresh_resumes()

main()
