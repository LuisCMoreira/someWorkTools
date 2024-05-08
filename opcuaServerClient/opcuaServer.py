import sys
sys.path.append('./packages')

from opcua import Server
import time

# Create a server instance
server = Server()

# Define the endpoint URL for the server
url = "opc.tcp://10.1.1.4:4840/equinotectester/server/"

# Set the endpoint URL for the server
server.set_endpoint(url)

# Set server name
server.set_server_name("OPC UA Server")

# Start the server
server.start()

try:
    # Create a new object node
    objects = server.get_objects_node()

    # Add a new object called "MyObject"
    myobj = objects.add_object(2, "EQNobject")

    # Add a variable node under "MyObject" called "MyVariable"
    myvar = myobj.add_variable(2, "EQNvariable", "Hello World")

    # Activate variable
    myvar.set_writable()

    # Run the server until stopped
    while True:
        # Change the value of the variable to "HelloWorld"
        myvar.set_value("Hello World")
        time.sleep(1)
        # Change the value of the variable to "This is a Test"
        myvar.set_value("This is a Test")
        time.sleep(1)

finally:
    # Stop the server
    server.stop()

