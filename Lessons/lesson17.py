# Lesson 17: Networking in Python
# In this lesson, we will explore basic networking concepts using Python's socket module.

# What is Networking?
# Networking involves connecting computers to share resources and information.
# Python provides the socket module to facilitate network communication.

# Using the socket Module
# The socket module provides access to the BSD socket interface.

import socket

# Creating a Simple TCP Client
# Example:
def simple_tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("example.com", 80))
    client_socket.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
    response = client_socket.recv(4096)
    print("Response:", response.decode())
    client_socket.close()

# Creating a Simple TCP Server
# Example:
def simple_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(1)
    print("Server listening on port 12345...")

    conn, addr = server_socket.accept()
    print("Connected by", addr)
    data = conn.recv(1024)
    if data:
        conn.sendall(data)
    conn.close()

# Hands-On Exercises:
# 1. Modify the TCP client to connect to a different server and port.
# 2. Enhance the TCP server to handle multiple connections.
# 3. Experiment with UDP communication using the socket module.

# Try it Yourself!
# Practice using sockets to create basic network applications.

# Solution Example:
# def udp_communication():
#     udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     udp_socket.sendto(b"Hello, UDP!", ("localhost", 12345))
#     data, addr = udp_socket.recvfrom(1024)
#     print("Received from", addr, ":", data.decode())
#     udp_socket.close()
