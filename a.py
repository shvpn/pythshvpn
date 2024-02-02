
import time
import ctypes
import os

def change_cmd_color(color_code):
    os.system(f'echo \x1b[1;{color_code}m')

# Example: Change to bright green color (32)
change_cmd_color(32)


name="Senghout"
age=17
name_gf="Chan Thai"
age_g=17
isMan=True
isGirl=False
First=str("ORK")
First_gf=str("SOPHAT")
M=1.72
G=1.52
hight=float(M)
hight_g=float(G)
Hecker="""Your code is in procces........
start hecking................
WiFi key: XXXXXX XXXXX XXXX 
IME: XXX XXXX XXX  XXXX
USER: OPEN TERMINAL"""
message="Tell me your gender:"
proc="GETTING INFO // call for sjfgbds sdbxfcvsjdbfsdhgbsdbfgsdufjsdhfgjdhvgdhg sdfgdvdfh dvbsdfshjfsdhfsdfgsdfgsdhfgsgdfjjvbn bgbsdbhsdgsdfsd fyinf d OKE:"
inf=input(message)
print("Your Gender Have Confirmed, So you are a",inf)
print(First, name)
print("Your Age is", age)
print(isMan)
print("Your hight is ", str(hight))
he=input("Press inter To start Hecking......")
print(Hecker)
d=0
while d<=100:
    
    time.sleep(0.1)
    print(proc , str(d), "%")
    d+=1

print("\n \n \n \033[1;31m<<COMPLETE>>\033[0m")

