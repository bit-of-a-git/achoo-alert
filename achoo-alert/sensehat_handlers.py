from sense_hat import SenseHat
import pollen
from config import RISK_COLOURS, SCROLL_SPEED


class SenseHatHandler:
    def __init__(self, sense):
        """
        Initialises the handler with a Sense HAT instance.
        """
        self.sense = sense

    def button_pressed(self, event):
        if event.action == "pressed":
            risk = pollen.fetch_highest_risk()
            if risk:
                colour = RISK_COLOURS.get(risk, [255, 255, 255])
                message = f"Currently a {risk} risk of pollen"
                self.display_sensehat_message(message, colour)
            else:
                self.display_sensehat_message("Error fetching risk", [255, 0, 0])

    def display_sensehat_message(self, message, colour: list[int]):
        self.sense.show_message(message, text_colour=colour, scroll_speed=SCROLL_SPEED)


if __name__ == "__main__":
    sense = SenseHat()
    sensehat_handler = SenseHatHandler(sense)
    sense.stick.direction_middle = sensehat_handler.button_pressed

    while True:
        pass
