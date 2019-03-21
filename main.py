#!/usr/bin/env python3

import time

import telebot
from telebot import types, apihelper


BOT_TOKEN = '637841439:AAHpbA6WJ17QL0413QbaPjvVAfNtN2uiIZA'
DEBUG = False

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message_handler(message):
	cid = message.chat.id
	uid = message.from_user.id
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True, row_width=1)
	markup.add('Расписание Уроков')
	markup.add('Расписание Звонков')
	markup.add('ФИО учителей и их кабинеты')
	text = 'Главное меню'
	return bot.send_message(cid, text, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text_message_handler(message):
	cid = message.chat.id
	uid = message.from_user.id
	if message.text == 'Расписание Уроков':
		text = '''
Понедельник – четверг
1 урок: с 8:00 до 8:40
2 урок: с 9:55 до 9:35
3 урок: с 9:50 до 10:30
4 урок: с 10:45 до 11:25
5 урок: с 11:40 до 12:20
6 урок: с 12:30 до 13:10

Пятница
1 урок: с 8:00 до 8:40
2 урок: с 8:50 до 9:30
3 урок: с 9:40 до 10:20
4 урок: с 10:35 до 11:15
5 урок: с 11:25 до 12:05
6 урок: с 12:10 до 12:45

Суббота
1 урок: с 8:00 до 8:40
2 урок: с 8:45 до 9:25
3 урок: с 9:30 до 10:10
4 урок: с 10:15 до 10:55
5 урок: с 11:00 до 11:40
6 урок: с 11:45 до 12:25 
'''
		return bot.send_message(cid, text)
	if message.text == 'Расписание Звонков':
		text = '''
Расписание уроков
ПОНЕДЕЛЬНИК
Биология
Русский язык
Физика
Английский язык
Алгебра
Литература
ВТОРНИК
География
История
Геометрия
Практикум по русскому языку
Химия
Проектная деятельность
СРЕДА
Русский язык
ОБЖ
Кубановедение
Английский язык
Алгебра
Литература
ЧЕТВЕРГ
Физика
Физическая культура
Алгебра
Русский язык
Английский язык
Литература
ПЯТНИЦА
Химия
История
Обществознание
Информатика
Геометрия
Биология
СУББОТА
География
Информационная работа
Физика
История
Физическая культура
Черчение
'''
		return bot.send_message(cid, text)
	if message.text == 'ФИО учителей и их кабинеты':
		text = '''
Русский язык, литература - Кутушева Евгения Владимировна (каб. 310)
Алгебра, геометрия -Тимошенко Елена Владимировна(каб. 209)
Английский язык - Истягина Светлана Павловна(каб. 135)/ Тараканова Ольга Викторовна(каб. 218)
История, обществознание, кубановедение - Иванина Алёна Геннадьевна(каб. 229)
География - Голикова Светлана Вячеславовна(каб. 120)
Биология - Богданова Галина Васильевна(каб. 323)
Черчение - Полумесная Ольга Семеновна(антинарко)
Физ-ра - Кузовкин Алексей Михайлович
ОБЖ - Плачковский Виктор Владимирович(каб. 321)
Физика - Мельник Ирина Николаевна(каб. 221)
Химия - Маклюк Марина Иванова(каб. 122)
Информатика - Пономаренко Елена Анатольевна(каб. 331)/ Зейтеньян Татьяна Анатольевна (каб. 231)
'''
		return bot.send_message(cid, text)


def main():
	if DEBUG:
		apihelper.proxy = {'https': 'socks5h://TV360_4_217166737:rkO8KhVov4x93EKs@0x5c.private.ss5.ch:1080'}
		bot.polling()
	else:
		while True:
			try:
				bot.polling(none_stop=True, interval=0)
			except Exception as e:
				print(e)
				time.sleep(30)


if __name__ == '__main__':
	main()
