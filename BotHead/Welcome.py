import configparser
import telebot
import telebot.types

config = configparser.ConfigParser()
config.read('config.ini')


class BotBrain:
    def __init__(self):
        """Bot Keys"""
        self.key = config.get('credenciais', 'token')
        self.bot = telebot.TeleBot(self.key, parse_mode='html')



        @self.bot.message_handler(commands=['opcao1'])
        def responder(msg):
            texto = """obrigado por escolher a opcao 1"""
            self.bot.reply_to(msg, texto)

        @self.bot.message_handler(commands=['opcao2'])
        def responder(msg):
            texto = """obrigado por escolher a opcao 2"""
            self.bot.reply_to(msg, texto)

        @self.bot.message_handler(commands=['opcao3'])
        def responder(msg):
            texto = """obrigado por escolher a opcao 3"""
            self.bot.reply_to(msg, texto)

        @self.bot.message_handler( func=lambda m: True) #commands=['start'])  #
        def responder(msg):
            texto = """Escolha uma opção para continuar (Clique no item):
             <b>/opcao1 </b>
             /opcao2 
             /opcao3 
        Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
            self.bot.reply_to(msg, texto)

        self.bot.infinity_polling()


