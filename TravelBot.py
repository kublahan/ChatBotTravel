import telebot
from telebot import types
import smtplib
import pymysql

bot = telebot.TeleBot('6283039234:AAGjnW-cTtY0r0aNcUN_J0g2j96FAOpf8kM')

@bot.message_handler(commands=['start'])#Добавили реакцию на команду start
def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Поздороваться")#Кнопка Поздороваться
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я ваш виртуальный справочник по путешествиям".format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(message, func);


@bot.message_handler(content_types=['text'])#Реакция на текст
def func(message):
        if(message.text == "👋 Поздороваться"):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("1 день")
                back = types.KeyboardButton("Вернуться в главное меню")
                markup.add(btn1, back)
                bot.send_message(message.chat.id, text="Как долго вы планируете путешествовать ?", reply_markup=markup)
                bot.register_next_step_handler(message, direction);

        elif(message.text == "Вернуться в главное меню"):
                start(message)
        else:
            bot.send_message(message.chat.id, text="Я вас не понимаю. Для ввода сообщения нажмите на кнопку.")


def direction(message):
    if (message.text == "1 день"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Белорусское направление")
        btn2 = types.KeyboardButton("Казанское направление")
        btn3 = types.KeyboardButton("Курское направление")
        btn4 = types.KeyboardButton("Киевское направление")
        btn5 = types.KeyboardButton("Павелецкое направление")
        btn6 = types.KeyboardButton("Ленинградское направление")
        btn7 = types.KeyboardButton("Савеловское направление")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn2, btn3, btn4, btn5, btn6, btn7, back)
        bot.send_message(message.chat.id, text="Какое направление выбираете ?", reply_markup=markup)
        bot.register_next_step_handler(message, distance);

    elif (message.text == "Вернуться в главное меню"):
        start(message)
    else:
        bot.send_message(message.chat.id, text="Я вас не понимаю. Для ввода сообщения нажмите на кнопку.")


def budget(message):
    if (message.text == "Белорусское направление"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1000 руб")
        btn2 = types.KeyboardButton("1300 руб")
        btn3 = types.KeyboardButton("1200 руб")
        btn4 = types.KeyboardButton("1100 руб")
        btn5 = types.KeyboardButton("900 руб")
        btn6 = types.KeyboardButton("1213 руб")
        btn7 = types.KeyboardButton("752 руб")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn2, btn3, btn4, btn5, btn6, btn7, back)
        bot.send_message(message.chat.id, text="Сколько вы готовы потратить на билет ?", reply_markup=markup)
        bot.register_next_step_handler(message, distance);

    elif (message.text == "Казанское направление"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1000 руб")
        btn2 = types.KeyboardButton("1300 руб")
        btn3 = types.KeyboardButton("1200 руб")
        btn4 = types.KeyboardButton("1100 руб")
        btn5 = types.KeyboardButton("900 руб")
        btn6 = types.KeyboardButton("1213 руб")
        btn7 = types.KeyboardButton("752 руб")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn2, btn3, btn4, btn5, btn6, btn7, back)
        bot.send_message(message.chat.id, text="Сколько вы готовы потратить на билет ?", reply_markup=markup)
        bot.register_next_step_handler(message, distance);

    elif (message.text == "Курское направление"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1000 руб")
        btn2 = types.KeyboardButton("1300 руб")
        btn3 = types.KeyboardButton("1200 руб")
        btn4 = types.KeyboardButton("1100 руб")
        btn5 = types.KeyboardButton("900 руб")
        btn6 = types.KeyboardButton("1213 руб")
        btn7 = types.KeyboardButton("752 руб")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn2, btn3, btn4, btn5, btn6, btn7, back)
        bot.send_message(message.chat.id, text="Сколько вы готовы потратить на билет ?", reply_markup=markup)
        bot.register_next_step_handler(message, distance);

    elif (message.text == "Киевское направление"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1000 руб")
        btn2 = types.KeyboardButton("1300 руб")
        btn3 = types.KeyboardButton("1200 руб")
        btn4 = types.KeyboardButton("1100 руб")
        btn5 = types.KeyboardButton("900 руб")
        btn6 = types.KeyboardButton("1213 руб")
        btn7 = types.KeyboardButton("752 руб")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn2, btn3, btn4, btn5, btn6, btn7, back)
        bot.send_message(message.chat.id, text="Сколько вы готовы потратить на билет ?", reply_markup=markup)
        bot.register_next_step_handler(message, distance);

    elif (message.text == "Павелецкое направление"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1000 руб")
        btn2 = types.KeyboardButton("1300 руб")
        btn3 = types.KeyboardButton("1200 руб")
        btn4 = types.KeyboardButton("1100 руб")
        btn5 = types.KeyboardButton("900 руб")
        btn6 = types.KeyboardButton("1213 руб")
        btn7 = types.KeyboardButton("752 руб")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn2, btn3, btn4, btn5, btn6, btn7, back)
        bot.send_message(message.chat.id, text="Сколько вы готовы потратить на билет ?", reply_markup=markup)
        bot.register_next_step_handler(message, distance);

    elif (message.text == "Ленинградское направление"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1000 руб")
        btn2 = types.KeyboardButton("1300 руб")
        btn3 = types.KeyboardButton("1200 руб")
        btn4 = types.KeyboardButton("1100 руб")
        btn5 = types.KeyboardButton("900 руб")
        btn6 = types.KeyboardButton("1213 руб")
        btn7 = types.KeyboardButton("752 руб")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn2, btn3, btn4, btn5, btn6, btn7, back)
        bot.send_message(message.chat.id, text="Сколько вы готовы потратить на билет ?", reply_markup=markup)
        bot.register_next_step_handler(message, distance);

    elif (message.text == "Савеловское направление"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1000 руб")
        btn2 = types.KeyboardButton("1300 руб")
        btn3 = types.KeyboardButton("1200 руб")
        btn4 = types.KeyboardButton("1100 руб")
        btn5 = types.KeyboardButton("900 руб")
        btn6 = types.KeyboardButton("1213 руб")
        btn7 = types.KeyboardButton("752 руб")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn2, btn3, btn4, btn5, btn6, btn7, back)
        bot.send_message(message.chat.id, text="Сколько вы готовы потратить на билет ?", reply_markup=markup)
        bot.register_next_step_handler(message, distance);

    elif (message.text == "Вернуться в главное меню"):
        start(message)
    else:
        bot.send_message(message.chat.id, text="Я вас не понимаю. Для ввода сообщения нажмите на кнопку.")


def distance(message):
    if (message.text == "Белорусское направление"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1 час от Белорусского вокзала, далее 1,5 км пешком")
        btn2 = types.KeyboardButton("1 час 20  минут от Белорусского вокзала")
        btn3 = types.KeyboardButton("Станция Гагарина, 2 часа 45 минут от Белоруссуого вокзала ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите расстояние", reply_markup=markup)
        bot.register_next_step_handler(message, place);

    elif (message.text == "Казанское направление"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Станция Голутвин,2 часа 10 минут от Казанского вокзала")
        btn2 = types.KeyboardButton("Станция Цемгигант, 1 час 45 минут от Казанского вокзала")
        btn3 = types.KeyboardButton("Станция Кратово, 55 минут от Казанского вокзала")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите расстояние", reply_markup=markup)
        bot.register_next_step_handler(message, place);

    elif (message.text == "Курское направление"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Станция Подольск,55 минут от Курского вокзала")
        btn2 = types.KeyboardButton("Станция Чехов, 1 час 25 минут от Курского вокзала, далее 10 минут на автобусе")
        btn3 = types.KeyboardButton("Станция Серпухов, 1 час 50 минут от Курского вокзала")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите расстояние", reply_markup=markup)
        bot.register_next_step_handler(message, place);

    elif (message.text == "Киевское направление"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Станция Переделкино, 20 минут от Киевского вокзала")
        btn2 = types.KeyboardButton("Станция Бекасово, 1 час 20 минут от Киевского вокзала")
        btn3 = types.KeyboardButton("Станция Балабаново, 1 час 20 минут от Киевского вокзала и 20 минут на автобусе")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите расстояние", reply_markup=markup)
        bot.register_next_step_handler(message, place);

    elif (message.text == "Павелецкое направление"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("15 минут пешком от вокзала")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, back)
        bot.send_message(message.chat.id, text="Выберите расстояние", reply_markup=markup)
        bot.register_next_step_handler(message, place);

    elif (message.text == "Ленинградское направление"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Станция Фирсаново, 42 минуты от Ленинградского вокзала")
        btn2 = types.KeyboardButton("Станция Подсолнечное,1 час 5 минут от Ленинградского вокзала")
        btn3 = types.KeyboardButton("Станция Клин, 1 час 30 минут от Ленинградского вокзала")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите расстояние", reply_markup=markup)
        bot.register_next_step_handler(message, place);

    elif (message.text == "Савеловское направление"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("С Савеловского вокзала до станции Долгопрудный, далее пешком")
        btn2 = types.KeyboardButton("С Савеловского вокзала до станции Долгопрудный, далее пешком")
        btn3 = types.KeyboardButton("С Савеловского вокзала до станции Катуар, затем на автобусе")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите расстояние", reply_markup=markup)
        bot.register_next_step_handler(message, place);


    elif (message.text == "Вернуться в главное меню"):
        start(message)
    else:
        bot.send_message(message.chat.id, text="Я вас не понимаю. Для ввода сообщения нажмите на кнопку.")



def place(message):
    if (message.text == "1 час от Белорусского вокзала, далее 1,5 км пешком"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Я предлагаю вам отправиться в Танковый музей", reply_markup=markup)

    elif (message.text == "1 час 20  минут от Белорусского вокзала"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Я предлагаю вам отправиться в Город Звенигород", reply_markup=markup)

    elif (message.text == "Станция Гагарина, 2 часа 45 минут от Белоруссуого вокзала"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Я предлагаю вам отправиться в Изба-музей Юрия Гагарина", reply_markup=markup)

    elif (message.text == "Станция Голутвин,2 часа 10 минут от Казанского вокзала"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Я предлагаю вам отправиться в Музейная фабрикапостилы", reply_markup=markup)

    elif (message.text == "Станция Цемгигант, 1 час 45 минут от Казанского вокзала"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Я предлагаю вам отправиться в Месторождение фосфорида ", reply_markup=markup)

    elif (message.text == "Станция Кратово, 55 минут от Казанского вокзала"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Я предлагаю вам отправиться в Красивые дачные поселки ", reply_markup=markup)

    elif (message.text == "Станция Подольск,55 минут от Курского вокзала"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Я предлагаю вам отправиться в Усадьба Дубровицы с храмом Пресвятой Богородицы", reply_markup=markup)

    elif (message.text == "Станция Чехов, 1 час 25 минут от Курского вокзала, далее 10 минут на автобусе"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Я предлагаю вам отправиться в Музей-усадьба Чехова", reply_markup=markup)

    elif (message.text == "Станция Серпухов, 1 час 50 минут от Курского вокзала"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Я предлагаю вам отправиться в Художественный музей", reply_markup=markup)

    elif (message.text == "Станция Переделкино, 20 минут от Киевского вокзала"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Я предлагаю вам отправиться в Дом творчества писателей Пастернака, Чуковского ", reply_markup=markup)

    elif (message.text == "Станция Бекасово, 1 час 20 минут от Киевского вокзала"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Я предлагаю вам отправиться в Большое железнодорожное кольцо", reply_markup=markup)

    elif (message.text == "Станция Балабаново, 1 час 20 минут от Киевского вокзала и 20 минут на автобусе"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Я предлагаю вам отправиться в Свято-Пафнутьев Боровский монастырь", reply_markup=markup)

    elif (message.text == "15 минут пешком от вокзала"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Я предлагаю вам отправиться в Кинотеатр <<Пять звезд>>", reply_markup=markup)

    elif (message.text == "Станция Фирсаново, 42 минуты от Ленинградского вокзала"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Я предлагаю вам отправиться в Съемочная площадка 18 века", reply_markup=markup)

    elif (message.text == "Станция Подсолнечное,1 час 5 минут от Ленинградского вокзала"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Я предлагаю вам отправиться в Крупное озеро в Подмосковье <<Сенеж>>", reply_markup=markup)

    elif (message.text == "Станция Клин, 1 час 30 минут от Ленинградского вокзала"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Я предлагаю вам отправиться в Музей-усадьба композитора Чайковского", reply_markup=markup)

    elif (message.text == "С Савеловского вокзала до станции Долгопрудный, далее пешком"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Я предлагаю вам отправиться в Дом Банзы или в Дом-усадьба Мысово", reply_markup=markup)


    elif (message.text == "С Савеловского вокзала до станции Катуар, затем на автобусе"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Марфино", reply_markup=markup)


    elif (message.text == "Вернуться в главное меню"):
        start(message)
    else:
        bot.send_message(message.chat.id, text="Я вас не понимаю. Для ввода сообщения нажмите на кнопку.")

bot.polling(none_stop=True, interval=0)