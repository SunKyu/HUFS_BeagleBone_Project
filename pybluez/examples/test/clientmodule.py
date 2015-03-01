# file: l2capclient.py
# desc: Demo L2CAP client for bluetooth module.
# $Id: l2capclient.py 524 2007-08-15 04:04:52Z albert $

import sys
import bluetooth
def clinetmodule(message, addr):
  if sys.version < '3':
    input = raw_input

  sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)
  bt_addr=addr
  port = 0x1003

  print("trying to connect to %s on PSM 0x%X" % (bt_addr, port))

  sock.connect((bt_addr, port))

  print("connected.  type stuff")
  sock.send(message)
  response = sock.recv(1024)
  print(response)
  sock.close()
  return response

