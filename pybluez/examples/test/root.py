#root.py code

from test_inquriry import *
import bluetooth
from clientmodule import *
from servermodule import *
import sys

addr = getaddr_rssi() #list of address and rssi
dic_addr = {}
parent = []
child = []
number = 0
count = 0
sensor_type = ""
light_state = 0
search_index = 0

def root():
  sleep(10)

  while 1: 
    sleep(10)

