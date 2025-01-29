import os

import anvil._serialise
import anvil.server
from dotenv import load_dotenv

from routefinder import RouteFinder
from schedule import Address, Schedule


class AnvilHandler:
    """
    A class to handle the interaction with Anvil.

    :author: Barrett Wise
    :date: 1/25/25
    """

    def __init__(self) -> None:
        load_dotenv(".env")
        anvil_key = os.getenv("ANVIL_KEY")
        if not anvil_key:
            raise ValueError("ANVIL_KEY not found in environment variables.")
        anvil.server.connect(anvil_key)
        self.start_location: Address
        self.schedule_file: anvil._serialise.StreamingMedia

    @anvil.server.callable
    @staticmethod
    def call_me(location_cords: tuple[float, float]) -> None:
        """
        A function that is called from the Anvil app.

        :param location_cords: The GPS coordinates of the location.
        :type location_cords: tuple[float, float]
        """

    def set_start_location(self, location_string: str) -> None:
        """
        Set the start location of the route.

        :param location_string: The start location of the route in the format:
                                "Street, City, State, ZIP, Country".
        :type location_string: str
        """
        address_parts = location_string.split(",")
        if len(address_parts) != 5:
            raise ValueError("Invalid address format.")
        self.start_location = Address(*address_parts)

    def get_route(self, calendar: anvil._serialise.StreamingMedia) -> dict[str, str]:
        """
        Generate a route based on the provided calendar and the start location.

        :param calendar: Anvil StreamingMedia object containing the calendar data.
        :return: A dictionary containing the route information.
        """
        if not self.start_location:
            raise ValueError("Start location has not been set.")

        schedule = Schedule(self.start_location, calendar)

        route_finder = RouteFinder(schedule)
        return route_finder.find_route()
