from realtcp import *
from time import *
from device_handlers import handle_command
import json

port = 1234
server = RealTCPServer()

def onTCPNewClient(client):
	def onTCPConnectionChange(type):
		print("connection to " + client.remoteIP() + " changed to state " + str(type))
		
	def onTCPReceive(data):
		print("received from " + client.remoteIP() + " with data: " + data)
		
        # Passes the data to the handler and fetches a response 
		response = handle_command(data)
		
        # Turns the returned dictionary to JSON
		response = json.dumps(response)
		
		# Sends the response to the client
		client.send(response)

	client.onConnectionChange(onTCPConnectionChange)
	client.onReceive(onTCPReceive)

def main():
	server.onNewClient(onTCPNewClient)
	print(server.listen(port))

	# don't let it finish
	while True:
		sleep(3600)

if __name__ == "__main__":
	main()