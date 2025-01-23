from dotenv import load_dotenv

from bt4u_interface import BT4U_Interface as bt4u
from routefinder import RouteFinder
from schedule import Address, Schedule

load_dotenv(".env")
schedule = Schedule(
    Address(
        "519 Hunt Club Rd",
        "Blacksburg",
        "Virginia",
        "24060",
        "United States",
    ),
    "../data/schedules/Fall2023.ics",
)
print("Schedule:")
print(schedule.courses)
print("\n")
route_finder = RouteFinder(schedule)