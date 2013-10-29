import socket
import sys
import select

def open_connection(host, port):
    # create and open socket connection
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((host, port))
    
    return my_socket

def format_response(msg):
        list = msg.split('::')
        print "[%s] %s" % (list[0], list[1])
def main():
    
    # Create and open our socket connection
    my_socket = open_connection("10.1.10.100", 5555) #10.1.10.100
    
    running = True
    while running:
        inputready, outputready, exceptready = select.select([my_socket, sys.stdin], [], [])
        
        for s in inputready:
            if s == sys.stdin:
                # handle standard input
                key_input = sys.stdin.readline()
                
                if key_input == "/quit\n":
                    running = False
                else:
                    sent = my_socket.send(key_input)
                    if sent == 0:
                        raise RuntimeError("socket connection broken")

            else:
                msg = s.recv(1024)

                if msg:
                    if "::" in msg:
                        format_response(msg)
                    else:
                        print msg
                else:
                    print "Disconnected from server!"
                    running = False

    # close connection
    my_socket.close()
    
    
if __name__ == "__main__":
    main()


            
# # receive data from connection 
# data = my_socket.recv(1024)
# 
# # print data received
# print "received:\n%s" %  data
# 
# # read keyboard input

#            
# # receive data from connection 
# data = my_socket.recv(1024)
# 
# # print data received
# print "received:\n%s" %  data

