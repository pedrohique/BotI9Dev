from BotHead import Welcome
# import telebot
# import telepot
# #import telebot.types
# import configparser
#
# config = configparser.ConfigParser()
# config.read('config.ini')
# key = config.get('credenciais', 'token')

# bot = telebot.TeleBot(key, parse_mode='html')
#
# @bot.message_handler(commands=['start'])  # func=lambda m: True)
# def responder(msg):
#     texto = """Escolha uma opção para continuar (Clique no item):
#      <b>/opcao1 </b>
#      /opcao2
#      /opcao3
# Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
#     bot.reply_to(msg, texto)
#
# @bot.message_handler(commands=['opcao1'])
# def responder(msg):
#     texto = """obrigado por escolher a opcao 1"""
#     bot.reply_to(msg, texto)
#
# @bot.message_handler(commands=['opcao2'])
# def responder(msg):
#     texto = """obrigado por escolher a opcao 2"""
#     bot.reply_to(msg, texto)
#
# @bot.message_handler(commands=['opcao3'])
# def responder(msg):
#     texto = """obrigado por escolher a opcao 3"""
#     bot.reply_to(msg, texto)
#
#
# bot.infinity_polling()

if __name__ == '__main__':
    Welcome.BotBrain()

#while True:
    #print(1)
    #try:
    # chat_id = updates['message']['chat']['id']
    # message = updates['message']['text']
    # print(message)
    #except:
       # pass
    #bot.polling()

