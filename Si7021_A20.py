#!/usr/bin/env python
# Simple function which uses smbus to interface with the Si7021-A20
# digital temperature and humidity sensor
# adapted from http://www.pibits.net/code/raspberry-pi-si7021-sensor-example.php
import smbus
import time

# Simple function which uses smbus to query the Si7021-A20 digital sensor
# This sensor has a default I2C address of 0x40.
def querySI(address=0x40):
    # Get I2C bus
    bus = smbus.SMBus(1)
    bus.write_byte(address, 0xF5)

    # Time delay
    time.sleep(0.3)
        
    # SI7021 address, 0x40  Read 2 bytes, Humidity
    data0 = bus.read_byte(address)
    data1 = bus.read_byte(address)

    # Convert the data using equation from section 5.1.1. of https://www.silabs.com/documents/public/data-sheets/Si7021-A20.pdf
    humidity = ((data0 * 256 + data1) * 125 / 65536.0) - 6
        
    time.sleep(0.3)
    bus.write_byte(address, 0xF3)
    time.sleep(0.3)
        
    # SI7021 address, 0x40 Read data 2 bytes, Temperature
    data0 = bus.read_byte(address)
    data1 = bus.read_byte(address)
        
    # Convert the data using euqation from section 5.1.2. of https://www.silabs.com/documents/public/data-sheets/Si7021-A20.pdf
    celsTemp = ((data0 * 256 + data1) * 175.72 / 65536.0) - 46.85
    fahrTemp = celsTemp * 1.8 + 32

    # Initialize the dictionary which will be returned
    sensorReading = {}
    sensorReading["Temp"], sensorReading["RH"] = celsTemp, humidity

    # print(f"Relative Humidity is : {humidity} %")
    # print(f"Temperature in Celsius is : {celsTemp} C")
    # print(f"Temperature in Fahrenheit is : {fahrTemp}")

    return sensorReading

