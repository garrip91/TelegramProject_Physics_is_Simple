import requests


# КАРКАС ПОЛНОЙ ССЫЛКИ:
# https://api.telegram.org/bot<token>/<METHOD_NAME>
API_link = "https://api.telegram.org/bot809303024:AAGoklo1kZBFI0yfv65P7C9BDMofv8guYCU"

updates = requests.get(API_link + "/getUpdates?offset=770445205").json()

#print(updates)

message = updates['result'][-1]['message']
chat_id = message['from']['id']
text = message['text']

sent_message = requests.get(API_link + F'/sendMessage?chat_id={chat_id}&text=Привет, ты написал {text}')




# {
    # 'ok': True,
	# 'result': [
	    # {
            # 'update_id': 770445205,
            # 'message': {
                # 'message_id': 751,
                # 'from': {
                    # 'id': 708929005,
                    # 'is_bot': False,
                    # 'first_name': 'garrip91',
                    # 'username': 'garrip91',
                    # 'language_code': 'ru'
                # },
                # 'chat': {
                    # 'id': 708929005,
                    # 'first_name': 'garrip91',
                    # 'username': 'garrip91',
                    # 'type': 'private'
                # },
                # 'date': 1631687301,
                # 'text': 'Everybody'
            # }
        # },
		# {
            # 'update_id': 770445206,
            # 'message': {
                # 'message_id': 753,
                # 'from': {
                    # 'id': 708929005,
                    # 'is_bot': False,
                    # 'first_name': 'garrip91',
                    # 'username': 'garrip91',
                    # 'language_code': 'ru'
                # },
                # 'chat': {
                    # 'id': 708929005,
                    # 'first_name': 'garrip91',
                    # 'username': 'garrip91',
                    # 'type': 'private'
                # },
                # 'date': 1631688126,
                # 'text': '/start',
                # 'entities': [
                    # {
                        # 'offset': 0,
                        # 'length': 6,
                        # 'type': 'bot_command'
                    # }
                # ]
            # }
        # }
	# ]
# }