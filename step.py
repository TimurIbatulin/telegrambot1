
import telebot
import bot_command as bc

API_TOKEN = ""

bot = telebot.TeleBot(API_TOKEN)

trip_dict = {}


class User:
    def __init__(self, trip):
        self.trip = trip
        self.amount = None


@bot.message_handler(content_types=["text"])
def send_welcome(message):
    msg = bot.reply_to(message, 'На какой тур записываем?',
                       reply_markup=bc.datbutton("act_recruiting"))
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    try:
        an = bc.dating_count(message.text, 'act_recruiting')
        chat_id = message.chat.id
        trip = message.text
        user = User(trip)
        trip_dict[chat_id] = user
        amount = an[1]
        user.amount = amount

        msg = bot.reply_to(
            message, f'Осталось только {amount}, сколько записываем?', reply_markup=bc.numbers())
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_age_step(message):
    try:
        chat_id = message.chat.id
        amount_new = message.text
        if not amount_new.isdigit():
            msg = bot.reply_to(
                message, 'Должно быть число. Нажми на нужную кнопку')
            bot.register_next_step_handler(msg, process_age_step)
            return
        user = trip_dict[chat_id]
        trip = user.trip
        user.amount = amount_new
        a = bc.writing(amount_new, trip)
        msg = bot.reply_to(
            message, a)
        bot.register_next_step_handler(msg, process_recording_contacts_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_recording_contacts_step(message):
    try:
        chat_id = message.chat.id
        user = trip_dict[chat_id]
        trip = user.trip
        amount = user.amount
        contacts = message.text
        a = bc.recording_contacts(
            amount, trip, message.from_user.first_name, contacts)
        bot.send_message(chat_id, a)
    except Exception as e:
        bot.reply_to(message, 'oooops')


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

bot.infinity_polling()
