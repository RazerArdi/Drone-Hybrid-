import time
from models.navigation_model import NavigationModel
from models.object_detection_model import ObjectDetectionModel
from models.landing_model import LandingModel
from utils.data_stream import DataStream
from utils.command_handler import CommandHandler

# Initialize Models
nav_model = NavigationModel()
obj_det_model = ObjectDetectionModel()
land_model = LandingModel()

# Initialize Data Stream and Command Handler
data_stream = DataStream(port="COM3", baud_rate=9600)
command_handler = CommandHandler()

def main():
    while True:
        # Get sensor data from Arduino
        sensor_data = data_stream.read_sensor_data()

        # Navigation decisions
        nav_command = nav_model.get_navigation_command(sensor_data)
        data_stream.send_command(nav_command)

        # Object Detection for obstacle avoidance
        if obj_det_model.detect_obstacle(sensor_data):
            avoidance_command = command_handler.get_avoidance_command()
            data_stream.send_command(avoidance_command)

        # Landing control
        if nav_model.is_near_landing_zone(sensor_data):
            landing_command = land_model.get_landing_command(sensor_data)
            data_stream.send_command(landing_command)

        time.sleep(0.1)  # Loop delay

if __name__ == "__main__":
    main()

