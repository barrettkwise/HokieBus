import os
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Union

import icalendar as ical
import requests


@dataclass
class Address:
    """
    A class to represent an address.

    :author: Barrett Wise
    :date: 1/19/25
    :param street: The street address.
    :type street: str
    :param city: The city.
    :type city: str
    :param county: The county.
    :type county: str
    :param state: The state.
    :type state: str
    :param zip_code: The zip code.
    :type zip_code: str
    :param country: The country.
    :type country: str
    """

    street: str
    city: str
    county: str
    state: str
    zip_code: str
    country: str

    def convert_address_to_gps(self) -> tuple[float, float]:
        """
        Convert the address to GPS coordinates.

        :return: The latitude and longitude of the address.
        :rtype: tuple[Union[float, None], Union[float, None]]
        """
        try:
            req = requests.get(
                "https://geocode.maps.co/search",
                params={
                    "q": str(self),
                    "api_key": os.getenv("GEOCODE_KEY"),
                    "format": "json",
                },
            )
            data = req.json()
            lat = float(data[0]["lat"])
            lon = float(data[0]["lon"])
        except requests.exceptions.RequestException:
            lat = 0.0
            lon = 0.0

        return lat, lon

    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.county}, {self.state}, {self.zip_code}, {self.country}"

    def __repr__(self) -> str:
        return f"Address({self.street}, {self.city}, {self.county}, {self.state}, {self.zip_code}, {self.country})"


class Schedule:
    """
    A class to represent a schedule of courses.

    :author: Barrett Wise
    :date: 1/16/25

    :param source_file: The path to the .ics file containing the user's schedule.
    :type source_file: str
    :param init_location: The address of where the user is located, used to determine the closest bus stop.
    :type init_location: Address
    """

    def __init__(self, source_file: str, init_location: Address) -> None:
        self.__source = Path(source_file)
        if self.__source.suffix != ".ics":
            raise ValueError("The source file must be a .ics file.")
        self.init_location = init_location
        self.courses = self.__read_schedule()

    def __read_schedule(self) -> list[dict[str, Union[str, datetime]]]:
        """
        Read the .ics file and extract the course information.

        :return: A list of dictionaries containing the course information.
        :rtype: list[dict[str, Union[str, datetime]]]
        """

        loc_pattern = r"Campus:\s*(.*?)\s*Building:\s*(.*?)\s*Room:\s*([0-9]*)"
        courses = []
        with self.__source.open() as f:
            cal = ical.Calendar.from_ical(f.read())
            for event in cal.walk("VEVENT"):
                location = str(event.get("location")).strip()
                match = re.search(loc_pattern, location)
                campus = ""
                building = ""
                room = ""
                if match:
                    campus = match.group(1)
                    building = match.group(2)
                    room = match.group(3)

                summary = str(event.get("summary")).strip().split()
                course_code = summary[-3] + " " + summary[-2]

                start = ical.vDatetime.from_ical(
                    event.get("dtstart").to_ical().decode("utf-8")
                )
                end = ical.vDatetime.from_ical(
                    event.get("dtend").to_ical().decode("utf-8")
                )

                info = {
                    "crn": course_code,
                    "campus": campus,
                    "building": building,
                    "room": room,
                    "start": start,
                    "end": end,
                }
                courses.append(info)
        return courses