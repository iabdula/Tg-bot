import telegram
from telegram.error import TelegramError
import telebot
from telebot import types
import sqlite3

# токены и идентификаторы
bot_token = '6364962491:AAGMjN310TMArYev5RY_BKQ9wz7OkpZ1npA'
channel_id = '@pmSainMovieCode'
TOKEN = '6364962491:AAGMjN310TMArYev5RY_BKQ9wz7OkpZ1npA'

# создание объектов ботов
bot = telebot.TeleBot(TOKEN)

# функция проверки подписки пользователя
def check_user_subscription(user_id):
    try:
        chat_member = bot.get_chat_member(chat_id=channel_id, user_id=user_id)
        if chat_member.status == 'member':
            return True
        else:
            return False
    except TelegramError as e:
        print('Произошла ошибка: {}'.format(e))
        return False

# словарь
movies = {
            '1': ('призрачная шестрека'  , 'https://t.me/pmSainMovieCode/2'),
            '2': ('последствия', 'https://t.me/pmSainMovieCode/5'),
            '3': ('дракула 2014', 'https://t.me/pmSainMovieCode/6'),
            '4': ('12 Angry Men', 'https://t.me/pmSainMovieCode/7'),
            '5': ('Schindler\'s List', 'https://t.me/pmSainMovieCode/8'),
            '6': ('Новый Человек-паук: Высокое напряжение','https://t.me/pmSainMovieCode/9'),
            '7': ('Человек-Паук: Возвращение домой (2017)','https://t.me/pmSainMovieCode/10'),
            '8': ('Человек-Паук: Вдали от дома (2019)','https://t.me/pmSainMovieCode/11'),
            '9': ('Силачка До Бон-сун','https://t.me/pmSainMovieCode/12'),
            '10':('Человек-Паук: Через вселенные (2018)','https://t.me/pmSainMovieCode/13'),
            '11':('Новый Человек-Паук (2012)','https://t.me/pmSainMovieCode/14'),
            '12':('Человек-Паук (2002)','https://t.me/pmSainMovieCode/15'),
            '13':('Человек-Паук 2 (2004)','https://t.me/pmSainMovieCode/16'),
            '14':('Человек-паук 3: Враг в отражении (2007)','https://t.me/pmSainMovieCode/17'),
            '15':('Мультфильм Человек-Паук (2017)','https://t.me/pmSainMovieCode/18'),
            '16':('Мультфильм Человек-паук (1994','https://t.me/pmSainMovieCode/19'),
            '17':('Мультфильм Великий Человек-паук','https://t.me/pmSainMovieCode/20'),
            '18':('Мультфильм Человек-Паук: Тотальный Веном','https://t.me/pmSainMovieCode/21'), 
            '19':('время (2011)','https://t.me/pmSainMovieCode/22'),
            '20':('Гордость и предупреждение','https://t.me/pmSainMovieCode/23'),
            '21':('Разрушение','https://t.me/pmSainMovieCode/24'),
            '22':('Левша','https://t.me/pmSainMovieCode/25'),
            '23':('Драйв','https://t.me/pmSainMovieCode/26'),
            '24':('Тихое место под соснами','https://t.me/pmSainMovieCode/27'),
            '25':('Дело храбрых','https://t.me/pmSainMovieCode/28'),
            '26':('Кровью и потом','https://t.me/pmSainMovieCode/29'),
            '27':('Джентельмены','https://t.me/pmSainMovieCode/30'),
            '28':('Гнев человеческий','https://t.me/pmSainMovieCode/31'),
            '29':('Я легенда','https://t.me/pmSainMovieCode/32'),
            '30':('Железный человек','https://t.me/pmSainMovieCode/33'),
            '31':('Железный человек 2','https://t.me/pmSainMovieCode/34'),
            '32':('Железный человек 3','https://t.me/pmSainMovieCode/35'),
            '33':('Дедпул','https://t.me/pmSainMovieCode/36'),
            '34':('Дедпул 2','https://t.me/pmSainMovieCode/37'),
            '35':('Дедпул 3','https://t.me/pmSainMovieCode/38'),
            '36':('Люди Икс: Начало. Росомаха','https://t.me/pmSainMovieCode/39'),
            '37':('Люди Икс: Первый класс','https://t.me/pmSainMovieCode/40'),
            '38':('Люди Икс: Дни минувшего будущего','https://t.me/pmSainMovieCode/41'),
            '39':('Люди Икс','https://t.me/pmSainMovieCode/42'),
            '40':('Люди Икс 2','https://t.me/pmSainMovieCode/43'),
            '41':('Люди Икс: Последняя битва','https://t.me/pmSainMovieCode/44'),
            '42':('Росомаха: Бессмертный','https://t.me/pmSainMovieCode/45'),
            '43':('Логан','https://t.me/pmSainMovieCode/46'),
            '44':('Хакер','https://t.me/pmSainMovieCode/47'),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('',''),
            '':('','')
         }

# обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("канал 1", url='https://t.me/pmSainMovieCode')
    button2 = types.InlineKeyboardButton("канал 2", url='https://t.me/daamnplug')
    markup.add(button1)
    markup.add(button2)
    bot.send_message(message.chat.id, 'Привет! Для начала использования нашим ботом пожалйста подпишитесь на каналы, а за тем пришлите код фильма', reply_markup=markup)
    bot.send_message(message.chat.id, 'введите код фильма')

# обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def send_movie(message):
    user_id = message.from_user.id
    if check_user_subscription(user_id):
        # получаем номер фильма из сообщения пользователя
        movie_num = message.text
        if movie_num in movies:
            # отправляем фильм
            bot.send_message(message.chat.id, f"Вот Ваш фильм: {movies[movie_num]}")
        else:
            # если номер не найден, отправляем сообщение о том, что фильм не найден
            bot.send_message(message.chat.id, 'К сожалению, такого фильма не существует.')
    else:
        # если пользователь не является подписчиком, отправляем сообщение с предложением подписаться   
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("канал 1", url='https://t.me/pmSainMovieCode')
        button2 = types.InlineKeyboardButton("канал 2", url='https://t.me/daamnplug')
        markup.add(button1)
        markup.add(button2)
        bot.send_message(message.chat.id, 'Вы еще не подписались на каналы, для получения фильмов, пожалуйста, подпишитесь на канал:', reply_markup=markup)

# запускаем бота
bot.polling()