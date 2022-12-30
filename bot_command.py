
from telebot import types


def starting():
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item1 = types.KeyboardButton("Актуальный набор")
    item2 = types.KeyboardButton("записать на тур")
    item3 = types.KeyboardButton("заявка на тур")
    markup.add(item1, item2, item3)
    return markup


def numbers():
    markup = types.ReplyKeyboardMarkup(row_width=4)
    item1 = types.KeyboardButton("1")
    item2 = types.KeyboardButton("2")
    item3 = types.KeyboardButton("3")
    item4 = types.KeyboardButton("4")
    item5 = types.KeyboardButton("5")
    item6 = types.KeyboardButton("6")
    item7 = types.KeyboardButton("7")
    item8 = types.KeyboardButton("8")
    item9 = types.KeyboardButton("9")
    item10 = types.KeyboardButton("10")
    item11 = types.KeyboardButton("11")
    markup.add(item1, item2, item3, item4, item5, item6,
               item7, item8, item9, item10, item11)
    # for i in range(1, 12):
    #     item = types.KeyboardButton(i)
    #     markup.add(item)
    return markup


def act_list(name):
    listt = actual_open(name).split('\n')
    newlist = []
    for i in listt:
        a = i.split()
        newlist.append(a)
    return newlist


def datbutton(data_file):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    newlist = act_list(data_file)
    for item in newlist:
        markup.add(types.KeyboardButton(f"{item[0]}"))
    return (markup)


def actual_open(name):
    with open(f'{name}.txt', 'r', encoding='UTF-8') as f:
        act_rec = f.read()
        return act_rec


def dating_count(trip, data_file):
    newlist = act_list(data_file)
    for item in newlist:
        if trip == item[0]:
            return item


def writing(amount, trip):
    listt = act_list('act_recruiting')
    new_list_act = []
    new = ''
    for item in listt:
        if trip == item[0]:
            item[1] = int(item[1]) - int(amount)
            item[1] = str(item[1])
            new = ' '.join(item)
        else:
            new = ' '.join(item)
        new_list_act.append(new)
        new = ''
    new = '\n'.join(new_list_act)
    with open(f'act_recruiting.txt', 'w', encoding='UTF-8') as f:
        f.write(new)
    return f"Записал на {trip} {amount} человек(а). Введите контакты туристов"


def recording_contacts(amount, trip, first_name, contacts):

    with open(f'data.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{trip} - {amount} человек от {first_name}\n{contacts}\n')
    return "Записал! Что дальше? /start"


def writing_trips(amount, trip, first_name, day, contacts):

    with open(f'requests.txt', 'a', encoding='UTF-8') as f:
        f.write(
            f'{trip} - {amount} человек от {first_name} дата: {day}\n{contacts}\n')
    return "Записал! Что дальше? /start"
