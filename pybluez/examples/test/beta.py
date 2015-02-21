from test_inquiry import *
import bluetooth
from clientmodule import *
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
  
  parse = data.split('/')
 
  if parse[2] == "root":
    #fill the condition
    parent.append(-1)
    print "pass"
    print "root condition"
  elif parse[2] == "search":
    #fill the condition
    print "search condition"
    if len(parent) is 0:
      #fill the condition
      parent.append(int(parse[0]))
      number =int(parse[1])+1
      count = int(parse[1])+1
      print "sensor number %d" %number
      data = "%d/%d/0" %(number, count) 
      client_sock.send('Echo => ' + data)
      client_sock.close()
      server_sock.close()
  
    else:
      count = parse[1]
      data = "%d/%d/1" %(number, count)
      client_sock.send('Echo => ' + data)


#--------- end of while--------
