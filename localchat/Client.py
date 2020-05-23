import sys
import socket
import select

def main():
    if len(sys.argv) is not 3:
        print("usage: %s [ip adress][port] " % sys.argv[0] )
        return(-1)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((sys.argv[1], int(sys.argv[2])))

        while True:
            s_msg = input().replace('b', '').encode('utf-8')
            if s_msg == '':
                break 
            else:
                s.sendall(s_msg)
            r_msg = s.recv(1024)
            if r_msg == '':
                break
            else:
                print(r_msg.decode())

if __name__ == '__main__':
    main()
