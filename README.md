# CS_361_TDePalatis



Type into your python terminal:
pip install beautifulsoup4 selenium pandas pyarrow Pillow requests

REQUESTING DATA:

1. Open image_socket.py. 

2. In line 65, update the path with where you would like the image to be saved to. You may update the Port 	to your liking.
	
3. In your code you need to have socket imported and set up as well as a Host and a Port chosen that 		matches image_socket.py.

Example:
	import socket as sock
	HOST = '127.0.0.1'
	PORT = #Choose a port
	socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
	socket.connect((HOST, PORT))

4. Define the url of your desired image and send it as a message to the socket.
Example:
	url_example = # the desired URL
	socket.send(url_example.encode('utf-8'))

RECEIVING DATA:
 1. In your program, set a variable to receive the response from the socket as a string.
	Example:
		message = str(socket.recv(1024))

2. Trim your variable string so that the path will not have any unnecessary artifacts of the sent message. In this example,

	Example:
		path = message[2:-1]

	#In this example, 
 		message = b’path‘
		path = path

3. Use this path variable to locate the newly downloaded image. Run image_socket.py. and then run your program!



[image_socket.py UML.pdf](https://github.com/TDePalatis/CS_361_TDePalatis/files/14391200/image_socket.py.UML.pdf)


