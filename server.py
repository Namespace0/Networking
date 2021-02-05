import socket
import threading
import datetime
import requests
import json

port = 8420;
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SRC = "192.168.1.188";

sock.bind((SRC, port))


IP_TABLE = {
	"Admin" : "35.188.146.38",
}



def handler(client_Socket, address):
	print('It worked')

status = True;


def Init():
	sock.listen(5)
	while status:

		client_Socket, address = sock.accept()

		try:
			CDATA = requests.get(f'http://ip-api.com/json/{address[0]}')
			address_data = json.loads(CDATA.content)
			cCountry = address_data["country"]
			cRegion = address_data["regionName"]


			print(f"[INCOMING {address[0]}] | {datetime.datetime.now()} | Location:{cCountry},{cRegion}")
		except:
			print(f"[INCOMING {address[0]}] | {datetime.datetime.now()} | Location: Unkown")
		
		client_Socket.send(bytes(f"Checking {address[0]} . . .  ", "utf-8"))
		thread = threading.Thread(target=handler, args=(client_Socket,address))
		thread.start()



print(f'[SERVER INITIATED] | {datetime.datetime.now()}')
Init()
