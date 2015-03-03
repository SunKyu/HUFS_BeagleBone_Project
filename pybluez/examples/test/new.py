from test_inquiry import *
import bluetooth
from clientmodule import *
from servermoudle import *
import sys
addr = getaddr_rssi() #list of address and rssi 
dic_addr ={} #address dictionary
parent = [] #parent
child = [] #childe list
number = -1
count = -1
indexflag  = 0 #need to change when all child visit (get, search)
get_target = -1 #store targetnumber
sensor_type = ""#store sensor_type
light_state = 0 #store light state


def search(dataparse, address):
 if len(parent) is not 0:
   response = "searchres/%s" %dataparse[1]
   clientmodule(response, address)
 else: 
   #need more case
   parent.append(int(dataparse[2]))
   count = int(dataparse[1])
   number = count+1
   if len(addr):
    message = "search/%d/%d" %(count, number)
   #need more case


#----end-----
def searchres(dataparse, address):



#----end-----
def get(dataparse, address):
  get_target = int(dataparse[1])
  sensor_type = dataparse[2]
  if int(dataparse[1]) is number:
    #send success message
    message = "%s/%s/%d" %("getres","success" ,light_state)
    if len(parent) is 1: 
      clientmodule(message, dic_addr[parent[0]])
    else:
      #do we need a case??

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
    light_state = int(dataparse[1])
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
  data = servermoudle()
  dataparse = data.split('/')
  schema = dataparse[0]
  address = dataparse[len(dataparse)-1]
  schemas[schema](dataparse, address)





