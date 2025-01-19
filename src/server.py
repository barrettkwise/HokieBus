from dotenv import load_dotenv
from flask import Flask

import utilities as util
from schedule import Address, Schedule

load_dotenv(".env")

app = Flask(__name__)
schedule = Schedule(
    "../schedules/Spring2025.ics",
    Address(
        "508 Broce Dr",
        "Blacksburg",
        "Montgomery",
        "Virginia",
        "24060",
        "United States",
    ),
)

print(schedule.init_location)
print(f"GPS cords: {schedule.init_location.convert_address_to_gps()}")

nearest_stops = util.__req_get_nearest_stops(
    schedule.init_location.convert_address_to_gps()[0],
    schedule.init_location.convert_address_to_gps()[1],
    5,
    "1/19/25",
)

print(nearest_stops["json"])