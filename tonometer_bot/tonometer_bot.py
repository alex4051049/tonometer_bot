import requests
import datetime

class BotHandler:
	
	def __init__(self, token):
		self.token = token
		self.api.url = 'https://api.telegram.org/bot{}/'.
						format('644537984:AAHvXxRBhhrJNWjYUqUIkifhIHjgnR9xGjY')
		 
	def get_updates(self, offset=None, timeout=30):
		method = 'getUpdates'
		params = {'timeout': timeout, 'offset': offset}
		resp = request.get(self.api_url + method, params)
		result_json = resp.json()['result']
		return result_json
	
	def send_message(self, chat_id, text):
		params = {'chat_id': chat, 'text': text}
		method = 'sendMessage'
		resp = request.post(self.api.url + method, params)
		return resp
	
	def get_las_update(self):
		get_result = self.get_updates()
		
		if len(get_result) > 0:
			last_update = get_result[-1]
		else:
			last_update = get_result[len(get_result)]	
		return last_update
	
	def main():
		update_id = last_update(get_updates_json(url))['update_id']
		while True:
			if update_id == last_update(get_updates_json(url))['update_id']:
				send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
				update_id += 1
			sleep(1)
			
	if __name__ == '__main__':
		main()		
