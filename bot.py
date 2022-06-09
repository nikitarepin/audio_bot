import telebot
import config
from gtts import gTTS


bot = telebot.TeleBot(config.token)

"""приветствие и отправка стикера"""
@bot.message_handler(commands=['start'])
def start(message):
	hello = '<b> "hello world" </b> - ' + f'{message.from_user.first_name}'
	stic = open('image/1.webp','rb')
	bot.send_sticker(message.chat.id, stic)
	bot.send_message(message.chat.id, hello, parse_mode = 'html')
	bot.send_message(message.chat.id, '<i>Этот бот, создает аудио из текста. Напиши сообщение</i> ⬇', parse_mode = 'html')
	



@bot.message_handler(content_types = ['text'])
def get_user_text(message):

	"""ввод пользователем сообщения и помещение его в пременную"""
	need_text = str(message.text)

	"""перевод сообщения в аудио на русском языке"""
	result = gTTS(need_text, lang = 'ru')

	"""сохранение аудио. имя аудиофайла - это id пользователя"""
	result.save(f'{message.from_user.id}'+'.mp3')

	"""открытие аудиофайла и его отправка пользователю"""
	audio_result = open(f'{message.from_user.id}.mp3','rb')
	bot.send_audio(message.chat.id, audio_result)	


#run
bot.polling(none_stop = True)
