import re
from datetime import datetime
from pathlib import Path
from typing import Union

import icalendar as ical


class Schedule:
    """
    A class to represent a schedule of courses.

    :author: Barrett Wise
    :date: 1/16/25
    :param source_file: The path to the ics file.
    :type source_file: str
    """

    @staticmethod
    def _read_schedule(source: Path) -> list[dict[str, Union[str, datetime]]]:
        """
        Read the ics file and extract the course information.

        :param source: The path to the ics file.
        :type source: Path
        :return: A list of dictionaries containing course information.
        """
        loc_pattern = r"Campus:\s*(.*?)\s*Building:\s*(.*?)\s*Room:\s*([0-9]*)"
        courses = []
        with source.open() as f:
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

    def __init__(self, source_file: str) -> None:
        self.source = Path(source_file)
        self.courses = self._read_schedule(self.source)

    def __str__(self) -> str:
        return "\n".join(str(course) for course in self.courses)