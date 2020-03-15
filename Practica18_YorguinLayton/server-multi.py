import socket, threading
from ChatFns import HOST, PORT
from ChatFns import send_img, receive_img

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
            data = cli_sock.recv(4096000)
            if data:
                if "/image" in data:
                    img = data.split("/image")[-1]
                    msg = receive_img(cli_sock, img)
                    b_usr(cli_sock, uname, msg)

                elif data[:-1] == "Bye":
                    CONNECTION_LIST.remove((uname, cli_sock))
                    cli_sock.close()
                    break

                else:
                    print "{0} spoke {1}".format(uname, data)
                    b_usr(cli_sock, uname, data)

        except Exception as x:
            print(x.message)
            break

def b_usr(cs_sock, sen_name, msg):
    for client in CONNECTION_LIST:
        if client[1] != cs_sock:
            if "/image" in msg:
                send_img(ser_sock, msg)

            else:
                client[1].send(sen_name + ':' + msg)



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
