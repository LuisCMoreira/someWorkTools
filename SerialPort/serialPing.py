import serial
import serial.tools.list_ports
import itertools

def find_serial_device():
    # List all available serial ports
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        print(f"Found device: {port.device}")
    return ports

def try_connection(port, baudrate, parity, stopbits, bytesize, timeout):
    try:
        with serial.Serial(port=port, baudrate=baudrate, parity=parity, stopbits=stopbits, bytesize=bytesize, timeout=timeout) as ser:
            # Attempt to read a line from the serial device
            line = ser.readline().decode('utf-8').strip()
            if line:
                print(f"Successful connection with settings: {baudrate}, {parity}, {stopbits}, {bytesize}")
                print(f"Received: {line}")
                return True
    except Exception as e:
        print(f"Failed to connect with settings: {baudrate}, {parity}, {stopbits}, {bytesize} - {e}")
    return False

def main():
    ports = find_serial_device()

    # Define possible settings to try
    baudrates = [9600, 19200, 38400, 57600, 115200]
    parities = [serial.PARITY_NONE, serial.PARITY_EVEN, serial.PARITY_ODD]
    stopbits = [serial.STOPBITS_ONE, serial.STOPBITS_TWO]
    bytesizes = [serial.EIGHTBITS, serial.SEVENBITS]
    timeout = 1  # Timeout in seconds

    # Print the variables to check their types
    print(f"baudrates: {baudrates}, type: {type(baudrates)}")
    print(f"parities: {parities}, type: {type(parities)}")
    print(f"stopbits: {stopbits}, type: {type(stopbits)}")
    print(f"bytesizes: {bytesizes}, type: {type(bytesizes)}")

    # Ensure all settings are lists
    assert all(isinstance(setting, list) for setting in [baudrates, parities, stopbits, bytesizes]), "All settings must be lists."

    # Try all combinations of settings
    for port in ports:
        for baudrate, parity, stopbits, bytesize in itertools.product(baudrates, parities, stopbits, bytesizes):
            if try_connection(port.device, baudrate, parity, stopbits, bytesize, timeout):
                break

if __name__ == "__main__":
    main()

