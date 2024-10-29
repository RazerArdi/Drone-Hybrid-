class LandingModel:
    def __init__(self):
        pass

    def get_landing_command(self, sensor_data):
        # Safe landing sequence
        if sensor_data["altitude"] > 1:
            return "descend"
        else:
            return "land"

