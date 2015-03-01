

from test_inquiry import *
import bluetooth
import sys
from clientmodule import *
addr = getaddr_rssi()
dic_addr ={}
dic_state={}
parent = []
child = [] 
number = -1
count = -1
total_count = 0
while 1:
    
  server_sock=bluetooth.BluetoothSocket( bluetooth.L2CAP )

  port = 0x1001

  server_sock.bind(("",port))
  server_sock.listen(1)

  client_sock,address = server_sock.accept()
  print("Accepted connection from ",address)

  if len(sys.argv) != 1:
    data = argv[1]
  else:
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
      if addr[SIZE].getrssi() < -80 :
        continue
               
      else:
        data_two = clinetmodule("%d/%d/search"%(number, count), addr[SIZE].getaddr())
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
    
            addr_two = address_two.split("'")
            dic_addr[int(parse2[0])] = addr_two[1]
            child.append(int(parse2[0]))
    
            data = "%d/%d/1" %(number, count)
            client_sock.send('Echo => ' + data)

        total_count = response[1]
    

    # first while end

    while 1:
      arr = []
      for j in range(0, total_count):
       arr.append(0)

      dic_state['light'] = arr
      dic_state['humid'] = arr
      dic_state['co2'] = arr

      for i in range(0, 5):
        new_arr = dic_state.get('light')
        for j in range(0, total_count):
          if number == j:
            #light state +1 or +0
            new_arr[j] = new_arr[j] + 1

          else:
            for k in child:
              data_two = clinetmodule("%s/%d/%s"%('get', j, 'light'), dic_addr[k])

              response = data_two.split('/')

              if response[2] == 'wait':
                server_sock_two = bluetooth.BluetoothSocket( bluetooth.L2CAP )
                port2 = 0x1002
                server_sock_two.bind(("",port2))
                
                server_sock_two.listen(1)
                client_sock_two,address_two = server_sock_two.accept()
                subdata = client_sock_two.recv(1024)
                parse2 = subdata.split('/')

                if parse2[3] == 'fail':
                  server_sock_two.close()
                  client_sock_two.close()
                  continue

                else:
                  new_arr[k] = new_arr[k] +int( parse2[2])
                  server_sock_two.close()
                  client_sock_two.close()
                  break

              else:
                #success
                if response[3] == 'fail':
                  continue

                else:
                  new_arr[k] = new_arr[k] + int(response[2])
                  break
        dic_state['light'] = new_arr

      #put
      new_array = dic_state.get('light')
      for j in range(0, total_count):
        if new_array[j] > 2:
          if j == number:
            #turn on light
            light =1
          else:
            for k in child:
              if sys.version < '3':
                input = raw_input
              sock3=bluetooth.BluetoothSocket(bluetooth.L2CAP)
              bt_addr3 = dic_addr[k]
              port = 0x1003

              sock3.connect((bt_addr3, port))

              sock3.send("%s/%d/%s" %('put', j, 'light'))
              sock3.close()


    print "pass"
    print "root condition"
  elif parse[2] == "search":
    #fill the condition
    print "search condition"
    if len(parent) is 0:
    #fill the condition
      parent.append(int(parse[0]))
      addr_one = adress.split("'")
      dic_addr[parent[0]] = addr_one[1]# need to address fill
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
        if addr[SIZE].getrssi() < -80 :
          continue

        else:
          data_two = clinetmodule("%d/%d/search"%(number, count), addr[SIZE].getaddr())
          response = data_two.split('/')    

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

            
            addr_two = address_two.split("'")
            dic_addr[int(parse2[0])] = addr_two[1]
            child.append(int(parse2[0]))

      data = "%d/%d/1" %(number, count)
      client_sock.send('Echo => ' + data)


      #end

      client_sock.close()
      server_sock.close()
    
    else: #when parents exist
      count = parse[1]
      data = "%d/%d/1" %(number, count)
      client_sock.send('Echo => ' + data)

  elif parse[0] == "get":
    if parse[1] == number:
      state =1 #light state
      client_sock.send('%s/%d/%d/%s' %('get',0,state, 'success'))

    else:
      #by fail...
      client_sock.send('%s/%d/%s' %('get', 0, 'wait'))
      success_fail = 'fail'
      for i in child:
        data_two = clinetmodule("%s/%d/%s"%('get', parse[1], 'light'), dic_addr[i])

        response = data_two.split('/')

        if response[2] == 'wait':
          server_sock_two = bluetooth.BluetoothSocket( bluetooth.L2CAP )
          port2 = 0x1002
          server_sock_two.bind(("",port2))
                
          server_sock_two.listen(1)
          client_sock_two,address_two = server_sock_two.accept()
          subdata = client_sock_two.recv(1024)
          parse2 = subdata.split('/')

          if parse2[3] == 'fail':
            server_sock_two.close()
            client_sock_two.close()
            continue

          else:
            success_fail = 'success'
            server_sock_two.close()
            client_sock_two.close()
            state = parse2[2] 
            client_sock.send("%s/%d/%d/%s" %('get', 0, state, 'success'))
            break


        else:
          #success
          if response[3] == 'fail':
            continue

          else:
            success_fail = 'success'
            state = response[2]#light stats    
            client_sock.send("%s/%d/%d/%s" %('get', 0, state, 'success'))
            break
                
      if sucess_fail == 'fail':
        client_sock.send("%s/%d/%d/%s" %('get', 0, 0, 'fail'))

  elif parse[0] == 'put':
    if parse[1] == number:
      #turn on light
      light =1

    else:
      for k in child:
        if sys.version < '3':
          input = raw_input
        sock3=bluetooth.BluetoothSocket(bluetooth.L2CAP)
        bt_addr3 = dic_addr[k]
        port = 0x1003

        sock3.connect((bt_addr3, port))

        sock3.send("%s/%d/%s" %('put', parse[1], parse[2]))
        sock3.close()

  server_sock.close()
  client_sock.close()

#--------- end of while--------
