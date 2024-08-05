#!/usr/bin/python
# -*- coding: UTF-8 -*-

import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md
from time import sleep, gmtime, strftime

def getShortValue(value):
    '''
    The state value is short type
    param value: unsigned int type
    return: 16-bit signed short type 
    '''
    if value >= pow(2, 15):
        return (~(value - 1) & (pow(2, 16) - 1)) * -1
    else:
        return value

def main():
    try:
        master = mt.TcpMaster("192.168.1.201", 502)
        master.set_timeout(5.0)
        print("Connected to Modbus server")

        joint_value = []    # Used to save the robot joint angle information
        joint_speed_value = [] # Used to save the robot joint speed information
        tcp_value = [] # Used to save TCP pose information of the robot
        tcp_speed_value = [] # Used to save the robot TCP speed information
        input_value = [] # Used to save the robot digital input port information
        output_value = [] # Used to save the robot digital output port information
        ainput_value = [] # Used to save the robot analog input port information
        aoutput_value = [] # Used to save robot analog output port information
        safety_params_enable_value = []
        collision_enable_value = []
        timestamp_value = []

        while True:
            try:
                hold_joint = master.execute(1, md.READ_HOLDING_REGISTERS, 200, 8)
                hold_joint_speed = master.execute(1, md.READ_HOLDING_REGISTERS, 210, 8)
                hold_tcp = master.execute(1, md.READ_HOLDING_REGISTERS, 220, 6)
                hold_safety_params_enable_status = master.execute(1, md.READ_HOLDING_REGISTERS, 228, 1)
                hold_collision_enable_status = master.execute(1, md.READ_HOLDING_REGISTERS, 229, 1)
                hold_tcp_speed = master.execute(1, md.READ_HOLDING_REGISTERS, 230, 1)
                hold_input = master.execute(1, md.READ_HOLDING_REGISTERS, 240, 3)
                hold_output = master.execute(1, md.READ_HOLDING_REGISTERS, 250, 2)
                hold_ainput = master.execute(1, md.READ_HOLDING_REGISTERS, 260, 3)
                hold_aoutput = master.execute(1, md.READ_HOLDING_REGISTERS, 270, 5)
                hold_timestamp = master.execute(1, md.READ_HOLDING_REGISTERS, 280, 4)

                # Process and save the data in the lists
                joint_value = [getShortValue(joint) / 5000.0 * 180 / 3.14 for joint in hold_joint]
                joint_speed_value = [getShortValue(speed) * 180 / 3.14 / 1000.0 for speed in hold_joint_speed]
                tcp_value = [getShortValue(tcp) / 10.0 if hold_tcp.index(tcp) < 3 else getShortValue(tcp) / 5000.0 * 180 / 3.14 for tcp in hold_tcp]
                safety_params_enable_value = [getShortValue(status) for status in hold_safety_params_enable_status]
                collision_enable_value = [getShortValue(status) for status in hold_collision_enable_status]
                tcp_speed_value = [getShortValue(speed) / 10.0 for speed in hold_tcp_speed]
                input_value = [input for input in hold_input]
                output_value = [output for output in hold_output]
                ainput_value = [getShortValue(ainput) / 1000.0 for ainput in hold_ainput]
                aoutput_value = [getShortValue(aoutput) / 1000.0 for aoutput in hold_aoutput]
                timestamp_value = [timestamp for timestamp in hold_timestamp]

                # Print the required data
                print("safety_params_enable_status =", safety_params_enable_value)
                print("collision_enable_status =", collision_enable_value)

                # Print and process the timestamp value
                timestamp_combined = timestamp_value[0] + (timestamp_value[1] << 16) + (timestamp_value[2] << 32) + (timestamp_value[3] << 48)
                print("Timestamp =", timestamp_combined)
                time_value = gmtime(timestamp_combined / 1000)
                print(strftime("%Y-%m-%d %H:%M:%S", time_value))

                # Clear the lists for the next read cycle
                joint_value.clear()
                safety_params_enable_value.clear()
                collision_enable_value.clear()
                joint_speed_value.clear()
                tcp_value.clear()
                tcp_speed_value.clear()
                input_value.clear()
                output_value.clear()
                ainput_value.clear()
                aoutput_value.clear()
                timestamp_value.clear()

                sleep(1)  # Wait for 1 second before the next read cycle

            except Exception as e:
                print(f"Error reading registers: {e}")
                break

    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    main()
