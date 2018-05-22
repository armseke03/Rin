# -*- coding: utf-8 -*-

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit, subprocess

cl = LINE()
#ririn = LINE("TOKENMU")

ririnMid = cl.profile.mid
ririnProfile = cl.getProfile()
ririnSettings = cl.getSettings()
ririnPoll = OEPoll(cl)
botStart = time.time()

print ("╔═════════════════════════\n║╔════════════════════════\n║╠❂➣ DNA BERHASIL LOGIN\n║╚════════════════════════\n╚═════════════════════════")

msg_dict = {}

wait = {
    "autoAdd": True,
    "autoJoin": True,
    "autoLeave": False,
    "autoRead": False,
    "autoRespon": True,
    "autoResponPc": False,
    "autoJoinTicket": True,
    "checkContact": False,
    "checkPost": False,
    "checkSticker": False,
    "changePictureProfile": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "leaveRoom": True,
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    },
    "Protectcancel": True,
    "Protectgr": True,
    "Protectinvite": True,
    "Protectjoin": False,
    "setKey": False,
    "sider": False,
    "unsendMessage": True
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}

list_language = {
    "list_textToSpeech": {
        "id": "Indonesia",
        "af" : "Afrikaans",
        "sq" : "Albanian",
        "ar" : "Arabic",
        "hy" : "Armenian",
        "bn" : "Bengali",
        "ca" : "Catalan",
        "zh" : "Chinese",
        "zh-cn" : "Chinese (Mandarin/China)",
        "zh-tw" : "Chinese (Mandarin/Taiwan)",
        "zh-yue" : "Chinese (Cantonese)",
        "hr" : "Croatian",
        "cs" : "Czech",
        "da" : "Danish",
        "nl" : "Dutch",
        "en" : "English",
        "en-au" : "English (Australia)",
        "en-uk" : "English (United Kingdom)",
        "en-us" : "English (United States)",
        "eo" : "Esperanto",
        "fi" : "Finnish",
        "fr" : "French",
        "de" : "German",
        "el" : "Greek",
        "hi" : "Hindi",
        "hu" : "Hungarian",
        "is" : "Icelandic",
        "id" : "Indonesian",
        "it" : "Italian",
        "ja" : "Japanese",
        "km" : "Khmer (Cambodian)",
        "ko" : "Korean",
        "la" : "Latin",
        "lv" : "Latvian",
        "mk" : "Macedonian",
        "no" : "Norwegian",
        "pl" : "Polish",
        "pt" : "Portuguese",
        "ro" : "Romanian",
        "ru" : "Russian",
        "sr" : "Serbian",
        "si" : "Sinhala",
        "sk" : "Slovak",
        "es" : "Spanish",
        "es-es" : "Spanish (Spain)",
        "es-us" : "Spanish (United States)",
        "sw" : "Swahili",
        "sv" : "Swedish",
        "ta" : "Tamil",
        "th" : "Thai",
        "tr" : "Turkish",
        "uk" : "Ukrainian",
        "vi" : "Vietnamese",
        "cy" : "Welsh"
    },
    "list_translate": {    
        "af": "afrikaans",
        "sq": "albanian",
        "am": "amharic",
        "ar": "arabic",
        "hy": "armenian",
        "az": "azerbaijani",
        "eu": "basque",
        "be": "belarusian",
        "bn": "bengali",
        "bs": "bosnian",
        "bg": "bulgarian",
        "ca": "catalan",
        "ceb": "cebuano",
        "ny": "chichewa",
        "zh-cn": "chinese (simplified)",
        "zh-tw": "chinese (traditional)",
        "co": "corsican",
        "hr": "croatian",
        "cs": "czech",
        "da": "danish",
        "nl": "dutch",
        "en": "english",
        "eo": "esperanto",
        "et": "estonian",
        "tl": "filipino",
        "fi": "finnish",
        "fr": "french",
        "fy": "frisian",
        "gl": "galician",
        "ka": "georgian",
        "de": "german",
        "el": "greek",
        "gu": "gujarati",
        "ht": "haitian creole",
        "ha": "hausa",
        "haw": "hawaiian",
        "iw": "hebrew",
        "hi": "hindi",
        "hmn": "hmong",
        "hu": "hungarian",
        "is": "icelandic",
        "ig": "igbo",
        "id": "indonesian",
        "ga": "irish",
        "it": "italian",
        "ja": "japanese",
        "jw": "javanese",
        "kn": "kannada",
        "kk": "kazakh",
        "km": "khmer",
        "ko": "korean",
        "ku": "kurdish (kurmanji)",
        "ky": "kyrgyz",
        "lo": "lao",
        "la": "latin",
        "lv": "latvian",
        "lt": "lithuanian",
        "lb": "luxembourgish",
        "mk": "macedonian",
        "mg": "malagasy",
        "ms": "malay",
        "ml": "malayalam",
        "mt": "maltese",
        "mi": "maori",
        "mr": "marathi",
        "mn": "mongolian",
        "my": "myanmar (burmese)",
        "ne": "nepali",
        "no": "norwegian",
        "ps": "pashto",
        "fa": "persian",
        "pl": "polish",
        "pt": "portuguese",
        "pa": "punjabi",
        "ro": "romanian",
        "ru": "russian",
        "sm": "samoan",
        "gd": "scots gaelic",
        "sr": "serbian",
        "st": "sesotho",
        "sn": "shona",
        "sd": "sindhi",
        "si": "sinhala",
        "sk": "slovak",
        "sl": "slovenian",
        "so": "somali",
        "es": "spanish",
        "su": "sundanese",
        "sw": "swahili",
        "sv": "swedish",
        "tg": "tajik",
        "ta": "tamil",
        "te": "telugu",
        "th": "thai",
        "tr": "turkish",
        "uk": "ukrainian",
        "ur": "urdu",
        "uz": "uzbek",
        "vi": "vietnamese",
        "cy": "welsh",
        "xh": "xhosa",
        "yi": "yiddish",
        "yo": "yoruba",
        "zu": "zulu",
        "fil": "Filipino",
        "he": "Hebrew"
    }
}

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
wait["myProfile"]["displayName"] = clProfile.displayName
wait["myProfile"]["statusMessage"] = clProfile.statusMessage
wait["myProfile"]["pictureStatus"] = clProfile.pictureStatus
coverId = ririn.getProfileDetail()["result"]["objectId"]
wait["myProfile"]["coverId"] = coverId

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    ririn.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                ririn.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@dee "
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
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if wait["setKey"] == True:
        if pesan.startswith(wait["keyCommand"]):
            cmd = pesan.replace(wait["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "• Gunakan「 " + key + " 」di depannya\n\n" + \
                  "「✭」 " + key + "Me\n" + \
                  "「✭」 " + key + "Mid「@」\n" + \
                  "「✭」 " + key + "Steal「@」\n" + \
                  "「✭」 " + key + "Cover「@」\n" + \
                  "「✭」 " + key + "Nk「@」\n" + \
                  "「✭」 " + key + "Kick1「@」\n" + \
                  "「✭」 " + key + "Clone「@」\n" + \
                  "「✭」 " + key + "Restore\n" + \
                  "「✭」 " + key + "Reject\n" + \
                  "「✭」 " + key + "Mybot\n" + \
                  "「✭」 " + key + "Setting\n" + \
                  "「✭」 " + key + "About\n" + \
                  "「✭」 " + key + "Restart\n" + \
                  "「✭」 " + key + "Runtime\n" + \
                  "「✭」 " + key + "Creator\n" + \
                  "「✭」 " + key + "Speed/Sp\n" + \
                  "「✭」 " + key + "Respontime\n" + \
                  "「✭」 " + key + "Tagall\n" + \
                  "「✭」 " + key + "Joinall\n" + \
                  "「✭」 " + key + "Byeall\n" + \
                  "「✭」 " + key + "Bye me\n" + \
                  "「✭」 " + key + "Leave「Namagrup」\n" + \
                  "「✭」 " + key + "Ginfo\n" + \
                  "「✭」 " + key + "Open\n" + \
                  "「✭」 " + key + "Close\n" + \
                  "「✭」 " + key + "Url\n" + \
                  "「✭」 " + key + "Gruplist\n" + \
                  "「✭」 " + key + "Open「nomer」\n" + \
                  "「✭」 " + key + "Close「nomer」\n" + \
                  "「✭」 " + key + "Infogrup「nomer」\n" + \
                  "「✭」 " + key + "Infomem「nomer」\n" + \
                  "「✭」 " + key + "Joinall「nomer」\n" + \
                  "「✭」 " + key + "Leaveall「nomer」\n" + \
                  "「✭」 " + key + "Remove chat\n" + \
                  "「✭」 " + key + "Lurking「on/off」\n" + \
                  "「✭」 " + key + "Lurkers\n" + \
                  "「✭」 " + key + "Sider「on/off」\n" + \
                  "「✭」 " + key + "Updatefoto\n" + \
                  "「✭」 " + key + "Updategrup\n" + \
                  "「✭」 " + key + "Updatebot\n" + \
                  "「✭」 " + key + "Broadcast:「Text」\n" + \
                  "「✭」 " + key + "Setkey「New Key」\n" + \
                  "「✭」 " + key + "Mykey\n" + \
                  "「✭」 " + key + "Resetkey\n" + \
                  "\n「 Turn In Media 」\n• Use「 " + key + " 」di depannya\n\n" + \
                  "「✭」 " + key + "Kode wilayah\n" + \
                  "「✭」 " + key + "Listmp3\n" + \
                  "「✭」 " + key + "Listvideo\n" + \
                  "「✭」 " + key + "Listimage\n" + \
                  "「✭」 " + key + "Liststicker\n" + \
                  "「✭」 " + key + "Addimg「Teks」\n" + \
                  "「✭」 " + key + "Dellimg「Teks」\n" + \
                  "「✭」 " + key + "Addmp3「Teks」\n" + \
                  "「✭」 " + key + "Dellmp3「Teks」\n" + \
                  "「✭」 " + key + "Addvideo「Teks」\n" + \
                  "「✭」 " + key + "Dellvideo「Teks」\n" + \
                  "「✭」 " + key + "Addsticker「Teks」\n" + \
                  "「✭」 " + key + "Dellsticker「Teks」\n" + \
                  "「✭」 " + key + "Spamtag:「jumlahnya」\n" + \
                  "「✭」 " + key + "Spamtag「@」\n" + \
                  "「✭」 " + key + "Spamcall:「jumlahnya」\n" + \
                  "「✭」 " + key + "Spamcall\n" + \
                  "「✭」 " + key + "Musik「Nama Penyanyi」\n" + \
                  "「✭」 " + key + "Get-fs「Query」\n" + \
                  "「✭」 " + key + "Get-line「ID Line」\n" + \
                  "「✭」 " + key + "Get-apk「Query」\n" + \
                  "「✭」 " + key + "Get-gif「Query」\n" + \
                  "「✭」 " + key + "Get-xxx「Query」\n" + \
                  "「✭」 " + key + "Get-anime「Query」\n" + \
                  "「✭」 " + key + "Get-mimpi「Query」\n" + \
                  "「✭」 " + key + "Get-audio「Query」\n" + \
                  "「✭」 " + key + "Get-mp3「Query」\n" + \
                  "「✭」 " + key + "Get-video「Query」\n" + \
                  "「✭」 " + key + "Get-bintang「Zodiak」\n" + \
                  "「✭」 " + key + "Get-zodiak「Zodiak」\n" + \
                  "「✭」 " + key + "Get-sholat「Nama Kota」\n" + \
                  "「✭」 " + key + "Get-cuaca「Nama Kota」\n" + \
                  "「✭」 " + key + "Get-lokasi「Nama Kota」\n" + \
                  "「✭」 " + key + "Get-lirik「Judul Lagu」\n" + \
                  "「✭」 " + key + "Get-instagram「User Name」\n" + \
                  "「✭」 " + key + "Get-date「tgl-bln-thn」\n" + \
                  "\n「 Setting Protection 」\n• Use「 " + key + " 」di depannya\n\n" + \
                  "「✭」 " + key + "Notag「on/off」\n" + \
                  "「✭」 " + key + "Protecall「on/off」\n" + \
                  "「✭」 " + key + "Protecturl「on/off」\n" + \
                  "「✭」 " + key + "Protectjoin「on/off」\n" + \
                  "「✭」 " + key + "Protectkick「on/off」\n" + \
                  "「✭」 " + key + "Protectinvite「on/off」\n" + \
                  "「✭」 " + key + "Protectcancel「on/off」\n" + \
                  "\n「 Setting User 」\n• Use「 " + key + " 」di depannya\n\n" + \
                  "「✭」 " + key + "Invite「on/off」\n" + \
                  "「✭」 " + key + "Sticker「on/off」\n" + \
                  "「✭」 " + key + "Unsend「on/off」\n" + \
                  "「✭」 " + key + "Respon「on/off」\n" + \
                  "「✭」 " + key + "Timeline「on/off」\n" + \
                  "「✭」 " + key + "Contact「on/off」\n" + \
                  "「✭」 " + key + "Autojoin「on/off」\n" + \
                  "「✭」 " + key + "Autoadd「on/off」\n" + \
                  "「✭」 " + key + "Welcome「on/off」\n" + \
                  "「✭」 " + key + "Autoleave「on/off」\n" + \
                  "「✭」 " + key + "Jointicket「on/off」\n" + \
                  "\n「 For Admin 」\n• Use「 " + key + " 」di depannya\n\n" + \
                  "「✭」 " + key + "Bot:on\n" + \
                  "「✭」 " + key + "Bot:expell\n" + \
                  "「✭」 " + key + "Staff:on\n" + \
                  "「✭」 " + key + "Staff:expell\n" + \
                  "「✭」 " + key + "Admin:on\n" + \
                  "「✭」 " + key + "Admin:expell\n" + \
                  "「✭」 " + key + "Botadd「@」\n" + \
                  "「✭」 " + key + "Botdell「@」\n" + \
                  "「✭」 " + key + "Staffadd「@」\n" + \
                  "「✭」 " + key + "Staffdell「@」\n" + \
                  "「✭」 " + key + "Adminadd「@」\n" + \
                  "「✭」 " + key + "Admindell「@」\n" + \
                  "「✭」 " + key + "Refresh\n" + \
                  "「✭」 " + key + "Listbot\n" + \
                  "「✭」 " + key + "Listadmin\n" + \
                  "「✭」 " + key + "Listprotect\n" + \
                  "\nKetik「 Refresh 」jika sudah\nmenggunakan command diatas...\n"
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "• Gunakan「 " + key + " 」di depannya\n\n" + \
                  "「✭」 " + key + "Blc\n" + \
                  "「✭」 " + key + "Ban:on\n" + \
                  "「✭」 " + key + "Unban:on\n" + \
                  "「✭」 " + key + "Ban「@」\n" + \
                  "「✭」 " + key + "Unban「@」\n" + \
                  "「✭」 " + key + "Talkban「@」\n" + \
                  "「✭」 " + key + "Untalkban「@」\n" + \
                  "「✭」 " + key + "Talkban:on\n" + \
                  "「✭」 " + key + "Untalkban:on\n" + \
                  "「✭」 " + key + "Banlist\n" + \
                  "「✭」 " + key + "Talkbanlist\n" + \
                  "「✭」 " + key + "Clearban\n" + \
                  "「✭」 " + key + "Refresh\n" + \
                  "\n「 Check Settings 」\n• Use「 " + key + " 」di depannya\n\n" + \
                  "「✭」 " + key + "Cek sider\n" + \
                  "「✭」 " + key + "Cek spam\n" + \
                  "「✭」 " + key + "Cek pesan \n" + \
                  "「✭」 " + key + "Cek respon \n" + \
                  "「✭」 " + key + "Cek leave\n" + \
                  "「✭」 " + key + "Cek welcome\n" + \
                  "「✭」 " + key + "Set sider:「Text」\n" + \
                  "「✭」 " + key + "Set spam:「Text」\n" + \
                  "「✭」 " + key + "Set pesan:「Text」\n" + \
                  "「✭」 " + key + "Set respon:「Text」\n" + \
                  "「✭」 " + key + "Set leave:「Text」\n" + \
                  "「✭」 " + key + "Set welcome:「Text」\n" + \
                  "「✭」 " + key + "Myname:「Nama」\n" + \
                  "「✭」 " + key + "Bot1name:「Nama」\n" + \
                  "「✭」 " + key + "Bot2name:「Nama」\n" + \
                  "「✭」 " + key + "Bot3name:「Nama」\n" + \
                  "「✭」 " + key + "Bot4name:「Nama」\n" + \
                  "「✭」 " + key + "Bot5name:「Nama」\n" + \
                  "「✭」 " + key + "Bot1up「Kirim fotonya」\n" + \
                  "「✭」 " + key + "Bot2up「Kirim fotonya」\n" + \
                  "「✭」 " + key + "Bot3up「Kirim fotonya」\n" + \
                  "「✭」 " + key + "Bot4up「Kirim fotonya」\n" + \
                  "「✭」 " + key + "Bot5up「Kirim fotonya」\n" + \
                  "「✭」 " + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "「✭」 " + key + "Spam:「Mid korban」「Jumlah」\n" + \
                  "\nKetik「 Refresh 」jika sudah\nmenggunakan command diatas...\n"
    return helpMessage1

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            Ticket = cl.reissueGroupTicket(op.param1)
                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            sw.leaveGroup(op.param1)
                            cl.updateGroup(X)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                Ticket = ki.reissueGroupTicket(op.param1)
                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                sw.kickoutFromGroup(op.param1,[op.param2])
                                sw.leaveGroup(op.param1)
                                ki.updateGroup(X)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    kk.updateGroup(X)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        Ticket = kc.reissueGroupTicket(op.param1)
                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        sw.kickoutFromGroup(op.param1,[op.param2])
                                        kc.updateGroup(X)
                            except:
                                try:
                                    if km.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            km.reissueGroupTicket(op.param1)
                                            X = km.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            Ticket = km.reissueGroupTicket(op.param1)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.kickoutFromGroup(op.param1,[op.param2])
                                            km.updateGroup(X)
                                except:
                                    try:
                                        if kb.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                kb.reissueGroupTicket(op.param1)
                                                X = kb.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                Ticket = kb.reissueGroupTicket(op.param1)
                                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                                kb.updateGroup(X)
                                    except:
                                        pass

        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Sorry anda bukan admin selfbot\nSelamat tinggal " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Haii " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        km.acceptGroupInvitation(op.param1)
                        ginfo = km.getGroup(op.param1)
                        km.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        km.leaveGroup(op.param1)
                    else:
                        km.acceptGroupInvitation(op.param1)
                        ginfo = km.getGroup(op.param1)
                        km.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                     try:
                         cl.kickoutFromGroup(op.param1,[op.param2])
                     except:
                         try:
                             ki.kickoutFromGroup(op.param1,[op.param2])
                         except:
                             try:
                                 kk.kickoutFromGroup(op.param1,[op.param2])
                             except:
                                 try:
                                     kc.kickoutFromGroup(op.param1,[op.param2])
                                 except:
                                     try:
                                         km.kickoutFromGroup(op.param1,[op.param2])
                                     except:
                                         try:
                                             kb.kickoutFromGroup(op.param1,[op.param2])
                                         except:
                                             pass

                return

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                leaveMembers(op.param1, [op.param2])
if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	random.choice(ABC).cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                random.choice(ABC).cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    random.choice(ABC).cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        random.choice(ABC).cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    pass
                return

        if op.type == 0:
            return
        if op.type == 5:
              if wait["autoAdd"] == True:
                  cl.findAndAddContactsByMid(op.param1)
                  sendMention(op.param1, op.param1, "Haii ", ", terimakasih sudah add saya")
                  cl.sendText(op.param1, wait["message"])
                  cl.sendContact(op.param1, "u923fca3dc907e047572ad25c24f1d29b")

        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if wait["autoBlock"] == True:
                cl.blockContact(op.param1)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        km.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param3)
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param3)
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param3)
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    km.kickoutFromGroup(op.param1,[op.param2])
                                    km.findAndAddContactsByMid(op.param3)
                                    km.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param3)
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            ki.findAndAddContactsByMid(op.param3)
                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                            cl.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Amid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.findAndAddContactsByMid(op.param3)
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.findAndAddContactsByMid(op.param3)
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                km.kickoutFromGroup(op.param1,[op.param2])
                                km.findAndAddContactsByMid(op.param3)
                                km.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.findAndAddContactsByMid(op.param3)
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    ki.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.findAndAddContactsByMid(op.param3)
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Bmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.findAndAddContactsByMid(op.param3)
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            km.kickoutFromGroup(op.param1,[op.param2])
                            km.findAndAddContactsByMid(op.param3)
                            km.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.findAndAddContactsByMid(op.param3)
                                kb.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    cl.findAndAddContactsByMid(op.param3)
                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                    kk.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.findAndAddContactsByMid(op.param3)
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.findAndAddContactsByMid(op.param3)
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            kk.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Cmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        km.kickoutFromGroup(op.param1,[op.param2])
                        km.findAndAddContactsByMid(op.param3)
                        km.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.findAndAddContactsByMid(op.param3)
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.findAndAddContactsByMid(op.param3)
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        km.kickoutFromGroup(op.param1,[op.param2])
                                        km.findAndAddContactsByMid(op.param3)
                                        km.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            kb.findAndAddContactsByMid(op.param3)
                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Dmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.findAndAddContactsByMid(op.param3)
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        km.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            km.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.findAndAddContactsByMid(op.param3)
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                km.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.findAndAddContactsByMid(op.param3)
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    km.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.findAndAddContactsByMid(op.param3)
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        km.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            kb.findAndAddContactsByMid(op.param3)
                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                            km.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Dmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        kb.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param3)
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kb.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param3)
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kb.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    kb.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        km.kickoutFromGroup(op.param1,[op.param2])
                                        km.findAndAddContactsByMid(op.param3)
                                        km.inviteIntoGroup(op.param1,[op.param3])
                                        kb.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                            cl.findAndAddContactsByMid(op.param3)
                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                            kb.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

        if op.type == 19:
            if op.param3 in admin:
                try:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    cl.findAndAddContactsByMid(op.param3)
                    cl.inviteIntoGroup(op.param1,[op.param3])
                except:
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param3)
                        ki.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param3)
                            kk.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            pass

                return

        if op.type == 19:
            if op.param3 in staff:
                try:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    cl.findAndAddContactsByMid(op.param3)
                    cl.inviteIntoGroup(op.param1,[op.param3])
                except:
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param3)
                        ki.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param3)
                            kk.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            pass

                return
            
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

            if op.param1 in Setmain["RAreadPoint"]:
                if op.param2 in Setmain["RAreadMember"][op.param1]:
                    pass
                else:
                    Setmain["RAreadMember"][op.param1][op.param2] = True
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        sider = cl.getContact(op.param2).picturePath
                        image = 'http://dl.profile.line.naver.jp'+sider
                        cl.sendImageWithURL(op.param1, image)

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                   if msg._from in wait["blacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in admin:
                           saints = cl.getContact(msg._from)
                           sendMention(msg.to, saints.mid, "", wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"PRDID":"a0768339-c2d3-4189-9653-2909e9bb6f58","PRDTYPE":"THEME","MSGTPL":"6"}, contentType=9)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["mentionKick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in admin:
                           cl.sendMessage(msg.to, "Jangan tag saya ogeb")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
                if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 16:
                    if wait["Timeline"] == True:
                            ret_ = "「 Detail Postingan 」"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cl.getContact(sender)
                                auth = "\n• Penulis : {}".format(str(contact.displayName))
                            else:
                                auth = "\n• Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                            ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n• Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                text = "\n• Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n• Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += text
                            cl.sendMessage(to, str(ret_))
                            channel.like(url[25:58], url[66:], likeType=1006)
                            channel.comment(url[25:58], url[66:], wait["message"])
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
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
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                if wait["stickerOn"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        r = s.get("https://store.line.me/stickershop/product/{}/id".format(urllib.parse.quote(pkg_id)))
                        soup = BeautifulSoup(r.content, 'html5lib')
                        data = soup.select("[class~=mdBtn01Txt]")[0].text
                        if data == 'Lihat Produk Lain':
                            ret_ = "「 Sticker Info 」"
                            ret_ += "\n• STICKER ID : {}".format(stk_id)
                            ret_ += "\n• STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\n• STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\n• STICKER URL : line://shop/detail/{}".format(pkg_id)
                            cl.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = cl.downloadFileURL(data)
                               cl.sendImage(msg.to,path)
                        else:
                            ret_ = "「 Sticker Info 」"
                            ret_ += "\n• PRICE : "+soup.findAll('p', attrs={'class':'mdCMN08Price'})[0].text
                            ret_ += "\n• AUTHOR : "+soup.select("a[href*=/stickershop/author]")[0].text
                            ret_ += "\n• STICKER ID : {}".format(str(stk_id))
                            ret_ += "\n• STICKER PACKAGES ID : {}".format(str(pkg_id))
                            ret_ += "\n• STICKER VERSION : {}".format(str(stk_ver))
                            ret_ += "\n• STICKER URL : line://shop/detail/{}".format(str(pkg_id))
                            ret_ += "\n• DESCRIPTION :\n"+soup.findAll('p', attrs={'class':'mdCMN08Desc'})[0].text
                            cl.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = cl.downloadFileURL(data)
                               cl.sendImage(msg.to,path)
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to," 「 Contact Info 」\n「✭」 Nama : " + msg.contentMetadata["displayName"] + "\n「✭」 MID : " + msg.contentMetadata["mid"] + "\n「✭」 Status Msg : " + contact.statusMessage + "\n「✭」 Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            cl.sendMessage(msg.to, "「Dia ke bl kak... hpus bl dulu lalu invite lagi」")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  cl.findAndAddContactsByMid(target)
                                  cl.inviteIntoGroup(msg.to,[target])
                                  ryan = cl.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  "「 Sukses Invite 」\nNama "
                                  ret_ = "「Ketik Invite off jika sudah done」"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  cl.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  cl.sendText(msg.to,"Anda terkena limit")
                                  wait["invite"] = False
                                  break
                                    
                                    
