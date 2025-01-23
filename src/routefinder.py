import json

import requests
from lxml import html

from bt4u_interface import BT4U_Interface as bt4u
from cache_handler import CacheHandler
from schedule import Address, Schedule


class RouteFinder:
    """
    Class to find the best route to take to get to a building on the Virginia Tech campus.

    :author: Barrett Wise
    :date: 1/22/25
    """

    def __init__(self, schedule: Schedule) -> None:
        """
        :param schedule: The schedule to find the best route for.
        :type schedule: Schedule
        """
        self.schedule = schedule
        self.buildings = RouteFinder.get_campus_addresses()
        self.find_route()

    def find_route(self) -> None:
        """
        Finds the best route to take to get to a building on the Virginia Tech campus.

        :return: None
        """

        address_cache = CacheHandler(
            "../data/addresses.json",
            12,
            RouteFinder.get_campus_addresses,
        )
        self.buildings = json.loads(address_cache.cache_file.read_text())
        for course in self.schedule.courses:
            building = course["building"]
            if building not in self.buildings.keys():
                print(f"Building {building} not found in the address cache.")
                continue
            building_address = self.buildings[building]
            bus_stop = bt4u.get_nearest_stops(
                building_address.get("latitude"), building_address.get("longitude"), 1
            )
            print(f"Closest bus stop to {building} is {bus_stop}.")

    @staticmethod
    def get_campus_addresses(update: bool = False) -> dict[str, Address] | str:
        """
        Fetches the addresses of all the buildings on the Virginia Tech campus from the VT website.

        :return: A dictionary containing the addresses of all the buildings on the Virginia Tech campus.
        :rtype: dict[str, Address]
        """

        if not update:
            return json.loads(open("../data/addresses.json").read())

        page = requests.get("https://www.vt.edu/about/locations/buildings.html")
        tree = html.fromstring(page.content)

        building_links = {
            building.text.strip(): building.attrib["href"]
            for building in tree.xpath('//li [@class="vt-subnav-droplist-item "]/a')
        }

        building_address_table = {}
        for building in building_links.keys():
            building_link = building_links[building]
            building_page = requests.get(building_link)
            building_tree = html.fromstring(building_page.content)
            address = building_tree.xpath(
                '//address [@class="vt-building-address"]/text()'
            )
            if address:
                building_address_table[building] = Address(
                    address[0],
                    "Blacksburg",
                    "Virginia",
                    "24061",
                    "United States",
                ).to_dict()
        return building_address_table
