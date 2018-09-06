import config
import telebot
#import put_new_words as load
#import common_function as api

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands = ['help'])
def help(message):
	cid = message.chat.id
	cmd = ['/start - начать тренировку','/next - показать следующую карточку','/correct - исправить перевод','/today - показать все слова за сегодня','/load - загрузить еще карточек','/help - список команд', '/dev - написать разработчикам']
	v_text = 'Доступные команды: \n'+'\n'.join(cmd)
	bot.send_message(cid, v_text)
	

if __name__ == '__main__':
	bot.polling(none_stop=True, timeout=500)













	


