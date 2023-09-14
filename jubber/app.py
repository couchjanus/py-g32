import telebot
import jubber.config as config 

import pytz
import datetime
from jubber import GREETINGS, HELP_MESSAGES, HOROSCOPE, EMOJI_UP, EMOJI_DOWN
from jubber.horo import get_daily_horoscope
import jubber.api as api
import json 


bot = telebot.TeleBot(config.TOKEN)

P_TIMEZONE = pytz.timezone(config.TIMEZONE)
TIMEZONE_NAME = config.TIMEZONE_NAME

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, GREETINGS)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, HELP_MESSAGES)
        
def get_edited_signature():
    return f"""<i>Updated: {str(datetime.datetime.now(P_TIMEZONE).strftime('%H:%M:%S'))}({TIMEZONE_NAME})</i>"""

@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
    text = HOROSCOPE
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler)

def day_handler(message):
    sign = message.text
    text = "What day do you want to know?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a date in format YYYY-MM-DD."
    sent_msg = bot.send_message(
        message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(
        sent_msg, fetch_horoscope, sign.capitalize())

def fetch_horoscope(message, sign):
    day = message.text
    horoscope = get_daily_horoscope(sign, day)
    data = horoscope["data"]
    horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\\n*Sign:* {sign}\\n*Day:* {data["date"]}'
    bot.send_message(message.chat.id, "Here's your horoscope!")
    bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")

@bot.message_handler(commands=['exchange'])
def send_exchange(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton('USD', callback_data='get-USD'), telebot.types.InlineKeyboardButton('EUR', callback_data='get-EUR'))

    bot.reply_to(message, 'Click on the currency of choice:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('get-'):
        get_ex_callback(query)
        
def get_ex_callback(query):
    bot.answer_callback_query(query.id)
    send_exchange_result(query.message, query.data[4:])

def send_exchange_result(message, ex_code):
    bot.send_chat_action(message.chat.id, 'typing')
    ex = api.get_exchange(ex_code)
    bot.send_message(
        message.chat.id, serialize_ex(ex),
        reply_markup=get_update_keyboard(ex),
        parse_mode='HTML'
        )
    
def get_update_keyboard(ex):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton('Update', callback_data=json.dumps({
    't': 'u', 'e': {'b': ex['buy'],'s': ex['sale'],'c': ex['ccy']}}
    ).replace(' ', '')), telebot.types.InlineKeyboardButton('Share', switch_inline_query=ex['ccy'])
    )
    return keyboard

def serialize_ex(ex_json, diff=None):
    result = f'''<b>{ex_json['base_ccy']} -> {ex_json['ccy']}:</b>\n\nBuy: {ex_json['buy']}'''
    if diff:
        result += f''' {serialize_exchange_diff(diff['buy_diff'])}\nSell: {ex_json['sale']} {serialize_exchange_diff(diff['sale_diff'])}\n'''
    else:
        result += f"\nSell: {ex_json['sale']}\n"
    return result

def serialize_exchange_diff(diff):
    result = ''
    if diff > 0:
        result = f'({str(diff)} {EMOJI_UP})'
    elif diff < 0:
        result = f'({str(diff)[1:]} {EMOJI_DOWN})'
    return result


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)