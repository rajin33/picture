import telebot
from telebot import types
from data import get_data

API_TOKEN = '5411310878:AAEV3Xkr2P1y1_lRm2uigm9RIQdIbFcZgEE'

bot = telebot.TeleBot(API_TOKEN)

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name



@bot.message_handler(commands=['start'])
def start_ex(message):
    """
    Start command. Here we are starting state
    """
    markup  = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        telebot.types.InlineKeyboardButton(text=f'Ethereum Contract Detection',callback_data=f"contract_detection"),
        telebot.types.InlineKeyboardButton(text=f'Sniper',callback_data=f"sniper"),
        )
    bot.send_message(message.chat.id,f"""Welcome to GuardLab\n\nGuardLab is the best and fastest Detect & snipe Bot.
We pride ourselves on being the most accurate and up-to-date scanner.\n\nCurrently supported chains: Ethereum
""",parse_mode='HTML',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
    if call.data == "sniper":
        markup  = telebot.types.InlineKeyboardMarkup(row_width=2)
        markup.add(
                telebot.types.InlineKeyboardButton(text=f'Wallets',callback_data=f"contract_detection55"),
                telebot.types.InlineKeyboardButton(text=f'Settings',callback_data=f"sniper44"),
                telebot.types.InlineKeyboardButton(text=f'Buy token',callback_data=f"snipe44r"),
                telebot.types.InlineKeyboardButton(text=f'Sell token',callback_data=f"sniper44"),
                telebot.types.InlineKeyboardButton(text=f'Private txn',callback_data=f"sniper4444"),
                telebot.types.InlineKeyboardButton(text=f'Referral',callback_data=f"snipe444r"),

                )
        bot.send_message(call.message.chat.id,"Welcome to the Sniper!",parse_mode='HTML',reply_markup=markup)
    elif call.data == "contract_detection":
        bot.send_message(call.message.chat.id, "Input the contract address")
        bot.register_next_step_handler(call.message, process_name_step)


def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        if len(name) == 42:
            datalist = get_data(name)
            finaltext = f"""@GuardLabsBot | {datalist[0]}\n🔹 ETHER: {datalist[1]}\n👥 Holders: {datalist[2]}\n💰 Liquidity: {datalist[3]}\n🕰 Timestamp: {datalist[4]}\n🍯 Honeypot: {datalist[5]}\n🪝 SimulationSellSuccess: {datalist[6]}\n🏷 SimulationResult: \nbuytax: {datalist[7]}\nselltax: {datalist[8]}\ntransfertax: {datalist[9]}\nhighTaxWallets:{datalist[10]}\n🚨isHoneypot: {datalist[11]}\n🥏Pair-name: {datalist[12]}"""
            markup  = telebot.types.InlineKeyboardMarkup(row_width=2)
            markup.add(
                telebot.types.InlineKeyboardButton(text=f'Ethereum Contract Detection',callback_data=f"contract_detection"),
                telebot.types.InlineKeyboardButton(text=f'Sniper',callback_data=f"sniper"),
                )
            msg = bot.send_message(chat_id, finaltext,reply_markup=markup)
        else:
            bot.send_message(chat_id, f"Your address is wrong. /start again")
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