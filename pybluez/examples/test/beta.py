from test_inquiry import *
import bluetooth
addr = getaddr_rssi()
parent = []
child = [] 
number = -1
count = -1
while 1:
  
  server_sock=bluetooth.BluetoothSocket( bluetooth.L2CAP )

  port = 0x1001

  server_sock.bind(("",port))
  server_sock.listen(1)

  client_sock,address = server_sock.accept()
  print("Accepted connection from ",address)

  data = client_sock.recv(1024)
  print("Data received:", data)
  
  parse = data.split('/', 1)
 
  if parse[2] == "root":
    #fill the condition
    print "pass"
  elif parse[2] == "serach":
    #fill the condition
    
    if len(parent) is 0:
      #fill the condition
      number = parse[1]+1
      client_sock.close()
      server_sock.close()
  
    else:
      count = parse[1]
      data = "%d/%d/1" %(number, count)
      client_sock.send('Echo => ' + data)


#--------- end of while--------
