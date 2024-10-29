class CommandHandler:
    def __init__(self):
        pass

    def get_avoidance_command(self):
        """Generate an avoidance command when an obstacle is detected."""
        return "move_left"

    def generate_command(self, action_type, intensity=0):
        """
        Generate a command string based on action type and intensity.

        Args:
            action_type (str): The type of action (e.g., 'move', 'rotate').
            intensity (int): The intensity or speed of the action.
        
        Returns:
            str: Command string formatted for serial communication.
        """
        return f"{action_type}:{intensity}"

    def parse_command_response(self, response):
        """
        Parse command response from the Arduino.

        Args:
            response (str): Response string from the Arduino.

        Returns:
            dict: Parsed response as a dictionary.
        """
        data = {}
        parts = response.strip().split(";")
        for part in parts:
            key, value = part.split(":")
            data[key] = float(value) if '.' in value else int(value)
        return data
``

