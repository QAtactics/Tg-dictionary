from telebot import TeleBot, types

bot = TeleBot(token='токен', parse_mode='html')

DEFINITOINS = {
    'регресс': 'Проверить что новый функционал не сломал существующий',
    'смоук': 'Проверка важных функциональностей',
    'http': ' Это протокол передачи текстовых данных. Нужен для передачи информации. Клиент передает информацию на бекенд.',
}

@bot.message_handler(commands=['start'])

def start_command_handler(message: types.Message):
    
    bot.send_message(
    chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
    text='Привет, тестировщик! Мой бот поможет тебе расшифровать сложные аббревиатуры и термины 🤓\nВведи интересующий термин, например, регресс, смоук или http',
    )
    
@bot.message_handler()
def message_handler(message: types.Message):
    definition = DEFINITOINS.get(
    message.text.lower(),
    )
    
 if definition is None:
    bot.send_message(
    chat_id=message.chat.id,
    text='😋 Я пока не знаю такого определения',
        ) 
        return
bot.send_message(
    chat_id=message.chat.id,
    text=f'Определение:\n<code>{definition}</code>',
    )

bot.send_message(
    chat_id=message.chat.id,
    text=f'Давай следующий термин',
    )

def main():
    bot.infinity_polling()
    
if __name__ == '__main__':
    main()
