from flask import Flask

import src.utilities as utilities
from src.schedule import Schedule

app = Flask(__name__)
schedule = Schedule("schedules/Fall2023.ics")

print(utilities.__req_get_current_bus_info())
