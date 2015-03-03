from test_inquiry import *
import bluetooth
from clientmodule import *
from servermoudle import *
import sys
addr = getaddr_rssi()
dic_addr ={}
parent = []
child = [] 
number = -1
count = -1
indexflag   = 0


light_state = 0

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
  if int(dataparse[1]) is number:
    #send success message
    message = "%s/%s/%d" %("getres","success" ,light_state)
    if len(parent) is 1: 
      clientmodule(message, dic_addr[parent[0]])
    else:
      #do we need a case??

  elif int(dataparse[1]) in child:
    #if the target in child array
    child_index = child.index(int(dataparse[1]))
    message = "%s/%s/%s" %(dataparse[0], dataparse[1], dataparse[2])
    clientmodule(message, dic_addr[child[child_index]])
  
  elif len(child) is 0: 
    #if this node is leaf node and incorrect number node
    #send fail message to parent 
    message = "%s/%s/%d" %("searchres", "fail", -1)
    clientmodule(message, dic_addr[parent[0]])

  else:
    #check the index flag
    #and then send message
    message = "%s/%s/%s" %(dataparse[0], dataparse[1], dataparse[2])
    clientmodule(message, dic_addr[child[indexflag]])
    indexflag= indexflag+1
    
  
    



#----end-----
def getres(dataparse, address):


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





