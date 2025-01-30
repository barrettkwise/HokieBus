import os
from operator import add

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

    @staticmethod
    @anvil.server.callable
    def call_me(
        latitude: float, longitude: float, calendar: anvil._serialise.StreamingMedia
    ) -> dict[str, str]:
        """
        A test function to check if the Anvil server is working.

        :param latitude: The latitude.
        :type latitude: float
        :param longitude: The longitude.
        :type longitude: float
        :param calendar: Anvil StreamingMedia object containing the calendar data.
        :type calendar: anvil._serialise.StreamingMedia
        :return: A dictionary containing the route information.
        :rtype: dict[str, str]
        """
        location_string = Address().convert_gps_to_address(latitude, longitude)
        address_parts = location_string.split(",")
        # print(address_parts)
        if len(address_parts) != 5:
            raise ValueError("Invalid address format.")

        address = Address(
            address_parts[0],
            address_parts[1],
            address_parts[2],
            address_parts[3],
            address_parts[4],
        )
        schedule = Schedule(address, calendar)
        return RouteFinder(schedule).find_route()