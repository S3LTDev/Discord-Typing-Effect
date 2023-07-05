# oooo     oooo      o      ooooo  oooo   ooooooo   ooooooooooo ooooooooooo 
# 8888o   888      888       888  88   o88     888 88  888  88 88    888   
# 88 888o8 88     8  88        888           o888      888         888     
# 88  888  88    8oooo88      88 888      o888   o     888       888    oo 
# o88o  8  o88o o88o  o888o o88o  o888o o8888oooo88    o888o    o888oooo888                                                                         
# link  https://github.com/max2tz/Discord-Typing-Effect
# author  max2tz https://github.com/max2tz
# license  GPL-3.0 License 

# 0x01 REQUEST FAILED
# 0x02 REQUEST SUCCESSFUL

import requests

if config_file == False:
    chid = input("CHANNEL ID >> ")
    usid = input("USER TOKEN >> ")
else:
    chid = 'token-here'
    usid = 'channel-id-here'


while True:
    response = requests.post(f'https://discord.com/api/v9/channels/{chid}/typing', headers={'Authorisation': usid})
    if response.status_code == 204:
        print("REQUEST SUCCESSFUL >> 0x02")
    else:
        print("REQUEST FAILED >> 0x01")
    time.sleep(7)
