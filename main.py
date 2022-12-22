import telebot
from telebot import types
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_command as bc


bot = telebot.TeleBot('5976873878:AAHtM8grXOPnWNqvXvllQN10hK36VfdMoo4')


@bot.message_handler(commands=["start"])
# Получение сообщений от юзера
def start(m, res=False):
        # Добавляем кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Актуальный набор")
        item2=types.KeyboardButton("записать на тур")
        item3=types.KeyboardButton("заявка на тур")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(m.chat.id, 'Нажми: \n"Актуальный набор" для получения информации о набираемых турах и свободных местах\nзаписать на тур — для записи туриста на тур(только после оплаты/предоплаты)\n заявка на тур - для создания заявки на набор тура',  reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему список на набор
    if message.text.strip() == 'Актуальный набор' :
        with open(f'act_recruiting.txt', 'r', encoding='UTF-8') as f:
            act_rec  = f.read()
            answer = (act_rec)
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'записать на тур' :
        with open(f'data.txt', 'r', encoding='UTF-8') as f:
            act_rec  = f.read().split('\n')
            answer = (act_rec)
    elif message.text.strip() == 'заявка на тур' :
        with open(f'requests.txt', 'r', encoding='UTF-8') as f:
            act_rec  = f.read().split('\n')
            answer = (act_rec)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)






# Запускаем бота
print('ok')
bot.polling(none_stop=True, interval=0)
