import serial

class DataStream:
    def __init__(self, port, baud_rate):
        self.serial_connection = serial.Serial(port, baud_rate)

    def read_sensor_data(self):
        line = self.serial_connection.readline().decode("utf-8")
        return self.parse_sensor_data(line)

    def send_command(self, command):
        self.serial_connection.write(command.encode("utf-8"))

    def parse_sensor_data(self, line):
        # Assume line is formatted as "altitude:5;distance:20"
        data = {}
        parts = line.split(";")
        for part in parts:
            key, value = part.split(":")
            data[key] = float(value)
        return data

