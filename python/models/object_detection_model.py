class ObjectDetectionModel:
    def __init__(self):
        pass

    def detect_obstacle(self, sensor_data):
        # Returns True if an obstacle is detected
        return sensor_data["obstacle_distance"] < 5
