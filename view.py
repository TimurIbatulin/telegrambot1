
# Надо загрузить библиотеку командой "pip install pytelegrambotapi"
import tokenn as t
import telebot
from telebot import types
import time

import bot_command as bc


bot = telebot.TeleBot(t.token())


@bot.message_handler(commands=["start"])
# Получение сообщений от юзера
def start(m, res=False):
        bot.send_message(m.chat.id, 'Нажми: \n"Актуальный набор" для получения информации о набираемых турах и свободных местах\nзаписать на тур — для записи туриста на тур(только после оплаты/предоплаты)\n заявка на тур - для создания заявки на набор тура', reply_markup=(bc.starting(m, res)))

@bot.message_handler(content_types=["text"])
def handle_text(message):

    for i in range(12):
        k = str(i)
        if message.text.strip() == k:
            answer = bc.writing(i, message.from_user.id)




    answer = bc.dating_count(message.text.strip())
    if answer != None:
        bot.send_message(message.chat.id, f'Осталось только {answer}, сколько записываем?', reply_markup=(bc.numbers()))
        answer = "ок"
    else:
        answer = bc.requests_count(message.text.strip())
        if answer != None:
            bot.send_message(message.chat.id, f'Осталось только {answer}, сколько записываем?', reply_markup=(bc.numbers()))
            answer = "ок"

    if message.text.strip() == 'Актуальный набор' :
        answer = bc.actual_open('act_recruiting')
        
    
    elif message.text.strip() == 'записать на тур' :
        bot.send_message(message.chat.id, 'На какой тур записываем?', reply_markup=(bc.datbutton()))
        answer = "ок"
        
        

    elif message.text.strip() == 'заявка на тур' :
        bot.send_message(message.chat.id, 'На какой тур заявку делаем?', reply_markup=(bc.regbutton()))
        answer = "ок"

    
    else:
        answer = "я не знаааааю что делать, начни сначала" 
        bot.send_message(message.chat.id,'...', reply_markup=(bc.starting(message, False)))
     
    
    bot.send_message(message.chat.id, answer)










# Запускаем бота
print('ok')
bot.polling(none_stop=True, interval=0)
