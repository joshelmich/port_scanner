import json

class tcp_error_print:
	tcp_errors = []
		
	def load_tcp_errors(self):
		with open('TCP_socket_error_codes.json') as json_data:
			self.tcp_errors = json.load(json_data)			
		return
			
	def get_error_string(self, number):
		if number < len(self.tcp_errors["codes"]):
			return self.tcp_errors["codes"][number]["text"]
		else:
			return "Error not found"
			
	
		

