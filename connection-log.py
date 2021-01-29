import socket
import time
REMOTE_SERVER = "1.1.1.1"
prev_state = -1
def is_connected(hostname):
  try:
    host = socket.gethostbyname(hostname)
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except:
     pass
  return False

while True:
    t = time.localtime()    
    current_time = time.strftime("%H:%M:%S", t)
    time.sleep(1)
    result = is_connected(REMOTE_SERVER)

    if result is True and prev_state == -1:
        line = "Trace started at [" +  current_time + "]"
        print(line, flush = True)
        file1 = open("connection-status-log.txt", "a")  # append mode
        file1.write(line + "\n") 
        file1.close()

    if result is True and prev_state != 1:
        line = "Connection Established at " +  current_time  
        print(line, flush = True)
        file1 = open("connection-status-log.txt", "a")  # append mode
        file1.write(line + "\n") 
        file1.close() 
        prev_state = 1
    
    elif result is False and prev_state != 0:
        line = "Disconnected at " +  current_time  
        print(line, flush = True)
        file1 = open("connection-status-log.txt", "a")  # append mode
        file1.write(line + "\n")
        file1.close() 
        prev_state = 0
    
