import requests


class NotificationManager:
    def telegram_bot_sendtext(self, bot_message):
        bot_token = "1954038233:AAE41ANEN4rdlFsg-Gf_p2yzEK5FJphDyvo"
        bot_chatID = "72636178"
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + \
                    bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response_tg = requests.get(send_text)

        return response_tg.json()
