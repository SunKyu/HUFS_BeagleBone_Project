from test_inquiry import *
import bluetooth
from clientmodule import *
from servermodule import *
import sys
import time

addr = getaddr_rssi() #list of address and rssi 
dic_addr ={} #address dictionary
dic_sensor = {
    "light" : [],
    "humid" : [],
    "temper" : [],
    }

parent = [] #parent
child = [] #childe list
number = -1
indexflag  = 0 #need to change when all child visit (get, search)
get_target = -1 #store targetnumber
sensor_type = ""#store sensor_type
light_state = 0 #store light state
search_index = 0 #store current search index
total_num = 0

# root message : "sensor_type"
def root(res):
  global number
  sensor_type = res
  global search_index
  number = 0
  message = "search/%d/%d" %(0, number)
  clientmodule(message, addr[search_index].getaddr())
  search_index = search_index + 1
  while 1:
    print "=================> debug point"
    data =servermodule()
    dataparse = data.split('/')
    address = dataparse[len(dataparse)-1]

    if dataparse[0] == "search":
      response = "searchres/%s" %(dataparse[1])
      clientmodule(response, address)
      
    elif dataparse[0] == "searchres":
      if number != int(dataparse[1]):
        child.append(int(dataparse[1]))
        dic_addr[int(dataparse[1])] = address
    
      if search_index is len(addr):
        total_num = int(dataparse[1])
        break
      else :
        message = "search/%d/%d" %(int(dataparse[1]), number)
        clientmodule(message, addr[search_index].getaddr())
        search_index = search_index + 1


  while 1:
    for i in range(0, total_num+1):
      dic_sensor["light"].append(0)
      dic_sensor["humid"].append(0)
      dic_sensor["temper"].append(0)

    
    #infinite loop
    for i in range(0, 5):
			print "---------------------5th ------------"
      num_index = 0
      while 1:
        if num_index ==total_num:
          break
        if num_index == number:
          # determine light state
          num_index = num_index + 1
          continue
      
        child_num = 0
        while 1:
          message = "%s/%d/%s" %("get", num_index, sensor_type)
          clientmodule(message, dic_addr[child[child_num]])
          child_num = child_num + 1
          data = servermodule()
          dataparse = data.split('/')
        
          if dataparse[1] == "success":
            if dataparse[2] == "1":
              dic_sensor["light"][num_index] = dic_sensor["light"][num_index] + 1
            break
        num_index = num_index + 1
    
    for i in range(0, total_num):
      message = ""
      if dic_sensor["light"][i] >= 3:
        message = "put/%d/%s/%d" %(i, sensor_type, 1)
      else :
        message = "put/%d/%s/%d" %(i, sensor_type, 0)

      for j in child:
        clientmodule(message, dic_addr[j])

    time.sleep(30)

      

    #need to add the analysis table
    #and put 
        



def search(dataparse, address):
  global number
  global search_index
  if len(parent) is not 0:
    response = "searchres/%s" %(dataparse[1])
    clientmodule(response, address)
  else: 
    parent.append(int(dataparse[2]))
    count = int(dataparse[1]) + 1
    number = count
    dic_addr[parent[0]]= address

    if len(addr) != 0:
      message = "search/%d/%d" %(count, number)
      clientmodule(message, addr[search_index].getaddr())
      search_index = search_index + 1

    else:
      message = "searchres/%d" %(count)
      clientmodule(message, address)

   
   #need more case


#----end-----
def searchres(dataparse, address):
  global search_index
  global number
  if number != int(dataparse[1]):
    child.append(int(dataparse[1]))
    dic_addr[int(dataparse[1])] = address

  if search_index == len(addr):
    print "nember", number
    print "parent : ", parent
    print "child : ", child
    message = "searchres/%d" %(int(dataparse[1]))
    clientmodule(message, dic_addr.get(int(parent[0])))

  else:
    message = "search/%d/%d" %(int(dataparse[1]), number)
    clientmodule(message, addr[search_index].getaddr())
    search_index = search_index + 1
  


#----end-----
def get(dataparse, address):
  global indexflag
  global number
  global get_target
  global sensor_type
  get_target = int(dataparse[1])
  sensor_type = dataparse[2]
  if int(dataparse[1]) is number:
    #send success messag
    light_state = 1
    message = "%s/%s/%d" %("getres","success" ,light_state)
     
    clientmodule(message, dic_addr[parent[0]])

  elif len(child) is 0: 
    #if this node is leaf node and incorrect number node
    #send fail message to parent 
    message = "%s/%s/%d" %("getres", "fail", -1)
    clientmodule(message, dic_addr[parent[0]])

  elif int(dataparse[1]) in child:
    #if the target in child array
    child_index = child.index(int(dataparse[1]))
    message = "%s/%s/%s" %(dataparse[0], dataparse[1], dataparse[2])
    clientmodule(message, dic_addr[child[child_index]])
  
  else:
    #check the index flag
    #and then send message
    message = "%s/%s/%s" %(dataparse[0], dataparse[1], dataparse[2])
    clientmodule(message, dic_addr[child[indexflag]])
    indexflag= indexflag+1
    
  
    



#----end-----
def getres(dataparse, address):
  if dataparse[1] is "success":
    #if data is success
    message = "%s/%s/%s" %(dataparse[0], dataparse[1], dataparse[2])
    clientmodule(message, dic_addr[parent[0]])
  else:
    #if data is fail
    if indexflag < len(child):
      #send get message other childs
      message = "%s/%d/%s" %("get",get_target , sensor_type) 
      clientmodule(message, dic_addr[child[indexflag]])
      indexflag = indexflag+1

    else:
      #send fail(getres) message to parent, because already check all child
      message = "%s/%s/%s" %(dataparse[0], dataparse[1], dataparse[2])
      clientmodule(message, dic_addr[parent[0]])


#----end-----
def put(dataparse, address):
  if int(dataparse[1]) is number:
    #need to add sensortype case
    light_state = int(dataparse[3])
  else:
    #send child the message 
    message = "%s/%s/%s/%s" %(dataparse[0], dataparse[1], dataparse[2], dataparse[3])
    for i in child:
      clientmodule(message, dic_addr[i])

#----end-----

schemas = {
    "search" : search,
    "searchres" : searchres,
    "get" : get,
    "getres" : getres,
    "put" : put
    }




while 1:
  if len(sys.argv) is not 1:
    root(sys.argv[1])
  data = servermodule()
  dataparse = data.split('/')
  schema = dataparse[0]
  address = dataparse[len(dataparse)-1]
  schemas[schema](dataparse, address)





