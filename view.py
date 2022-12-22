
# Надо загрузить библиотеку командой "pip install pytelegrambotapi"

import telebot
from telebot import types
import bot_command as bc
# bot_command пока не сделала, написала всё тут. надо будет ыункции команд туда вынестит

bot = telebot.TeleBot('5976873878:AAHtM8grXOPnWNqvXvllQN10hK36VfdMoo4')


@bot.message_handler(commands=["start"])
# Получение сообщений от юзера
def start(m, res=False):
        

        # # Добавляем кнопки
        # markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        # item1=types.KeyboardButton("Актуальный набор")
        # item2=types.KeyboardButton("записать на тур")
        # item3=types.KeyboardButton("заявка на тур")
        # markup.add(item1)
        # markup.add(item2)
        # markup.add(item3)
         bot.send_message(m.chat.id, 'Нажми: \n"Актуальный набор" для получения информации о набираемых турах и свободных местах\nзаписать на тур — для записи туриста на тур(только после оплаты/предоплаты)\n заявка на тур - для создания заявки на набор тура', reply_markup=(bc.starting(m, res)))

@bot.message_handler(content_types=["text"])
def handle_text(message):
    
    if message.text.strip() == 'Актуальный набор' :
        answer = bc.actual_open()
        
    
    elif message.text.strip() == 'записать на тур' :
        answer = bc.requesting()
        with open(f'data.txt', 'r', encoding='UTF-8') as f:
            act_rec  = f.read().split('\n')
            answer = (act_rec)
    elif message.text.strip() == 'заявка на тур' :
        with open(f'requests.txt', 'r', encoding='UTF-8') as f:
            act_rec  = f.read().split('\n')
            answer = (act_rec)
    
    bot.send_message(message.chat.id, answer)






# Запускаем бота
print('ok')
bot.polling(none_stop=True, interval=0)
