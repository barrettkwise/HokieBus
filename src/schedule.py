import os
import re
from io import BytesIO, TextIOWrapper
from pathlib import Path

import anvil._serialise
import anvil.media
import icalendar as ical
from geocodio import GeocodioClient


class Address:
    """
    A class to represent an address.

    :author: Barrett Wise
    :date: 1/19/25
    """

    def __init__(
        self,
        address: str,
        city: str,
        state: str,
        zip_code: str,
        country: str,
    ) -> None:
        """
        :param street: The street address.
        :type street: str
        :param city: The city.
        :type city: str
        :param state: The state.
        :type state: str
        :param zip_code: The zip code.
        :type zip_code: str
        :param country: The country.
        :type country: str
        """
        self.street = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country
        self.latitude = self.__convert_address_to_gps()[0]
        self.longitude = self.__convert_address_to_gps()[1]

    def __convert_address_to_gps(self) -> tuple[float, float]:
        """
        Convert the address to GPS coordinates.

        :return: The latitude and longitude of the address.
        :rtype: tuple[float, float]
        """
        client = GeocodioClient(os.getenv("GEOCODE_KEY"))

        location = client.geocode(
            f"{self.street}, {self.city}, {self.state} {self.zip_code}",
            country=self.country,
            limit=3,
        )
        if location is None:
            raise ValueError("Invalid address.")

        coords = location["results"][0]["location"]
        return (coords["lat"], coords["lng"])

    def __str__(self) -> str:
        return (
            f"{self.street}, {self.city}, {self.state}, {self.zip_code}, {self.country}"
        )

    def __repr__(self) -> str:
        return f"Address({self.street}, {self.city}, {self.state}, {self.zip_code}, {self.country})"

    def to_dict(self) -> dict[str, str | float | None]:
        return {
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "country": self.country,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }


class Schedule:
    """
    A class to represent a schedule of courses.

    :author: Barrett Wise
    :date: 1/16/25
    """

    def __init__(
        self, init_location: Address, source_file: str | anvil._serialise.StreamingMedia
    ) -> None:
        """
        :param source_file: The path to the .ics file containing the user's schedule.
        :type source_file: str | anvil._serialise.StreamingMedia
        :param init_location: The address of where the user is located, used to determine the closest bus stop.
        :type init_location: Address
        """
        if isinstance(source_file, anvil._serialise.StreamingMedia):
            self.__source = BytesIO(source_file.get_bytes())
        else:
            self.__source = Path(source_file)
        self.init_location = init_location
        self.courses = self.__read_schedule()

    def __read_schedule(self) -> list[dict[str, str]]:
        """
        Read the .ics file and extract the course information.

        :return: A list of dictionaries containing the course information.
        :rtype: list[dict[str, str]]
        """
        loc_pattern = r"Campus:\s*(.*?)\s*Building:\s*(.*?)\s*Room:\s*([0-9]*)"
        courses = []

        if isinstance(self.__source, BytesIO):
            f = TextIOWrapper(self.__source)
        else:
            f = self.__source.open()

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

                start = str(
                    ical.vDatetime.from_ical(
                        event.get("dtstart").to_ical().decode("utf-8")
                    ).strftime("%m/%d/%Y, %H:%M:%S %p")
                )
                end = str(
                    ical.vDatetime.from_ical(
                        event.get("dtend").to_ical().decode("utf-8")
                    ).strftime("%m/%d/%Y, %H:%M:%S %p")
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