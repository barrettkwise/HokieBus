from dotenv import load_dotenv

from routefinder import RouteFinder
from schedule import Address, Schedule

load_dotenv(".env")
schedule = Schedule(
    Address(
        "508 Broce Dr",
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
