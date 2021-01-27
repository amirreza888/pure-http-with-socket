import socket


# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Get the content of htdocs/index.html
    fin = open('./index.html')
    content = fin.read()
    print(content)
    fin.close()

    # Send HTTP response
    response = 'HTTP/1.0 200 OK\n\n'+content
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()


# GET / HTTP/1.1
# Host: 127.0.0.1:8000
# Connection: keep-alive
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# Sec-Fetch-Site: none
# Sec-Fetch-Mode: navigate
# Sec-Fetch-User: ?1
# Sec-Fetch-Dest: document
# Accept-Encoding: gzip, deflate, br
# Accept-Language: en-US,en;q=0.9
# Cookie: _ga=GA1.1.261527631.1608024936; _ga_54PQE8ZGYH=GS1.1.1610024069.7.0.1610024141.0; csrftoken=Hfhq1LZxePVgdvBtdoZuqHWumGpTfkzvwB7IxYqpCw3LcnJ4g1fk7CGSz6K3atQL