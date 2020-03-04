import socket, threading
from ChatFns import HOST, PORT

def accept_client():
    while True:
        #accept
        cli_sock, cli_add = ser_sock.accept()
        uname = cli_sock.recv(1024)[:-1]
        CONNECTION_LIST.append((uname, cli_sock))
        print('%s is now connected' %uname)
        thread_client = threading.Thread(target = broadcast_usr, args=[uname, cli_sock])
        thread_client.daemon = True
        thread_client.start()

def broadcast_usr(uname, cli_sock):
    while True:
        try:
            data = cli_sock.recv(1024)
            if "/image" in data:
                receive_imag(ser_sock, data)
            if data:
                print "{0} spoke {1}".format(uname, data)
                b_usr(cli_sock, uname, data)
                if data[:-1] == "Bye":
                    CONNECTION_LIST.remove((uname, cli_sock))
                    cli_sock.close()
                    break
        except Exception as x:
            print(x.message)
            break

def b_usr(cs_sock, sen_name, msg):
    for client in CONNECTION_LIST:
        if client[1] != cs_sock:
            client[1].send(sen_name + ':' + msg)
            #if "/image " in data:
            #client[1].send(msg)
            #send(img)

def receive_imag(s, size):
    img = open("imgServer.jpg", 'wb')
    r_size = 0
    t = s.recv(4096000)
    d_img = t.split(' ',1)[-1]
    r_size = len(d_img)

    while r_size < size:
        d_img = d_img + t
        pass
    img.write(d_img.decode('base64'))


if __name__ == "__main__":
    CONNECTION_LIST = []

    # socket
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind
    #HOST = 'localhost'
    #PORT = 5011
    ser_sock.bind((HOST, PORT))

    # listen
    ser_sock.listen(1)
    print('Chat server started on port : ' + str(PORT))

    thread_ac = threading.Thread(target = accept_client)
    thread_ac.start()
    thread_ac.join()
    s.close()
    #thread_bs = threading.Thread(target = broadcast_usr)
    #thread_bs.start()
