import anvil.server
from anvil import *

from ._anvil_designer import Form1Template


class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def file_loader_1_change(self, file, **event_args):
        """This method is called when a new file is loaded into this FileLoader"""
        result = anvil.server.call("upload", file)

        # clear all components to allow for multiple uploads
        self.map.clear()

        # Configure the map center and zoom
        self.map.center = GoogleMap.LatLng(37.2296, -80.4139)
        self.map.zoom = 13
        for location, bus_stop in result.items():
            print(f"Closest stop to {location} is {bus_stop}")
            mark = self.map.Marker(
                animation=GoogleMap.Animation.DROP,
                position=GoogleMap.LatLng(
                    float(bus_stop["Latitude"]), float(bus_stop["Longitude"])
                ),
                label=location,
            )
            self.map.add_component(mark)
