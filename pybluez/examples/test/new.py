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

def search():

#----end-----
def searchres():


#----end-----
def get():


#----end-----
def getres():


#----end-----
def put():


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
  schemas[schema]()
