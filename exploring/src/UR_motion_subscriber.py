# Echo client program
import rospy
import socket
import time

HOST = "192.168.1.3" # The remote host
PORT = 30002 # The sa        y_2 = -0.345 - j * 0.05


print "Starting Program"

count = 0
i = 1
j = 1
k = 1
while (count < 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    time.sleep(0.5)
    print "Robot starts Moving to 3 positions based on pose positions"
    s.send ("movej([-2.57, -1.67, -2.31, -2.34, -2.53,-3.21], a=1.0, v=0.3)" + "\n")
    time.sleep(10)
    print "Starting to search"
    while (i < 5):
        y = -0.345 - i * 0.05
        track_1 = str("movej(p[-0.325, " + str(y) + " ,0.116, 0.0165, 2.29, -2.23], a=1.0, v=0.1)")
        s.send (track_1 + "\n")
        time.sleep(5)
        i = i + 1
        print "I'm on track 1"
    s.send ("movej([-2.57, -1.67, -2.31, -2.34, -2.53,-3.21], a=1.0, v=0.3)" + "\n")
    time.sleep(10)
    while (j < 5):
        x = -0.325 - j * 0.05
        y_2 = -0.345 - j * 0.05
        track_2 = str("movej(p["+ str(x) +" ," + str(y_2) + " ,0.116, 0.0165, 2.29, -2.23], a=1.0, v=0.1)")
        s.send (track_2 + "\n")
        time.sleep(5)
        j = j + 1
        print "I'm on track 2"
    s.send ("movej([-2.57, -1.67, -2.31, -2.34, -2.53,-3.21], a=1.0, v=0.3)" + "\n")
    time.sleep(10)
    while (k < 5):
        x = -0.325 + k * 0.05
        y_3 = -0.345 - k * 0.05
        track_3 = str("movej(p["+ str(x) +" ," + str(y_3) + " ,0.116, 0.0165, 2.29, -2.23], a=1.0, v=0.1)")
        s.send (track_3 + "\n")
        time.sleep(5)
        k = k + 1
        print "I'm on track 3"
    s.send ("movej([-2.57, -1.67, -2.31, -2.34, -2.53,-3.21], a=1.0, v=0.3)" + "\n")
    time.sleep(10)
    count = count + 1
    print "Finish searching"
    print "The count is:", count
    print "Program finish"

    time.sleep(1)
    data = s.recv(1024)

    s.close()
    print ("Received", repr(data))

print "Status data received from robot"
