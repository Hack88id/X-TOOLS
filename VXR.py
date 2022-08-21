import os,time,random,rich
from rich.panel import Panel as nel
from rich import print as cetak
from os import system
from time import sleep


#------[ System ]------
system('git pull && clear')
system('clear')
code = random.choice(['928165','619351','19361','92610','01734','8163','01429','027419','0262','01731','81539','91539','81916','14201','0172','01539'])

#-----[ Warna ]-----
p = '\033[1;0m' #Putih
h = '\033[1;32m' #Hijau
u = '\033[1;95m' #Ungu
k = '\033[1;33m' #Kuning
b = '\033[1;96m' #Biru
m = '\033[1;31m' #Merah

ran = random.choice ([h,u,k,m,b,])
ran1 = random.choice ([h,u,k,m,b,])
ran2 = random.choice ([h,u,k,m,b,])
ran3 = random.choice ([h,u,k,m,b,])
ran4 = random.choice ([h,u,k,m,b,])
def menu():
        print (f'''{ran2}
	  _             _
	   `           '
	    `         '
	     `       '
	    ___________
	    | [×] [×] |
	    |    -    |
	    |   ___   |
	    ===========
	        | |
	=====================
	= INFORMASI TOOLS   =
	= Author : Riko     =
	= Github : hack88id =
	=====================

{ran}╭────────────────────────────────╮
{ran}│           {ran1}MENU TOOLS{ran}           │
{ran}├──────┬─────────────────────────┤
{ran}│  {ran1}NO  {ran}│     {ran1}TOOLS               {ran}│
{ran}├──────┼─────────────────────────┤
{ran}│ {k}[{u}01{k}] {ran}│ {m}SPAM SMS                {ran}│
{ran}├──────┼─────────────────────────┤
{ran}│ {k}[{u}02{k}] {ran}│ {m}HACK FACEBOOK {b}({k}TARGET{b})  {ran}│
{ran}├──────┼─────────────────────────┤
{ran}│ {k}[{u}03{k}] {ran}│ {m}LACAK IP                {ran}│
{ran}├──────┼─────────────────────────┤
{ran}│ {k}[{u}04{k}] {ran}│ {m}BUAT WORDLIST           {ran}│
{ran}├──────┼─────────────────────────┤
{ran}│ {k}[{u}05{k}] {ran}│ {m}DDOS ATACK v1           {ran}│
{ran}├──────┼─────────────────────────┤
{ran}│ {k}[{u}06{k}] {ran}│ {m}DDOS ATACK v2           {ran}│
{ran}├──────┼─────────────────────────┤
{ran}│ {k}[{u}00{k}] {ran}│ {m}EXIT                    {ran}│
{ran}├──────┼─────────────────────────┤
{ran}│ {k}[{u}99{k}] {ran}│ {m}INSTALL BAHAN           {ran}│
{ran}╰──────┴─────────────────────────╯
''')

def pilih():
	plh = input(f'{h}[{b}•{h}] {u}Choice :{m} ')
	if plh == "01":
		system('python bot.py')
	elif plh == "02":
		tar = input('Masukan id/nomor/gmail Target : ')
		wl = input('Masukan Letak Wordlis : ')
		system(f'python faceboom.py -t {tar} -w {wl}')
	elif plh == "06":
		ip = input('Masukan Ip Server : ')
		port = input('Masukan Port Server : ')
		turbo = input('Masukan Jumlah Turbo : ')
		system(f'python hammer.py -s {ip} -p {port} -t {turbo}')
	elif plh == "03":
		iptar = input('Masukan Ip Terget : ')
		system(f'python ipgeolocation.py -t {iptar}')
	elif plh == "04":
		system('python cupp.py -i')
	elif plh == "08":
		link08 = input('Masukan Url : ')
		system('xdg-open {link08}')
	elif plh == "05":
		ip31 = input('Masukan Ip Server : ')
		port31 = input('Masukan Port : ')
		jum31 = input('Masukan Jumlah : ')
		system(f'python2 LITEDDOS.py {ip31} {port31} {jum31}')
	elif plh == "00":
		exit()
	elif plh == "99":
		system('pkg install python3 && pip install requests && pip install json && pip install rich && pip install mechanize pkg install python2')
		print (']---------------[\n Install Selesai\n]---------------[')
def login():
	print (f'''{ran}
	aaaaaaaaa
       aa       aa
       aa       aa
       aa       aa
     aaaaaaaaaaaaaaa
     aa           aa
     aa           aa
     aa           aa
     aaaaaaaaaaaaaaa

   {ran1}Human  verification

{ran2}Your kode : {ran3}{code}

''')

	kd = input(f'{ran}[{ran1}•{ran}] {ran4}Input Kode :{ran2} ')

	if kd not in('928165','619351','19361','92610','01734','8163','01429','027419','0262','01731','81539','91539','81916','14201','0172','01539','1'):
		print (f'\n{m}Login Fail [X]')
		exit()
	else:
		print (f'\n{h}Login Sukses [✓]')
		sleep(2)
		system('clear')
		menu()
		pilih()
login()

