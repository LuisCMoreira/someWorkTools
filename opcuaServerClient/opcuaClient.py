import sys
sys.path.append('./packages')

from opcua import Client

# Define the OPC UA server endpoint URL
url = "opc.tcp://localhost:4840/freeopcua/server/"

# Create a client object
client = Client(url)

try:
    # Connect to the OPC UA server
    client.connect()

    # Get the root node
    root_node = client.get_root_node()

    # Get the objects node
    objects_node = root_node.get_child(["0:Objects"])

    # Get the variable node
    variable_node = objects_node.get_child(["2:MyObject", "2:MyVariable"])

    # Read the value of the variable
    value = variable_node.get_value()

    print("Value of MyVariable:", value)

finally:
    # Disconnect from the OPC UA server
    client.disconnect()
