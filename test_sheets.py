from pymodbus.client.sync import ModbusSerialCLient as ModbusClient
from pymodbus.register_read_message import ReadInputRegistersResponse
import datetime, time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('mydata.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Raspi_data").sheet

client = ModbusClient(method = 'RTU', port = '/dev/ttyUSB0', stopbits = 1, bytesize = 8, parity = '0', baudrate = '9600', timeout = 0.6)
connection = client.connect()
print(connection)
value = client.read_input_registers(212, 2, unit = 1)
x = (value.getRegister(0))
y = (value.getRegister(1))
a = (hex(x))
b = (hex(y))
c = (a[2:])
d = (b[2:])
z = str(str(c) + str(d))

import struct
g = struct.unpack('!f', bytes.fromhex(z))[0]
print('Academic Block Vplus = ', g)

value1 = client.read_input_registers(200, 2, unit = 1)
x1 = (value1.getRegister(0))
y1 = (value1.getRegister(1))
a1 = (hex(x1))
b1 = (hex(y1))
c1 = (a1[2:])
d1 = (b1[2:])
z1 = str(str(c1) + str(d1))

import struct
g1= struct.unpack('!f', bytes.fromhex(z1))[0]
print('Academic Block Qv = ', g1)

value2 = client.read_input_registers(216, 2, unit = 1)
x2 = (value2.getRegister(0))
y2 = (value2.getRegister(1))
a2 = (hex(x2))
b2 = (hex(y2))
c2 = (a2[2:])
d2 = (b2[2:])
z2 = str(str(c2) + str(d2))

import struct
g2 = struct.unpack('!f', bytes.fromhex(z2))[0]
print('Academic Block Vminus = ', g2)

time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
print(time)
Vplus = g
Qv  =g1
Vminus = g2
values = [time, Vplus, Qv, Vminus]
sheet.append_row(values)