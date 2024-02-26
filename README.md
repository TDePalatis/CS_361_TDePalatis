#Communication Contract


1. How you will communicate with each other:
We will primarily use Microsoft Teams as well as Google Docs and Canvas discussions
within group 131. We gave each other our phone numbers in case of an emergency as
well.
2. Expectations for responsiveness:
Responses to questions and collaboration should be given within 24 hours. If no
response is received a text message can be expected.
3. Expectation to finish early:
We want to make sure that we don’t get too far behind. This means that we will start
early and hopefully finish early as well. We believe that there should be significant
progress made weekly. In order to assure this, communication about a section of an
assignment must occur at least 5 days before the due date to put together a plan.
4. Do Your Part:
If someone fails to do their part on a section of the assignment they can expect to do a
little more on the next. This will create a fair and equal environment. If one of us just
isn’t doing their part of the assignment at all, a message to a professor will be made out.
This is only in extreme circumstances.
5. Communication Style:
We want to create an environment where both of us feel comfortable to share our ideas
and work easily together. We need to keep our chat positive. There isn’t really a
punishment that comes with this rule because we are adults. However, we need to keep
this rule in mind to ensure good productivity.


# image_socket.py README

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


