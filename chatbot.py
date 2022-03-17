from email.mime import audio
import telebot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datetime import datetime
CHAVE_API = "(preencha sua chave do bot)"
bot = telebot.TeleBot(CHAVE_API)
iabot = ChatBot("Sophiabot")
iabot = ChatBot(
    "Sophiabot",
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3"
)


data_e_hora = datetime.now()
str_hora = data_e_hora.strftime("%H")

if str_hora > '0' and str_hora < '07' :
    turno = 'Madrugada'
    saudacao = 'Boa noite'

if str_hora > '06' and str_hora < '13':
    turno = 'Manhã'
    saudacao = 'Bom dia'

if str_hora > '12' and str_hora < '19':
    turno = 'Tarde'
    saudacao = 'Boa tarde'

if str_hora > '18' and str_hora < '24' and str_hora > '00':
    turno = 'Noite'
    saudacao = 'Boa noite'

print(str_hora)
print(turno)
print(saudacao)

conversa = ListTrainer(iabot)
conversa.train([
    'Oi',
    'Olá',
    'Tudo bem?',
    'Sim tudo bem',
    'eu sou a Shophiabot e estou aprendendo!'
])

saudacoes = [
    'fOlá',
    'folá',
    'fola',
    'fOI',
    'fOi',
    'foi',
    'feae',
    'fBom dia',
    'fBOM DIA',
    'fbom dia',
    'fBoa tarde',
    'fBOA TARDE',
    'fboa tarde',
    'fBoa noite',
    'fBOA NOITE',
    'fboa noite',
]


def verificar(mensagem):
    for i in saudacoes:
        if mensagem.text == i:
            menssagem_e_saudacao = True
            break
        else:
            menssagem_e_saudacao = False

    if menssagem_e_saudacao == True:
        testo_de_saudacao = 'Olá ' + mensagem.from_user.first_name + ' '+saudacao+'!'
        bot.send_message(mensagem.chat.id, testo_de_saudacao)
    else:
        return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    resposta = iabot.get_response(mensagem.text)
    # if float(resposta.confidence) > 0.5:
    #bot.send_message(mensagem.chat.id, mensagem.from_user.first_name)
    bot.send_message(mensagem.chat.id, resposta)
    # else:
    #bot.send_message(mensagem.chat.id, "Não entedi :( Conte me mais")


bot.polling()
