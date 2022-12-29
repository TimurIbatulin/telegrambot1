
import tokenn as t
import telebot
import bot_command as bc


bot = telebot.TeleBot(t.token())

trip_dict = {}


class User:
    def __init__(self, trip):
        self.trip = trip
        self.amount = None
        self.day = None


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Нажми: \n"Актуальный набор" для получения информации о набираемых турах и свободных местах\nзаписать на тур — для записи туриста на тур(только после оплаты/предоплаты)\n заявка на тур - для создания заявки на набор тура', reply_markup=bc.starting())


@bot.message_handler(content_types=["text"])
def handle_text(message):

    if message.text == 'Актуальный набор':
        bot.reply_to(message, bc.actual_open('act_recruiting'))
    elif message.text == 'записать на тур':
        msg = bot.reply_to(message, 'На какой тур записываем?',
                           reply_markup=bc.datbutton("act_recruiting"))
        bot.register_next_step_handler(msg, process_act_rec_step)
    elif message.text == 'заявка на тур':
        msg = bot.reply_to(message, 'На какой тур заявку делаем?',
                           reply_markup=bc.datbutton("trips"))
        bot.register_next_step_handler(msg, process_trips_step)
    else:
        bot.send_message(
            message.chat.id, "я не знаааааю что делать, начни сначала /start")


def process_trips_step(message):
    try:
        an = bc.dating_count(message.text, "trips")
        chat_id = message.chat.id
        trip = message.text
        user = User(trip)
        trip_dict[chat_id] = user
        amount = an[1]
        user.amount = amount
        msg = bot.reply_to(
            message, f'Осталось только {amount}, сколько записываем?', reply_markup=bc.numbers())
        bot.register_next_step_handler(msg, process_trips_amount_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_trips_amount_step(message):
    try:
        chat_id = message.chat.id
        amount_new = message.text
        user = trip_dict[chat_id]
        user.amount = amount_new
        msg = bot.reply_to(message, 'На какую дату заявку делаем?')
        bot.register_next_step_handler(msg, process_trips_day_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_trips_day_step(message):
    try:
        chat_id = message.chat.id
        day = message.text
        user = trip_dict[chat_id]
        user.day = day
        msg = bot.reply_to(message, 'Введите контакты туристов?')
        bot.register_next_step_handler(msg, process_trips_contacts_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_trips_contacts_step(message):
    try:
        chat_id = message.chat.id
        user = trip_dict[chat_id]
        contacts = message.text
        trip = user.trip
        day = user.day
        amount = user.amount
        a = bc.writing_trips(
            amount, trip,  message.from_user.first_name, day, contacts)
        bot.send_message(chat_id, a)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_act_rec_step(message):
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
        bot.register_next_step_handler(msg, process_amount_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_amount_step(message):
    try:
        chat_id = message.chat.id
        amount_new = message.text
        user = trip_dict[chat_id]
        trip = user.trip
        user.amount = amount_new
        a = bc.writing(amount_new, trip)
        msg = bot.reply_to(message, a)
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
print('ok')
bot.infinity_polling()
