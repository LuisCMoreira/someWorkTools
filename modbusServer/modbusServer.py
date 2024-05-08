import sys
sys.path.append('./packages')

import modbus_server
import time

# Create a Modbus server instance
s = modbus_server.Server( host="10.1.1.4",port=505)

# Start the Modbus server
s.start()

# Initialize a variable to track the coil state
coil_state = False

start_address = 10
values = [300]
encoding = 'h'
signal= -1

try:
    while True:
        # Toggle the coil state (blink the coil)
        coil_state = not coil_state
        s.set_coil(1, coil_state)  # Set the state of coil 1
        s.set_coil(2, not coil_state) 
        ## encoding must be "h" (short), "H" (unsigned short), "e" (float16), or "f" (float32) not utf-16
        s.set_holding_registers(start_address, values, encoding)
        if (values[0] < 1):
            signal=1
        if values[0] >350:
            signal=-1
        values=[values[0]+signal]
        
        ##print(coil_state)

        # Delay for a certain period
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Server stopped")
    s.stop()