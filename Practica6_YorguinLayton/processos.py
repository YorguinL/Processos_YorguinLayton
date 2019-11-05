import time
from multiprocessing import Process

def t(s):
    while True:
        time.sleep(s)
        print time.strftime("%H:%M:%S")

def main():
    p = Process (target = t, args = (1,))
    p.start()
    for i in range(10):
        print p.pid
        time.sleep(0.5)
    p.terminate()
    print 'fi'

if __name__ == '__main__':
    main()
