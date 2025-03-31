import serial.tools.list_ports

def find_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    if not ports:
        print("No serial ports detected.")
    else:
        for port in ports:
            print(f"Port: {port.device}, Description: {port.description}, VID: {port.vid}, PID: {port.pid}")