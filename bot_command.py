import telebot
from telebot import types
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


def starting(m, res):
        # Добавляем кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Актуальный набор")
        item2=types.KeyboardButton("записать на тур")
        item3=types.KeyboardButton("заявка на тур")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        return (markup)

def datbutton():
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        listt = actual_open().split('\n')
        newlist = []
        for i in listt:
                a = i.split()
                newlist.append(a)
        for item in newlist:
                markup.add(types.KeyboardButton(f"{item[0]}"))
        return (markup)


        

        
        
        item2=types.KeyboardButton("записать на тур")
        item3=types.KeyboardButton("заявка на тур")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)


def actual_open ():
        with open(f'act_recruiting.txt', 'r', encoding='UTF-8') as f:
                act_rec  = f.read()
                answer = (act_rec)
                return answer

# def dating():
#         with open(f'data.txt', 'a', encoding='UTF-8') as f:



# def requesting():
#         with open(f'requests.txt', 'w', encoding='UTF-8') as f:


listt = actual_open().split('\n')
newlist = []
for i in listt:
        a = i.split()
        newlist.append(a)
for item in newlist:
        print (item[0])


