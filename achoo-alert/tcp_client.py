import socket
import json
import logging
import logging_config


class TCPClient:
    """
    A class to send messages to a TCP server.
    """

    def __init__(self, server_ip, server_port):
        # Initalises the TCP client
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = None

    def connect(self):
        try:
            # Creates a socket object
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connects to the server
            self.client_socket.connect((self.server_ip, self.server_port))
            logging.info(f"Connected to server at {self.server_ip}, {self.server_port}")

        except Exception as e:
            logging.error(
                f"Failed to connect to {self.server_ip}:{self.server_port} - {e}"
            )
            self.client_socket = None

    def send_message(self, message):
        if self.client_socket:
            try:
                # Sends the message to the server
                self.client_socket.send(message.encode())
                logging.info(f"Message sent: {message}")

                response = self.client_socket.recv(1024)
                logging.info(response.decode())

            except Exception as e:
                logging.error(f"Error sending message: {e}")
        else:
            logging.warning("No active connection. Please connect first.")

    def close(self):
        if self.client_socket:
            self.client_socket.close()
            logging.info("Connection closed.")


# For test usage
if __name__ == "__main__":
    tcp_client = TCPClient("192.168.1.39", 1234)
    tcp_client.connect()
    if tcp_client.client_socket:
        test_string = {"device": "ac", "action": "off"}
        test_string = json.dumps(test_string)
        return_message = tcp_client.send_message(test_string)
        if return_message:
            logging.info(f"Received response: {return_message}")
        # Closes the connection after sending the message
        tcp_client.close()
