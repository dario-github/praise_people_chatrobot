"""
    WeChat KUAKUA_Robot v0.1
"""

# -*- coding:utf-8 -*- 

import itchat, re
from itchat.content import *
import random
import json

"""
    Constants
"""

kua_list = []
with open ("kua.txt", "r", encoding='utf-8') as f:
	for line in f:
		kua_list.append(line.strip())
		
REPLY = {'夸我': kua_list,
         'default': 
         ['你真是太棒了！',
		     '你真不错！',
		     '好开心！',
		     '嗯哪！']}

# @itchat.msg_register([TEXT], isGroupChat=True)
@itchat.msg_register([TEXT], isFriendChat=True, isGroupChat=True)
# @itchat.msg_register([TEXT])
def text_reply(msg):
    # 这里一定要修改成你想加群的群的名称
    if msg['User']['NickName'] in ('kaggle冲刺群', '我爱我家', 'Pati\U0001f955', '陈相'):
        user = msg['User'].get('NickName')
        if not user:
            pass
        else:
            print("Message from: %s" % user.encode('utf-8'))
            # 发送者的昵称
            username = msg.get('ActualNickName', msg['User'].get('RemarkName'))
            print('Who sent it: %s' % username)
    
            match = re.search('夸我|求夸|夸一下|夸一下|夸', msg['Text'])
            if match:
                print('-+-+' * 5)
                print('Message content:{}'.format(msg['Content']))
                print('夸我 is: %s' % (match is not None))
                randomIdx = random.randint(0, len(REPLY['夸我']) - 1)
                # itchat.send('@' + '{}\n{}'.format(username, REPLY['夸我'][randomIdx]), msg['FromUserName'])
                itchat.send('{}'.format(REPLY['夸我'][randomIdx]), msg['FromUserName'])
		  # else:
		  # 	randomIdx = random.randint(0, len(REPLY['default']) - 1)
		  # 	itchat.send('@' + '%s\n%s' % (username, REPLY['default'][randomIdx]), msg['FromUserName'])
            print('isAt is:%s' % msg.get('isAt'))
    
            if msg.get('isAt'):
                randomIdx = random.randint(0, len(REPLY['default']) - 1)
                # itchat.send('@' + '{}\n{}'.format(username, REPLY['default'][randomIdx]), msg['FromUserName'])
                itchat.send('{}'.format(REPLY['default'][randomIdx]), msg['FromUserName'])
                print('-+-+'*5)

itchat.auto_login(enableCmdQR=True, hotReload=True)
itchat.run()

