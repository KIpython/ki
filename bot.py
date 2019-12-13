#Импорт модулей
import random
import telebot
from telebot.types import Message
from telebot import types
from telebot.types import KeyboardButton
from telebot.types import ReplyKeyboardMarkup

bot = telebot.TeleBot("772032411:AAFgTaXmyu3lggm7RC5oATBz_MJqvzNGkvE") #Токен


@bot.message_handler(commands=["start"])					#Приветственное сообщение
def send_welcome(message):									#Приветственное сообщение
    bot.send_message(										#Приветственное сообщение
        message.chat.id,									#Приветственное сообщение
        '''◾️ Здравствуйте, для продолжения подтвердите свой возраст.
🔞 Нажимая на кнопку «Мне есть 18», Вы подтверждаете наличие 18 лет.
⌛️ Работаем каждый день с 10:00 - 23:00.''', reply_markup=keyboardyears()); 	#Приветственное сообщение


#bot.send_photo(message.chat.id, open('ok.jpg', 'rb'));     #Отправка фото при приветствование (По желанию заказчика)

def keyboardyears():										#Клавиатура
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Мне больше 18 лет")			#Клавиатура
    btn2 = types.KeyboardButton(text='''Мне меньше 18 лет''')			#Клавиатура
    markup.add(btn1, btn2)
    return markup 

def keyboardgohome():										#Клавиатура
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    home = types.KeyboardButton(text="Домой 🏠")			#Клавиатура
    markup.add(home)
    return markup                                        #Клавиатура

def keyboardmenu():										#Клавиатура
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    city1 = types.KeyboardButton(text="Каталог🗂")			#Клавиатура
    cityone = types.KeyboardButton(text="Новости")			#Клавиатура
    citytwo = types.KeyboardButton(text="Информационный Бот")
    citythree = types.KeyboardButton(text="Контакты📞")
    cityfour = types.KeyboardButton(text="Диспетчер📱")
    markup.add(city1, cityone, citythree, cityfour, citytwo)
    return markup                                           #Клавиатура
   
def keyboardsalytgo1():										#Клавиатура
	markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
	salytgohome = types.KeyboardButton(text="Ещё 5")
	salytgo5 = types.KeyboardButton(text="Домой 🏠")			#Клавиатура
	markup.add(salytgohome, salytgo5)
	return markup    

def keyboardsalytgo2():										#Клавиатура
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    salytgohome1 = types.KeyboardButton(text="🔸Ещё 5")			#Клавиатура
    salytgo51 = types.KeyboardButton(text="Домой 🏠")			#Клавиатура
    markup.add(salytgohome1, salytgo51)
    return markup   

def keyboardsalytgo4():										#Клавиатура
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    salytgohome24 = types.KeyboardButton(text="▪️Ещё 5")			#Клавиатура
    salytgo524 = types.KeyboardButton(text="Домой 🏠")			#Клавиатура
    markup.add(salytgohome24, salytgo524)
    return markup       

def keyboardsalytgo3():										#Клавиатура
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    salytgohome12 = types.KeyboardButton(text="🔹Ещё 5")			#Клавиатура
    salytgo512 = types.KeyboardButton(text="Домой 🏠")			#Клавиатура
    markup.add(salytgohome12, salytgo512)
    return markup 

def keyboardsalytgo5():										#Клавиатура
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    salytgohome35 = types.KeyboardButton(text="▫️Ещё 5")			#Клавиатура
    salytgo535 = types.KeyboardButton(text="Домой 🏠")			#Клавиатура
    markup.add(salytgohome35, salytgo535)
    return markup  

def keyboardsalytgo6():										#Клавиатура
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    salytgohome46 = types.KeyboardButton(text="🔻Ещё 5")			#Клавиатура
    salytgo546 = types.KeyboardButton(text="Домой 🏠")			#Клавиатура
    markup.add(salytgohome46, salytgo546)
    return markup   

def keyboardpetgo1():										#Клавиатура
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    petgohome47 = types.KeyboardButton(text="🔘Ещё 5")			#Клавиатура
    spetgo547 = types.KeyboardButton(text="Домой 🏠")			#Клавиатура
    markup.add(petgohome47, spetgo547)
    return markup 




def keyboardcatalog():										#Клавиатура
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    city12 = types.KeyboardButton(text="Бенгальские🎇")			#Клавиатура
    cityone2 = types.KeyboardButton(text="Петарды💥")			#Клавиатура
    citytwo2 = types.KeyboardButton(text="Римские свечи")
    citythree2 = types.KeyboardButton(text="Салют🎆")
    cityfour2 = types.KeyboardButton(text="Фонтан/фаер🎉")
    cityfive2 = types.KeyboardButton(text="Домой 🏠")
    markup.add(city12, cityone2, citythree2, cityfour2, citytwo2, cityfive2)
    return markup  
                                       #Клавиатура

@bot.message_handler(content_types=['text'])				#Ответы на слова
def send_text(message):						
	if message.text == 'Домой 🏠':					#Ответы на слова
   		bot.send_message(message.chat.id, ''' ◾️ Здравствуйте, для продолжения подтвердите свой возраст.
🔞 Нажимая на кнопку «Мне есть 18», Вы подтверждаете наличие 18 лет.
⌛️ Работаем каждый день с 10:00 - 23:00. ''', reply_markup=keyboardyears());
	if message.text == 'Мне больше 18 лет':					#Ответы на слова
		bot.send_message(message.chat.id, ''' Вы перешли в раздел «Меню» 
⚙️ Выберите из списка интересующую Вас кнопку. ''', reply_markup=keyboardmenu());
	if message.text == 'Мне меньше 18 лет':					#Ответы на слова
		bot.send_message(message.chat.id, ''' Нам очень жаль, но, к сожалению, Вы не достигли возраста совершеннолетия (18 лет).
Если же Вы ошиблись с выбором, либо Вам исполнилось 18 лет, Вы всегда можете нажать на кнопку «Домой 🏠» ''', reply_markup=keyboardgohome());
	if message.text == '📱 Главное меню':					#Ответы на слова
		bot.send_message(message.chat.id, 'Вы в главном меню', reply_markup=keyboardmenu());
	if message.text == 'Каталог🗂':				
		bot.send_message(message.chat.id, ''' ⚙️ Вы перешли в раздел формирования заказа.
❗️ Выберите услугу, которой хотите воспользоваться ❗️ ''', reply_markup=keyboardcatalog());
	




	if message.text == 'Бенгальские🎇':				
		bot.send_photo(message.chat.id, open('images/free_1.jpg', 'rb'));	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить", callback_data="one_1")
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Бенгальские огни Неон Видео:''', reply_markup=keyboard);
		bot.send_message(message.chat.id, '''Цена 50р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

		bot.send_photo(message.chat.id, open('images/free_2.jpg', 'rb'));	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить", callback_data="one_1")
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Бенгальская свеча 20 см Видео:''', reply_markup=keyboard);
		bot.send_message(message.chat.id, '''Цена 30р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

		bot.send_photo(message.chat.id, open('images/free_3.jpg', 'rb'));	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить", callback_data="one_1")
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Бенгальские огни 40 см Видео:https://www.youtube.com/watch?v=Lge0r3oJZgY&feature=youtu.be''', reply_markup=keyboard);	
		bot.send_message(message.chat.id, '''Цена 250р по курсу призм на день покупки
Курс призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

		bot.send_photo(message.chat.id, open('images/free_4.jpg', 'rb'));	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить", callback_data="one_1")
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Бенгальские огни 65 см Видео:https://www.youtube.com/watch?v=wSZ6uUROZsM&t=1s''', reply_markup=keyboard);	
		bot.send_message(message.chat.id, '''Цена 350р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	if message.text == 'Новости':									#Ответы на слова
		bot.send_message(message.chat.id, 'Тут будут новости');				#Ответы на слова
	if message.text == 'Подарки🎁':									#Ответы на слова
		bot.send_message(message.chat.id, 'Тут будет описание подарков');				#Ответы на слова
	#САЛЮТЫ
	


	if message.text == 'Салют🎆':
	
	#САЛЮТ (ТОВАР 1)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_1.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Далматин 40 залпов, калибр 1 Видео: https://youtu.be/NaDkdwtf4hE''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 3500р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 2)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_2.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Настоящий 100 залпов, калибр 1,2 Видео:https://youtu.be/PYwGgN3bXHo''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 11000р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 3)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_3.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Париж 36 залпов, калибр 1,2 Видео: https://youtu.be/BTPZNenRyZU''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 4500р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 4)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_4.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Бой курантов 49 залпов, калибр 1,2 Видео: https://youtu.be/YywpzdhtjYs''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 5500р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 5)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_5.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Молния 25, залпов,калибр 1,2 Видео: https://youtu.be/aae1DC-U8jE''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 3000р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''', reply_markup=keyboardsalytgo1());	#ОПИСАНИЕ


	if message.text == 'Ещё 5':
	#САЛЮТ (ТОВАР 6)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_6.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Пироград 49 залпов, калибр 2 - Мощный высотный салют Видео: https://youtu.be/6btHl13yQzs''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 16000р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 7)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_7.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Красочное шоу 180 залпов, калибр 0,8 Видео:https://youtu.be/EUrCSczef0c''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 8500р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 8)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_8.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Азарт 100 залпов, калибр 0.8  Видео:https://youtu.be/TnZPe8EPUec''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 5000р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 9)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_9.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Артиллерия 1.75 Видео:''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 1600р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 10)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_10.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Ракеты Сатурн 25 выстрелов Видео:''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 100р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''', reply_markup=keyboardsalytgo2());	#ОПИСАНИЕ 

	if message.text == '🔸Ещё 5':
	#САЛЮТ (ТОВАР 11)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_11.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Новатор 42 х 0.9-1.1.2 сборка Видео: https://www.youtube.com/watch?time_continue=52&v=..''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 3300р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 12)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_12.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Пиро магия 25 х 1 Видео:https://youtu.be/pTU180h9dMA''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 1850р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 13)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_13.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Фейерверк Счастливчик 25 залпов Видео:https://youtu.be/BCNn-8l4b54''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 250р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 14)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_14.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Фейерверк Счастливчик 49 залпов Видео:https://youtu.be/BCNn-8l4b54''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 500р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 15)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_15.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Ночной Город 16 х 1 Видео:https://youtu.be/LW4_NHIoLXo''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 1100р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''', reply_markup=keyboardsalytgo3());	#ОПИСАНИЕ  

	if message.text == '🔹Ещё 5':
    #САЛЮТ (ТОВАР 16)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_16.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Мега Хит 57 х 1, 1,2 -  разнокалиберный + веер Видео:https://youtu.be/HUd8aSMicYA''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 6700р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ
	#САЛЮТ (ТОВАР 17)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_17.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Манипулятор 16 х 1,2 Видео:https://youtu.be/4FcU5VYbp_c''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 1800р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 18)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_18.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Мега шоу 142 х 1,2 +  веерный Видео: https://youtu.be/pWr6Fkf3M1w''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 18500р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 19)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_19.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Сомбреро 12 х 0.8 Видео: https://youtu.be/hvy-EM7ZZ2Q''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 600р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 20)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_20.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Солнечный зайчик 1.2 х 16 Видео: https://youtu.be/86fMpse0koM''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 1850р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''', reply_markup=keyboardsalytgo4());	#ОПИСАНИЕ 

	if message.text == '▪️Ещё 5':
	#САЛЮТ (ТОВАР 21)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_21.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Топ-2. 36 х 1 + веерный Видео: https://www.youtube.com/watch?v=x80S1Uwvy70''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 3000р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 22)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_22.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Супер шоу 108 х 1 + веерый Видео: https://youtu.be/vrdxmyD0SYo''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 10000р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 23)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_23.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Черная Борода 99 х 1 Видео:https://youtu.be/0bhqjqEiEa4''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 8500р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 24)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_24.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Супер звезда 16 х 0.8 Видео:https://www.youtube.com/watch?v=GyecKi8wIhY''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 750р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 25)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_25.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Мульт - 17. 49 х 0.8 Видео: https://youtu.be/l_RjsWs6vZA''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 2500р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''', reply_markup=keyboardsalytgo5());	#ОПИСАНИЕ 

	if message.text == '▫️Ещё 5':
	#САЛЮТ (ТОВАР 26)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_26.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Рождественская История 19 х 1 Видео: https://youtu.be/RkzKSDt03V8''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 1250р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 27)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_27.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Мираж 49 х 0.8 Видео:https://www.youtube.com/watch?v=94mnNzQp9X4''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 2500р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 28)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_28.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Блиц 16 х 0.8 Видео:https://youtu.be/edd2idI8NKg''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 800р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 29)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_29.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Девятнашка 1,2 х 19 Видео: https://youtu.be/lW-3xwjL5Es''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 2000р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 30)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_30.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Байконур 100 х 0.8 Видео: https://youtu.be/9gCWlGMFBqw''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 5000р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''', reply_markup=keyboardsalytgo6());	#ОПИСАНИЕ

	if message.text == '🔻Ещё 5':

	#САЛЮТ (ТОВАР 31)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_31.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Энигма 1,2 х 36 залпов Видео:https://youtu.be/sp2aG_t_oGE''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 4000р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 32)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_32.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Винни Пух 36 залпов,калибр 38 мм Видео: https://www.youtube.com/watch?v=HPsnMlb11J4&featu..''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 7500р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 33)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_33.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Ну Погоди 25,калибр 38 мм Видео:https://youtu.be/52H80zXiy24''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 5500р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 34)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_34.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Резонанс 28 залпов,калибр 30 мм Видео:https://youtu.be/7EjFjCGtaeM''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 3500р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 35)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_35.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Легенда 25 залпов,калибр 30 мм Видео:https://youtu.be/A6aZ9gBrmHM''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 3300р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''', reply_markup=keyboardsalytgo7());	#ОПИСАНИЕ

	if message.text == '🔺Ещё 5':
	#САЛЮТ (ТОВАР 36)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_36.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Пиро Танец, калибр 20 мм Видео:https://www.youtube.com/watch?v=WD1PpSOWhxU&featu..''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 1250р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 37)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_37.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Летучий Голандец 48 залпов Видео:https://youtu.be/YIeKNl45Hy4''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 5500р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 38)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_38.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Юбиляр 50 залпов, калибр 26 мм Видео:https://youtu.be/4mb8O1G11rk''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 3950р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 39)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_39.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Слезы Ангела 36 залпов, калибр 26 мм Видео:https://www.youtube.com/watch?v=HEeUlZav2YQ''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 2750р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАP 40)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_40.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Тайник с Золотом 100 залпов,калибр 20 мм Видео:https://www.youtube.com/watch?v=TxibiV7UrCg''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 5000р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ

	#САЛЮТ (ТОВАР 41)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/one_41.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Салют Пиро Радуга 19 залпов, калибр 20 мм Видео:https://www.youtube.com/watch?v=BVHnBzcHbfA&featu..4''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 1000р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''', reply_markup=keyboardgohome());	#ОПИСАНИЕ

	

	if message.text == 'Петарды💥':					
		#Петарды💥 (ТОВАР 1)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/two_1.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Петарды Оригинал Видео:https://youtu.be/2X9uSuKITSg''', reply_markup=keyboard);	#ОПИСАНИЕ			
		bot.send_message(message.chat.id, '''Цена 220р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ  

		#Петарды💥 (ТОВАР 2)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/two_2.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Пулеметная лента 90 выстрелов Видео:''', reply_markup=keyboard);	#ОПИСАНИЕ			
		bot.send_message(message.chat.id, '''Цена 100р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ  

		#Петарды💥 (ТОВАР 3)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/two_3.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Петарды Кирдык - мощный взрыв Видео:https://youtu.be/MKDXJBCK62o''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 200р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ  

		#Петарды💥 (ТОВАР 4)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/two_4.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Ракеты свистульки Видео: ''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 100р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ  

		#Петарды💥 (ТОВАР 5)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/two_5.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Ракеты два цвета Видео:''', reply_markup=keyboard);	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 500р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ  

		#Петарды💥 (ТОВАР 6)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/two_6.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Хлопок Видео:https://youtu.be/s8WsxtruHUc''', reply_markup=keyboardpetgo1());	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 100р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''', reply_markup=keyboardpetgo1());	#ОПИСАНИЕ  


	if message.text == '🔘Ещё 5':

		#Петарды💥 (ТОВАР 7)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/two_7.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Петарды Квадро Бум 20 шт''');	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 450р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ  

		#Петарды💥 (ТОВАР 8)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/two_8.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Петарды Корсар 1''');	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 50р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ  

		#Петарды💥 (ТОВАР 9)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/two_9.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Петарды Шухер Видео:''', reply_markup=keyboardgohome());	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 350р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''', reply_markup=keyboardgohome());	#ОПИСАНИЕ  

		#Петарды💥 (ТОВАР 10)									#Ответы на слова
		bot.send_photo(message.chat.id, open('images/two_10.jpg', 'rb')); #КАРТИНКА	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить PZM ", callback_data="one_1") #КНОПКА
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Петарды Атас Видео:''', reply_markup=keyboardgohome());	#ОПИСАНИЕ
		bot.send_message(message.chat.id, '''Цена 300р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''', reply_markup=keyboardgohome());	#ОПИСАНИЕ  






	if message.text == 'Римские свечи':	
		bot.send_photo(message.chat.id, open('images/four_1.jpg', 'rb'));	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить", callback_data="one_1")
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Римская свеча 04 х 100 Видео: https://youtu.be/0sSZYdRAAIE''', reply_markup=keyboard);
		bot.send_message(message.chat.id, '''Цена 700р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ  

		bot.send_photo(message.chat.id, open('images/four_2.jpg', 'rb'));	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить", callback_data="one_1")
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Римская свеча 2 х 8 Видео: https://youtu.be/zV6qmAe15yk''', reply_markup=keyboard);
		bot.send_message(message.chat.id, '''Цена 2000р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ  

		bot.send_photo(message.chat.id, open('images/four_3.jpg', 'rb'));	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить", callback_data="one_1")
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Римская Свеча 1.2 х 8 Видео:https://youtu.be/zV6qmAe15yk''', reply_markup=keyboard);	
		bot.send_message(message.chat.id, '''Цена 700р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ  


		bot.send_photo(message.chat.id, open('images/four_4.jpg', 'rb'));	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить", callback_data="one_1")
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Римская Свеча 8 х 0.8 Видео:https://youtu.be/_g8d0ioS9cc''', reply_markup=keyboard);	
		bot.send_message(message.chat.id, '''Цена 300р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''', reply_markup=keyboardgohome());	#ОПИСАНИЕ  


	if message.text == 'Фонтан/фаер🎉':				
		bot.send_photo(message.chat.id, open('images/five_1.jpg', 'rb'));	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить", callback_data="one_1")
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Фонтан Арарат Видео:https://youtu.be/N-V5xhh03KQ''', reply_markup=keyboard);
		bot.send_message(message.chat.id, '''Цена 250р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ  


		bot.send_photo(message.chat.id, open('images/five_2.jpg', 'rb'));	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить", callback_data="one_1")
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Стробофаер 90 секунд Видео:https://youtu.be/GmM6QYK2T8A''', reply_markup=keyboard);
		bot.send_message(message.chat.id, '''Цена 200р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ  


		bot.send_photo(message.chat.id, open('images/five_3.jpg', 'rb'));	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить", callback_data="one_1")
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Фаер Ультрас 60 сек без чеки Видео:''', reply_markup=keyboard);	
		bot.send_message(message.chat.id, '''Цена 200р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ  


		bot.send_photo(message.chat.id, open('images/five_4.jpg', 'rb'));	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить", callback_data="one_1")
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Фонтаны в торт 12 см - 12 штук в упаковке Видео:''', reply_markup=keyboard);	
		bot.send_message(message.chat.id, '''Цена 350р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ  


		bot.send_photo(message.chat.id, open('images/five_5.jpg', 'rb'));	
		keyboard = types.InlineKeyboardMarkup(row_width=1)
		first_button = types.InlineKeyboardButton(text="Оплатить", callback_data="one_1")
		keyboard.add(first_button)	
		bot.send_message(message.chat.id, '''Фаер Ультрас 60 сек без чеки Видео:''', reply_markup=keyboard);	
		bot.send_message(message.chat.id, '''Цена 700р по курсу призм на день покупки
Курc призм: @KursPrizmEveryMinute''');	#ОПИСАНИЕ  


































	if message.text == 'Информационный Бот':									#Ответы на слова
		bot.send_message(message.chat.id, '📝 Вы перешли в раздел «Информационный Бот»', reply_markup=keyboardgohome());	
		keyboard = types.InlineKeyboardMarkup()
		first_button = types.InlineKeyboardButton(text="➡️Перейти", url="https://t.me/PiroGradInfo_bot")
		keyboard.add(first_button)
		bot.send_message(message.chat.id,'''▶️ Вы хотите перейти в «Информационный Бот»?''', reply_markup=keyboard);
	if message.text == 'Диспетчер📱':									#Ответы на слова
		bot.send_message(message.chat.id, '📝 Вы перешли в раздел «Связь с диспетчером»', reply_markup=keyboardgohome());	
		keyboard = types.InlineKeyboardMarkup()
		first_button = types.InlineKeyboardButton(text="📞Связаться", url="https://t.me/Pavelkuzmin1912")
		keyboard.add(first_button)
		bot.send_message(message.chat.id,'''▶️ Вы хотите связаться с диспетчером?''', reply_markup=keyboard);
	if message.text == 'Контакты📞':									#Ответы на слова
		bot.send_message(message.chat.id, '''Связаться с нами | Пиро-град.рф
Контакты для связи:
@saprone
@Pavelkuzmin1912
Тел: +79643957383
Многоканальный : +7(812) 408-26-81
Почта: pavel.interstroi@yandex.ru
 ООО"ПИРОГРАД". ИНН: 7811728227
Самовывоз в Санкт-Петербурге:
1. Станция метро ул.Дыбенко, Кудрово, ул. Ленинградская, дом 1 (напротив Макдональдс)
2. Станция метро Бухарестская, ул. Салова, дом 70 (большое здание автоцентра, центральный вход)''', reply_markup=keyboardgohome());	
	if message.text == 'бот':									#Ответы на слова
		bot.send_message(message.chat.id, 'Выберите город:', reply_markup=keyboardgohome());	
	if message.text == '':									#Ответы на слова
		bot.send_message(message.chat.id, 'Выберите город:', reply_markup=keyboardgohome());				#Ответы на слова
	elif message.text == '':								#Ответы на слова
		bot.send_message(message.chat.inlined, '');		#Ответы на слова

@bot.callback_query_handler(func=lambda call: True)			# Ответы на inline кнопки
def callback_inline(call):									# Ответы на inline кнопки
    # Ответы на inline кнопки
    if call.message:										# Ответы на inline кнопки
        if call.data == "one_1":					# Ответы на inline кнопки
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''❗️Перед оплатой, уточняйте наличие необходимого количества товара
Контакты для связи:
@saprone
@Pavelkuzmin1912
Тел: +79643957383
Многоканальный : +7(812) 408-26-81

Кошелек для оплаты:
PRIZM-54EQ-PELD-2WUB-8GJS6

Публичный ключ:
f48ecaac25f231d1bcc9e0e396c2fc0fcfbca3a25fa41acb3e24632e530c8471

После оплаты сделайте скриншот или пришлите ссылку на транзакцию. 
Далее подготовьте данные для отправки или доставки по Санкт-Петербургу.
ФИО
Город
Номер телефона
❗️Отправки осуществляются транспортной компанией Боксбери!

❗️для Боксберри нужно:
ФИО получателя, номер телефона, пункт выдачи (НЕ адрес получателя, а именно пункт выдачи с сайта!) 

Самовывоз: (г.Санкт-Петербург)
Магазин Кудрово
Станция метро Ул.Дыбенко, Кудрово, Ленинградская до 1 (напротив здания Макдональдс)


Купчино 
Станция метро Бухарестская ул. Салова 70 ( Большое здание автоцентра центральный вход магазин ПироГрад)''');
    # Ответы на inline кнопки						
    if call.message:										# Ответы на inline кнопки
        if call.data == "":					# Ответы на inline кнопки
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''''');
    # Ответы на inline кнопки	
    if call.message:										# Ответы на inline кнопки
        if call.data == "":					# Ответы на inline кнопки
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''''');
    # Ответы на inline кнопки	
    if call.message:										# Ответы на inline кнопки
        if call.data == "":					# Ответы на inline кнопки
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''''');

#bot.send_message(message.chat.id, '''Вступительное сообщение ''');
#    bot.send_photo(message.chat.id, open('three.jpg', 'rb'));#Фото, по желанию
#    keyboard = types.InlineKeyboardMarkup()					 
#    first_button = types.InlineKeyboardButton(text="Бесплатно 🎯", callback_data="ONE_CALLBACKw")	#CALLBACК Запрос
#    second_button = types.InlineKeyboardButton(text="Оплатить 💰", callback_data="SECOND_CALLBACKq")#CALLBACК Запрос
#    keyboard.add(first_button, second_button)				 #Добавляемкнопки		
#    bot.send_message(message.chat.id,'''Выберите способ:''', reply_markup=keyboard); #Сообщение

bot.polling(timeout=60)