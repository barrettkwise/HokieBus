import os

import anvil._serialise
import anvil.server
from dotenv import load_dotenv

from routefinder import RouteFinder
from schedule import Address, Schedule


@anvil.server.callable
def upload(calendar: anvil._serialise.StreamingMedia) -> dict[str, str]:
    schedule = Schedule(
        Address(
            "519 Hunt Club Rd",
            "Blacksburg",
            "Virginia",
            "24060",
            "United States",
        ),
        calendar,
    )
    route_finder = RouteFinder(schedule)
    return route_finder.find_route()


if __name__ == "__main__":
    load_dotenv(".env")

    anvil.server.connect(os.getenv("ANVIL_KEY"))
    anvil.server.wait_forever()