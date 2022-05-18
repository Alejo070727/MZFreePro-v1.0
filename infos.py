from pyobigram.utils import sizeof_fmt,nice_time
import datetime
import time
import os

def text_progres(index,max):
	try:
		if max<1:
			max += 1
		porcent = index / max
		porcent *= 100
		porcent = round(porcent)
		make_text = ''
		index_make = 1
		make_text += '\n['
		while(index_make<21):
			if porcent >= index_make * 5: make_text+='▓'
			else: make_text+='░'
			index_make+=1
		make_text += ']\n'
		return make_text
	except Exception as ex:
			return ''

def porcent(index,max):
    porcent = index / max
    porcent *= 100
    porcent = round(porcent)
    return porcent

def createDownloading(filename,totalBits,currentBits,speed,time,tid=''):
    msg = '📥𝐃𝐞𝐬𝐜𝐚𝐫𝐠𝐚𝐧𝐝𝐨 𝐀𝐫𝐜𝐡𝐢𝐯𝐨.. \n\n'
    msg+= '🔖𝐍𝐨𝐦𝐛𝐫𝐞: ' + str(filename)+'\n'
    msg+= '📦𝐓𝐚𝐦𝐚ñ𝐨: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= '🗂𝐃𝐞𝐬𝐜𝐚𝐫𝐠𝐚𝐝𝐨: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= '📶𝐕𝐞𝐥𝐨𝐜𝐢𝐝𝐚𝐝: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= '🕐𝐓𝐢𝐞𝐦𝐩𝐨: ' + str(datetime.timedelta(seconds=int(time))) +'\n\n'

    msg = '📡𝐃𝐞𝐬𝐜𝐚𝐫𝐠𝐚𝐧𝐝𝐨 𝐀𝐫𝐜𝐡𝐢𝐯𝐨..\n\n'
    msg += '🔖𝐍𝐨𝐦𝐛𝐫𝐞: '+filename+'\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += '🗂𝐓𝐨𝐭𝐚𝐥: '+sizeof_fmt(totalBits)+'\n'
    msg += '🗃𝐃𝐞𝐬𝐜𝐚𝐫𝐠𝐚𝐝𝐨: '+sizeof_fmt(currentBits)+'\n'
    msg += '📶𝐕𝐞𝐥𝐨𝐜𝐢𝐝𝐚𝐝: '+sizeof_fmt(speed)+'/s\n'
    msg += '🕐𝐓𝐢𝐞𝐦𝐩𝐨 𝐝𝐞 𝐃𝐞𝐬𝐜𝐚𝐫𝐠𝐚: '+str(datetime.timedelta(seconds=int(time)))+'s\n' 
    if tid!='':
        msg+= '/cancel_' + tid
    return msg
def createUploading(filename,totalBits,currentBits,speed,time,originalname=''):
    msg = '⏫𝐒𝐮𝐛𝐢𝐞𝐧𝐝𝐨 𝐀 𝐋𝐚 𝐍𝐮𝐛𝐞☁... \n\n'
    msg+= '🔖𝐍𝐨𝐦𝐛𝐫𝐞: ' + str(filename)+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= '⏫𝐒𝐮𝐛𝐢𝐞𝐧𝐝𝐨: ' + str(filename)+'\n'
    msg+= '🗂𝐓𝐚𝐦𝐚ñ𝐨 𝐓𝐨𝐭𝐚𝐥: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= '🗂𝐒𝐮𝐛𝐢𝐝𝐨: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= '📶𝐕𝐞𝐥𝐨𝐜𝐢𝐝𝐚𝐝: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= '🕐𝐓𝐢𝐞𝐦𝐩𝐨: ' + str(datetime.timedelta(seconds=int(time))) +'\n'

    msg = '⏫𝐒𝐮𝐛𝐢𝐞𝐧𝐝𝐨 𝐀 𝐋𝐚 𝐍𝐮𝐛𝐞☁...\n\n'
    msg += '🔖𝐍𝐨𝐦𝐛𝐫𝐞: '+filename+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= '📁𝐏𝐚𝐫𝐭𝐞: ' + str(filename)+'\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += '🗂𝐓𝐨𝐭𝐚𝐥: '+sizeof_fmt(totalBits)+'\n'
    msg += '🗃𝐃𝐞𝐬𝐜𝐚𝐫𝐠𝐚𝐝𝐨: '+sizeof_fmt(currentBits)+'\n'
    msg += '📶𝐕𝐞𝐥𝐨𝐜𝐢𝐝𝐚𝐝: '+sizeof_fmt(speed)+'/s\n'
    msg += '🕐𝐓𝐢𝐞𝐦𝐩𝐨 𝐝𝐞 𝐃𝐞𝐬𝐜𝐚𝐫𝐠𝐚: '+str(datetime.timedelta(seconds=int(time)))+'s\n'

    return msg
def createCompresing(filename,filesize,splitsize):
    msg = '📚𝐂𝐨𝐦𝐩𝐫𝐢𝐦𝐢𝐞𝐧𝐝𝐨... \n\n'
    msg+= '📄𝐍𝐨𝐦𝐛𝐫𝐞: ' + str(filename)+'\n'
    msg+= '📂𝐓𝐚𝐦𝐚ñ𝐨 𝐓𝐨𝐭𝐚𝐥: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '🗃️𝐓𝐚𝐦𝐚ñ𝐨 𝐏𝐚𝐫𝐭𝐞𝐬: ' + str(sizeof_fmt(splitsize))+'\n'
    msg+= '🏷️𝐂𝐚𝐧𝐭𝐢𝐝𝐚𝐝 𝐏𝐚𝐫𝐭𝐞𝐬: ' + str(round(int(filesize/splitsize)+1,1))+'\n\n'
    return msg
def createFinishUploading(filename,filesize,split_size,current,count,findex):
    msg = '🌀𝐅𝐢𝐧𝐚𝐥𝐢𝐳𝐚𝐝𝐨🌀\n\n'
    msg+= '📄𝐍𝐨𝐦𝐛𝐫𝐞: ' + str(filename)+'\n'
    msg+= '📦𝐓𝐚𝐦𝐚ñ𝐨 𝐓𝐨𝐭𝐚𝐥: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '🗃️𝐓𝐚𝐦𝐚ñ𝐨 𝐏𝐚𝐫𝐭𝐞𝐬: ' + str(sizeof_fmt(split_size))+'\n'
    msg+= '🗒️𝐏𝐚𝐫𝐭𝐞𝐬 𝐒𝐮𝐛𝐢𝐝𝐚𝐬: ' + str(current) + '/' + str(count) +'\n\n'
    msg+= '🗑️𝐁𝐨𝐫𝐫𝐚𝐫 𝐀𝐫𝐜𝐡𝐢𝐯𝐨: ' + '/del_'+str(findex)
    return msg

def createFileMsg(filename,files):
    import urllib
    if len(files)>0:
        msg= '<b>🖇𝐄𝐧𝐥𝐚𝐜𝐞𝐬🖇</b>\n'
        for f in files:
            url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
            #msg+= '<a href="'+f['url']+'">🔗' + f['name'] + '🔗</a>'
            msg+= "<a href='"+url+"'>🔗"+f['name']+'🔗</a>\n'
        return msg
    return ''

def createFilesMsg(evfiles):
    msg = '📂𝐀𝐫𝐜𝐡𝐢𝐯𝐨𝐬 ('+str(len(evfiles))+')📑\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                fname = f['name'] + fext
                msg+= '/txt_'+ str(i) + ' /del_'+ str(i) + '\n' + fname +'\n\n'
                i+=1
            except:pass
    return msg
def createStat(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = '⚙️𝐂𝐨𝐧𝐟𝐢𝐠𝐮𝐫𝐚𝐜𝐢𝐨𝐧𝐞𝐬 𝐃𝐞 𝐔𝐬𝐮𝐚𝐫𝐢𝐨⚙️\n\n'
    msg+= '🔖𝐍𝐨𝐦𝐛𝐫𝐞: @' + str(username)+'\n'
    msg+= '📑𝐔𝐬𝐞𝐫: ' + str(userdata['moodle_user'])+'\n'
    msg+= '🗳𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝: ' + str(userdata['moodle_password'])+'\n'
    msg+= '📡𝐇𝐨𝐬𝐭: ' + str(userdata['moodle_host'])+'\n'
    if userdata['cloudtype'] == 'moodle':
        msg+= '🏷𝐑𝐞𝐩𝐨𝐈𝐃: ' + str(userdata['moodle_repo_id'])+'\n'
    msg+= '🏷𝐂𝐥𝐨𝐮𝐝𝐓𝐲𝐩𝐞: ' + str(userdata['cloudtype'])+'\n'
    msg+= '📟𝐔𝐩𝐓𝐲𝐩𝐞: ' + str(userdata['uploadtype'])+'\n'
    if userdata['cloudtype'] == 'cloud':
        msg+= '🗂Dir: /' + str(userdata['dir'])+'\n'
    msg+= '📚𝐓𝐚𝐦𝐚ñ𝐨 𝐝𝐞 𝐙𝐢𝐩𝐬 : ' + sizeof_fmt(userdata['zips']*1024*1024) + '\n\n'
    msgAdmin = 'No'
    if isadmin:
        msgAdmin = 'Si'
    msg+= '🦾𝐀𝐝𝐦𝐢𝐧 : ' + msgAdmin + '\n'
    proxy = 'NO'
    if userdata['proxy'] !='':
       proxy = 'SI'
    tokenize = 'NO'
    if userdata['tokenize']!=0:
       tokenize = 'SI'
    msg+= '🔌𝐏𝐫𝐨𝐱𝐲 : ' + proxy + '\n'
    msg+= '⚡𝐓𝐨𝐤𝐞𝐧𝐢𝐳𝐞 : ' + tokenize + '\n\n'
    msg+= '⚙️𝐂𝐨𝐧𝐟𝐢𝐠𝐮𝐫𝐚𝐫 𝐌𝐨𝐨𝐝𝐥𝐞⚙️\n🔥𝐄𝐣𝐞𝐦𝐩𝐥𝐨 /account 𝐔𝐬𝐞𝐫,𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝'
    return msg
