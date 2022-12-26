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


def numbers():
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        for i in range(12):
                item=types.KeyboardButton(i)
                markup.add(item)

        return (markup)

def act_list(name):
        listt = actual_open(name).split('\n')
        newlist = []
        for i in listt:
                a = i.split()
                newlist.append(a)
        return newlist


def datbutton():
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        newlist = act_list('act_recruiting')
        for item in newlist:
                markup.add(types.KeyboardButton(f"{item[0]}"))
        return (markup)

def regbutton():
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        newlist = act_list('trips')
        for item in newlist:
                markup.add(types.KeyboardButton(f"{item[0]}"))
        return (markup)



def actual_open (name):
        with open(f'{name}.txt', 'r', encoding='UTF-8') as f:
                act_rec  = f.read()
                answer = (act_rec)
                return answer

def dating_count(trip):
        newlist = act_list('act_recruiting')
        for item in newlist:
                if trip == item[0]:
                        tripdate = trip
                        tripdate 
                        return item[1]

def requests_count(trip):
        newlist = act_list('trips')

        for item in newlist:
                if trip == item[0]:
                        tripreg = trip
                        tripreg
                        return item[1]

def writing(i, id):
        print (tripdate, tripreg)
        if tripdate != None:
                with open(f'data.txt', 'a', encoding='UTF-8') as f:
                        f.write(f'{tripdate} - {i} человек от {id}')
                
                listt = act_list('act_recruiting')
                newlistact = []
                new = ''
                for item in listt:
                        if tripdate == item[0]:
                                item[1] = int(item[1]) - int(i)
                                str(item[1])
                                new = ''.join(item)
                        else:
                                new = ''.join(item)
                        newlistact.append(new)
                        new = ''
                new = '\n'.join(newlistact)
                with open(f'act_recruiting.txt', 'w', encoding='UTF-8') as f:
                        f.write(new)
                return "ок"
        elif tripreg != None:
                with open(f'requests.txt', 'a', encoding='UTF-8') as f:
                        f.write(f'{tripdate} - {i} человек от {id}')
                               
                return "ок"
        else:
                return 'не ок'


