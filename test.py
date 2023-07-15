from Controller.DataBase.Reader import *
from pyModbusTCP.client import ModbusClient
import struct
import binascii





cl=ModbusClient(host="5.26.186.85",port=502,unit_id=5,timeout=2000,auto_open=True)

reg=cl.read_holding_registers(6018,2)
print (f"Gelen : {reg} ")






