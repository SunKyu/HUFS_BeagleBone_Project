
from test_inquiry import *
import bluetooth
from clientmodule import *
addr = getaddr_rssi()
dic_addr ={}
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
    number = int(parse[1])+1
    count = int(parse[1])+1
    data = "%d/%d/search" %(number, count)

    #make!!
    SIZE = len(addr)
    while SIZE != 0:
      SIZE = SIZE - 1
      if addr[SIZE].get_rssi() < -80 :
        continue
               
      else:
        data_two = clinetmodule("search", addr[SIZE].get_addr())
        response = data_two('/')
                  
        if response[2] == 1:
          continue
             
        else:
          server_sock_two = bluetooth.BluetoothSocket( bluetooth.L2CAP )
          port2 = 0x1002
          server_sock_two.bind(("",port2))
          server_sock_two.listen(1)
          client_sock_two,address_two = server_sock_two.accept()
          subdata = client_sock.recv(1024)
          parse2 = subdata.split('/')
          while parse2[2] == "search":
            data2 = "%d/%d/1" %(int(parse2[0]), int(parse2[1]))
            client_sock_two.send('Echo => ' + data2)
            server_sock_two.close()
            client_sock_two.close()
    
            server_sock_two = bluetooth.BluetoothSocket( bluetooth.L2CAP )
            port2 = 0x1002
            server_sock_two.bind(("",port2))
            server_sock_two.listen(1)
            client_sock_two,address_two = server_sock_two.accept()
            subdata = client_sock.recv(1024)
            parse2 = subdata.split('/')
    
            dic_addr[int(parse2[0])] = address_two
            child.append(int(parse2[0]))
    
            data = "%d/%d/1" %(number, count)
            client_sock.send('Echo => ' + data)


    print "pass"
    print "root condition"
  elif parse[2] == "search":
    #fill the condition
    print "search condition"
    if len(parent) is 0:
    #fill the condition
      parent.append(int(parse[0]))
      dic_addr[parent[0]] = address# need to address fill
      print dic_addr
      number =int(parse[1])+1
      count = int(parse[1])+1
      print "sensor number %d" %number
      data = "%d/%d/0" %(number, count) 
      client_sock.send('Echo => ' + data)

      #make
      SIZE = len(addr)
      while SIZE != 0:
        SIZE = SIZE - 1
        if addr[SIZE].get_rssi() < -80 :
          continue

        else:
          data_two = clinetmodule("search", addr[SIZE].get_addr())
          response = data_two('/')    

          if response[2] == 1:
            continue

          else:
            server_sock_two = bluetooth.BluetoothSocket( bluetooth.L2CAP )
            port2 = 0x1002
            server_sock_two.bind(("",port2))
            server_sock_two.listen(1)
            client_sock_two,address_two = server_sock_two.accept()
            subdata = client_sock.recv(1024)
            parse2 = subdata.split('/')
            while parse2[2] == "search":
              data2 = "%d/%d/1" %(int(parse2[0]), int(parse2[1]))
              client_sock_two.send('Echo => ' + data2)
              server_sock_two.close()
              client_sock_two.close()

              server_sock_two = bluetooth.BluetoothSocket( bluetooth.L2CAP )
              port2 = 0x1002
              server_sock_two.bind(("",port2))
              server_sock_two.listen(1)
              client_sock_two,address_two = server_sock_two.accept()
              subdata = client_sock.recv(1024)
              parse2 = subdata.split('/')

            dic_addr[int(parse2[0])] = address_two
            child.append(int(parse2[0]))

      data = "%d/%d/1" %(number, count)
      client_sock.send('Echo => ' + data)


      #end

      client_sock.close()
      server_sock.close()
    
    else:
      count = parse[1]
      data = "%d/%d/1" %(number, count)
      client_sock.send('Echo => ' + data)


#--------- end of while--------
