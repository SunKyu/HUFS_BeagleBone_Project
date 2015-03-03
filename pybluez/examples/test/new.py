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

def search(dataparse, address):
 if len(parnet) is not 0:
   response = "searchres/%s" %dataparse[1]
   clientmodule(response, address)
 else:
   parent[
#----end-----
def searchres(dataparse):


#----end-----
def get(dataparse):


#----end-----
def getres(dataparse):


#----end-----
def put(dataparse):


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

