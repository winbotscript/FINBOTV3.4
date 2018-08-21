#Authorized by http://line.me/ti/p/~kangnur04
#ALFINONH
from FinbotV1.finbotpy import *
from FinbotV1.finbot.ttypes import *
from FinbotV1.finbotpy import FinbotLoginService, FinbotService
from FinbotV1.finbotpy.ttypes import LoginRequest
from FinbotServer.protocol import TCompactProtocol
from FinbotServer.transport import THttpClient
from datetime import datetime
from datetime import timedelta, date
from time import sleep
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import pytz, pafy, time, timeit, random, sys, ast, re, os, json, requests, threading, subprocess, string, codecs, ctypes, urllib, urllib.parse, shutil, atexit, six, ffmpy, youtube_dl
from multiprocessing import Pool, Process
from ffmpy import FFmpeg
_session = requests.session()

botStart = time.time()
mulai = time.time()
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

bot_login = codecs.open('finbotLogged.json', 'r', 'utf-8')
run_bot = json.load(bot_login)

host = 'https://gwx.line.naver.jp'
FINBOT_TIMELINE_API = 'https://gwx.line.naver.jp/mh/api'
FINBOT_TIMELINE_MH = 'https://gwx.line.naver.jp/mh'
FINBOT_OBS_DOMAIN = 'https://obs-tw.line-apps.com'
FINBOT_AUTH_QUERY_PATH = '/api/v4p/rs'
FINBOT_AUTH_QUERY_PATH_FIR = '/api/v4/TalkService.do'
FINBOT_CERTIFICATE_PATH = '/Q'
FINBOT_API_QUERY_PATH_FIR = '/S4'

UA = run_bot['DESKTOPMAC']['UA']
LA = run_bot['DESKTOPMAC']['LA']
UA1 = run_bot['CHROMEOS']['UA']
LA1 = run_bot['CHROMEOS']['LA']
UA2 = run_bot['DESKTOPWIN']['UA']
LA2 = run_bot['DESKTOPWIN']['LA']
UA3 = run_bot["IOS"]["UA"]
LA3 = run_bot["IOS"]["LA"]
UA4 = run_bot['WIN10']['UA']
LA4 = run_bot["WIN10"]['LA']
UA5 = run_bot['CLOVAFRIENDS']['UA']
LA5 = run_bot["CLOVAFRIENDS"]["LA"]

if run_bot['authToken'] == "":
    fino = FINBOTV1()
    run_bot['authToken'] = str(fino.authToken)
    channel = FinbotChannel(fino, channelId="1341209850")
    finoMID = fino.getProfile().mid
    run_bot['authTokenMid'] = finoMID
    run_bot["Creator"] = finoMID
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
else:
    try:
        fino = FINBOTV1(run_bot['authToken'])
        channel = FinbotChannel(fino, channelId="1341209850")
        finoMID = fino.getProfile().mid
        run_bot['authTokenMid'] = finoMID
        run_bot["Creator"] = finoMID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
    except:
        fino = FINBOTV1(run_bot['authToken'])
        channel = FinbotChannel(fino, channelId="1341209850")
        finoMID = fino.getProfile().mid
        run_bot['authTokenMid'] = finoMID
        run_bot["Creator"] = finoMID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)

if run_bot['kang'] == "":
    kang = FINBOTV1()
    run_bot['kang'] = str(kang.authToken)
    channel = FinbotChannel(kang, channelId="1341209850")
    myMID = kang.getProfile().mid
    run_bot['kangMid'] = myMID
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
else:
    try:
        kang = FINBOTV1(run_bot['kang'])
        channel = FinbotChannel(kang, channelId="1341209850")
        myMID = kang.getProfile().mid
        run_bot['kangMid'] = myMID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
    except:
        kang = FINBOTV1(run_bot['kang'])
        channel = FinbotChannel(kang, channelId="1341209850")
        myMID = kang.getProfile().mid
        run_bot['kangMid'] = myMID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)

if run_bot['fino1'] == "":
    fn1 = FINBOTV1()
    channel = FinbotChannel(fn1,channelId="1341209850")
    run_bot['fino1'] = str(fn1.authToken)
    fn1MID = fn1.getProfile().mid
    run_bot["fino1Mid"] = fn1MID
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
else:
    try:
        fn1 = FINBOTV1(run_bot['fino1'])
        channel = FinbotChannel(fn1,channelId="1341209850")
        fn1MID = fn1.getProfile().mid
        run_bot["fino1Mid"] = fn1MID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
    except:
        fn1 = FINBOTV1(run_bot['fino1'])
        channel = FinbotChannel(fn1,channelId="1341209850")
        fn1MID = fn1.getProfile().mid
        run_bot["fino1Mid"] = fn1MID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)

if run_bot['fino2'] == "":
    fn2 = FINBOTV1()
    channel = FinbotChannel(fn2,channelId="1341209850")
    run_bot['fino2'] = str(fn2.authToken)
    fn2MID = fn2.getProfile().mid
    run_bot["fino2Mid"] = fn2MID
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
else:
    try:
        fn2 = FINBOTV1(run_bot['fino2'])
        channel = FinbotChannel(fn2,channelId="1341209850")
        fn2MID = fn2.getProfile().mid
        run_bot["fino2Mid"] = fn2MID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
    except:
        fn2 = FINBOTV1(run_bot['fino2'])
        channel = FinbotChannel(fn2,channelId="1341209850")
        fn2MID = fn2.getProfile().mid
        run_bot["fino2Mid"] = fn2MID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)

if run_bot['fino3'] == "":
    fn3 = FINBOTV1()
    channel = FinbotChannel(fn3,channelId="1341209850")
    run_bot['fino3'] = str(fn3.authToken)
    fn3MID = fn3.getProfile().mid
    run_bot["fino3Mid"] = fn3MID
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
else:
    try:
        fn3 = FINBOTV1(run_bot['fino3'])
        channel = FinbotChannel(fn3,channelId="1341209850")
        fn3MID = fn3.getProfile().mid
        run_bot["fino3Mid"] = fn3MID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
    except:
        fn3 = FINBOTV1(run_bot['fino3'])
        channel = FinbotChannel(fn3,channelId="1341209850")
        fn3MID = fn3.getProfile().mid
        run_bot["fino3Mid"] = fn2MID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)

if run_bot['fino4'] == "":
    fn4 = FINBOTV1()
    channel = FinbotChannel(fn4,channelId="1341209850")
    run_bot['fino4'] = str(fn4.authToken)
    fn4MID = fn4.getProfile().mid
    run_bot["fino4Mid"] = fn4MID
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
else:
    try:
        fn4 = FINBOTV1(run_bot['fino4'])
        channel = FinbotChannel(fn4,channelId="1341209850")
        fn4MID = fn4.getProfile().mid
        run_bot["fino4Mid"] = fn4MID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
    except:
        fn4 = FINBOTV1(run_bot['fino4'])
        channel = FinbotChannel(fn4,channelId="1341209850")
        fn4MID = fn4.getProfile().mid
        run_bot["fino4Mid"] = fn4MID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)

if run_bot['fino5'] == "":
    fn5 = FINBOTV1()
    channel = FinbotChannel(fn5,channelId="1341209850")
    run_bot['fino5'] = str(fn5.authToken)
    fn5MID = fn5.getProfile().mid
    run_bot["fino5Mid"] = fn5MID
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
else:
    try:
        fn5 = FINBOTV1(run_bot['fino5'])
        channel = FinbotChannel(fn5,channelId="1341209850")
        fn5MID = fn5.getProfile().mid
        run_bot["fino5Mid"] = fn5MID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
    except:
        fn5 = FINBOTV1(run_bot['fino5'])
        channel = FinbotChannel(fn5,channelId="1341209850")
        fn5MID = fn5.getProfile().mid
        run_bot["fino5Mid"] = fn5MID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)

if run_bot['kicker1'] == "":
    k1 = FINBOTV1()
    run_bot['kicker1'] = str(k1.authToken)
    k1MID = k1.getProfile().mid
    run_bot["kicker1Mid"] = k1MID
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
else:
    try:
        k1 = FINBOTV1(run_bot['kicker1'])
        k1MID =k1.getProfile().mid
        run_bot["kicker1Mid"] = k1MID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
    except:
        k1 = FINBOTV1(run_bot['kicker1'])
        k1MID = k1.getProfile().mid
        run_bot["kicker1Mid"] = k1MID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
        
if run_bot['kicker2'] == "":
    k2 = FINBOTV1()
    run_bot['kicker2'] = str(k2.authToken)
    k2MID = k2.getProfile().mid
    run_bot["kicker2Mid"] = k2MID
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
else:
    try:
        k2 = FINBOTV1(run_bot['kicker2'])
        k2MID =k2.getProfile().mid
        run_bot["kicker2Mid"] = k2MID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
    except:
        k2 = FINBOTV1(run_bot['kicker2'])
        k2MID = k2.getProfile().mid
        run_bot["kicker2Mid"] = k2MID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)

if run_bot['kicker3'] == "":
    k3 = FINBOTV1()
    run_bot['kicker3'] = str(k3.authToken)
    k3MID = k3.getProfile().mid
    run_bot["kicker3Mid"] = k3MID
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
else:
    try:
        k3 = FINBOTV1(run_bot['kicker3'])
        k3MID =k3.getProfile().mid
        run_bot["kicker3Mid"] = k3MID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
    except:
        k3 = FINBOTV1(run_bot['kicker3'])
        k3MID = k3.getProfile().mid
        run_bot["kicker3Mid"] = k3MID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
try:
    run_bot["assist"] = {}
    run_bot['assist'][myMID] = True
    run_bot['assist'][fn1MID] = True
    run_bot["assist"][fn2MID] = True
    run_bot["assist"][fn3MID] = True
    run_bot["assist"][fn4MID] = True
    run_bot["assist"][fn5MID] = True
    run_bot["assist"][k1MID] = True
    run_bot["assist"][k2MID] = True
    run_bot["assist"][k3MID] = True
    backupData()
except:
    print ("\nRunning...")

settBot = codecs.open("finbot1.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
bot_run = json.load(settBot)
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

finobot = FinbotPoll(kang)
_FINBOT = run_bot["assist"]
Bots = [myMID,fn1MID,fn2MID,fn3MID,fn4MID,fn5MID,k1MID,k2MID,k3MID]
admin = run_bot["Admin"]
Owner = bot_run["ALFINONH"]
Creator = ["u4d2f1c2fbee16358f12c749f406cfbf0"]
Master = Owner + str(_FINBOT)

FNO = [fn1,fn2,fn3,fn4,fn5]
KAC  = [fn1,fn2,fn3,fn4,fn5]
_Random = random.choice(FNO)
_SendChat = fino.sendMessage
_SendChatt1 = fino.sendText
_Chat = kang.sendMessage
_Chat1 = fn1.sendMessage
_Chat2 = fn2.sendMessage
_Chat3 = fn3.sendMessage
_Chat4 = fn4.sendMessage
_Chat5 = fn5.sendMessage
_Chatt = kang.sendText
_Chatt1 = fn1.sendText
_Chatt2 = fn2.sendText
_Chatt3 = fn3.sendText
_Chatt4 = fn4.sendText
_Chatt5 = fn5.sendText
protectname = []
msg_dict = {}
msg_dict1 = {}
run = {"finbot":True, "addMe":False}

if bot_run["restartBot"] != None:
    _Chat(bot_run["restartBot"], "\nRestarted")
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")

def backupData():
    try:
        backup = bot_run
        f = codecs.open('finbot1.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup1 = run_bot
        f = codecs.open('finbotLogged.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = images
        f = codecs.open('image.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = audios
        f = codecs.open('audio.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = videos
        f = codecs.open('video.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup5 = stickers
        f = codecs.open('sticker.json','w','utf-8')
        json.dump(backup5, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        print (error)
        return False

def command(text):
    pesan = text.lower()
    if pesan.startswith(bot_run["keyCommand"]):
        cmd = pesan.replace(bot_run["keyCommand"],"")
    else:
        cmd = ""
    return cmd

def getJson(url, headers=None):
    if headers is None:
        return json.loads(_session.get(url).text)
    else:
        return json.loads(_session.get(url, headers=headers).text)

def defaultCallback(str):
    print(str)

def DESKTOPMAC(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': UA,'X-Line-Application': LA,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client

def CHROMEOS(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': UA1,'X-Line-Application': LA1,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client
 
def DESKTOPWIN(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': UA2,'X-Line-Application': LA2,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client

def IOS(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': UA3,'X-Line-Application': LA3,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client

def WIN10(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': UA4,'X-Line-Application': LA4,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client

def CLOVAFRIENDS(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': UA5,'X-Line-Application': LA5,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client

def autoRestart():
    if time.time() - botStart > int(bot_run["timeRestart"]):
        backupData()
        time.sleep(5)
        restartBot()

def restart_program():
    print ("\nRestarted\nPlease Wait...\n")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def restartBot():
    print ("\nRestarting\nPlease Wait...\n")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                kang.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > timedelta(1):
            del msg_dict1[msg_id]

def atend():
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
atexit.register(atend)

def atend1():
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
atexit.register(atend)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d D %02d H %02d M %02d S' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d D %02d H %02d M %02d S' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "[ Total {} ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i.) " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(kang.getGroup(to).name))
                except:
                    no = "\n[ FINBOT ]"
        _Chat(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        _Chat(to, "[ INFO Mention member] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Hai.. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+bot_run["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(kang.getGroup(to).name))
                except:
                    no = "\n[ FINBOT ]"
        _Chat(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        _Chat(to, "[ INFO Sider Member] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Welcome ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = kang.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+bot_run["welcome"]+"\nGrup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(kang.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        _Chat(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        _Chat(to, "[ INFO Welcome Member] Error :\n" + str(error))

def getMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    _Chat(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def getMention1(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    _Chat1(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def getMention2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    _Chat2(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def getMention3(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    _Chat3(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def getMention4(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    _Chat4(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def getMention5(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    _Chat5(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def finbot(alfino):
    global time
    global ast
    global groupParam
    try:
        if alfino.type == 0:
            return
        if alfino.type == 5:
            if bot_run["autoBlock"] == True:
                _Chat(alfino.param1, "...Autoblock on")
                kang.blockContact(alfino.param1)
                
            if bot_run["autoAdd"] == True:
                if alfino.param2 not in Bots and alfino.param2 not in Master:
                    if (bot_run["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        kang.findAndAddContactsByMid(alfino.param1)
                        _Chat(alfino.param1, bot_run["message"])

        if alfino.type == 11:
            if alfino.param1 in bot_run["Pro_Qr"]:
                try:
                    if kang.getGroup(alfino.param1).preventedJoinByTicket == False:
                        if alfino.param2 not in Bots and alfino.param2 not in Master:
                            Ticket = kang.reissueGroupTicket(alfino.param1)
                            k1.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                            k2.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                            X = k2.getGroup(alfino.param1)
                            X.preventedJoinByTicket = True
                            k2.updateGroup(X)
                            bot_run["Blacklist_User"][alfino.param2] = True
                            k1.kickoutFromGroup(alfino.param1,[alfino.param2])
                            k1.leaveGroup(msg.to)
                            k2.leaveGroup(msg.to)
                except:
                    try:
                        if fn1.getGroup(alfino.param1).preventedJoinByTicket == False:
                            if alfino.param2 not in Bots and alfino.param2 not in Master:
                                Ticket = fn1.reissueGroupTicket(alfino.param1)
                                k2.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                k1.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                X = k1.getGroup(alfino.param1)
                                X.preventedJoinByTicket = True
                                k1.updateGroup(X)
                                bot_run["Blacklist_User"][alfino.param2] = True
                                k2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                k2.leaveGroup(alfino.param1)
                                k1.leaveGroup(msg.to)
                    except:
                        pass

            if bot_run["nyusup"] == True:
                try:
                    if kang.getGroup(alfino.param1).preventedJoinByTicket == False:
                        if alfino.param2 not in Bots and alfino.param2 not in Master:
                            Ticket = kang.reissueGroupTicket(alfino.param1)
                            fino.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                            fn1.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                            fn2.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                            fn3.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                            fn4.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                            fn5.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                except:
                    pass

            if alfino.param3 == '1':
                if alfino.param1 in protectname:
                    try:
                        if alfino.param2 not in Bots and alfino.param2 not in Master:
                        	group = kang.getGroup(alfino.param1)
                        group.name = bot_run["pro_name"][alfino.param1]
                        kang.updateGroup(group)
                        _Chat(alfino.param1, "Group Name protected\nYou have been warned..!")
                        _Chat(alfino.param1, None, contentMetadata={'mid': alfino.param2}, contentType=13)
                        bot_run["Blacklist_User"][alfino.param2] = True
                    except:
                        pass

            if alfino.param3 == '1':
                if alfino.param1 in bot_run['pname']:
                    try:
                        G = kang.getGroup(alfino.param1)
                    except:
                        try:
                            G = fn1.getGroup(alfino.param1)
                        except:
                            try:
                                G = fn2.getGroup(alfino.param1)
                            except:
                                try:
                                    G = fn3.getGroup(alfino.param1)
                                except:
                                    try:
                                        G = fn4.getGroup(alfino.param1)
                                    except:
                                        try:
                                            G = fn5.getGroup(alfino.param1)
                                        except:
                                            pass
                    G.name = bot_run['pro_name'][alfino.param1]
                    try:
                        kang.updateGroup(G)
                    except:
                        try:
                            fn1.updateGroup(G)
                        except:
                            try:
                                fn2.updateGroup(G)
                            except:
                                try:
                                    fn3.updateGroup(G)
                                except:
                                    try:
                                        fn4.updateGroup(G)
                                    except:
                                        try:
                                            fn5.updateGroup(G)
                                        except:
                                            pass
                    if alfino.param2 in Bots and alfino.param2 in Master:
                        pass
                    else:
                        try:
                            fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                        except:
                            try:
                                fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                            except:
                                try:
                                    fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                except:
                                    try:
                                        fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    except:
                                        try:
                                            fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        except:
                                            pass

        if alfino.type == 13:
            if finoMID in alfino.param3:
                if bot_run["autoLeave"] == True:
                    if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in Creator and alfino.param2 not in admin:
                        fino.acceptGroupInvitation(alfino.param1)
                        ginfo = fino.getGroup(alfino.param1)
                        contact = fino.getContact(alfino.param2)
                        _SendChat(alfino.param1,"Hallo... " +str(ginfo.name))
                        _SendChat(alfino.param1,"Sorry...! \n" +str(contact.displayName) + " Sedang gk mood... ")
                        fino.leaveGroup(alfino.param1)
                    else:
                        fino.acceptGroupInvitation(alfino.param1)
                        ginfo = fino.getGroup(alfino.param1)
                        _SendChat(alfino.param1,"Hello... " +str(ginfo.name))

            if myMID in alfino.param3:
                if bot_run["autoLeave"] == True:
                    if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in Creator and alfino.param2 not in admin:
                        kang.acceptGroupInvitation(alfino.param1)
                        ginfo = kang.getGroup(alfino.param1)
                        contact = kang.getContact(alfino.param2)
                        _Chat(alfino.param1,"Thanks for invite me to " +str(ginfo.name))
                        _Chat(alfino.param1,"Sorry...No permission! \n" +str(contact.displayName) + " You are not included in our schedule and our customers")
                        kang.leaveGroup(alfino.param1)
                    else:
                        kang.acceptGroupInvitation(alfino.param1)
                        ginfo = kang.getGroup(alfino.param1)
                        _Chat(alfino.param1,"Thanks for invite me to " +str(ginfo.name))

            if myMID in alfino.param3:
                G = kang.getGroup(alfino.param1)
                if bot_run["autoJoin"] == True:
                    if bot_run["limiter"]["on"] == True:
                        if len(G.members) <= bot_run["limiter"]["members"]:
                            kang.acceptGroupInvitation(alfino.param1)
                            group = kang.getGroup(alfino.param1)
                            _Chat(alfino.param1,"Maaf jumlah member\n " + str(group.name) + " kurang dari " + str(bot_run["limiter"]["members"]))
                            kang.leaveGroup(alfino.param1)
                        else:
                            kang.acceptGroupInvitation(alfino.param1)
                    else:
                        kang.acceptGroupInvitation(alfino.param1)
                elif bot_run["limiter"]["on"] == True:
                    if len(G.members) <= bot_run["limiter"]["members"]:
                        kang.rejectGroupInvitation(alfino.param1)
            else:
                Inviter = alfino.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in bot_run["Blacklist_User"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kang.cancelGroupInvitation(alfino.param1, matched_list)

            if finoMID in alfino.param3:
                G = fino.getGroup(alfino.param1)
                if bot_run["autoJoin"] == True:
                    if bot_run["limiter"]["on"] == True:
                        if len(G.members) <= bot_run["limiter"]["members"]:
                            fino.acceptGroupInvitation(alfino.param1)
                            group = fino.getGroup(alfino.param1)
                            _SendChat(alfino.param1,"Maaf jumlah member\n " + str(group.name) + " kurang dari " + str(bot_run["limiter"]["members"]))
                            fino.leaveGroup(alfino.param1)
                        else:
                            fino.acceptGroupInvitation(alfino.param1)
                    else:
                        fino.acceptGroupInvitation(alfino.param1)

            if fn1MID in alfino.param3:
                if bot_run["autoJoin"] == True:
                    if alfino.param2 in Creator:
                        fn1.acceptGroupInvitation(alfino.param1)
                    else:
                        fn1.acceptGroupInvitation(alfino.param1)

            if fn2MID in alfino.param3:
                if bot_run["autoJoin"] == True:
                    if alfino.param2 in Creator:
                        fn2.acceptGroupInvitation(alfino.param1)
                    else:
                        fn2.acceptGroupInvitation(alfino.param1)

            if fn3MID in alfino.param3:
                if bot_run["autoJoin"] == True:
                    if alfino.param2 in Creator:
                        fn3.acceptGroupInvitation(alfino.param1)
                    else:
                        fn3.acceptGroupInvitation(alfino.param1)

            if fn4MID in alfino.param3:
                if bot_run["autoJoin"] == True:
                    if alfino.param2 in Creator:
                        fn4.acceptGroupInvitation(alfino.param1)
                    else:
                        fn4.acceptGroupInvitation(alfino.param1)

            if fn5MID in alfino.param3:
                if bot_run["autoJoin"] == True:
                    if alfino.param2 in Creator:
                        fn5.acceptGroupInvitation(alfino.param1)
                    else:
                        fn5.acceptGroupInvitation(alfino.param1)

            if alfino.param3 in bot_run["Blacklist_User"]:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Master:
                    pass
                else:
                    try:
                        if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                            fn1.cancelGroupInvitation(alfino.param1,[alfino.param3])
                            bot_run["Blacklist_User"][alfino.param2] = True
                            with open('finbot1.json','w') as fp:
                                json.dump(bot_run, fp, sort_keys=True, indent=4)
                            fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                    except:
                        try:
                            if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                fn2.cancelGroupInvitation(alfino.param1,[alfino.param3])
                                bot_run["Blacklist_User"][alfino.param2] = True
                                with open('finbot1.json','w') as fp:
                                    json.dump(bot_run, fp, sort_keys=True, indent=4)
                                fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                        except:
                            try:
                                if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                    fn3.cancelGroupInvitation(alfino.param1,[alfino.param3])
                                    bot_run["Blacklist_User"][alfino.param2] = True
                                    with open('finbot1.json','w') as fp:
                                    	json.dump(bot_run, fp, sort_keys=True, indent=4)
                                    fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                            except:
                                try:
                                    if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                        fn4.cancelGroupInvitation(alfino.param1,[alfino.param3])
                                        bot_run["Blacklist_User"][alfino.param2] = True
                                        with open('finbot1.json','w') as fp:
                                        	json.dump(bot_run, fp, sort_keys=True, indent=4)
                                        fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                except:
                                    try:
                                        if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                            fn5.cancelGroupInvitation(alfino.param1,[alfino.param3])
                                            bot_run["Blacklist_User"][alfino.param2] = True
                                            with open('finbot1.json','w') as fp:
                                            	json.dump(bot_run, fp, sort_keys=True, indent=4)
                                            fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    except:
                                        pass

        if alfino.type == 17:
            if alfino.param1 in bot_run["Welcome"]:
                if alfino.param2 in Bots and alfino.param2 in Master and alfino.param2 in admin:
                    pass
                ginfo = kang.getGroup(alfino.param1)
                contact = kang.getContact(alfino.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(alfino.param1, [alfino.param2])
                kang.sendImageWithURL(alfino.param1, image)

            if alfino.param2 in bot_run["Blacklist_User"]:
                try:
                    if alfino.param3 not in bot_run["Blacklist_User"]:
                        _Random.kickoutFromGroup(alfino.param1,[alfino.param2])
                except:
                    pass

            if alfino.param1 in bot_run["Pro_Join"]:
                if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                    except:
                        try:
                            fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                        except:
                            try:
                                fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                            except:
                                try:
                                    fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                except:
                                    try:
                                        fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    except:
                                        pass

        if alfino.type == 19:
            if alfino.param1 in bot_run["Pro_Member"]:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Creator:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    try:
                        if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                            bot_run["Blacklist_User"][alfino.param2] = True
                            with open('finbot1.json','w') as fp:
                                json.dump(bot_run, fp, sort_keys=True, indent=4)
                            user = kang.getContact(alfino.param2)
                            _Chat(alfino.param1,"Nahh kikil beraksi!! " + str(user.displayName))
                            try:
                                if alfino.param3 not in bot_run["Blacklist_User"]:
                                    _Random.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    _Random.findAndAddContactsByMid(alfino.param3)
                                    _Random.inviteIntoGroup(alfino.param1,[alfino.param3])
                            except:
                                try:
                                    if alfino.param3 not in bot_run["Blacklist_User"]:
                                        _Random.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        _Random.findAndAddContactsByMid(alfino.param3)
                                        _Random.inviteIntoGroup(alfino.param1,[alfino.param3])
                                except:
                                    pass
                        else:
                            pass
                    except:
                        try:
                            if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                bot_run["Blacklist_User"][alfino.param2] = True
                                with open('finbot1.json','w') as fp:
                                    json.dump(bot_run, fp, sort_keys=True, indent=4)
                                k1.acceptGroupInvitation(alfino.param1)
                                k1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                k1.findAndAddContactsByMid(alfino.param3)
                                k1.inviteIntoGroup(alfino.param1,[alfino.param3])
                                x = k1.getGroup(alfino.param1)
                                x.preventedJoinByTicket = False
                                k1.updateGroup(x)
                                invsend = 0
                                Ti = k1.reissueGroupTicket(alfino.param1)
                                fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                Ticket = k1.reissueGroupTicket(alfino.param1)
                        except:
                            try:
                                if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                    bot_run["Blacklist_User"][alfino.param2] = True
                                    with open('finbot1.json','w') as fp:
                                    	json.dump(bot_run, fp, sort_keys=True, indent=4)
                                    k2.acceptGroupInvitation(alfino.param1)
                                    k2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    k2.findAndAddContactsByMid(alfino.param3)
                                    k2.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    x = k2.getGroup(alfino.param1)
                                    x.preventedJoinByTicket = False
                                    k2.updateGroup(x)
                                    invsend = 0
                                    Ti = k2.reissueGroupTicket(alfino.param1)
                                    fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    Ticket = k2.reissueGroupTicket(alfino.param1)
                            except:
                            	pass

        if alfino.type == 19:
            if alfino.param3 in Creator:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        k1.acceptGroupInvitation(alfino.param1)
                        k1.inviteIntoGroup(alfino.param1,[alfino.param3])
                        k1.kickoutFromGroup(alfino.param1,[alfino.param2])
                        x = k1.getGroup(alfino.param1)
                        x.preventedJoinByTicket = False
                        k1.updateGroup(x)
                        invsend = 0
                        Ti = k1.reissueGroupTicket(alfino.param1)
                        fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        Ticket = k1.reissueGroupTicket(alfino.param1)
                    except:
                        try:
                           k2.acceptGroupInvitation(alfino.param1)
                           k2.inviteIntoGroup(alfino.param1,[alfino.param3])
                           k2.kickoutFromGroup(alfino.param1,[alfino.param2])
                           x = k2.getGroup(alfino.param1)
                           x.preventedJoinByTicket = False
                           k2.updateGroup(x)
                           invsend = 0
                           Ti = k2.reissueGroupTicket(alfino.param1)
                           fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                           Ticket = k2.reissueGroupTicket(alfino.param1)
                        except:
                            try:
                                k3.acceptGroupInvitation(alfino.param1)
                                k3.inviteIntoGroup(alfino.param1,[alfino.param3])
                                k3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                x = k3.getGroup(alfino.param1)
                                x.preventedJoinByTicket = False
                                k3.updateGroup(x)
                                invsend = 0
                                Ti = k3.reissueGroupTicket(alfino.param1)
                                kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                G = k3.getGroup(alfino.param1)
                                G.preventedJoinByTicket = True
                                k3.updateGroup(G)
                                k3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                Ticket = k3.reissueGroupTicket(alfino.param1)
                            except:
                                pass

            if alfino.param3 in k1MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        k2.acceptGroupInvitation(alfino.param1)
                        k2.kickoutFromGroup(alfino.param1,[alfino.param2])
                        k2.inviteIntoGroup(alfino.param1,[alfino.param3])
                        x = k2.getGroup(alfino.param1)
                        x.preventedJoinByTicket = False
                        k2.updateGroup(x)
                        invsend = 0
                        Ti = k2.reissueGroupTicket(alfino.param1)
                        fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        Ticket = k2.reissueGroupTicket(alfino.param1)
                    except:
                        pass

            if alfino.param3 in k2MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        k3.acceptGroupInvitation(alfino.param1)
                        k3.kickoutFromGroup(alfino.param1,[alfino.param2])
                        k3.inviteIntoGroup(alfino.param1,[alfino.param3])
                        x = k3.getGroup(alfino.param1)
                        x.preventedJoinByTicket = False
                        k3.updateGroup(x)
                        invsend = 0
                        Ti = k3.reissueGroupTicket(alfino.param1)
                        fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        Ticket = k3.reissueGroupTicket(alfino.param1)
                    except:
                        pass

            if alfino.param3 in k3MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        k1.acceptGroupInvitation(alfino.param1)
                        k1.kickoutFromGroup(alfino.param1,[alfino.param2])
                        k1.inviteIntoGroup(alfino.param1,[alfino.param3])
                        x = k1.getGroup(alfino.param1)
                        x.preventedJoinByTicket = False
                        k1.updateGroup(x)
                        invsend = 0
                        Ti = k1.reissueGroupTicket(alfino.param1)
                        fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                        Ticket = k1.reissueGroupTicket(alfino.param1)
                    except:
                        pass

        if alfino.type == 19:
            if alfino.param3 in myMID:
                if alfino.param2 in Bots:
                    pass
                if alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                        fn1.inviteIntoGroup(alfino.param1,[alfino.param3])
                        kang.acceptGroupInvitation(alfino.param1)
                    except:
                        try:
                            fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                            fn2.inviteIntoGroup(alfino.param1,[alfino.param3])
                            kang.acceptGroupInvitation(alfino.param1)
                        except:
                            try:
                                G = fn3.getGroup(alfino.param1)
                                G.preventedJoinByTicket = False
                                fn3.updateGroup(G)
                                Ticket = fn3.reissueGroupTicket(alfino.param1)
                                kang.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn1.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn2.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn3.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn4.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn5.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                G = fn3.getGroup(alfino.param1)
                                G.preventedJoinByTicket = True
                                fn3.updateGroup(G)
                                fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                Ticket = fn3.reissueGroupTicket(alfino.param1)
                            except:
                                try:
                                    fn4.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    kang.acceptGroupInvitation(alfino.param1)
                                    fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                except:
                                    try:
                                        k2.acceptGroupInvitation(alfino.param1)
                                        k2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        k2.inviteIntoGroup(alfino.param1,alfino.param3)
                                        x = k2.getGroup(alfino.param1)
                                        x.preventedJoinByTicket = False
                                        k2.updateGroup(x)
                                        invsend = 0
                                        Ti = k2.reissueGroupTicket(alfino.param1)
                                        fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                        kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                        fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                        fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                        fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                        fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                        fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                        Ticket = k2.reissueGroupTicket(alfino.param1)
                                    except:
                                        try:
                                            k1.acceptGroupInvitation(alfino.param1)
                                            k1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                            k1.inviteIntoGroup(alfino.param1,alfino.param3)
                                            x = k1.getGroup(alfino.param1)
                                            x.preventedJoinByTicket = False
                                            k1.updateGroup(x)
                                            invsend = 0
                                            Ti = k1.reissueGroupTicket(alfino.param1)
                                            fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                            kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                            fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                            fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                            fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                            fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                            fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                            Ticket = k1.reissueGroupTicket(alfino.param1)
                                        except:
                                            pass
                return
            if alfino.param3 in fn1MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                        fn2.inviteIntoGroup(alfino.param1,[alfino.param3])
                        fn1.acceptGroupInvitation(alfino.param1)
                    except:
                        try:
                            fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                            fn3.inviteIntoGroup(alfino.param1,[alfino.param3])
                            fn1.acceptGroupInvitation(alfino.param1)
                        except:
                            try:
                                G = fn4.getGroup(alfino.param1)
                                G.preventedJoinByTicket = False
                                fn4.updateGroup(G)
                                Ticket = fn4.reissueGroupTicket(alfino.param1)
                                kang.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn1.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn2.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn3.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn4.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn5.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fino.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                G = fn4.getGroup(alfino.param1)
                                G.preventedJoinByTicket = True
                                fn4.updateGroup(G)
                            except:
                                try:
                                    fn5.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    fn1.acceptGroupInvitation(alfino.param1)
                                    fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                                except:
                                    try:
                                        kang.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        kang.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        fn1.acceptGroupInvitation(alfino.param1)
                                    except:
                                        try:
                                            fn2.inviteIntoGroup(alfino.param1,[alfino.param3])
                                            fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                            fn1.acceptGroupInvitation(alfino.param1)
                                        except:
                                            pass
                return
            if alfino.param3 in fn2MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                        fn3.inviteIntoGroup(alfino.param1,[alfino.param3])
                        fn2.acceptGroupInvitation(alfino.param1)
                    except:
                        try:
                            fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                            fn4.inviteIntoGroup(alfino.param1,[alfino.param3])
                            fn2.acceptGroupInvitation(alfino.param1)
                        except:
                            try:
                                G = fn5.getGroup(alfino.param1)
                                G.preventedJoinByTicket = False
                                fn5.updateGroup(G)
                                Ticket = fn5.reissueGroupTicket(alfino.param1)
                                kang.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn1.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn2.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn3.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn4.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fino.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                G = fn5.getGroup(alfino.param1)
                                G.preventedJoinByTicket = True
                                fn5.updateGroup(G)
                            except:
                                try:
                                    kang.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    fn2.acceptGroupInvitation(alfino.param1)
                                    fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                except:
                                    try:
                                        fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        fn1.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        fn2.acceptGroupInvitation(alfino.param1)
                                    except:
                                        pass
                return
            if alfino.param3 in fn3MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                        fn4.inviteIntoGroup(alfino.param1,[alfino.param3])
                        fn3.acceptGroupInvitation(alfino.param1)
                    except:
                        try:
                            fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                            fn5.inviteIntoGroup(alfino.param1,[alfino.param3])
                            fn3.acceptGroupInvitation(alfino.param1)
                        except:
                            try:
                                G = kang.getGroup(alfino.param1)
                                G.preventedJoinByTicket = False
                                kang.updateGroup(G)
                                Ticket = kang.reissueGroupTicket(alfino.param1)
                                fn1.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn2.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn3.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn4.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn5.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fino.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                G = kang.getGroup(alfino.param1)
                                G.preventedJoinByTicket = True
                                kang.updateGroup(G)
                            except:
                                try:
                                    fn1.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    fn3.acceptGroupInvitation(alfino.param1)
                                    fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                except:
                                    try:
                                        fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        fn2.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        fn3.acceptGroupInvitation(alfino.param1)
                                    except:
                                        pass
                return
            if alfino.param3 in fn4MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                        fn5.inviteIntoGroup(alfino.param1,[alfino.param3])
                        fn4.acceptGroupInvitation(alfino.param1)
                    except:
                        try:
                            kang.kickoutFromGroup(alfino.param1,[alfino.param2])
                            kang.inviteIntoGroup(alfino.param1,[alfino.param3])
                            fn4.acceptGroupInvitation(alfino.param1)
                        except:
                            try:
                                G = fn1.getGroup(alfino.param1)
                                G.preventedJoinByTicket = False
                                fn1.updateGroup(G)
                                Ticket = fn1.reissueGroupTicket(alfino.param1)
                                kang.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn2.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn3.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn4.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn5.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fino.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                G = fn1.getGroup(alfino.param1)
                                G.preventedJoinByTicket = True
                                fn1.updateGroup(G)
                            except:
                                try:
                                    fn2.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    fn4.acceptGroupInvitation(alfino.param1)
                                    fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                except:
                                    try:
                                        fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        fn3.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        fn4.acceptGroupInvitation(alfino.param1)
                                    except:
                                        pass
                return
            if alfino.param3 in fn5MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        kang.kickoutFromGroup(alfino.param1,[alfino.param2])
                        kang.inviteIntoGroup(alfino.param1,[alfino.param3])
                        fn5.acceptGroupInvitation(alfino.param1)
                    except:
                        try:
                            fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                            fn1.inviteIntoGroup(alfino.param1,[alfino.param3])
                            fn5.acceptGroupInvitation(alfino.param1)
                        except:
                            try:
                                G = fn2.getGroup(alfino.param1)
                                G.preventedJoinByTicket = False
                                fn2.updateGroup(G)
                                Ticket = fn2.reissueGroupTicket(alfino.param1)
                                kang.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn1.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn3.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn4.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fn5.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                fino.acceptGroupInvitationByTicket(alfino.param1,Ticket)
                                G = fn2.getGroup(alfino.param1)
                                G.preventedJoinByTicket = True
                                fn2.updateGroup(G)
                            except:
                                try:
                                    fn3.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    fn5.acceptGroupInvitation(alfino.param1)
                                    fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                except:
                                    try:
                                        fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        fn4.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        fn5.acceptGroupInvitation(alfino.param1)
                                    except:
                                        pass
                return
            if alfino.param3 in admin:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    bot_run["Blacklist_User"][alfino.param2] = True
                    try:
                        fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                        fn1.findAndAddContactsByMid(alfino.param3)
                        fn1.inviteIntoGroup(alfino.param1,[alfino.param3])
                    except:
                        try:
                            fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                            fn2.findAndAddContactsByMid(alfino.param3)
                            fn2.inviteIntoGroup(alfino.param1,[alfino.param3])
                        except:
                            try:
                                fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                fn3.findAndAddContactsByMid(alfino.param3)
                                fn3.inviteIntoGroup(alfino.param1,[alfino.param3])
                            except:
                                try:
                                    fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    fn4.findAndAddContactsByMid(alfino.param3)
                                    fn4.inviteIntoGroup(alfino.param1,[alfino.param3])
                                except:
                                    try:
                                        fn5.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        fn5.findAndAddContactsByMid(alfino.param3)
                                        fn4.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    except:
                                        try:
                                            kang.kickoutFromGroup(alfino.param1,[alfino.param2])
                                            kang.findAndAddContactsByMid(alfino.param3)
                                            kang.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        except:
                                            pass
                return

        if alfino.type == 32:
            if alfino.param1 in bot_run["Pro_Cancel"]:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    try:
                        if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                            bot_run["Blacklist_User"][alfino.param2] = True
                            with open('finbot1.json','w') as fp:
                                json.dump(bot_run, fp, sort_keys=True, indent=4)
                            user = kang.getContact(alfino.param2)
                            _Chat(alfino.param1,"No permission!! You're not an admin\nPlease Do not cancel for a group member invited\nYou have been warned: " + str(user.displayName))
                            try:
                                if alfino.param3 not in bot_run["Blacklist_User"]:
                                    fn1.findAndAddContactsByMid(alfino.param3)
                                    fn1.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                            except:
                                try:
                                    if alfino.param3 not in bot_run["Blacklist_User"]:
                                        fn2.findAndAddContactsByMid(alfino.param3)
                                        fn2.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                except:
                                    pass
                        else:
                            pass
                    except:
                        pass

            if alfino.param3 in k1MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    try:
                        if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                            bot_run["Blacklist_User"][alfino.param2] = True
                            try:
                                fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                fn1.inviteIntoGroup(alfino.param1,[alfino.param3])
                            except:
                                try:
                                    fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    fn2.inviteIntoGroup(alfino.param1,[alfino.param3])
                                except:
                                    try:
                                        fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        fn3.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    except:
                                        try:
                                            fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                            fn4.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        except:
                                            pass
                        else:
                            pass
                    except:
                        try:
                            if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                bot_run["Blacklist_User"][alfino.param2] = True
                                k2.acceptGroupInvitation(alfino.param1)
                                k2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                k2.findAndAddContactsByMid(alfino.param3)
                                k2.inviteIntoGroup(alfino.param1,[alfino.param3])
                                x = k2.getGroup(alfino.param1)
                                x.preventedJoinByTicket = False
                                k2.updateGroup(x)
                                invsend = 0
                                Ti = k2.reissueGroupTicket(alfino.param1)
                                fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                Ticket = k2.reissueGroupTicket(alfino.param1)
                        except:
                            try:
                                if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                    bot_run["Blacklist_User"][alfino.param2] = True
                                    k3.acceptGroupInvitation(alfino.param1)
                                    k3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    k3.findAndAddContactsByMid(alfino.param3)
                                    k3.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    x = k3.getGroup(alfino.param1)
                                    x.preventedJoinByTicket = False
                                    k3.updateGroup(x)
                                    invsend = 0
                                    Ti = k3.reissueGroupTicket(alfino.param1)
                                    fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    Ticket = k3.reissueGroupTicket(alfino.param1)
                            except:
                                pass

            if alfino.param3 in k2MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    try:
                        if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                            bot_run["Blacklist_User"][alfino.param2] = True
                            try:
                                fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                fn1.inviteIntoGroup(alfino.param1,[alfino.param3])
                            except:
                                try:
                                    fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    fn2.inviteIntoGroup(alfino.param1,[alfino.param3])
                                except:
                                    try:
                                        fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        fn3.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    except:
                                        try:
                                            fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                            fn4.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        except:
                                            pass
                        else:
                            pass
                    except:
                        try:
                            if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                bot_run["Blacklist_User"][alfino.param2] = True
                                k3.acceptGroupInvitation(alfino.param1)
                                k3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                k3.findAndAddContactsByMid(alfino.param3)
                                k3.inviteIntoGroup(alfino.param1,[alfino.param3])
                                x = k3.getGroup(alfino.param1)
                                x.preventedJoinByTicket = False
                                k3.updateGroup(x)
                                invsend = 0
                                Ti = k3.reissueGroupTicket(alfino.param1)
                                fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                Ticket = k3.reissueGroupTicket(alfino.param1)
                        except:
                            try:
                                if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                    bot_run["Blacklist_User"][alfino.param2] = True
                                    k1.acceptGroupInvitation(alfino.param1)
                                    k1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    k1.findAndAddContactsByMid(alfino.param3)
                                    k1.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    x = k1.getGroup(alfino.param1)
                                    x.preventedJoinByTicket = False
                                    k1.updateGroup(x)
                                    invsend = 0
                                    Ti = k1.reissueGroupTicket(alfino.param1)
                                    fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    Ticket = k1.reissueGroupTicket(alfino.param1)
                            except:
                                pass

            if alfino.param3 in k3MID:
                if alfino.param2 in Bots:
                    pass
                elif alfino.param2 in Master:
                    pass
                elif alfino.param2 in admin:
                    pass
                else:
                    try:
                        if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                            bot_run["Blacklist_User"][alfino.param2] = True
                            try:
                                fn1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                fn1.inviteIntoGroup(alfino.param1,[alfino.param3])
                            except:
                                try:
                                    fn2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    fn2.inviteIntoGroup(alfino.param1,[alfino.param3])
                                except:
                                    try:
                                        fn3.kickoutFromGroup(alfino.param1,[alfino.param2])
                                        fn3.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    except:
                                        try:
                                            fn4.kickoutFromGroup(alfino.param1,[alfino.param2])
                                            fn4.inviteIntoGroup(alfino.param1,[alfino.param3])
                                        except:
                                            pass
                        else:
                            pass
                    except:
                        try:
                            if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                bot_run["Blacklist_User"][alfino.param2] = True
                                k2.acceptGroupInvitation(alfino.param1)
                                k2.kickoutFromGroup(alfino.param1,[alfino.param2])
                                k2.findAndAddContactsByMid(alfino.param3)
                                k2.inviteIntoGroup(alfino.param1,[alfino.param3])
                                x = k2.getGroup(alfino.param1)
                                x.preventedJoinByTicket = False
                                k2.updateGroup(x)
                                invsend = 0
                                Ti = k2.reissueGroupTicket(alfino.param1)
                                fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                Ticket = k2.reissueGroupTicket(alfino.param1)
                        except:
                            try:
                                if alfino.param2 not in Bots and alfino.param2 not in Master and alfino.param2 not in admin:
                                    bot_run["Blacklist_User"][alfino.param2] = True
                                    k1.acceptGroupInvitation(alfino.param1)
                                    k1.kickoutFromGroup(alfino.param1,[alfino.param2])
                                    k1.findAndAddContactsByMid(alfino.param3)
                                    k1.inviteIntoGroup(alfino.param1,[alfino.param3])
                                    x = k1.getGroup(alfino.param1)
                                    x.preventedJoinByTicket = False
                                    k1.updateGroup(x)
                                    invsend = 0
                                    Ti = k1.reissueGroupTicket(alfino.param1)
                                    fino.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    kang.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn1.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn2.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn3.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn4.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    fn5.acceptGroupInvitationByTicket(alfino.param1,Ti)
                                    Ticket = k1.reissueGroupTicket(alfino.param1)
                            except:
                                pass

        if alfino.type == 55:
            try:
                if alfino.param1 in bot_run["readPoint"]:
                   if alfino.param2 in bot_run["readMember"][alfino.param1]:
                       pass
                   else:
                       bot_run["readMember"][alfino.param1][alfino.param2] = True
                else:
                   pass
            except:
                pass
            if bot_run['setWicked'][alfino.param1]==True:
                if alfino.param1 in bot_run['setTime']:
                    Name = kang.getContact(alfino.param2).displayName
                    Ppname = kang.getContact(alfino.param2).pictureStatus
                    if Name in bot_run['setSider'][alfino.param1]:
                        pass
                    else:
                        bot_run['setSider'][alfino.param1] += "\n~ " + Name
                        siderMembers(alfino.param1, [alfino.param2])
                        kang.sendImageWithURL(alfino.param1, "http://dl.profile.line-cdn.net/" + Ppname)

            if alfino.param2 in bot_run["Blacklist_User"]:
                random.choice(KAC).kickoutFromGroup(alfino.param1,[alfino.param2])
            else:
                pass

        if alfino.type == 26:
            msg = alfino.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != kang.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if bot_run["scanner"] == True:
                    kang.sendChatChecked(to, msg_id)
                if to in bot_run["scanPoint"]:
                    if sender not in bot_run["scanROM"][msg.to]:
                        bot_run["scanROM"][msg.to][sender] = True
                if bot_run["unsendMessage"] == True:
                    try:
                        msg = alfino.message
                        if msg.toType == 0:
                            kang.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                        else:
                            kang.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                            msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    except Exception as error:
                        print (error)
                if msg.contentType == 0:
                    msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                if msg.contentType == 1:
                    path = kang.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Check up your pict',"data":path,"from":msg._from,"createdTime":msg.createdTime}
                if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                       data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                       path = kang.downloadFileURL(data)
                       msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}

        if alfino.type == 65:
            if bot_run["unsendMessage"] == True:
                try:
                    at = alfino.param1
                    msg_id = alfino.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Check up your pict':
                                ginfo = kang.getGroup(at)
                                pelaku = kang.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Destroy Picture Detected 」\n• Sender : "
                                ret_ = "• Group Name : {}".format(str(ginfo.name))
                                ret_ += "\n• Send time : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(pelaku.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':pelaku.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                _Chat(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                kang.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = kang.getGroup(at)
                                pelaku = kang.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Destroy Message Detected 」\n"
                                ret_ += "• Sender : {}".format(str(pelaku.displayName))
                                ret_ += "\n• Group Name : {}".format(str(ginfo.name))
                                ret_ += "\n• Send time : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Message : {}".format(str(msg_dict[msg_id]["text"]))
                                _Chat(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

            if bot_run["unsendMessage"] == True:
                try:
                    at = alfino.param1
                    msg_id = alfino.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = kang.getGroup(at)
                                pelaku = kang.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Destroy sticker Detected 」\n"
                                ret_ += "• Sender : {}".format(str(pelaku.displayName))
                                ret_ += "\n• Group Name : {}".format(str(ginfo.name))
                                ret_ += "\n• Send time : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                _Chat(at, str(ret_))
                                kang.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if alfino.type == 26:
           if run["finbot"] == True:
               msg = alfino.message
               if msg._from not in Bots:
                 if bot_run["talkban"] == True:
                   if msg._from in bot_run["Talkblacklist"]:
                      try:
                          kang.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          pass

        if alfino.type == 26:
           if run["finbot"] == True:
               if bot_run["ResponPc"] == True:
                 if msg.toType == 0:
                     kang.sendChatChecked(msg._from,msg.id)
                     contact = kang.getContact(msg._from)
                     _Chatt(msg._from, "╔═══════════════╗\n「Auto Reply」\n  ??🄸🄽 🄱🄾🅃\nHaii... {}".format(contact.displayName) + "\n Mohon maaf....!\nIni adalah pesan otomatis, \nJika ada yang penting hubungi saya nanti\n Terima Kasih\n\n╚═══════════════╝")
               if "MENTION" in msg.contentMetadata.keys() != None:
                 if bot_run['detectMention'] == True:
                     contact = kang.getContact(msg._from)
                     cName = contact.pictureStatus
                     balas = ["http://dl.profile.line-cdn.net/" + cName]
                     ret_ = random.choice(balas)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention["MENTIONEES"]
                     for mention in mentionees:
                           if mention["M"] in mid:
                                  sendMessageWithMention(msg._from,bot_run["Respontag"])
                                  break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if bot_run["MentionKick"] == True:
                     contact = kang.getContact(msg._from)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in mid:
                                  _Chat(to,"don't tag me")
                                  _Random.kickoutFromGroup(msg.to,[msg._from])
                                  break

        if alfino.type == 25 or alfino.type == 26:
            msg = alfino.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 1:
                 if sender in Creator:
                    if bot_run["Addimage"]["status"] == True:
                        path = kang.downloadObjectMsg(msg.id)
                        images[bot_run["Addimage"]["name"]] = str(path)
                        f = codecs.open("image.json","w","utf-8")
                        json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                        _Chat(to, "Berhasil menambahkan photo {}".format(str(bot_run["Addimage"]["name"])))
                        bot_run["Addimage"]["status"] = False                
                        bot_run["Addimage"]["name"] = ""

               if msg.contentType == 2:
                 if sender in Creator:
                    if bot_run["Addvideo"]["status"] == True:
                        path = kang.downloadObjectMsg(msg.id)
                        videos[bot_run["Addvideo"]["name"]] = str(path)
                        f = codecs.open("video.json","w","utf-8")
                        json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                        _Chat(to, "Berhasil menambahkan video {}".format(str(bot_run["Addvideo"]["name"])))
                        bot_run["Addvideo"]["status"] = False                
                        bot_run["Addvideo"]["name"] = ""

               if msg.contentType == 3:
                 if sender in Creator:
                    if bot_run["Addaudio"]["status"] == True:
                        path = kang.downloadObjectMsg(msg.id)
                        audios[bot_run["Addaudio"]["name"]] = str(path)
                        f = codecs.open("audio.json","w","utf-8")
                        json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                        _Chat(to, "Berhasil menambahkan mp3 {}".format(str(bot_run["Addaudio"]["name"])))
                        bot_run["Addaudio"]["status"] = False                
                        bot_run["Addaudio"]["name"] = ""

               if msg.contentType == 7:
                 if sender in Creator:
                    if bot_run["Addsticker"]["status"] == True:
                        stickers[bot_run["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                        f = codecs.open("sticker.json","w","utf-8")
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        _Chat(to, "Berhasil menambahkan sticker {}".format(str(bot_run["Addsticker"]["name"])))
                        bot_run["Addsticker"]["status"] = False                
                        bot_run["Addsticker"]["name"] = ""

               if msg.contentType == 1:
                 if sender in Creator:
                    if bot_run["changePicture"] == True:
                       path = kang.downloadObjectMsg(msg_id)
                       path1 = fn1.downloadObjectMsg(msg_id)
                       path2 = fn2.downloadObjectMsg(msg_id)
                       path3 = fn3.downloadObjectMsg(msg_id)
                       path4 = fn4.downloadObjectMsg(msg_id)
                       path5 = fn5.downloadObjectMsg(msg_id)
                       bot_run["changePicture"] = False
                       kang.updateProfilePicture(path)
                       getMention(to,"Picture profile updated @!",[sender])
                       fn1.updateProfilePicture(path1)
                       getMention1(to,"Picture profile updated @!",[sender])
                       fn2.updateProfilePicture(path2)
                       getMention2(to,"Picture profile updated @!",[sender])
                       fn3.updateProfilePicture(path3)
                       getMention3(to,"Picture profile updated @!",[sender])
                       fn4.updateProfilePicture(path4)
                       getMention4(to,"Picture profile updated @!",[sender])
                       fn5.updateProfilePicture(path5)
                       getMention5(to,"Picture profile updated @!",[sender])

                 if sender in Creator:
                    if bot_run["kickerPicture"] == True:
                       path1 = k1.downloadObjectMsg(msg_id)
                       path2 = k2.downloadObjectMsg(msg_id)
                       path3 = k3.downloadObjectMsg(msg_id)
                       bot_run["kickerPicture"] = False
                       k1.updateProfilePicture(path1)
                       k1.sendMessage(msg.to, bot_run["Responcft"])
                       k2.updateProfilePicture(path2)
                       k2.sendMessage(msg.to, bot_run["Responcft"])
                       k3.updateProfilePicture(path3)
                       k3.sendMessage(to, bot_run["Responcft"])

                 if sender in Creator:
                    if bot_run["changePictureCover"] == True:
                       path1 = kang.downloadObjectMsg(msg_id)
                       bot_run["changePictureCover"] = False
                       kang.updateProfileCover(path1)
                       _Chat(to, bot_run["Responcft"])

                 if sender in Creator:
                     if myMID in bot_run["foto"]:
                         path = kang.downloadObjectMsg(msg.id)
                         del bot_run["foto"][myMID]
                         kang.updateProfilePicture(path)
                         getMention(to,"Picture profile updated @!",[sender])

                 if sender in Creator:
                     if fn1MID in bot_run["foto"]:
                         path = fn1.downloadObjectMsg(msg.id)
                         del bot_run["foto"][fn1MID]
                         fn1.updateProfilePicture(path)
                         getMention1(to,"Picture profile updated @!",[sender])

                 if sender in Creator:
                     if fn2MID in bot_run["foto"]:
                         path = fn2.downloadObjectMsg(msg.id)
                         del bot_run["foto"][fn2MID]
                         fn2.updateProfilePicture(path)
                         getMention2(to,"Picture profile updated @!",[sender])

                 if sender in Creator:
                     if fn3MID in bot_run["foto"]:
                         path = fn3.downloadObjectMsg(msg.id)
                         del bot_run["foto"][fn3MID]
                         fn3.updateProfilePicture(path)
                         getMention3(to,"Picture profile updated @!",[sender])

                 if sender in Creator:
                     if fn4MID in bot_run["foto"]:
                         path = fn4.downloadObjectMsg(msg.id)
                         del bot_run["foto"][fn4MID]
                         fn4.updateProfilePicture(path)
                         getMention4(to,"Picture profile updated @!",[sender])

                 if sender in Creator:
                     if fn5MID in bot_run["foto"]:
                         path = fn5.downloadObjectMsg(msg.id)
                         del bot_run["foto"][fn5MID]
                         fn5.updateProfilePicture(path)
                         getMention5(to,"Picture profile updated @!",[sender])

                 if sender in Creator:
                     if k1MID in bot_run["foto"]:
                         path = k1.downloadObjectMsg(msg.id)
                         del bot_run["foto"][k1MID]
                         k1.updateProfilePicture(path)
                         k1.sendMessage(to,bot_run["Responcft"])

                 if sender in Creator:
                     if k2MID in bot_run["foto"]:
                         path = k2.downloadObjectMsg(msg.id)
                         del bot_run["foto"][k2MID]
                         k2.updateProfilePicture(path)
                         k2.sendMessage(to,bot_run["Responcft"])

                 if sender in Creator:
                     if k3MID in bot_run["foto"]:
                         path = k3.downloadObjectMsg(msg.id)
                         del bot_run["foto"][k3MID]
                         k3.updateProfilePicture(path)
                         k3.sendMessage(to,bot_run["Responcft"])

               if msg.contentType == 2:
                   if sender in Creator:
                       if myMID in bot_run["video"]:
                            path = kang.downloadObjectMsg(msg_id)
                            del bot_run["video"][myMID]
                            kang.updateProfileVideoPicture(path)
                            getMention(to,"Photo Profile switch to video @!",[sender])

               if msg.toType == 2:
                 if sender in Creator:
                   if bot_run["groupPicture"] == True:
                     path = kang.downloadObjectMsg(msg_id)
                     bot_run["groupPicture"] = False
                     kang.updateGroupPicture(msg.to, path)
                     getMention(to,"Group picture profile updated \n@!"[sender])

               if msg.contentType == 13:
                  if bot_run["invite"] == True:
                    if sender in Master or sender in admin:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = kang.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                _Chat(to,"-> " + _name + "\nThis user has been joined ")
                                break
                            elif invite in bot_run["Blacklist_User"]:
                                _Chat(to,"Failure invitation, " + _name + "Blacklist user")
                                _Chat(to,"Please contact an owner/admin!, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    kang.findAndAddContactsByMid(target)
                                    kang.inviteIntoGroup(msg.to,[target])
                                    _Chat(to,"Target invited : \n ➡" + _name)
                                    bot_run["invite"] = False
                                    break
                                except:
                                    try:
                                        kang.findAndAddContactsByMid(invite)
                                        kang.inviteIntoGroup(alfino.param1,[invite])
                                        bot_run["invite"] = False
                                    except:
                                        _Chat(to,"Error invitation\n or Limited invitation")
                                        bot_run["invite"] = False
                                        break

                  if bot_run["invite1"] == True:
                    if sender in Master or sender in admin:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = fn1.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                _Chat1(to,"-> " + _name + "\nThis user has been joined ")
                                break
                            elif invite in bot_run["Blacklist_User"]:
                                _Chat1(to,"Failure invitation, " + _name + "Blacklist user")
                                _Chat1(to,"Please contact an owner/admin!, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    fn1.findAndAddContactsByMid(target)
                                    fn1.inviteIntoGroup(msg.to,[target])
                                    _Chat1(to,"Target invited : \n ➡" + _name)
                                    bot_run["invite1"] = False
                                    break
                                except:
                                    try:
                                        fn1.findAndAddContactsByMid(invite)
                                        fn1.inviteIntoGroup(alfino.param1,[invite])
                                        bot_run["invite1"] = False
                                    except:
                                        _Chat1(to,"Error invitation\n or Limited invitation")
                                        bot_run["invite1"] = False
                                        break

                  if bot_run["invite2"] == True:
                    if sender in Master or sender in admin:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = fn2.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                _Chat2(to,"-> " + _name + "\nThis user has been joined ")
                                break
                            elif invite in bot_run["Blacklist_User"]:
                                _Chat2(to,"Failure invitation, " + _name + "Blacklist user")
                                _Chat2(to,"Please contact an owner/admin!, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    fn2.findAndAddContactsByMid(target)
                                    fn2.inviteIntoGroup(msg.to,[target])
                                    _Chat2(to,"Target invited : \n ➡" + _name)
                                    bot_run["invite1"] = False
                                    break
                                except:
                                    try:
                                        fn2.findAndAddContactsByMid(invite)
                                        fn2.inviteIntoGroup(alfino.param1,[invite])
                                        bot_run["invite2"] = False
                                    except:
                                        _Chat2(to,"Error invitation\n or Limited invitation")
                                        bot_run["invite2"] = False
                                        break

                  if bot_run["invite3"] == True:
                    if sender in Master or sender in admin:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = fn3.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                _Chat3(to,"-> " + _name + "\nThis user has been joined ")
                                break
                            elif invite in bot_run["Blacklist_User"]:
                                _Chat3(to,"Failure invitation, " + _name + "Blacklist user")
                                _Chat3(to,"Please contact an owner/admin!, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    fn3.findAndAddContactsByMid(target)
                                    fn3.inviteIntoGroup(msg.to,[target])
                                    _Chat3(to,"Target invited : \n ➡" + _name)
                                    bot_run["invite3"] = False
                                    break
                                except:
                                    try:
                                        fn3.findAndAddContactsByMid(invite)
                                        fn3.inviteIntoGroup(alfino.param1,[invite])
                                        bot_run["invite3"] = False
                                    except:
                                        _Chat3(to,"Error invitation\n or Limited invitation")
                                        bot_run["invite3"] = False
                                        break

                  if bot_run["invite4"] == True:
                    if sender in Master or sender in admin:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = fn4.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                _Chat4(to,"-> " + _name + "\nThis user has been joined ")
                                break
                            elif invite in bot_run["Blacklist_User"]:
                                _Chat4(to,"Failure invitation, " + _name + "Blacklist user")
                                _Chat4(to,"Please contact an owner/admin!, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    fn4.findAndAddContactsByMid(target)
                                    fn4.inviteIntoGroup(msg.to,[target])
                                    _Chat4(to,"Target invited : \n ➡" + _name)
                                    bot_run["invite4"] = False
                                    break
                                except:
                                    try:
                                        fn4.findAndAddContactsByMid(invite)
                                        fn4.inviteIntoGroup(alfino.param1,[invite])
                                        bot_run["invite4"] = False
                                    except:
                                        _Chat4(to,"Error invitation\n or Limited invitation")
                                        bot_run["invite4"] = False
                                        break

                  if bot_run["invite5"] == True:
                    if sender in Master or sender in admin:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = fn5.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                _Chat5(to,"-> " + _name + "\nThis user has been joined ")
                                break
                            elif invite in bot_run["Blacklist_User"]:
                                _Chat5(to,"Failure invitation, " + _name + "Blacklist user")
                                _Chat5(to,"Please contact an owner/admin!, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    fn5.findAndAddContactsByMid(target)
                                    fn5.inviteIntoGroup(msg.to,[target])
                                    _Chat5(to,"Target invited : \n ➡" + _name)
                                    bot_run["invite5"] = False
                                    break
                                except:
                                    try:
                                        fn5.findAndAddContactsByMid(invite)
                                        fn5.inviteIntoGroup(alfino.param1,[invite])
                                        bot_run["invite5"] = False
                                    except:
                                        _Chat5(to,"Error invitation\n or Limited invitation")
                                        bot_run["invite5"] = False
                                        break

               if msg.contentType == 13:
                 if bot_run["contact"] == True:
                    msg.contentType = 0
                    _Chat(to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = kang.getContact(msg.contentMetadata["mid"])
                        path = kang.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        _Chat(to,"♐ Nama : " + msg.contentMetadata["displayName"] + "\n♐ MID : " + msg.contentMetadata["mid"] + "\n♐ Status Msg : " + contact.statusMessage + "\n♐ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        kang.sendImageWithURL(msg.to, image)
#Add Contact
                 if bot_run["addContact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        target = msg.contentMetadata["mid"]
                        kang.findAndAddContactsByMid(target)
                        _Chat(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn1.findAndAddContactsByMid(target)
                        _Chat1(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn2.findAndAddContactsByMid(target)
                        _Chat2(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn3.findAndAddContactsByMid(target)
                        _Chat3(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn4.findAndAddContactsByMid(target)
                        _Chat4(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn5.findAndAddContactsByMid(target)
                        _Chat5(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        bot_run["addContact"] = False

                 if run["addMe"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        target = msg.contentMetadata["mid"]
                        kang.findAndAddContactsByMid(target)
                        _Chat(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn1.findAndAddContactsByMid(target)
                        _Chat1(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn2.findAndAddContactsByMid(target)
                        _Chat2(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn3.findAndAddContactsByMid(target)
                        _Chat3(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn4.findAndAddContactsByMid(target)
                        _Chat4(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn5.findAndAddContactsByMid(target)
                        _Chat5(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        run["addMe"] = False

                 if bot_run["botAdd"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        target = msg.contentMetadata["mid"]
                        fn1.findAndAddContactsByMid(target)
                        _Chat1(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn2.findAndAddContactsByMid(target)
                        _Chat2(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn3.findAndAddContactsByMid(target)
                        _Chat3(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn4.findAndAddContactsByMid(target)
                        _Chat4(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn5.findAndAddContactsByMid(target)
                        _Chat5(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        bot_run["botAdd"] = False

                 if bot_run["bot1Add"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        target = msg.contentMetadata["mid"]
                        kang.findAndAddContactsByMid(target)
                        _Chat(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn2.findAndAddContactsByMid(target)
                        _Chat2(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn3.findAndAddContactsByMid(target)
                        _Chat3(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn4.findAndAddContactsByMid(target)
                        _Chat4(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn5.findAndAddContactsByMid(target)
                        _Chat5(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        bot_run["bot1Add"] = False

                 if bot_run["bot2Add"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        target = msg.contentMetadata["mid"]
                        kang.findAndAddContactsByMid(target)
                        _Chat(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn1.findAndAddContactsByMid(target)
                        _Chat1(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn3.findAndAddContactsByMid(target)
                        _Chat3(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn4.findAndAddContactsByMid(target)
                        _Chat4(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn5.findAndAddContactsByMid(target)
                        _Chat5(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        bot_run["bot2Add"] = False

                 if bot_run["bot3Add"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        target = msg.contentMetadata["mid"]
                        kang.findAndAddContactsByMid(target)
                        _Chat(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn1.findAndAddContactsByMid(target)
                        _Chat1(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn2.findAndAddContactsByMid(target)
                        _Chat2(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn4.findAndAddContactsByMid(target)
                        _Chat4(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn5.findAndAddContactsByMid(target)
                        _Chat5(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        bot_run["bot3Add"] = False

                 if bot_run["bot4Add"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        target = msg.contentMetadata["mid"]
                        kang.findAndAddContactsByMid(target)
                        _Chat(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn1.findAndAddContactsByMid(target)
                        _Chat1(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn2.findAndAddContactsByMid(target)
                        _Chat2(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn3.findAndAddContactsByMid(target)
                        _Chat3(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn5.findAndAddContactsByMid(target)
                        _Chat5(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        bot_run["bot4Add"] = False

                 if bot_run["bot5Add"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        target = msg.contentMetadata["mid"]
                        kang.findAndAddContactsByMid(target)
                        _Chat(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn1.findAndAddContactsByMid(target)
                        _Chat1(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn2.findAndAddContactsByMid(target)
                        _Chat2(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn3.findAndAddContactsByMid(target)
                        _Chat3(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        fn4.findAndAddContactsByMid(target)
                        _Chat4(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        bot_run["bot5Add"] = False

                 if bot_run["kickerAdd"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        target = msg.contentMetadata["mid"]
                        k1.findAndAddContactsByMid(target)
                        k1.sendMessage(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        k2.findAndAddContactsByMid(target)
                        k2.sendMessage(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        k3.findAndAddContactsByMid(target)
                        k3.sendMessage(to,"Nama : " + msg.contentMetadata["displayName"] + "\nSucces add as friend")
                        bot_run["kickerAdd"] = False

                 if sender in Master or sender in admin:
                  if bot_run["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in bot_run["Blacklist_User"]:
                        getMention(to,"This user is already blacklist @!",[sender])
                        bot_run["wblacklist"] = False
                    else:
                        bot_run["wblacklist"] = True
                        bot_run["Blacklist_User"][msg.contentMetadata["mid"]] = True
                        _Chat(to,"Add to Blacklist user")
                        bot_run["wblacklist"] = False

                 if sender in Master or sender in admin:
                  if bot_run["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in bot_run["Blacklist_User"]:
                        del bot_run["Blacklist_User"][msg.contentMetadata["mid"]]
                        getMention(to,"Blacklist deleted @!",[sender])
                        bot_run["dblacklist"] = False
                    else:
                        _Chat(to,"No blacklist")
                        bot_run["dblacklist"] = False

                 if sender in Master or sender in admin:
                  if bot_run["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in bot_run["Talkblacklist"]:
                        getMention(to,"This user is already Talkblacklist @!",[sender])
                        bot_run["Talkwblacklist"] = False
                    else:
                        bot_run["Talkwblacklist"] = True
                        bot_run["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        getMention(to,"Talklist added @!",[sender])
                        bot_run["Talkwblacklist"] = False

                 if sender in Master or sender in admin:
                  if bot_run["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in bot_run["Talkblacklist"]:
                        del bot_run["Talkblacklist"][msg.contentMetadata["mid"]]
                        _Chat(to,bot_run["ResponDTBL"])
                        bot_run["Talkdblacklist"] = False
                    else:
                        _Chat(to,"No Talkblacklist")
                        bot_run["Talkdblacklist"] = False

                 if sender in Creator:
                  if bot_run["addAdmin"] == True:
                    if msg.contentMetadata["mid"] in run_bot["Admin"]:
                        getMention(to,"This user is an admin @!",[sender])
                        bot_run["addAdmin"] = False
                    else:
                        bot_run["addAdmin"] = True
                        run_bot["Admin"][msg.contentMetadata["mid"]] = True
                        getMention(to,"User has been added as an admin @!",[sender])
                        bot_run["addAdmin"] = False

                 if sender in Creator:
                  if bot_run["delAdmin"] == True:
                    if msg.contentMetadata["mid"] in run_bot["Admin"]:
                        del run_bot["Admin"][msg.contentMetadata["mid"]]
                        getMention(to,"This user is not an admin @!",[sender])
                        bot_run["delAdmin"] = False
                    else:
                        bot_run["delAdmin"] = True
                        getMention(to,"Admin has been removed @!",[sender])
                        bot_run["delAdmin"] = False

               if msg.contentType == 16:
                 if bot_run["checkPost"] == True:
                     try:
                         ret_ = "╔════[ Post Detail ]"
                         if msg.contentMetadata["serviceType"] == "GB":
                             contact = kang.getContact(sender)
                             auth = "\n╠❐ Author : {}".format(str(contact.displayName))
                         else:
                             auth = "\n╠❐ Author : {}".format(str(msg.contentMetadata["serviceName"]))
                         purl = "\n╠❐ Url : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                         ret_ += auth
                         ret_ += purl
                         if "mediaOid" in msg.contentMetadata:
                             object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                             if msg.contentMetadata["mediaType"] == "V":
                                 if msg.contentMetadata["serviceType"] == "GB":
                                     ourl = "\n╠❐ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                     murl = "\n╠❐ Url Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                 else:
                                     ourl = "\n╠❐ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                     murl = "\n╠❐ Url Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                 ret_ += murl
                             else:
                                 if msg.contentMetadata["serviceType"] == "GB":
                                     ourl = "\n╠❐ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                 else:
                                     ourl = "\n╠❐ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                             ret_ += ourl
                         if "stickerId" in msg.contentMetadata:
                             stck = "\n╠❐ Sticker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                             ret_ += stck
                         if "text" in msg.contentMetadata:
                             text = "\n╠❐ Note : {}".format(str(msg.contentMetadata["text"]))
                             ret_ += text
                         ret_ += "\n╚══[ 🄵🄸🄽 🄱🄾🅃 ]"
                         _Chat(to, str(ret_))
                     except:
                         getMention(to,"Invalid Post @!",[sender])

               if msg.contentType == 7:
                if bot_run["stickerOn"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        r = s.get("https://store.line.me/stickershop/product/{}/id".format(urllib.parse.quote(pkg_id)))
                        soup = BeautifulSoup(r.content, 'html5lib')
                        data = soup.select("[class~=mdBtn01Txt]")[0].text
                        if data == 'Check more product':
                            ret_ = "「 Sticker Info 」"
                            ret_ += "\n• STICKER ID : {}".format(stk_id)
                            ret_ += "\n• STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\n• STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\n• STICKER URL : line://shop/detail/{}".format(pkg_id)
                            _Chat(to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = kang.downloadFileURL(data)
                               kang.sendImage(msg.to,path)
                        else:
                            ret_ = "「 Sticker Info 」"
                            ret_ += "\n• PRICE : "+soup.findAll('p', attrs={'class':'mdCMN08Price'})[0].text
                            ret_ += "\n• AUTHOR : "+soup.select("a[href*=/stickershop/author]")[0].text
                            ret_ += "\n• STICKER ID : {}".format(str(stk_id))
                            ret_ += "\n• STICKER PACKAGES ID : {}".format(str(pkg_id))
                            ret_ += "\n• STICKER VERSION : {}".format(str(stk_ver))
                            ret_ += "\n• STICKER URL : line://shop/detail/{}".format(str(pkg_id))
                            ret_ += "\n• DESCRIPTION :\n"+soup.findAll('p', attrs={'class':'mdCMN08Desc'})[0].text
                            _Chat(to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = kang.downloadFileURL(data)
                               kang.sendImage(msg.to,path)

               if msg.contentType == 0:
                    if bot_run["AutoRead"] == True:
                        kang.sendChatChecked(msg.to, msg_id)
                        atend()
                    if text is None:
                        return
                    else:
                    	for sticker in stickers:
                         if sender in Creator:
                           if text.lower() == sticker:
                              sid = stickers[text.lower()]["STKID"]
                              spkg = stickers[text.lower()]["STKPKGID"]
                              kang.sendSticker(to, spkg, sid)
                         for image in images:
                          if sender in Creator:
                           if text.lower() == image:
                              kang.sendImage(msg.to, images[image])
                         for audio in audios:
                          if sender in Creator:
                           if text.lower() == audio:
                              kang.sendAudio(msg.to, audios[audio])
                         for video in videos:
                          if sender in Creator:
                           if text.lower() == video:
                              kang.sendVideo(msg.to, videos[video])
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "finbot on":
                            if sender in Creator or sender in admin:
                                run["finbot"] = True
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                _Chat(to, "Bot@Relogin \nDay : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n Time : [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "finbot off":
                            if sender in Creator or sender in admin:
                                run["finbot"] = False
                                _Chat(to, "system Logout")

                        elif cmd == "#":
                          if run["finbot"] == True:
                            if sender in Creator:
                                kang.inviteIntoGroup(msg.to,[k1MID])

                        elif cmd == "##":
                          if run["finbot"] == True:
                            if sender in Creator:
                                kang.inviteIntoGroup(msg.to,[k2MID])

                        elif cmd == "###":
                          if run["finbot"] == True:
                            if sender in Creator:
                                kang.inviteIntoGroup(msg.to,[k3MID])

                        elif cmd == "####":
                          if run["finbot"] == True:
                            if sender in Creator:
                                kang.inviteIntoGroup(msg.to,[k1MID,k2MID,k3MID])

                        elif cmd == ".. " or cmd == "cit":
                          if run["finbot"] == True:
                            if sender in Creator:
                                kang.inviteIntoGroup(msg.to,[fn1MID,fn2MID,fn3MID,fn4MID,fn5MID,k1MID,k2MID,k3MID])
                                fn1.acceptGroupInvitation(msg.to)
                                fn2.acceptGroupInvitation(msg.to)
                                fn3.acceptGroupInvitation(msg.to)
                                fn4.acceptGroupInvitation(msg.to)
                                fn5.acceptGroupInvitation(msg.to)

                        elif cmd == "crot" or cmd == "xxx":
                          if run["finbot"] == True:
                            if sender in Creator:
                                kang.inviteIntoGroup(msg.to,[fn1MID,fn2MID,fn3MID,fn4MID,fn5MID,k1MID,k2MID,k3MID])
                                fn1.acceptGroupInvitation(msg.to)
                                fn2.acceptGroupInvitation(msg.to)
                                fn3.acceptGroupInvitation(msg.to)
                                fn4.acceptGroupInvitation(msg.to)
                                fn5.acceptGroupInvitation(msg.to)

                        elif cmd == "all in" or cmd == "rein":
                          if run["finbot"] == True:
                            if sender in Creator:
                                G = kang.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kang.updateGroup(G)
                                invsend = 0
                                Ticket = kang.reissueGroupTicket(msg.to)
                                fn1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fn2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fn3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fn4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fn5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fn1.inviteIntoGroup(msg.to,[k1MID,k2MID,k3MID])
                                G = fn2.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                fn2.updateGroup(G)

                        elif cmd == "finbot in" or cmd == "fin in":
                          if run["finbot"] == True:
                            if sender in Creator:
                                G = kang.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kang.updateGroup(G)
                                invsend = 0
                                Ticket = kang.reissueGroupTicket(msg.to)
                                fn1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fn2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fn3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fn4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fn5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kang.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kang.updateGroup(G)

                        elif cmd == "k in" or cmd == "kicker in":
                          if run["finbot"] == True:
                            if sender in Creator:
                                G = kang.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kang.updateGroup(G)
                                invsend = 0
                                Ticket = kang.reissueGroupTicket(msg.to)
                                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = k2.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k2.updateGroup(G)

                        elif cmd == "kickerbye" or cmd == "citbye":
                          if run["finbot"] == True:
                            if sender in Creator:
                                k1.leaveGroup(msg.to)
                                k2.leaveGroup(msg.to)
                                k3.leaveGroup(msg.to)

                        elif cmd == "kickerbye inv" or cmd == "citbye stand":
                          if run["finbot"] == True:
                            if sender in Creator:
                                k1.leaveGroup(msg.to)
                                k2.leaveGroup(msg.to)
                                k3.leaveGroup(msg.to)
                                fn1.inviteIntoGroup(msg.to,k1MID)
                                fn2.inviteIntoGroup(msg.to,k2MID)
                                fn3.inviteIntoGroup(msg.to,k3MID)

                        elif cmd == "byeall" or cmd == "bye bye" or cmd == '... ':
                          if run["finbot"] == True:
                            if sender in Creator:
                                #kang.leaveGroup(msg.to)
                                fn1.leaveGroup(msg.to)
                                fn2.leaveGroup(msg.to)
                                fn3.leaveGroup(msg.to)
                                fn4.leaveGroup(msg.to)
                                fn5.leaveGroup(msg.to)

                        elif cmd == "absen" or cmd == "check":
                          if run["finbot"] == True:
                            if sender in Creator or sender in admin:
                                getMention(to,"FINBOT ALREADY @!",[sender])
                                getMention1(to,"Assist 1 ready @!",[sender])
                                getMention2(to,"Assist 2 ready @!",[sender])
                                getMention3(to,"Assist 3 ready @!",[sender])
                                getMention4(to,"Assist 4 ready @!",[sender])
                                getMention5(to,"Assist 5 ready @!",[sender])

                        elif "Inviteme: " in msg.text:
                          if sender in Creator:
                            gid = msg.text.replace("Inviteme: ","")
                            if gid == "":
                                _Chat(to,"Invalid group id")
                            else:
                                try:
                                    kang.findAndAddContactsByMid(sender)
                                    kang.inviteIntoGroup(gid,[sender])
                                except:
                                    _Chat(to,"Mungkin saya tidak di dalaam grup itu")

                        elif "f1Inviteme: " in msg.text:
                          if sender in Creator:
                            gid = msg.text.replace("Inviteme: ","")
                            if gid == "":
                                _Chat1(to,"Invalid group id")
                            else:
                                try:
                                    fn1.findAndAddContactsByMid(sender)
                                    fn1.inviteIntoGroup(gid,[sender])
                                except:
                                    _Chat1(to,"Mungkin saya tidak di dalaam grup itu")

                        elif cmd == "setting" or cmd == 'settbot':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╔═══════════\n"
                                md+="║۝🄵🄸🄽 🄱🄾🅃۝\n"
                                md+="╠═══════════\n"
                                if bot_run["autoJoin"] == True: md+="║❏〘 Auto join 〙『 📲 』\n"
                                else: md+="║❏〘 Auto join 〙『 📴 』\n"
                                if bot_run["autoAdd"] == True: md+="║❏〘 Auto add 〙『 📲 』\n"
                                else: md+="║❏〘 Auto add 〙『 📴 』\n"
                                if bot_run["autoBlock"] == True: md+="║❏〘 Auto block 〙『 📲 』\n"
                                else: md+="║❏〘 Auto block 〙『 📴 』\n"
                                if bot_run["autoLeave"] == True: md+="║❏〘 Auto leave 〙『 📲 』\n"
                                else: md+="║❏〘 Auto leave 〙『 📴 』\n"
                                if bot_run["AutoRead"] == True: md+="║❏〘 Auto read 〙『 📲 』\n"
                                else: md+="║❏〘 Auto read 〙『 📴 』\n"
                                if bot_run["invite"] == True: md+="║❏〘 Auto Inv 〙『 📲 』\n"
                                else: md+="║❏〘 Auto Inv 〙『 📴 』\n"
                                if bot_run["autokick"] == True: md+="║❏〘 Warning 〙『 📲 』\n"
                                else: md+="║❏〘 Warning 〙『 📴 』\n"
                                if bot_run["checkPost"] == True: md+="║❏〘 CheckPost 〙『 📲 』\n"
                                else: md+="║❏〘 CheckPost 〙『 📴 』\n"
                                if bot_run["contact"] == True: md+="║❏〘 Contact 〙『 📲 』\n"
                                else: md+="║❏〘 Contact 〙『 📴 』\n"
                                if bot_run["changePicture"] == True: md+="║❏〘 Change pict 〙『 📲 』\n"
                                else: md+="║❏〘 Change pict 〙『 📴 』\n"
                                if bot_run["nyusup"] == True: md+="║❏〘 Mode Nyusup 〙『 📲 』\n"
                                else: md+="║❏〘 Mode Nyusup 〙『 📴 』\n"
                                if bot_run["limiter"]["on"] == True: md+="║❏〘 limiter 〙" + "『 " + str(bot_run["limiter"]["members"]) + " 』" + "\n"
                                else: md+="􀠁􀆩􏿿║❏〘 limiter 〙:『 📴 』\n"
                                if bot_run["scanner"] == True: md+="║❏〘 Scanner 〙『 📲 』\n"
                                else: md+="║❏〘 Scanner 〙『 📴 』\n"
                                if bot_run["detectMention"] == True: md+="║❏〘 Respon 〙『 📲 』\n"
                                else: md+="║❏〘 Respon 〙『 📴 』\n"
                                if bot_run["detectMention1"] == True: md+="║❏〘 Respon cont 〙『 📲 』\n"
                                else: md+="║❏〘 Respon cont 〙『 📴 』\n"
                                if bot_run["ResponPc"] == True: md+="║❏〘 Respon PC 〙『 📲 』\n"
                                else: md+="║❏〘 Respon PC 〙『 📴 』\n"
                                if bot_run["MentionKick"] == True: md+="║❏〘 Respon kick 〙『 📲 』\n"
                                else: md+="║❏〘 Respon kick 〙『 📴 』\n"
                                if bot_run["unsendMessage"] == True: md+="║❏〘 unsend Msg 〙『 📲 』\n"
                                else: md+="║❏〘 unsend Msg 〙『 📴 』\n"
                                if msg.to in bot_run["Welcome"]: md+="║❏〘 Welcome 〙『 📲 』\n"
                                else: md+="║❏〘 Welcome 〙『 📴 』\n"
                                if bot_run["pname"] == True: md+="║❏〘 Lockname 〙『 📲 』\n"
                                else: md+="║❏〘 Lockname 〙『 📴 』\n╚═══════════\n"
                                _Chat(to, md+"╔═══════════\n" + "║〘 日付 〙: ["+ datetime.strftime(timeNow,'%Y-%m-%d')+"]\n" + "╠═══════════\n" + "║〘 時間 〙[ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n" + "╚═══════════")

                        elif cmd == "settpro" or cmd == 'sett protect':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md ="\n"
                                md+="[ PROTECTION ]\n"
                                md+="\n"
                                if msg.to in bot_run["Pro_Qr"]: md+="Pro QR [ ON ]\n"
                                else: md+="Pro QR [ OFF ]\n"
                                if msg.to in bot_run["Pro_Join"]: md+="Pro Joined [ ON ]\n"
                                else: md+="Pro Joined [ OFF ]\n"
                                if msg.to in bot_run["Pro_Member"]: md+="Pro Member [ ON ]\n"
                                else: md+="Pro Member [ OFF ]\n"
                                if msg.to in bot_run["Pro_Invite"]: md+="Pro Invite [ ON ]\n"
                                else: md+="Pro Invite [ OFF ]\n"
                                if msg.to in bot_run["Pro_Cancel"]: md+="Pro cancel [ ON ]\n"
                                else: md+="Pro cancel [ OFF ]\n"
                                _Chat(msg.to, md+"\n" + "["+ datetime.strftime(timeNow,'%Y-%m-%d')+"]\n" + "[ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n" + "")

                        elif cmd == "costumer":
                          if run["finbot"] == True:
                            if sender in Master:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in Creator:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +kang.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +kang.getContact(m_id).displayName + "\n"
                                _Chat(msg.to,"[ FINBOT]\n\nMaster:\n"+ma+"\nAdmin:\n"+mb+"\nTotal [ %s ]FINBOT" %(str(len(Creator)+len(run_bot["Admin"]))))

                        elif cmd == "listpro":
                          if run["finbot"] == True:
                            if sender in Master:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                mf = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                f = 0
                                gid = bot_run["Pro_Qr"]
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +kang.getGroup(group).name + "\n"
                                gid = bot_run["Pro_Member"]
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +kang.getGroup(group).name + "\n"
                                gid = bot_run["Pro_Join"]
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +kang.getGroup(group).name + "\n"
                                gid = bot_run["Pro_Cancel"]
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +kang.getGroup(group).name + "\n"
                                gid = protectname
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +kang.getGroup(group).name + "\n"
                                gid = bot_run["Pro_Invite"]
                                for group in gid:
                                    f = f + 1
                                    end = '\n'
                                    mf += str(f) + ". " +kang.getGroup(group).name + "\n"
                                _Chat(msg.to,"\nCustom Protection\n\nURL Pro :\n"+ma+"\nKICKER Pro :\n"+mb+"\nJOINER Pro  :\n"+md+"\nCANCEL Pro :\n"+mc+"\nPro Gname :\n"+me+"\nPro Invite :\n"+mf+"\nTotal [ %s ] Mode protection is being Maintained" %(str(len(bot_run["Pro_Qr"])+len(bot_run["Pro_Member"])+len(bot_run["Pro_Join"])+len(bot_run["Pro_Cancel"])+len(protectname)+len(bot_run["Pro_Invite"]))))

                        elif cmd == "allbots" or cmd == 'listbot':
                          if run["finbot"] == True:
                            if sender in Master:
                                ma = ""
                                a = 0
                                for m_id in run_bot["assist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +kang.getContact(m_id).displayName + "\n"
                                _Chat(msg.to,"\n"+ma+"\nTotal %s AllBots" %(str(len(bot_run["assist"]))))

#SETT MODIFY N MANAGE BOTS AUTH

                        elif 'induk login: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('induk login: ','')
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Replace failed")
                              else:
                                  run_bot["kang"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  _Chat(to, "Restarted by new authToken\n[ {} ]".format(str(spl)))

                        elif 'mylogin: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('mylogin: ','')
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Replace failed")
                              else:
                                  run_bot["authToken"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  _Chat(to, "bot login by new client\n {}".format(str(spl))+"\n\nPlease restart for run your client")

                        elif 'bot1 login: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('bot1 login: ','')
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Replace failed")
                              else:
                                  run_bot["fino1"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  _Chat(to, "[ Bot1 login by new authToken ]\n[ {} ]".format(str(spl)))

                        elif 'bot2 login: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('bot2 login: ','')
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Replace failed")
                              else:
                                  run_bot["fino2"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  _Chat(to, "[ Bot2 login by new authToken ]\n[ {} ]".format(str(spl)))

                        elif 'bot3 login: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('bot3 login: ','')
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Replace failed")
                              else:
                                  run_bot["fino3"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  _Chat(to, "[ Bot3 login by new authToken ]\n[ {} ]".format(str(spl)))

                        elif 'bot4 login: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('bot4 login: ','')
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Replace failed")
                              else:
                                  run_bot["fino4"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  _Chat(to, "[ Bot4 login by new authToken ]\n[ {} ]".format(str(spl)))

                        elif 'bot5 login: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('bot5 login: ','')
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Replace failed")
                              else:
                                  run_bot["fino5"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  _Chat(to, "[ Bot5 login by new authToken ]\n[ {} ]".format(str(spl)))

                        elif 'kicker1 login: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('kicker1 login: ','')
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Replace failed")
                              else:
                                  run_bot["kicker1"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  _Chat(to, "Kicker1 login by new authToken\n[ {} ]".format(str(spl)))

                        elif 'kicker2 login: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('kicker2 login: ','')
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Replace failed")
                              else:
                                  run_bot["kicker2"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  _Chat(to, "Kicker2 login  by new authToken\n[ {} ]".format(str(spl)))

                        elif 'kicker3 login: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('kicker3 login: ','')
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Replace failed")
                              else:
                                  run_bot["kicker3"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  _Chat(to, "Kicker3 login by new authToken\n[ {} ]".format(str(spl)))

                        elif cmd == "rm bot" or cmd == 'remove allbot':
                          if run["finbot"] == True:
                            if sender in Master:
                                run_bot["kang"] = ""
                                run_bot["kangMid"] = ""
                                run_bot["fino1"] = ""
                                run_bot["fino1Mid"] = ""
                                run_bot["fino2"] = ""
                                run_bot["fino2Mid"] = ""
                                run_bot["fino3"] = ""
                                run_bot["fino3Mid"] = ""
                                run_bot["fino4"] = ""
                                run_bot["fino4Mid"] = ""
                                run_bot["fino5"] = ""
                                run_bot["fino5Mid"] = ""
                                run_bot["kicker1"] = ""
                                run_bot["kicker1Mid"] = ""
                                run_bot["kicker2"] = ""
                                run_bot["kicker2Mid"] = ""
                                run_bot["kicker3"] = ""
                                run_bot["kicker3Mid"] = ""
                                with open('finbotLogged.json', 'w') as fp:
                                	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                _Chat(to,"All bots authThoken has been removed")
                                getMention(to,"Please regenerate your Bot authToken before restarting your system\n @!", [sender])

 #SETT MODIFY AUTH TYPE N VERSION
                        elif 'la chrome: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('la chrome: ','')
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Replace failed")
                              else:
                                  run_bot["CHROMEOS"]["LA"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  _Chat(to, "X-LineAccess Modified by version: \n {}".format(str(spl)))
                        elif 'ua chrome: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('ua chrome: ','')
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Replace failed")
                              else:
                                  run_bot["CHROMEOS"]["UA"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  _Chat(to, "User Agent Modified by version: \n {}".format(str(spl)))

                        elif 'la mac: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('la mac: ','')
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Replace failed")
                              else:
                                  run_bot["DESKTOPMAC"]["LA"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  _Chat(to, "X-LineAccess Modified by version: \n {}".format(str(spl)))
                        elif 'ua mac: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('ua mac: ','')
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Replace failed")
                              else:
                                  run_bot["DESKTOPMAC"]["UA"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  _Chat(to, "User Agent Modified by version: \n {}".format(str(spl)))

 #TOKEN BOT
                        elif cmd == 'auth mac' or cmd == "desktopmac":
                           if sender in Master or sender in admin:
                              client = DESKTOPMAC(FINBOT_AUTH_QUERY_PATH_FIR, None, FinbotService.Client)
                              qr = client.getAuthQrcode(keepLoggedIn=1, systemName="FINBOT-PC")
                              uri = "line://au/q/" + qr.verifier
                              _Chat(to,"[ FINBOT TOKEN ]\n\n" + "[ " +str(uri) + " ]" + "\n\nKlik this link for 1 minute \nAuthorized by: \n[ http://line.me/ti/p/~kangnur04 ]")
                              header = {'User-Agent': UA,'X-Line-Application': LA,"x-lal" : "ja-US_US","x-lpqs" : FINBOT_AUTH_QUERY_PATH_FIR,'X-Line-Access': qr.verifier}
                              getAccessKey = getJson(host + FINBOT_CERTIFICATE_PATH, header)
                              client = DESKTOPMAC(FINBOT_AUTH_QUERY_PATH, None, FinbotLoginService.Client)
                              req = LoginRequest()
                              req.type = 1
                              req.verifier = qr.verifier
                              req.e2eeVersion = 1
                              res = client.loginZ(req)
                              client = DESKTOPMAC(FINBOT_API_QUERY_PATH_FIR, {'X-Line-Access':res.authToken}, FinbotService.Client)
                              _Chat(to,"[ Login succes at FINBOT-PC ]\nBy version "+ UA + "\n" + "[ " +str(res.authToken)+ " ]")

                        elif cmd == 'auth chrome' or cmd == "chromeos":
                           if sender in Master or sender in admin:
                              client = CHROMEOS(FINBOT_AUTH_QUERY_PATH_FIR, None, FinbotService.Client)
                              qr = client.getAuthQrcode(keepLoggedIn=1, systemName="FINBOT-PC")
                              uri = "line://au/q/" + qr.verifier
                              _Chat(to,"[ FINBOT TOKEN ]\n\n" + "[ " +str(uri) + " ]" + "\n\nKlik this link for 1 minute \nAuthorized by: \n[ http://line.me/ti/p/~kangnur04 ]")
                              header = {'User-Agent': UA1,'X-Line-Application': LA1,"x-lal" : "ja-US_US","x-lpqs" : FINBOT_AUTH_QUERY_PATH_FIR,'X-Line-Access': qr.verifier}
                              getAccessKey = getJson(host + FINBOT_CERTIFICATE_PATH, header)
                              client = CHROMEOS(FINBOT_AUTH_QUERY_PATH, None, FinbotLoginService.Client)
                              req = LoginRequest()
                              req.type = 1
                              req.verifier = qr.verifier
                              req.e2eeVersion = 1
                              res = client.loginZ(req)
                              client = CHROMEOS(FINBOT_API_QUERY_PATH_FIR, {'X-Line-Access':res.authToken}, FinbotService.Client)
                              _Chat(to,"[ Login succes at FINBOT-PC ]\nBy version "+ UA1 + "\n" + "[ " +str(res.authToken)+ " ]")
  
                        elif cmd == 'auth win' or cmd == "desktopwin":
                           if sender in Master or sender in admin:
                              client = DESKTOPWIN(FINBOT_AUTH_QUERY_PATH_FIR, None, FinbotService.Client)
                              qr = client.getAuthQrcode(keepLoggedIn=1, systemName="FINBOT")
                              uri = "line://au/q/" + qr.verifier
                              _Chat(to,"[ FINBOT TOKEN ]\n\n" + "[ " +str(uri) + " ]" + "\n\nKlik this link for 1 minute \nAuthorized by: \n[ http://line.me/ti/p/~kangnur04 ]")
                              header = {'User-Agent': UA2,'X-Line-Application': LA2,"x-lal" : "ja-US_US","x-lpqs" : FINBOT_AUTH_QUERY_PATH_FIR,'X-Line-Access': qr.verifier}
                              getAccessKey = getJson(host + FINBOT_CERTIFICATE_PATH, header)
                              client = DESKTOPWIN(FINBOT_AUTH_QUERY_PATH, None, FinbotLoginService.Client)
                              req = LoginRequest()
                              req.type = 1
                              req.verifier = qr.verifier
                              req.e2eeVersion = 1
                              res = client.loginZ(req)
                              client = DESKTOPWIN(FINBOT_API_QUERY_PATH_FIR, {'X-Line-Access':res.authToken}, FinbotService.Client)
                              _Chat(to,"Login succes")
                              _Chat(to,str(res.authToken))

                        elif cmd == 'auth ios' or cmd == "ios":
                           if sender in Master or sender in admin:
                              client = IOS(FINBOT_AUTH_QUERY_PATH_FIR, None, FinbotService.Client)
                              qr = client.getAuthQrcode(keepLoggedIn=1, systemName="FINBOT")
                              uri = "line://au/q/" + qr.verifier
                              _Chat(to,"[ FINBOT TOKEN ]\n\n" + "[ " +str(uri) + " ]" + "\n\nKlik this link for 1 minute \nAuthorized by: \n[ http://line.me/ti/p/~kangnur04 ]")
                              header = {'User-Agent': UA3,'X-Line-Application': LA3,"x-lal" : "ja-US_US","x-lpqs" : FINBOT_AUTH_QUERY_PATH_FIR,'X-Line-Access': qr.verifier}
                              getAccessKey = getJson(host + FINBOT_CERTIFICATE_PATH, header)
                              client = IOS(FINBOT_AUTH_QUERY_PATH, None, FinbotLoginService.Client)
                              req = LoginRequest()
                              req.type = 1
                              req.verifier = qr.verifier
                              req.e2eeVersion = 1
                              res = client.loginZ(req)
                              client = IOS(FINBOT_API_QUERY_PATH_FIR, {'X-Line-Access':res.authToken}, FinbotService.Client)
                              _Chat(to,"Login succes")
                              _Chat(to,str(res.authToken))

                        elif cmd == "win10":
                           if sender in Master or sender in admin:
                              client = WIN10(FINBOT_AUTH_QUERY_PATH_FIR, None, FinbotService.Client)
                              qr = client.getAuthQrcode(keepLoggedIn=1, systemName="FINBOT")
                              uri = "line://au/q/" + qr.verifier
                              _Chat(to,"[ FINBOT TOKEN ]\n\n" + "[ " +str(uri) + " ]" + "\n\nKlik this link for 1 minute \nAuthorized by: \n[ http://line.me/ti/p/~kangnur04 ]")
                              header = {'User-Agent': UA4,'X-Line-Application': LA4,"x-lal" : "ja-US_US","x-lpqs" : FINBOT_AUTH_QUERY_PATH_FIR,'X-Line-Access': qr.verifier}
                              getAccessKey = getJson(host + FINBOT_CERTIFICATE_PATH, header)
                              client = WIN10(FINBOT_AUTH_QUERY_PATH, None, FinbotLoginService.Client)
                              req = LoginRequest()
                              req.type = 1
                              req.verifier = qr.verifier
                              req.e2eeVersion = 1
                              res = client.loginZ(req)
                              client = WIN10(FINBOT_API_QUERY_PATH_FIR, {'X-Line-Access':res.authToken}, FinbotService.Client)
                              _Chat(to,"Login succes")
                              _Chat(to,str(res.authToken))
                              
                        elif cmd == 'clova' or cmd == "clovafriends":
                           if sender in Master or sender in admin:
                              client = CLOVAFRIENDS(FINBOT_AUTH_QUERY_PATH_FIR, None, FinbotService.Client)
                              qr = client.getAuthQrcode(keepLoggedIn=1, systemName="FINBOT")
                              uri = "line://au/q/" + qr.verifier
                              _Chat(to,"[ FINBOT TOKEN ]\n\n" + "[ " +str(uri) + " ]" + "\n\nKlik this link for 1 minute \nAuthorized by: \n[ http://line.me/ti/p/~kangnur04 ]")
                              header = {'User-Agent': UA5,'X-Line-Application': LA5,"x-lal" : "ja-US_US","x-lpqs" : FINBOT_AUTH_QUERY_PATH_FIR,'X-Line-Access': qr.verifier}
                              getAccessKey = getJson(host + FINBOT_CERTIFICATE_PATH, header)
                              client = CLOVAFRIENDS(FINBOT_AUTH_QUERY_PATH, None, FinbotLoginService.Client)
                              req = LoginRequest()
                              req.type = 1
                              req.verifier = qr.verifier
                              req.e2eeVersion = 1
                              res = client.loginZ(req)
                              client = CLOVAFRIENDS(FINBOT_API_QUERY_PATH_FIR, {'X-Line-Access':res.authToken}, FinbotService.Client)
                              _Chat(to,"Login succes")
                              _Chat(to,str(res.authToken))

                        elif cmd == "creator" or cmd == 'owner':
                            if sender in Master:
                                _Chat(to,"╔═══════════\n║Creator \n║〘 ۝🄵🄸🄽 🄱🄾🅃۝ 〙\n╠═══════════\n║http://line.me/ti/p/~kangnur04\n╚═══════════")
                                _Chat(to, None, contentMetadata={'mid': finoMID}, contentType=13)

                        elif cmd == "add me" or cmd == 'bot add me':
                            if sender in Master:
                                kang.findAndAddContactsByMid(sender)
                                getMention(to,"Add success @!",[sender])
                                fn1.findAndAddContactsByMid(sender)
                                getMention1(to,"Add success @!",[sender])
                                fn2.findAndAddContactsByMid(sender)
                                getMention2(to,"Add success @!",[sender])
                                fn3.findAndAddContactsByMid(sender)
                                getMention3(to,"Add success @!",[sender])
                                fn4.findAndAddContactsByMid(sender)
                                getMention4(to,"Add success @!",[sender])
                                fn5.findAndAddContactsByMid(sender)
                                getMention5(to,"Add success @!",[sender])
                                k1.findAndAddContactsByMid(sender)
                                k2.findAndAddContactsByMid(sender)
                                k3.findAndAddContactsByMid(sender)
                                getMention(to,"Kicker Add success @!",[sender])

                        elif cmd == "about" or cmd == "informasi":
                          if run["finbot"] == True:
                            if sender in Master:
                               arr = []
                               today = datetime.today()
                               future = datetime(2019,3,1)
                               hari = (str(future - today))
                               comma = hari.find(",")
                               hari = hari[:comma]
                               blockedlist = kang.getBlockedContactIds()
                               creator = kang.getContact(run_bot["Creator"])
                               teman = kang.getAllContactIds()
                               gid = kang.getGroupIdsJoined()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               eltime = time.time() - mulai
                               bot = runtime(eltime)
                               ret_ = "╔═════════════"
                               ret_ += "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』"
                               ret_ += "\n╠═════════════"
                               ret_ += "\n║『 Creator 』:{}".format(creator.displayName)
                               ret_ += "\n╠═════════════"
                               ret_ += "\n║ 日付 : {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                               ret_ += "\n║ グループ : {}".format(str(len(gid)))
                               ret_ += "\n║ 友人 』: {}".format(str(len(teman)))
                               ret_ += "\n║ ブロック : {}".format(str(len(blockedlist)))
                               ret_ += "\n║ 失効した 』: {}".format(hari)
                               ret_ += "\n║ バージョン : 🄵🄸🄽 🄱🄾🅃 V.4"
                               ret_ += "\n║ 時間 : {}".format(datetime.strftime(timeNow,'%Y-%m-%d'))
                               ret_ += "\n╠═════════════"
                               ret_ += "\n║『 Runtime 』"
                               ret_ += "\n║ {}".format(bot)
                               ret_ += "\n╚═════════════"
                               _Chat(to,str(ret_))

                        elif cmd == "me" or msg.text.lower() == 'me':
                          if run["finbot"] == True:
                            if sender in Master:
                               _Chat(to,None,contentMetadata = {'mid': myMID}, contentType=13)

                        elif cmd == "oi" or cmd == 'all':
                          if run["finbot"] == True:
                            if sender in Master:
                                group = kang.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                cb = ""
                                cb2 = ""
                                strt = int(0)
                                akh = int(0)
                                for md in nama:
                                    akh = akh + int(6)
                                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                                    strt = strt + int(7)
                                    akh = akh + 1
                                    cb2 += "@nrik \n"
                                cb = (cb[:int(len(cb)-1)])
                                _Chat(to,cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)

                        elif cmd == "mid":
                               _Chat(to, msg._from)

                        elif cmd == "welcome" or cmd == 'wc':
                          if run["finbot"] == True:
                            if sender in Master:
                               try:
                                   ginfo = fino.getGroup(msg.to)
                                   gcreator = ginfo.creator.displayName
                               except:
                                   gcreator = "Gcreator puskun boss"
                               else:
                                   ret_ = "Di Group"
                                   ret_ += "\n{}".format(ginfo.name)
                                   ret_ +="\n{}".format(gcreator)
                                   _SendChat(to,str(ret_))
                                   fino.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+ginfo.pictureStatus)

                        elif cmd.startswith('stealmid '):
                          if run["finbot"] == True:
                            if sender in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = kang.getContact(key1)
                               _Chat(to, "『 User Name 』 : "+str(mi.displayName)+"\n『 User Mid 』 : " + key1)
                               _Chat(to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif cmd.startswith('info '):
                          if run["finbot"] == True:
                            if sender in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = kang.getContact(key1)
                               _Chat(to, "『 User Name 』 : "+str(mi.displayName)+"\n『 User Mid 』 : " + key1+"\n『 User Bio 』 : "+str(mi.statusMessage))
                               _Chat(to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(kang.getContact(key1)):
                                   kang.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   kang.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "cek. " or cmd == 'crash':
                          if run["finbot"] == True:
                            if sender in Master:
                               _Chat(to, None, contentMetadata={'mid': "ud108eea8074da128b9cd064a8a28e27a,'"}, contentType=13)

                        elif cmd == "rm chat" or cmd == 'mychat':
                          if run["finbot"] == True:
                            if sender in Creator:
                               try:
                                   fino.removeAllMessages(alfino.param2)
                                   _Chat(to, "『 Done Boss 』")
                               except:
                                   pass

                        elif cmd == "delchat" or cmd == 'rechat':
                          if run["finbot"] == True:
                            if sender in Master:
                               try:
                                   kang.removeAllMessages(alfino.param2)
                                   fn1.removeAllMessages(alfino.param2)
                                   fn2.removeAllMessages(alfino.param2)
                                   fn3.removeAllMessages(alfino.param2)
                                   fn4.removeAllMessages(alfino.param2)
                                   fn5.removeAllMessages(alfino.param2)
                                   _Chat(to, "『 Done Boss 』")
                               except:
                                   pass

                        elif cmd.startswith("cast: "):
                          if run["finbot"] == True:
                            if sender in Master:
                               sep = text.split(" ")
                               text = text.replace(sep[0] + " ","")
                               friends = fino.getAllContactIds()
                               for friend in friends:
                               	_SendChatt1(friend, "[ Broadcast ]\n{}".format(str(text)))
                               	#fino.sendMessage(msg.to, "Berhasil broadcast ke {} teman".format(str(len(friends))))

                        elif cmd.startswith("fbroadcast: "):
                          if run["finbot"] == True:
                            if sender in Master:
                               sep = text.split(" ")
                               text = text.replace(sep[0] + " ","")
                               friends = kang.getAllContactIds()
                               for friend in friends:
                               	_Chatt(friend, "[ BROADCAST ]\n{}".format(str(text)))
                               	_Chat(to, "Berhasil broadcast ke {} teman".format(str(len(friends))))

                        elif cmd.startswith("broadcast: "):
                          if run["finbot"] == True:
                            if sender in Master:
                               sep = text.split(" ")
                               text = text.replace(sep[0] + " ","")
                               groups = kang.getGroupIdsJoined()
                               for group in groups:
                                   _Chatt(group,"『 Broadcast 』\n{}".format(str(text)))
                                   _Chat(to, "▪Berhasil broadcast ke {} group".format(str(len(groups))))

                        elif cmd == "mykey":
                          if run["finbot"] == True:
                            if sender in Master:
                               _Chat(to, "「Mykey」\n▪「 " + str(bot_run["keyCommand"]) + " 」")
 
                        elif cmd.startswith("setkey "):
                          if run["finbot"] == True:
                            if sender in Master:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   _Chat(to, "▪Gagal mengganti key")
                               else:
                                   bot_run["keyCommand"] = str(key).lower()
                                   _Chat(to, "「Setkey」\n▪「{}」".format(str(key).lower()))
                                   
                        elif cmd == "resetkey":
                          if run["finbot"] == True:
                            if sender in Master:
                               bot_run["keyCommand"] = ""
                               getMention(to, "Refreshing key\n@!", [sender])

                        elif cmd == "reboot":
                          if run["finbot"] == True:
                            if sender in Master:
                               getMention(to, "『 Finbot rebooting... 』\n@!", [sender])
                               bot_run["restartPoint"] = msg.to
                               restartBot()

                        elif cmd == "restart":
                          if run["finbot"] == True:
                            if sender in Master:
                               getMention(to,"Restarting authToken...\n@!", [sender])
                               eltime = time.time() - mulai
                               rest = "Deploy time\n" +waktu(eltime)
                               _Chat(to,rest)
                               bot_run["restartPoint"] = msg.to
                               restart_program()

                        elif cmd == "runtime" or cmd == 'deploy':
                          if run["finbot"] == True:
                            if sender in Master:
                               eltime = time.time() - mulai
                               bot_ = "╔═════════════"
                               bot_ += "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』"
                               bot_ += "\n╠═════════════"
                               bot_ += "\n║『 Deploy Time 』"
                               bot_ += "\n║{}".format(waktu(eltime)) 
                               bot_ += "\n╚═════════════"
                               _Chat(to,str(bot_))

                        elif cmd == "info group" or cmd == "ginfo":
                          if sender in Master:
                            try:
                                G = kang.getGroup(msg.to)
                                ret_ = ""
                                try:
                                	gCreator = G.creator.displayName
                                except:
                                    gCreator = "『 PUSKUN 』"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "『 Closed 』"
                                    gTicket = "『 No prevent 』"
                                else:
                                    gQr = "『 Opened 』"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(kang.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "╔═════════════"
                                ret_ += "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』"
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group Name 』"
                                ret_ += "\n║{}".format(G.name)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group ID 』"
                                ret_ += "\n║{}".format(G.id)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group Creator 』"
                                ret_ += "\n║{}".format(gCreator)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Since 』"
                                ret_ += "\n║{}".format(str(timeCreated))
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Total Member 』"
                                ret_ += "\n║{}".format(str(len(G.members)))
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Total Pending 』"
                                ret_ += "\n║{}".format(gPending)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Qr Status 』"
                                ret_ += "\n║ {}".format(gQr)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Url Group 』"
                                ret_ += "\n║ {}".format(gTicket)
                                ret_ += "\n╚═════════════"
                                _Chat(to, str(ret_))
                                kang.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except:
                                pass

                        elif cmd == ".group" or cmd == 'lg':
                          if run["finbot"] == True:
                            if sender in Master:
                               ma = ""
                               a = 0
                               gid = kang.getGroupIdsJoined()
                               for i in gid:
                                   G = kang.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "│ " + str(a) + ". " +G.name+ "\n"
                               _Chat(to,"╭──────────\n"+ma+"╰──────────\n╭──────────\n│『Total「"+str(len(gid))+"」Groups』)\n│▪Check Group member type⇣\n│[Ex] Member 1\n│\n│▪Check List Group type⇣\n│[Ex] Group 1\n╰──────────")

                        elif cmd.startswith("listgroup "):
                          if sender in Master:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = kang.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = kang.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "『 PUSKUN 』"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "『 Closed 』"
                                    gTicket = "『 No prevent 』"
                                else:
                                    gQr = "『 Opened 』"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(kang.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "╔═════════════"
                                ret_ += "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』"
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group Name 』"
                                ret_ += "\n║{}".format(G.name)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group ID 』"
                                ret_ += "\n║{}".format(G.id)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group Creator 』"
                                ret_ += "\n║{}".format(gCreator)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Since 』"
                                ret_ += "\n║{}".format(str(timeCreated))
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Total Member 』"
                                ret_ += "\n║  {}".format(str(len(G.members)))
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Total Pending 』"
                                ret_ += "\n║  {}".format(gPending)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Qr Status 』"
                                ret_ += "\n║  {}".format(gQr)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Url Group 』"
                                ret_ += "\n║  {}".format(gTicket)
                                ret_ += "\n╚═════════════"
                                _Chat(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("listmember "):
                          if sender in Master:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = kang.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = kang.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n║⇨ "+ str(no) + ". " + mem.displayName
                                _Chat(to,"╔═════════════" + "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』" + "\n╠═════════════" + "\n║『 Group 』 :  " + str(G.name) + " \n╠═════════════" + "\n║『 User Name Member 』" + "\n╠═════════════" + ret_ + "\n╠═════════════" + "\n║『 Total Member %i 』" % len(G.members) + "╚═════════════")
                            except: 
                                pass

                        elif cmd.startswith("gmember "):
                          if sender in Master:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = kang.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = kang.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ = kang.getContact(mem)
                                _Chat(to,None, contentMetadata={'mid': mem}, contentType=13)
                            except: 
                                pass

                        elif cmd == "listfriend" or cmd == 'temen':
                          if run["finbot"] == True:
                            if sender in Master:
                               ma = ""
                               a = 0
                               gid = kang.getAllContactIds()
                               for i in gid:
                                   G = kang.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "◇ " + str(a) + ". " +G.displayName+ "\n"
                               _Chat(to,"『 User Name Friend 』\n"+ma+"\n『 Total「"+str(len(gid))+"」Friends 』")

                        elif cmd == "glink":
                          if run["finbot"] == True:
                            if sender in Master:
                                if msg.toType == 2:
                                   x = kang.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      kang.updateGroup(x)
                                   gurl = kang.reissueGroupTicket(msg.to)
                                   _Chat(to,"╔═════════════" + "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』" + "\n╠═════════════" + "\n║『 User Name Group 』" + "\n║"+str(x.name)+ " \n╠═════════════" + "\n║『 Gurl 』" + "\n║ http://line.me/R/ti/g/"+gurl + "\n╚═════════════")

                        elif cmd == "ourl":
                          if run["finbot"] == True:
                            if sender in Master:
                                if msg.toType == 2:
                                   X = kang.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   kang.updateGroup(X)
                                   getMention(to, "『 Url opened 』\n@!", [sender])

                        elif cmd == "curl":
                          if run["finbot"] == True:
                            if sender in Master:
                                if msg.toType == 2:
                                   X = kang.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   kang.updateGroup(X)
                                   getMention(to,"『 Url Closed 』\n@!", [sender])

                        elif cmd == "addimage":
                          if run["finbot"] == True:
                            if sender in Master:
                              if msg.toType == 2:
                                bot_run["Addimage"] = True
                                getMention(to, "『 Send your pict 』\n@!", [sender])

                        elif cmd == "changefoto" or cmd == 'cft':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["changePicture"] = True
                                getMention(to,"『 Send your pict 』\n@!", [sender])

                        elif cmd == "kickerfoto" or cmd == 'k cft':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["kickerPicture"] = True
                                getMention(to,"『 Send your pict 』\n@!", [sender])

                        elif cmd == "coverfoto" or cmd == 'cvf':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["changePictureCover"] = True
                                getMention(to,"『 Send your pict 』\n@!", [sender])

                        elif cmd == "cfotogroup" or cmd == 'cfg':
                          if run["finbot"] == True:
                            if sender in Master:
                              if msg.toType == 2:
                                bot_run["groupPicture"] = True
                                getMention(to,"『 Send your pict 』\n@!", [sender])

                        elif cmd == "updatefoto" or cmd == 'myft':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["foto"][myMID] = True
                                getMention(to,"『 Send your pict 』\n@!", [sender])

                        elif cmd == "f1cft" or cmd == 'f1ft':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["foto"][fn1MID] = True
                                getMention1(to,"『 Send your pict 』\n@!", [sender])

                        elif cmd == "f2cft" or cmd == 'f2ft':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["foto"][fn2MID] = True
                                getMention2(to,"『 Send your pict 』\n@!", [sender])

                        elif cmd == "f3cft" or cmd == 'f3ft':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["foto"][fn3MID] = True
                                getMention3(to,"『 Send your pict 』\n@!", [sender])

                        elif cmd == "f4cft" or cmd == 'f4ft':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["foto"][fn4MID] = True
                                getMention4(to,"『 Send your pict 』\n@!", [sender])

                        elif cmd == "f5cft" or cmd == 'f5ft':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["foto"][fn5MID] = True
                                getMention5(to,"『 Send your pict 』\n@!", [sender])

                        elif cmd == "cvp" or cmd == 'cvideo':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["video"][myMID] = True
                                getMention(to,"『 Send your Video 』\n@!", [sender])

                        elif cmd.startswith("myname: "):
                          if sender in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = fino.getProfile()
                                profile.displayName = string
                                fino.updateProfile(profile)
                                getMention(to, "Checkup your name profile @!", [sender])

                        elif cmd.startswith("cname: "):
                          if sender in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = kang.getProfile()
                                profile.displayName = string
                                kang.updateProfile(profile)
                                _Chat(to,bot_run["ResponCname"] + string + "")

                        elif cmd.startswith("f1name: "):
                          if sender in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = fn1.getProfile()
                                profile.displayName = string
                                fn1.updateProfile(profile)
                                _Chat1(to,bot_run["ResponCname"] + string + "")

                        elif cmd.startswith("f2name: "):
                          if sender in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = fn2.getProfile()
                                profile.displayName = string
                                fn2.updateProfile(profile)
                                _Chat2(to,bot_run["ResponCname"] + string + "")

                        elif cmd.startswith("f3name: "):
                          if sender in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = fn3.getProfile()
                                profile.displayName = string
                                fn3.updateProfile(profile)
                                _Chat3(to,bot_run["ResponCname"] + string + "")

                        elif cmd.startswith("f4name: "):
                          if sender in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = fn4.getProfile()
                                profile.displayName = string
                                fn4.updateProfile(profile)
                                _Chat4(to,bot_run["ResponCname"] + string + "")

                        elif cmd.startswith("f5name: "):
                          if sender in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = fn5.getProfile()
                                profile.displayName = string
                                fn5.updateProfile(profile)
                                _Chat5(to,bot_run["ResponCname"] + string + "")

                        elif cmd.startswith("k1name: "):
                          if sender in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = k1.getProfile()
                                profile.displayName = string
                                k1.updateProfile(profile)
                                k1.sendText(Creator,"Genti nama beres boss... " + string + "")

                        elif cmd.startswith("k2name: "):
                          if sender in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = k2.getProfile()
                                profile.displayName = string
                                k2.updateProfile(profile)
                                k2.sendText(Creator,"Genti nama beres boss... " + string + "")

                        elif cmd.startswith("k3name: "):
                          if sender in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = k3.getProfile()
                                profile.displayName = string
                                k3.updateProfile(profile)
                                k3.sendText(Creator,"Genti nama beres boss... " + string + "")

                        elif cmd.startswith("allname: "):
                          if sender in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = kang.getProfile()
                                profile1 = fn1.getProfile()
                                profile2 = fn2.getProfile()
                                profile3 = fn3.getProfile()
                                profile4 = fn4.getProfile()
                                profile5 = fn5.getProfile()
                                profile.displayName = string
                                profile1.displayName = string
                                profile2.displayName = string
                                profile3.displayName = string
                                profile4.displayName = string
                                profile5.displayName = string
                                kang.updateProfile(profile)
                                fn1.updateProfile(profile1)
                                fn2.updateProfile(profile2)
                                fn3.updateProfile(profile3)
                                fn4.updateProfile(profile4)
                                fn5.updateProfile(profile5)
                                getMention(to,"[ Name Already changed ]\n@!",[sender])

                        elif cmd.startswith("cbio: "):
                          if sender in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = kang.getProfile()
                                profile.statusMessage = string
                                kang.updateProfile(profile)
                                getMention(to,"Updated message  status\n@!",[sender])

                        elif cmd.startswith("allbio: "):
                          if sender in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = kang.getProfile()
                                profile1 = fn1.getProfile()
                                profile2 = fn2.getProfile()
                                profile3 = fn3.getProfile()
                                profile4 = fn4.getProfile()
                                profile5 = fn5.getProfile()
                                profile.statusMessage = string
                                profile1.statusMessage = string
                                profile2.statusMessage = string
                                profile3.statusMessage = string
                                profile4.statusMessage = string
                                profile5.statusMessage = string
                                kang.updateProfile(profile)
                                _Chat(to,"Update status Message " + string + "")
                                fn1.updateProfile(profile1)
                                _Chat1(to,"Update status Message " + string + "")
                                fn2.updateProfile(profile2)
                                _Chat2(to,"Update status Message " + string + "")
                                fn3.updateProfile(profile3)
                                _Chat3(to,"Update status Message " + string + "")
                                fn4.updateProfile(profile4)
                                _Chat4(to,"Update status Message " + string + "")
                                fn5.updateProfile(profile5)
                                _Chat5(to,"Update status Message " + string + "")
                                
                        elif cmd == "mention" or cmd == 'sepi':
                          if run["finbot"] == True:
                            if sender in Master:
                               group = kang.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 39):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (19, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (60, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)

                        elif cmd == "byeme" or cmd == 'byebye':
                          if run["finbot"] == True:
                            if sender in Master:
                                G = kang.getGroup(msg.to)
                                _Chat(to, "さようなら...!"+str(G.name))
                                kang.leaveGroup(msg.to)

                        elif cmd == "spres" or cmd == 'sprespon':
                          if run["finbot"] == True:
                            if sender in Master:
                                get_profile_time_start = time.time()
                                get_profile = kang.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = kang.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = kang.getContact(myMID)
                                get_contact_time = time.time() - get_contact_time_start
                                _Chat(to, "╔═════════════\n║【Speed Respon】\n╠═══════════════\n║▪➣Get Profile\n║   %.10f\n╠═══════════════\n║▪➣Get Contact\n║   %.10f\n╠═══════════════\n║▪➣Get Group\n║   %.10f\n╚═══════════════" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if run["finbot"] == True:
                            if sender in Master:
                               get_profile_time_start = time.time()
                               get_profile = kang.getProfile()
                               get_profile_time = time.time() - get_profile_time_start
                               getMention(to,"Speed test...\n\n %.18f" % (get_profile_time/3)+ "\n@!",[sender])

                        elif cmd == "benchmark" or cmd == "spbot":
                          if run["finbot"] == True:
                            if sender in Master:
                               get_profile_time_start1 = time.time()
                               get_profile = fn1.getProfile()
                               get_profile_time1 = time.time() - get_profile_time_start1
                               getMention1(to,"Speed test...\n\n %.18f" % (get_profile_time1/3)+ "\n@!",[sender])
                               
                               get_profile_time_start2 = time.time()
                               get_profile = fn2.getProfile()
                               get_profile_time2 = time.time() - get_profile_time_start2
                               getMention2(to,"Speed test...\n\n %.18f" % (get_profile_time2/3)+ "\n@!",[sender])
                               
                               get_profile_time_start3 = time.time()
                               get_profile = fn3.getProfile()
                               get_profile_time3 = time.time() - get_profile_time_start3
                               getMention3(to,"Speed test...\n\n %.18f" % (get_profile_time3/3)+ "\n@!",[sender])
                               
                               get_profile_time_start4 = time.time()
                               get_profile = fn4.getProfile()
                               get_profile_time4 = time.time() - get_profile_time_start4
                               getMention4(to,"Speed test...\n\n %.18f" % (get_profile_time4/3)+ "\n@!",[sender])
                               
                               get_profile_time_start5 = time.time()
                               get_profile = fn5.getProfile()
                               get_profile_time5 = time.time() - get_profile_time_start5
                               getMention5(to,"Speed test...\n\n %.18f" % (get_profile_time5/3)+ "\n@!",[sender])

                        elif cmd == "lurking on" or cmd == "setlastpoint":
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 bot_run['readPoint'][msg.to] = msg_id
                                 bot_run['readMember'][msg.to] = {}
                                 _Chat(to, "Set the lastseens' point(｀・ω・´)\n\nDate : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "lurking off" or cmd == "resetcctv":
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del bot_run['readPoint'][msg.to]
                                 del bot_run['readMember'][msg.to]
                                 _Chat(to, "Set the lastseens dissable\n\nDate : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "lurkers" or cmd == "viewlastseen":
                          if sender in Master or sender in admin:
                            if msg.to in bot_run['readPoint']:
                                if bot_run['readMember'][msg.to] != {}:
                                    aa = []
                                    for x in bot_run['readMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Seens ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(kang.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        _Chat(to,textx+"\nDate : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]",contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')},contentType = 0)
                                    except:
                                        pass
                                    try:
                                        del bot_run['readPoint'][msg.to]
                                        del bot_run['readMember'][msg.to]
                                    except:
                                        pass
                                    bot_run['readPoint'][msg.to] = msg.id
                                    bot_run['readMember'][msg.to] = {}
                                else:
                                    _Chat(to, "Seens empty...")
                            else:
                                    _Chat(to, "Please type lurking on/setlastpoint before.. ")

                        elif cmd == "sider on" or cmd == 'cctv on':
                          if run["finbot"] == True:
                           if sender in Master or sender in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  _Chat(to, "╔════════════\n║▫Date : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n║▫Time [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╠════════════\n║『Status in maintained』\n╚════════════")
                                  del bot_run['setTime'][msg.to]
                                  del bot_run['setSider'][msg.to]
                                  del bot_run['setWicked'][msg.to]
                              except:
                                  pass
                              bot_run['setTime'][msg.to] = msg.id
                              bot_run['setSider'][msg.to] = ""
                              bot_run['setWicked'][msg.to]=True

                        elif cmd == "sider off" or cmd == 'cctv off':
                          if run["finbot"] == True:
                           if sender in Master:
                              if msg.to in bot_run['setTime']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  bot_run['setWicked'][msg.to]=False
                                  _Chat(to, "╔════════════\n║▫Date : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n║▫Time [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╠════════════\n║『Status dissable』\n╚════════════")
                              else:
                                  _Chat(to, "Not sett")
#==========================[/TEXTTOSPEEC/FIN]===========================
                        elif cmd.startswith("say-"):
                          if sender in Master or sender in admin:
                             sep = text.split("-")
                             sep = sep[1].split(" ")
                             lang = sep[0]
                             say = text.replace("say-" + lang + " ","")
                             if lang not in bot_run["wlist_textToSpeech"]:
                             	return _Chat(to, "Language not found")
                             tts = gTTS(text=say, lang=lang)
                             tts.save("tts.mp3")
                             kang.sendAudio(to,"tts.mp3")
#==========================[TRANSLATOR/FIN]===========================
                        elif cmd.startswith("tr-"):
                          if sender in Master or sender in admin:
                             sep = text.split("-")
                             sep = sep[1].split(" ")
                             lang = sep[0]
                             say = text.replace("tr-" + lang + " ","")
                             if lang not in bot_run["wlist_translate"]:
                             	return _Chat(to, "Language not found")
                             translator = Translator()
                             hasil = translator.translate(say, dest=lang)
                             A = hasil.text
                             _Chat(to, str(A))

                        elif cmd.startswith('gn '):
                          if sender in Master:
                              X = kang.getGroup(msg.to)
                              X.name = msg.text.replace('gn ',"")
                              kang.updateGroup(X)

                        elif cmd.startswith('gc '):
                          if sender in Master:
                              try:
                                  key = eval(msg.contentMetadata["MENTION"])
                                  u = key["MENTIONEES"][0]["M"]
                                  cname = kang.getContact(u).displayName
                                  cmid = kang.getContact(u).mid
                                  cstatus = kang.getContact(u).statusMessage
                                  cpic = kang.getContact(u).picturePath
                                  #print(str(a))
                                  _Chat(receiver, 'Nama : '+cname+'\nMID : '+cmid+'\nStatus Msg : '+cstatus+'\nPicture : http://dl.profile.line.naver.jp'+cpic)
                                  _Chat(receiver, None, contentMetadata={'mid': cmid}, contentType=13)
                                  if "videoProfile='{" in str(kang.getContact(u)):
                                      kang.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                  else:
                                      kang.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic)
                              except Exception as e:
                                  _Chat(receiver, str(e))

                        elif cmd.startswith("searchmusic "):
                          if sender in Master or sender in admin:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                key = bot_run["keyCommand"]
                                setKey = key.title()
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ ʀᴇsᴜʟᴛ ᴍᴜsɪᴄ ]"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n╠ {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴍᴜsɪᴄ ] ".format(str(len(data["result"])))
                                    ret_ += "\n\nᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴇᴛᴀɪʟs ᴍᴜsɪᴄ, sɪʟᴀʜᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ {}sᴇᴀʀᴄʜᴍᴜsɪᴄ {}|「ɴᴜᴍʙᴇʀ」".format(str(setKey), str(search))
                                    _Chat(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "╔══════[ ᴍᴜsɪᴄ ]"
                                            ret_ += "\n╠❐ ᴛɪᴛʟᴇ : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n╠❐ ᴀʟʙᴜᴍ : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n╠❐ sɪᴢᴇ : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n╠❐ ʟɪɴᴋ :  {}".format(str(data["result"]["mp3"][0]))
                                            ret_ += "\n╚[ 『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』]"
                                            kang.sendImageWithURL(to, str(data["result"]["img"]))
                                            _Chat(to, str(ret_))
                                            kang.sendAudioWithURL(to, str(data["result"]["mp3"][0]))

                        elif cmd.startswith("searchlyric "):
                          if sender in Master or sender in admin:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                key = bot_run["keyCommand"]
                                setKey = key.title()
                                cond = query.split("|")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ ʀᴇsᴜʟᴛ ʟʏʀɪᴄ ]"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n╠❐ {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴍᴜsɪᴄ ]".format(str(len(data["results"])))
                                    ret_ += "\n\nᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴇᴛᴀɪʟs ʟʏʀɪᴄ, sɪʟᴀʜᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ {}sᴇᴀʀᴄʜʟʏʀɪᴄ {}|「ɴᴜᴍʙᴇʀ」".format(str(setKey), str(search))
                                    _Chat(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                        _Chat(to, str(lyric))

                        elif cmd.startswith("checkdate: "):
                          if sender in Master or sender in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            _Chat(to,"♐ I N F O R M A T I O N♐\n\n"+"♐ Date Of Birth : "+lahir+"\n♐ Age : "+usia+"\n♐ Birth Day: "+ultah+"\n♐ Zodiak : "+zodiak)

                        elif cmd.startswith("primbonnama "):
                            sep = text.split(" ")
                            nama = text.replace(sep[0] + " ","")
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0'
                                r = s.get("http://primbon.com/arti_nama.php?nama1={}&proses=+Submit%21+".format(urllib.parse.quote(nama)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                for primbon in soup.findAll('div', attrs={'id':'body'}):
                                    data = primbon.get_text()
                                    rep = data.replace('ARTI','<b>ARTI')
                                    res = rep.replace('< Hitung Kembali','</b>')
                                    data1 = BeautifulSoup(res, 'html5lib')
                                    for content in data1:
                                        ret_ = content.b.string
                                        _Chat(to, ret_)

                        elif cmd.startswith("get-mimpi "):
                          if sender in Master or sender in admin:
                            sep = msg.text.split(" ")
                            mimpi = msg.text.replace(sep[0] + " ","")  
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0'
                                r = s.get("http://primbon.com/tafsir_mimpi.php?mimpi={}&submit=+Submit+".format(urllib.parse.quote(mimpi)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                for anu in soup.find_all('i'):
                                    ret_ = anu.get_text()
                                    _Chat(to,ret_)

                        elif cmd.startswith("get-bintang "):
                          if sender in Master or sender in admin:
                            sep = msg.text.split(" ")
                            url = msg.text.replace(sep[0] + " ","")    
                            with requests.session() as s:
                                s.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                r = s.get("https://www.vemale.com/zodiak/{}".format(urllib.parse.quote(url)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                ret_ = ""
                                for a in soup.select('div.vml-zodiak-detail'):
                                    ret_ += a.h1.string
                                    ret_ += "\n"+ a.h4.string
                                    ret_ += " : "+ a.span.string +""
                                for b in soup.select('div.col-center'):
                                    ret_ += "\nTanggal : "+ b.string
                                for d in soup.select('div.number-zodiak'):
                                    ret_ += "\nAngka keberuntungan : "+ d.string
                                for c in soup.select('div.paragraph-left'):
                                    ta = c.text
                                    tab = ta.replace("    ", "")
                                    tabs = tab.replace(".", ".\n")
                                    ret_ += "\n"+ tabs
                                    #print (ret_)
                                _Chat(to, str(ret_))

                        elif cmd.startswith("get-apk "):
                          if sender in Master or sender in admin:
                            sep = msg.text.split(" ")
                            query = msg.text.replace(sep[0] + " ","")
                            cond = query.split("|")
                            search = str(cond[0])
                            with requests.session() as s:
                                s.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                r = s.get("https://apkpure.com/id/search?q={}".format(str(search)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                data = soup.findAll('dl', attrs={'class':'search-dl'})
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "「 Pencarian Aplikasi 」\n"
                                    for apk in data:
                                        num += 1
                                        link = "https://apkpure.com"+apk.find('a')['href']
                                        title = apk.find('a')['title']
                                        ret_ += "\n {}. {}".format(str(num), str(title))
                                    ret_ += "\n\n Total {} Result".format(str(len(data)))
                                    ret = "Selanjutnya ketik:\nGet-apk {} | angka".format(str(search))
                                    _Chat(to, str(ret_))
                                    _Chat(to, str(ret))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data):
                                        apk = data[num - 1]
                                        with requests.session() as s:
                                            s.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                            r = s.get("https://apkpure.com{}/download?from=details".format(str(apk.find('a')['href'])))
                                            soup = BeautifulSoup(r.content, 'html5lib')
                                            data = soup.findAll('div', attrs={'class':'fast-download-box'})
                                            for down in data:
                                                load = down.select("a[href*=https://download.apkpure.com/]")[0]
                                                file = load['href']
                                                ret_ = "File info :\n"+down.find('span', attrs={'class':'file'}).text
                                                with requests.session() as web:
                                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                                    r = web.get("https://api-ssl.bitly.com/v3/shorten?access_token=497e74afd44780116ed281ea35c7317285694bf1&longUrl={}".format(urllib.parse.quote(file)))
                                                    data = r.text
                                                    data = json.loads(data)
                                                    ret_ += "\nLink Download :\n"+data["data"]["url"]
                                                _Chat(to, str(ret_))

                        elif cmd.startswith("kode wilayah"):
                          if sender in Master or sender in admin:
                            ret_ = "「 Daftar Kode Wilayah 」\n\n"
                            ret_ += "248 = Alternatif - Cibubur\n119 = Ancol - bandara\n238 = Asia afrika - Bandung\n169 = Asia afrika - Hang lekir"
                            ret_ += "\n276 = Asia afrika - Sudirman\n295 = Bandengan - kota\n294 = Bandengan - Selatan\n255 = Boulevard Barat raya"
                            ret_ += "\n102 = Buncit raya\n272 = Bundaran - HI\n93 = Cideng barat\n289 = Cikini raya\n242 = Ciledug raya - Cipulir"
                            ret_ += "\n175 = Ciloto - Puncak\n142 = Daan mogot - Grogol\n143 = Daan mogot - Pesing\n338 = Dewi sartika - Cawang"
                            ret_ += "\n124 = DI Panjaitan - By pass\n123 = DI Panjaitan - Cawang\n13 = Dr Satrio - Casablanca\n105 = Dr Satrio - Karet"
                            ret_ += "\n245 = Dukuh atas - MRT Jakarta\n334 = Fachrudin raya\n252 = Fatmawati - Blok A\n253 = Fatmawati - Cipete raya"
                            ret_ += "\n203 = Flyover Daan mogot\n336 = Flyover Jati baru\n172 = Flyover Senen - Kramat\n77 = Gunung sahari"
                            ret_ += "\n137 = Hasyim Ashari\n273 = Jalan MH Thamrin\n327 = Jalan RS Fatmawati\n292 = Jl. Otista 3\n333 = Jl. Panjang - Kebon jeruk"
                            ret_ += "\n226 = JORR - Bintaro\n227 = JORR - Fatmawati\n173 = Kramat raya - Senen\n117 = Kyai Caringin - Cideng\n126 = Letjen Suprapto - Senen"
                            ret_ += "\n204 = Mangga besar\n319 = Margaguna raya\n326 = Margonda raya\n310 = Mas Mansyur - Karet\n309 = Mas Mansyur - Tn. Abang"
                            ret_ += "\n64 = Matraman\n140 = Matraman - Salemba\n284 = Metro Pdk. Indah\n191 = MT Haryono - Pancoran\n160 = Pancoran barat"
                            ret_ += "\n331 = Pejompongan - Slipi\n332 = Pejompongan - Sudirman\n312 = Perempatan pramuka\n171 = Permata hijau - Panjang\n99 = Petojo Harmoni"
                            ret_ += "\n223 = Pramuka - Matraman\n222 = Pramuka raya\n314 = Pramuka raya - jl. Tambak\n313 = Pramuka - Salemba raya\n130 = Puncak raya KM84"
                            ret_ += "\n318 = Radio dalam raya\n328 = RS Fatmawati - TB\n274 = Senayan city\n132 = Slipi - Palmerah\n133 = Slipi - Tomang"
                            ret_ += "\n162 = S Parman - Grogol\n324 = Sudirman - Blok M\n18 = Sudirman - Dukuh atas\n325 = Sudirman - Semanggi\n112 = Sudirman - Setiabudi"
                            ret_ += "\n246 = Sudirman - Thamrin\n320 = Sultan agung - Sudirman\n100 = Suryo pranoto\n220 = Tanjung duren\n301 = Tol kebon jeruk"
                            ret_ += "\n41 = Tomang/Simpang\n159 = Tugu Pancoran\n145 = Warung jati - Pejaten\n205 = Yos Sudarso - Cawang\n206 = Yos Sudarso - Tj. Priuk"
                            ret_ += "\n\nUntuk melihat cctv,\nKetik lihat (kode wilayah)"                            
                            _Chat(to, ret_)

                        elif cmd.startswith("lihat "):
                          if sender in Master or sender in admin:
                            sep = msg.text.split(" ")
                            cct = msg.text.replace(sep[0] + " ","")
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
                                r = s.get("http://lewatmana.com/cam/{}/bundaran-hi/".format(urllib.parse.quote(cct)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                try:
                                    ret_ = "「 Informasi CCTV 」\nDaerah "
                                    ret_ += soup.select("[class~=cam-viewer-title]")[0].text
                                    ret_ += "\nCctv update per 5 menit"
                                    vid = soup.find('source')['src']
                                    ret = "Untuk melihat wilayah lainnya, Ketik kode wilayah"
                                    _Chat(to, ret_)
                                    kang.sendVideoWithURL(to, vid)
                                    _Chat(to, ret)
                                except:
                                    getMention(to, "Data cctv tidak ditemukan!\n@!", [sender])

                        elif cmd.startswith("search-image: "):
                          if sender in Master or sender in admin:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            with requests.session() as web:
                            	web.headers["User-Agent"] = random.choice(bot_run["userAgent"])
                            r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                            data = r.text
                            data = json.loads(data)
                            if data["result"] != []:
                            	items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            kang.sendImageWithURL(to, str(path))

                        elif cmd.startswith("search-youtube: "):
                          if sender in Master or sender in admin:
                            sep = msg.text.split(" ")
                            params = msg.text.replace(sep[0] + " ","")
                            with requests.session() as web:
                            	web.headers["User-Agent"] = random.choice(bot_run["userAgent"])
                            r = web.get("https://www.youtube.com/results", params = params)
                            soup = BeautifulSoup(r.content, "html5lib")
                            ret_ = "╔══[ Youtube Result ]"
                            datas = []
                            for data in soup.select(".yt-lockup-title > a[title]"):
                            	if "&lists" not in data["href"]:
                            	     datas.append(data)
                            for data in datas:
                            	ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                            ret_ += "\n╚══[ Total {} ]".format(len(datas))
                            _Chat(to, str(ret_))

                        elif cmd.startswith("ytmp4: "):
                          if sender in Master or sender in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n♐ Author : ' + str(vid.author)
                                    durasi = '\n♐ Duration : ' + str(vid.duration)
                                    suka = '\n♐ Likes : ' + str(vid.likes)
                                    rating = '\n♐ Rating : ' + str(vid.rating)
                                    deskripsi = '\n♐ Deskripsi : ' + str(vid.description)
                                kang.sendVideoWithURL(msg.to, me)
                                _Chat(to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                getMention(to,"Failure @!",[sender])

                        elif cmd.startswith("ytmp3: "):
                          if sender in Master or sender in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n♐ Author : ' + str(vid.author)
                                    durasi = '\n♐ Duration : ' + str(vid.duration)
                                    suka = '\n♐ Likes : ' + str(vid.likes)
                                    rating = '\n♐ Rating : ' + str(vid.rating)
                                    deskripsi = '\n♐ Description : ' + str(vid.description)
                                kang.sendImageWithURL(msg.to, me)
                                kang.sendAudioWithURL(msg.to, shi)
                                _Chat(to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                getMention(to,"Failure @!",[sender])

                        elif cmd.startswith("video "):
                          if sender in Master or sender in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                url = "https://www.youtube.com/results?search_query=" + query
                                response = urllib.request.urlopen(url)
                                html = response.read()
                                soup = BeautifulSoup(html, "html.parser")
                                results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                dl = 'https://www.youtube.com' + results['href']
                                start = timeit.timeit()
                                vid = pafy.new(dl)
                                stream = vid.streams
                                for s in stream:
                                    vin = s.url
                                    hasil = vid.title
                                    hasil += '\n\nAuthorized : ' +str(vid.author)
                                    hasil += '\nDuration   : ' +str(vid.duration)+ ' (' +s.quality+ ') '
                                    hasil += '\nRating   : ' +str(vid.rating)
                                    hasil += '\nWatched    : ' +str(vid.viewcount)+ 'x '
                                    hasil += '\nPublished : ' +vid.published
                                    hasil += '\n\nTime taken : %s' % (start)
                                    hasil += '\n\n Wait for encoding...'
                                kang.sendVideoWithURL(msg.to,vin)
                                _Chatt(to,hasil)
                            except:
                                getMention(to,"Failure @!",[sender])

                        elif cmd.startswith("urban "):
                          if sender in Master or sender in admin:
                            sep = msg.text.split(" ")
                            judul = msg.text.replace(sep[0] + " ","")
                            url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                            with requests.session() as s:
                                s.headers["User-Agent"] = random.choice(bot_run["userAgent"])
                                r = s.get(url)
                                data = r.text
                                data = json.loads(data)
                                y = "[ Result Urban ]"
                                y += "\nTags: "+ data["tags"][0]
                                y += ","+ data["tags"][1]
                                y += ","+ data["tags"][2]
                                y += ","+ data["tags"][3]
                                y += ","+ data["tags"][4]
                                y += ","+ data["tags"][5]
                                y += ","+ data["tags"][6]
                                y += ","+ data["tags"][7]
                                y += "\n[1]\nAuthor: "+str(data["list"][0]["author"])
                                y += "\nWord: "+str(data["list"][0]["word"])
                                y += "\nLink: "+str(data["list"][0]["permalink"])
                                y += "\nDefinition: "+str(data["list"][0]["definition"])
                                y += "\nExample: "+str(data["list"][0]["example"])
                                _Chat(to, str(y))

                        elif cmd.startswith("checkdate: "):
                          if sender in Master or sender in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            _Chat(to,"♐ I N F O R M A T I O N♐\n\n"+"♐ Date Of Birth : "+lahir+"\n♐ Age : "+usia+"\n♐ Date of birth : "+ultah+"\n♐ Zodiak : "+zodiak)

                        elif cmd == "bokep":
                          if sender in Master or sender in admin:
                            _Chat(msg.to,"nekopoi.host")
                            _Chat(msg.to,"sexvideobokep.com")
                            _Chat(msg.to,"memek.com")
                            _Chat(msg.to,"pornktube.com")
                            _Chat(msg.to,"faketaxi.com")
                            _Chat(msg.to,"videojorok.com")
                            _Chat(msg.to,"watchmygf.mobi")
                            _Chat(msg.to,"xnxx.com")
                            _Chat(msg.to,"pornhd.com")
                            _Chat(msg.to,"xvideos.com")
                            _Chat(msg.to,"vidz7.com")
                            _Chat(msg.to,"m.xhamster.com")
                            _Chat(msg.to,"xxmovies.pro")
                            _Chat(msg.to,"youporn.com")
                            _Chat(msg.to,"pornhub.com")
                            _Chat(msg.to,"anyporn.com")
                            _Chat(msg.to,"hdsexdino.com")
                            _Chat(msg.to,"rubyourdick.com")
                            _Chat(msg.to,"anybunny.mobi")
                            _Chat(msg.to,"cliphunter.com")
                            _Chat(msg.to,"sexloving.net")
                            _Chat(msg.to,"free.goshow.tv")
                            _Chat(msg.to,"eporner.com")
                            _Chat(msg.to,"Pornhd.josex.net")
                            _Chat(msg.to,"m.hqporner.com")
                            _Chat(msg.to,"m.spankbang.com")
                            _Chat(msg.to,"m.4tube.com")
                            _Chat(msg.to,"brazzers.com")

                        elif cmd.startswith("spamtag "):
                          if run["finbot"] == True:
                           if sender in Master or sender in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    jmlh = int(bot_run["limitTag"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                _Chat(to,zxc,contentMetadata = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')},contentType = 0)
                                            except Exception as e:
                                                _Chat(to,str(e))
                                    else:
                                        _Chat(to,"Total limited 1000")

                        elif cmd.startswith("hii "):
                          if run["finbot"] == True:
                           if sender in Master or sender in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    jmlh = int(bot_run["limitTag"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                _Chat(to,zxc,contentMetadata = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')},contentType = 0)
                                            except Exception as e:
                                                _Chat(to,str(e))
                                    else:
                                        _Chat(to,"Total Limited 1000")

                        elif cmd == "spamcall" or cmd == 'naik':
                          if run["finbot"] == True:
                           if sender in Master or sender in admin:
                             if msg.toType == 2:
                                group = kang.getGroup(msg.to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(bot_run["limitCall"])
                                _Chat(to, "{} Call Reissued".format(str(bot_run["limitCall"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        kang.acquireGroupCallRoute(msg.to)
                                        kang.inviteIntoGroupCall(msg.to, contactIds=members)
                                     except Exception as e:
                                        _Chat(to,str(e))
                                else:
                                    _Chat(to,"Limited list")

                        elif cmd.startswith('get-idline: '):
                          if run["finbot"] == True:
                           if sender in Master:
                              msgs = msg.text.replace('.get-idline: ','')
                              conn = kang.findContactsByUserid(msgs)
                              if True:
                                  _Chat(to, "http://line.me/ti/p/~" + msgs)
                                  _Chat(to, None, contentMetadata={'mid': conn.mid}, contentType=13)

                        elif cmd.startswith("idline "):
                          if sender in Master:
                            sep = text.split(" ")
                            user = text.replace(sep[0] + " ","")
                            conn = kang.findContactsByUserid(user)
                            try:
                                anu = conn.mid
                                dn = conn.displayName
                                bio = conn.statusMessage
                                sendMention(to, anu, "「 Contact Line ID 」\n• Nama : ", "\n• Nick : "+dn+"\n• Bio : "+bio+"\n• Contact link : http://line.me/ti/p/~"+user)
                                kang.sendContact(to, anu)
                            except Exception as e:
                                _Chat(to, str(e))

                        elif cmd.startswith("saveimg "):
                          if sender in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in images:
                                bot_run["Addimage"]["status"] = True
                                bot_run["Addimage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                getMention(to, "Silahkan kirim fotonya...",[sender])
                            else:
                                getMention(to, "Foto sudah termasuk dalam daftar... @!",[sender])
                                
                        elif cmd.startswith("rmimg "):
                          if sender in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in images:
                                kang.deleteFile(images[str(name.lower())])
                                del images[str(name.lower())]
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                _Chat(to, "Berhasil menghapus {}".format( str(name.lower())))
                            else:
                                getMention(to, "Foto itu tidak ada dalam daftar.. @!",[sender])
                                 
                        elif cmd == "listimg":
                           if sender in Master:
                             no = 0
                             ret_ = "[ Daftar Image ]\n\n"
                             for image in images:
                                 no += 1
                                 ret_ += str(no) + ". " + image.title() + "\n"
                             ret_ += "\nTotal [ {} ] Images".format(str(len(images)))
                             _Chat(to, ret_)

                        elif cmd.startswith("addvideo "):
                          if sender in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in videos:
                                bot_run["Addvideo"]["status"] = True
                                bot_run["Addvideo"]["name"] = str(name.lower())
                                videos[str(name.lower())] = ""
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                getMention(to, "Silahkan kirim videonya... @!",[sender])
                            else:
                                getMention(to, "Video itu sudah tersimpan dalam daftar @!",[sender])
                                
                        elif cmd.startswith("dellvideo "):
                          if sender in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in videos:
                                kang.deleteFile(videos[str(name.lower())])
                                del videos[str(name.lower())]
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                _Chat(to, "Video deleted {}".format( str(name.lower())))
                            else:
                                getMention(to, "No list video... @!",[sender])
                                 
                        elif cmd == "listvideo":
                           if sender in Master:
                             no = 0
                             ret_ = "[ Daftar Video ]\n\n"
                             for video in videos:
                                 no += 1
                                 ret_ += str(no) + ". " + video.title() + "\n"
                             ret_ += "\nTotal [ {} ]Videos".format(str(len(videos)))
                             _Chat(to, ret_)
                             getMention(to,"\nEx play video\nType in video title or  name of the video you previously sett @!",[sender])

                        elif cmd.startswith("addmp3 "):
                          if sender in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in audios:
                                bot_run["Addaudio"]["status"] = True
                                bot_run["Addaudio"]["name"] = str(name.lower())
                                audios[str(name.lower())] = ""
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                getMention(to, "Send Mp3... @!",[sender])
                            else:
                                getMention(to, "Mp3 already exists @!",[sender])
                                
                        elif cmd.startswith("dellmp3 "):
                          if sender in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in audios:
                                kang.deleteFile(audios[str(name.lower())])
                                del audios[str(name.lower())]
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                _Chat(to, "Mp3 deleted {}".format( str(name.lower())))
                            else:
                                getMention(to, "No list @!",[sender])
                                 
                        elif cmd == "listmp3":
                           if sender in Master:
                             no = 0
                             ret_ = "[ Daftar Lagu ]\n\n"
                             for audio in audios:
                                 no += 1
                                 ret_ += str(no) + ". " + audio.title() + "\n"
                             ret_ += "\nTotal [ {} ]Lagu".format(str(len(audios)))
                             _Chat(to, ret_)
                             getMention(to,"Ex play music\nType in song title or name of the song you previously sett\n@!",[sender])
                       
                        elif cmd.startswith("addsticker "):
                          if sender in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in stickers:
                                bot_run["Addsticker"]["status"] = True
                                bot_run["Addsticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = ""
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                getMention(to, "Send sticker...  @!",[sender])
                            else:
                                getMention(to, "Sticker already exists @!",[sender])
                                
                        elif cmd.startswith("dellsticker "):
                          if sender in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in stickers:
                                del stickers[str(name.lower())]
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                _Chat(to, "Sticker deleted {}".format( str(name.lower())))
                            else:
                                getMention(to, "No Sticker list@!",[sender])
                                 
                        elif text.lower() == "liststicker":
                           if sender in Master:
                             no = 0
                             ret_ = "Sticker List\n\n"
                             for sticker in stickers:
                                 no += 1
                                 ret_ += str(no) + ". " + sticker.title() + "\n"
                             ret_ += "\nTotal [ {} ] Stickers".format(str(len(stickers)))
                             _Chat(to, ret_)

                        elif ("Mek " in msg.text):
                          if run["finbot"] == True:
                            if sender in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in bot_run["assist"]:
                                       try:
                                           G = kang.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           kang.updateGroup(G)
                                           invsend = 0
                                           Ticket = kang.reissueGroupTicket(msg.to)
                                           k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           k1.kickoutFromGroup(msg.to, [target])
                                           X = k2.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           k2.updateGroup(X)
                                           k1.leaveGroup(msg.to)
                                           k2.leaveGroup(msg.to)
                                       except:
                                           pass

                        elif ("hai " in msg.text):
                          if run["finbot"] == True:
                            if sender in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in bot_run["assist"]:
                                       try:
                                           G = kang.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           kang.updateGroup(G)
                                           invsend = 0
                                           Ticket = kang.reissueGroupTicket(msg.to)
                                           k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           k1.kickoutFromGroup(msg.to, [target])
                                           k1.leaveGroup(msg.to)
                                           X = kang.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           kang.updateGroup(X)
                                       except:
                                           pass

                        elif ("Dam " in msg.text):
                          if run["finbot"] == True:
                            if sender in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in bot_run["assist"]:
                                       try:
                                           _Random.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif cmd == "contact:on" or cmd == 'k on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["contact"] = True
                                bot_run["checkPost"] = False
                                bot_run["addContact"] = False
                                getMention(to,"Contact detection enable @!",[sender])

                        elif cmd == "contact:off" or cmd == 'k off':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["contact"] = False
                                getMention(to,"Contact detection dissable @!",[sender])


                        elif cmd == "bot add": 
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["botAdd"] = True
                                bot_run["bot1Add"] = False
                                bot_run["bot2Add"] = False
                                bot_run["bot3Add"] = False
                                bot_run["bot4Add"] = False
                                bot_run["bot5Add"] = False
                                bot_run["kickerAdd"] = False
                                getMention(to,"Send contact target @!",[sender])

                        elif cmd == "bot1 add": 
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["botAdd"] = False
                                bot_run["bot1Add"] = True
                                bot_run["bot2Add"] = False
                                bot_run["bot3Add"] = False
                                bot_run["bot4Add"] = False
                                bot_run["bot5Add"] = False
                                bot_run["kickerAdd"] = False
                                getMention1(to,"Send contact target @!",[sender])

                        elif cmd == "bot2 add": 
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["botAdd"] = False
                                bot_run["bot1Add"] = False
                                bot_run["bot2Add"] = True
                                bot_run["bot3Add"] = False
                                bot_run["bot4Add"] = False
                                bot_run["bot5Add"] = False
                                bot_run["kickerAdd"] = False
                                getMention2(to,"Send contact target @!",[sender])

                        elif cmd == "bot3 add": 
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["botAdd"] = False
                                bot_run["bot1Add"] = False
                                bot_run["bot2Add"] = False
                                bot_run["bot3Add"] = True
                                bot_run["bot4Add"] = False
                                bot_run["bot5Add"] = False
                                bot_run["kickerAdd"] = False
                                getMention3(to,"Send contact target @!",[sender])

                        elif cmd == "bot4 add": 
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["botAdd"] = False
                                bot_run["bot1Add"] = False
                                bot_run["bot2Add"] = False
                                bot_run["bot3Add"] = False
                                bot_run["bot4Add"] = True
                                bot_run["bot5Add"] = False
                                bot_run["kickerAdd"] = False
                                getMention4(to,"Send contact target @!",[sender])

                        elif cmd == "bot5 add": 
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["botAdd"] = False
                                bot_run["bot1Add"] = False
                                bot_run["bot2Add"] = False
                                bot_run["bot3Add"] = False
                                bot_run["bot4Add"] = False
                                bot_run["bot5Add"] = True
                                bot_run["kickerAdd"] = False
                                getMention5(to,"Send contact target @!",[sender])

                        elif cmd == "kicker add": 
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["botAdd"] = False
                                bot_run["bot1Add"] = False
                                bot_run["bot2Add"] = False
                                bot_run["bot3Add"] = False
                                bot_run["bot4Add"] = False
                                bot_run["bot5Add"] = False
                                bot_run["kickerAdd"] = True
                                getMention(to,"Send contact target @!",[sender])

                        elif cmd == "checkpost:on" or cmd == 'timeline on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["checkPost"] = True
                                bot_run["contact"] = False
                                bot_run["addContact"] = False
                                getMention(to,"Check post enable @!",[sender])

                        elif cmd == "checkpost:off" or cmd == 'post:off':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["checkPost"] = False
                                getMention(to,"Check post dissable @!",[sender])

                        elif cmd == "add contact:on" or text.lower() == 'add cont on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["addContact"] = True
                                bot_run["contact"] = False
                                bot_run["checkPost"] = False
                                getMention(msg.to,"Send contact Target @!",[sender])

                        elif cmd == "respon:on" or cmd == 'auto respon on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["detectMention"] = True
                                bot_run["detectMention1"] = False
                                getMention(to,"『 Auto respon enable 』\n@!", [sender])

                        elif cmd == "respon:off" or cmd == 'auto respon off':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["detectMention"] = False
                                getMention(to,"『 Auto respon dissable 』\n@!", [sender])

                        elif cmd == "respon1:on" or cmd == 'auto rsp1 on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["detectMention1"] = True
                                bot_run["detectMention"] = False
                                getMention(to,"『 Auto respon1 enable 』\n@!", [sender])

                        elif cmd == "respon1:off" or cmd == 'auto rsp1 off':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["detectMention1"] = False
                                getMention(to,"Auto respon1 dissable\n@!", [sender])

                        elif cmd == "autojoin on" or cmd == 'join on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["autoJoin"] = True
                                getMention(to,"『 Auto join enable 』\n@!", [sender])

                        elif cmd == "autojoin off" or cmd == 'join off':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["autoJoin"] = False
                                getMention(to,"『 Auto Join dissable 』\n@!", [sender])

                        elif cmd == "autoleave on" or cmd == 'leave on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["autoLeave"] = True
                                getMention(to,"Auto leave enable\n@!", [sender])

                        elif cmd == "autoleave off" or cmd == 'leave off':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["autoLeave"] = False
                                getMention(to,"Auto leave dissable\n@!", [sender])

                        elif cmd == "autoadd on" or cmd == 'add on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["autoAdd"] = True
                                getMention(to,"Auto add enable\n@!", [sender])

                        elif cmd == "autoadd off" or cmd == 'add off':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["autoAdd"] = False
                                getMention(to,"Auto add dissable\n@!", [sender])

                        elif cmd == "jointicket on" or cmd == 'ticket on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["Auto_Join_Ticket"] = True
                                getMention(to,"Auto Join Ticket enable\n@!", [sender])

                        elif cmd == "jointicket off" or cmd == 'ticket off':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["Auto_Join_Ticket"] = False
                                getMention(to,"Auto Join Ticket dissable\n@!", [sender])

                        elif cmd == "talkban add:on" or text.lower() == 'talkban:on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["Talkwblacklist"] = True
                                bot_run["Talkdblacklist"] = False
                                getMention(to,"Send contact Target @!", [sender])

                        elif cmd == "talkban dell:on" or text.lower() == 'untalkban:on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["Talkdblacklist"] = True
                                bot_run["Talkwblacklist"] = False
                                getMention(to,"Send contact Target @!", [sender])

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                bot_run["wblacklist"] = True
                                bot_run["dblacklist"] = False
                                getMention(to,"Send contact Target @!", [sender])

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                bot_run["dblacklist"] = True
                                bot_run["wblacklist"] = False
                                getMention(to,"Send contact Target @!", [sender])

                        elif cmd == "add admin:on" or text.lower() == 'add admin on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["addAdmin"] = True
                                bot_run["delAdmin"] = False
                                getMention(msg.to,"Send contact Target @!",[sender])

                        elif cmd == "del admin:on" or text.lower() == 'delete admin on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["delAdmin"] = True
                                bot_run["addAdmin"] = False
                                getMention(msg.to,"Send contact Target @!",[sender])

                        elif cmd == "invite on" or cmd == 'inv mem':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["invite"] = True
                                bot_run["invite1"] = False
                                bot_run["invite2"] = False
                                bot_run["invite3"] = False
                                bot_run["invite4"] = False
                                bot_run["invite5"] = False
                                getMention(to,"Send contact Target\n@!", [sender])

                        elif cmd == "f1invite on" or cmd == 'f1inv':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["invite"] = False
                                bot_run["invite1"] = True
                                bot_run["invite2"] = False
                                bot_run["invite3"] = False
                                bot_run["invite4"] = False
                                bot_run["invite5"] = False
                                getMention1(to,"Send contact Target\n@!", [sender])

                        elif cmd == "f2invite on" or cmd == 'f2inv':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["invite"] = False
                                bot_run["invite1"] = False
                                bot_run["invite2"] = True
                                bot_run["invite3"] = False
                                bot_run["invite4"] = False
                                bot_run["invite5"] = False
                                getMention2(to,"Send contact Target\n@!", [sender])

                        elif cmd == "f3invite on" or cmd == 'f3inv':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["invite"] = False
                                bot_run["invite1"] = False
                                bot_run["invite2"] = False
                                bot_run["invite3"] = True
                                bot_run["invite4"] = False
                                bot_run["invite5"] = False
                                getMention3(to,"Send contact Target\n@!", [sender])

                        elif cmd == "f4invite on" or cmd == 'f4inv':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["invite"] = False
                                bot_run["invite1"] = False
                                bot_run["invite2"] = False
                                bot_run["invite3"] = False
                                bot_run["invite4"] = True
                                bot_run["invite5"] = False
                                getMention4(to,"Send contact Target\n@!", [sender])

                        elif cmd == "f5invite on" or cmd == 'f5inv':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["invite"] = False
                                bot_run["invite1"] = False
                                bot_run["invite2"] = False
                                bot_run["invite3"] = False
                                bot_run["invite4"] = False
                                bot_run["invite5"] = True
                                getMention5(to,"Send contact Target\n@!", [sender])

                        elif cmd == "read on" or cmd == 'rd on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["AutoRead"] = True
                                bot_run["scanner"] = False
                                getMention(to,"Auto read Message enable\n@!", [sender])

                        elif cmd == "read off" or cmd == 'rd off':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["AutoRead"] = False
                                getMention(to,"Read Message dissable\n@!", [sender])

                        elif cmd == "nyusup on" or cmd == 'nsp on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["nyusup"] = True
                                getMention(to,"Spyer enable\n@!", [sender])

                        elif cmd == "nyusup off" or cmd == 'nsp off':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["nyusup"] = False
                                getMention(to,"Spyer dissable\n@!", [sender])

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["stickerOn"] = True
                                getMention(to,"Detecting sticker\n@!", [sender])

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["stickerOn"] = False
                                getMention(to,"Auto Detect stick dissable\n@!", [sender])

                        elif cmd == "qr on" or text.lower() == 'proqr on':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                bot_run["Pro_Qr"][msg.to] = True
                                getMention(to,"Protecting Group QR\n@!", [sender])

                        elif cmd == "qr off" or text.lower() == 'proqr off':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                del bot_run["Pro_Qr"][msg.to]
                                getMention(to,"QR Unprotected\n@!", [sender])

                        elif cmd == "cancel on" or text.lower() == 'procancel on':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                bot_run["Pro_Cancel"][msg.to] = True
                                getMention(to,"Protecting Canceler\n@!", [sender])

                        elif cmd == "cancel off" or text.lower() == 'procancel off':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                del bot_run["Pro_Cancel"][msg.to]
                                getMention(to,"Protect cancel dissable \n@!", [sender])

                        elif cmd == "inv on" or text.lower() == 'proinv on':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                bot_run["Pro_Invite"][msg.to] = True
                                getMention(to,"Block Inv enable\n@!", [sender])

                        elif cmd == "inv off" or text.lower() == 'proinv off':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                del bot_run["Pro_Invite"][msg.to]
                                getMention(to,"Auto Block inv dissable\n@!", [sender])

                        elif cmd == "m on" or text.lower() == 'promem on':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                bot_run["Pro_Member"][msg.to] = True
                                getMention(to,"Member Protected\n@!", [sender])

                        elif cmd == "m off" or text.lower() == 'promem off':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                del bot_run["Pro_Member"][msg.to]
                                getMention(to,"Member Unprotected\n@!", [sender])

                        elif cmd == "lock gname" or cmd == 'lgn':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                bot_run['pname'][msg.to] = True
                                bot_run['pro_name'][msg.to] = kang.getGroup(msg.to).name
                                getMention(to,"Group name protected\n@!", [sender])

                        elif cmd == "unlock gname" or cmd == 'ugn':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                del bot_run['pname'][msg.to]
                                getMention(to,"Group name unprotected\n@!", [sender])

                        elif cmd == "tagkick on" or cmd == 'notag on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["Mentionkick"] = True
                                getMention(to,"Auto kick Mention enable\n@!", [sender])

                        elif cmd == "tagkick off" or cmd == 'notag off':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["MentionKick"] = False
                                getMention(to,"Auto Kick Mention dissable\n@!", [sender])

                        elif cmd == "block:on" or cmd == 'block on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["autoBlock"] = True
                                getMention(to,"Auto Block enable\n@!", [sender])

                        elif cmd == "block:off" or cmd == 'block off':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["autoBlock"] = False
                                getMention(to,"Auto Block dissable\n@!", [sender])

                        elif cmd == "msg:on" or cmd == 'unsend on':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                bot_run["unsendMessage"] = True
                                bot_run["scanner"] = True
                                bot_run["AutoRead"] = False
                                bot_run['scanPoint'][msg.to] = msg_id
                                bot_run['scanROM'][msg.to] = {}
                                getMention(to,"UnsendMessage enable\n@!", [sender])

                        elif cmd == "msg:off" or cmd == 'unsend off':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                bot_run["unsendMessage"] = False
                                bot_run["scanner"] = False
                                getMention(to,"UnsendMessage dissable\n@!", [sender])

                        elif cmd == "rpc on" or cmd == 'cpc on':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["ResponPc"] = True
                                bot_run["unsendMessage"] = False
                                bot_run["scanner"] = False
                                bot_run["AutoRead"] = False
                                getMention(to,"Auto respon PC enable\n@!", [sender])

                        elif cmd == "rpc off" or cmd == 'cpc off':
                          if run["finbot"] == True:
                            if sender in Master:
                                bot_run["ResponPc"] = False
                                getMention(to,"Auto respon PC dissable\n@!", [sender])

                        elif cmd == "welcome:on" or cmd == 'wc:on':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                bot_run["Welcome"][msg.to] = True
                                getMention(to,"Notif join enable\n@!", [sender])

                        elif cmd == "welcome:off" or cmd == 'wc:off':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                del bot_run["Welcome"][msg.to]
                                getMention(to,"Notif join dissable\n@!", [sender])

                        elif cmd == "refresh" or cmd == 'fresh':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                bot_run["unsendMessage"] = False
                                bot_run["scanner"] = False
                                bot_run["AutoRead"] = False
                                bot_run["Auto_Join_Ticket"] = False
                                bot_run["detectMention"] = False
                                bot_run["detectMention1"] = False
                                bot_run["MentionKick"] = False
                                bot_run["contact"] = False
                                getMention(to,"Refresh done\n@!", [sender])

                        elif cmd == "pro all on" or cmd == 'protect all on':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                bot_run["Pro_Qr"][msg.to] = True
                                bot_run["Pro_Invite"][msg.to] = True
                                bot_run["Pro_Cancel"][msg.to] = True
                                bot_run["Pro_Member"][msg.to] = True
                                bot_run["Pro_Join"][msg.to] = True
                                bot_run["pname"][msg.to] = True
                                getMention(to, "All pro on\n@!", [sender])

                        elif cmd == "pro all off" or cmd == 'protect all off':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                                getMention(to, "All pro off\n@!", [sender])
                                del bot_run["Pro_Qr"][msg.to]
                                del bot_run["Pro_Invite"][msg.to]
                                del bot_run["Pro_Cancel"][msg.to]
                                del bot_run["Pro_Member"][msg.to]
                                del bot_run["Pro_Join"][msg.to]
                                del bot_run["pname"][msg.to]

                        elif cmd == "dbn" or cmd == 'clearban':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                              bot_run["Blacklist_User"] = {}
                              ragets = kang.getContacts(bot_run["Blacklist_User"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              _Chat(to,"Removed" +mc)

                        elif cmd.startswith("autorestart: "):
                          if run["finbot"] == True:
                           if sender in Master:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                bot_run["timeRestart"] = num
                                _Chat(to,"🄵🄸🄽 🄱🄾🅃 \nAutorestart in:『" +strnum+" Seconds』Remaining time... ")

                        elif cmd.startswith("limiter: "):
                          if run["finbot"] == True:
                           if sender in Master:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                bot_run["limiter"]["members"] = num
                                _Chat(to,"Limit member switch to " +strnum)

                        elif cmd.startswith("spamtag: "):
                          if run["finbot"] == True:
                           if sender in Master:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                bot_run["limitTag"] = num
                                _Chat(to,"Total Spamtag switch to " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if run["finbot"] == True:
                           if sender in Master:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                bot_run["limitCall"] = num
                                _Chat(to,"Total Spamcall switch to " +strnum)

                        elif 'Set pesan: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('Set pesan: ',"")
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Something went wrong!")
                              else:
                                  bot_run["message"] = spl
                                  _Chat(to, "「PrivMsg」\nPriv Msg switch to:\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Replace failed")
                              else:
                                  bot_run["welcome"] = spl
                                  _Chat(to, "「Welcome Msg」\nWelcome Msg switch to:\n\n「{}」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Replace failed")
                              else:
                                  bot_run["Respontag"] = spl
                                  _Chat(to, "「Respon msg」\nRespon Msg switch to:\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Replace failed")
                              else:
                                  bot_run["message1"] = spl
                                  _Chat(to, "「Spam Msg」\nSpam Msg switch to:\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if sender in Master:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  _Chat(to, "Replace failed")
                              else:
                                  bot_run["mention"] = spl
                                  _Chat(to, "「Sider Msg」\nSider Msg switch to:\n\n「{}」".format(str(spl)))

                        elif cmd == "cek limit":
                            if sender in Master:
                               _Chat(to, "Total Limiter [ " + str(bot_run["limiter"]["members"]) + " ]" +"\n\nSpamtag limiter [ " + str(bot_run["limitTag"]) + " ]" + "\n\nSpamcall limiter [ " + str(bot_run["limitCall"]) + " ]" )

                        elif cmd == "cek pesan":
                            if sender in Master:
                               _Chat(to, "「Pesan Msg」\nPesan Msg:\n\n「 " + str(bot_run["message"]) + " 」")

                        elif cmd == "cek welcome":
                            if sender in Master:
                               _Chat(to, "「Welcome Msg」\nWelcome Msg:\n\n「 " + str(bot_run["welcome"]) + " 」")

                        elif cmd == "cek respon":
                            if sender in Master:
                               _Chat(to, "「Respon Msg」\nRespon Msg:\n\n「 " + str(bot_run["Respontag"]) + " 」")

                        elif cmd == "cek spam":
                            if sender in Master:
                               _Chat(to, "「Spam Msg」\nSpam Msg:\n\n「 " + str(bot_run["message1"]) + " 」")

                        elif cmd == "cek sider":
                            if sender in Master:
                               _Chat(to, "「Sider Msg」\nSider Msg:\n\n「 " + str(bot_run["mention"]) + " 」")

                        elif cmd == "cek autorestart":
                            if sender in Master:
                               _Chat(to, "「Autorestart」:\n\nIn remaining time:「 " + str(bot_run["timeRestart"]) + " /scnds」")

                        elif cmd == "my token":
                            if sender in Master:
                               _SendChat(to, "[ Here's your token ]\n" + str(run_bot["authToken"]))

                        elif cmd == "induk token":
                            if sender in Master:
                               _Chat(to, "[ Here's finbot token ]\n" + str(run_bot["kang"]))

                        elif cmd == "bot1 token":
                            if sender in Master:
                               _Chat1(to, "[ Here's bot1 token ]\n" + str(run_bot["fino1"]))

                        elif cmd == "bot2 token":
                            if sender in Master:
                               _Chat2(to, "[ Here's bot2 token ]\n" + str(run_bot["fino2"]))

                        elif cmd == "bot3 token":
                            if sender in Master:
                               _Chat3(to, "[ Here's bot3 token ]\n" + str(run_bot["fino3"]))

                        elif cmd == "bot4 token":
                            if sender in Master:
                               _Chat4(to, "[ Here's bot4 token ]\n" + str(run_bot["fino4"]))

                        elif cmd == "bot5 token":
                            if sender in Master:
                               _Chat5(to, "[ Here's bot5 token ]\n" + str(run_bot["fino5"]))

                        elif ("talkban " in msg.text):
                          if run["finbot"] == True:
                            if sender in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           bot_run["Talkblacklist"][target] = True
                                           with open('finbot1.json','w') as fp:
                                           	json.dump(bot_run, fp, sort_keys=True, indent=4)
                                           getMention(to,"Talkban user added @!",[sender])
                                       except:
                                           pass

                        elif ("talkban dell " in msg.text):
                          if run["finbot"] == True:
                            if sender in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del bot_run["Talkblacklist"][target]
                                           with open('finbot1.json','w') as fp:
                                           	json.dump(bot_run, fp, sort_keys=True, indent=4)
                                           getMention(to,"Talkban user deleted @!",[sender])
                                       except:
                                           pass

                        elif ("pro admin " in msg.text):
                            if sender in Master:
                                 key = eval(msg.contentMetadata["MENTION"])
                                 key["MENTIONEES"][0]["M"]
                                 targets = []
                                 for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                 for target in targets:
                                    try:
                                        run_bot["Admin"][target] = True
                                        with open('finbotLogged.json','w') as fp:
                                        	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                        getMention(to," Admin has been promoted by @!",[sender])
                                    except:
                                         pass

                        elif ("rm admin " in msg.text):
                            if sender in Master:
                                 key = eval(msg.contentMetadata["MENTION"])
                                 key["MENTIONEES"][0]["M"]
                                 targets = []
                                 for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                 for target in targets:
                                    try:
                                        del run_bot["Admin"][target]
                                        with open('finbotLogged.json','w') as fp:
                                        	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                        getMention(to,"An Admin has been removed by @!",[sender])
                                    except:
                                         pass                          

                        elif cmd == "adminlist" or text.lower() == 'admin list':
                          if run["finbot"] == True:
                            if sender in Master:
                              if run_bot["Admin"] == {}:
                                _Chat(msg.to,"No admin added")
                              else:
                                ma = ""
                                a = 0
                                for m_id in run_bot["Admin"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +kang.getContact(m_id).displayName + "\n"
                                _Chat(msg.to," Adminlist\n\n"+ma+"\nTotal [ %s ] Admin User" %(str(len(run_bot["Admin"]))))

                        elif cmd == "admin cont" or text.lower() == 'admin cont':
                          if run["finbot"] == True:
                            if sender in Master:
                              if run_bot["Admin"] == {}:
                                    _Chat(msg.to,"No admin list added")
                              else:
                                    ma = ""
                                    for i in run_bot["Admin"]:
                                        ma = kang.getContact(i)
                                        _Chat(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "remove admin" or cmd == 'clear  admin':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                              bot_run["Admin"] = {}
                              ragets = kang.getContacts(bot_run["Blacklist_User"])
                              mc = "「%i」User Admin" % len(ragets)
                              _Chat(to,"Removed" +mc)

                        elif ("ban " in msg.text):
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           bot_run["Blacklist_User"][target] = True
                                           with open('finbot1.json','w') as fp:
                                           	json.dump(bot_run, fp, sort_keys=True, indent=4)
                                           getMention(to,"User has been banned @!",[sender])
                                       except:
                                           pass

                        elif ("unban " in msg.text):
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del bot_run["Blacklist_User"][target]
                                           with open('finbot1.json','w') as fp:
                                           	json.dump(bot_run, fp, sort_keys=True, indent=4)
                                           getMention(to,"User unbanned @!",[sender])
                                       except:
                                           pass

                        elif cmd == "banlist" or cmd == 'bn':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                              if bot_run["Blacklist_User"] == {}:
                                _Chat(to,"No blacklist user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in bot_run["Blacklist_User"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + "│ " +kang.getContact(m_id).displayName + "\n"
                                _Chat(to,"╭─「 Banned List 」─\n"+ma+"\n╰──────────\nTotal「%s」Blacklist User" %(str(len(bot_run["Blacklist_User"]))))

                        elif cmd == "talkbanlist" or cmd == 'tbn':
                          if run["finbot"] == True:
                            if sender in Master:
                              if bot_run["Talkblacklist"] == {}:
                                _Chat(to,"No Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in bot_run["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +kang.getContact(m_id).displayName + "\n"
                                _Chat(to,"|| Talkban List\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(bot_run["Talkblacklist"]))))

                        elif cmd == "blc" or cmd == 'blcontact':
                          if run["finbot"] == True:
                            if sender in Master or sender in admin:
                              if bot_run["Blacklist_User"] == {}:
                                    _Chat(to,"No blacklist")
                              else:
                                    ma = ""
                                    for i in bot_run["Blacklist_User"]:
                                        ma = kang.getContact(i)
                                        _Chat(to, None, contentMetadata={'mid': i}, contentType=13)

                        elif "/ti/g/" in msg.text.lower():
                          if run["finbot"] == True:
                            #if sender in Master:
                              if bot_run["Auto_Join_Ticket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = kang.findGroupByTicket(ticket_id)
                                     kang.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     groups = fino.findGroupByTicket(ticket_id)
                                     fino.acceptGroupInvitationByTicket(groups.id,ticket_id)
                                     group1 = fn1.findGroupByTicket(ticket_id)
                                     fn1.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group2 = fn2.findGroupByTicket(ticket_id)
                                     fn2.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     group3 = fn3.findGroupByTicket(ticket_id)
                                     fn3.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     group4 = fn4.findGroupByTicket(ticket_id)
                                     fn4.acceptGroupInvitationByTicket(group4.id,ticket_id)
                                     group5 = fn5.findGroupByTicket(ticket_id)
                                     fn5.acceptGroupInvitationByTicket(group5.id,ticket_id)

    except Exception as error:
        print (error) 

while True:
    try:
        autoRestart()
        operations = finobot.singleTrace(count=50)
        if operations is not None:
            for alfino in operations:
                finbot(alfino)
                finobot.setRevision(alfino.revision)
    except Exception as e:
        print (e)