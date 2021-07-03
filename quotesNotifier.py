from configparser import ConfigParser
import os
import requests,json
import telebot

devKeys = os.environ.get('DevKeys')
config = ConfigParser()
config.read(devKeys)

telegramToken=config['telegram']['accessToken']
tb = telebot.TeleBot(telegramToken)

ChatIds= {
    "GiddyUp":"-1001428866192",
    "DirectAcmp":"1458048263",
    "DirectMS":"1613066759",
    "Papachi":"344789208"
}

def getMotivationalMessage():
    params = {
        'method':'getQuote',
        'lang':'en',
        'format':'json'
    }
    res = requests.get('http://api.forismatic.com/api/1.0/',params)
    jsonText =json.loads(res.text)
    author =  jsonText["quoteAuthor"]
    text = jsonText["quoteText"]
    if author == '':
        author = 'Unknown'
    message = text+'\n-'+author
    return message


def sendQuotes():
    quote = getMotivationalMessage()
    tb.send_message(ChatIds['GiddyUp'], quote)
    tb.send_message(ChatIds['Papachi'], quote)


if __name__ == '__main__':
    sendQuotes()
    


