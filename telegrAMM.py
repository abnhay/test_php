'''
pip install pyTelegramBotApi
pip3 install pyTelegramBotApi
upgrade pip >>>python -m pip install --upgrade pip
'''
#from pydoc import text
import telebot
from telebot import types
from importlib import reload
import sys
import json

reload(sys)
#print(reload(sys))
#print(sys.version[0])=3
#sys.setdefaultencoding('utf-8')

tok = '5301607846:AAGWP43A2zXMJw8m64HiaOFfDt8GtGgt_Zw'

bot = telebot.TeleBot(tok)



#عند الظغط على زر البدء 
@bot.message_handler(commands=['start'])

def start(message):
    #انشاء ازرار    
    kebort = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='[ ~DEV~ ]',callback_data='val_dev')
    button2 = types.InlineKeyboardButton(text='[ START ]',callback_data='val_start')
    kebort.add(button1,button2)   

    id_user = message.from_user.id #ID USERS
    name_user = message.from_user.first_name #NAME USERS
    user_name = message.from_user.username #USER USERS
    
    ms_start_err = f'Welcom Manage your Instagram account\n======= ======== =======\nHi {name_user}\n======= ======== =======\nUserS: @{user_name}\n======= ======== =======\nID : {id_user}'#Manage your Instagram account
    bot.reply_to(message,ms_start_err,reply_markup=kebort)




@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.message:
        
        if call.data == 'val_dev':
            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='If you encounter any problems, please contact us via id DEV >@knk_1k && CH >@abnhay')

            


        if call.data == 'val_start':
            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='Hi login')



print('BOT WOREKING ...')
bot.polling()
