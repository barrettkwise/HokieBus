import anvil.server
from anvil import *
from anvil.js.window import navigator

from ._anvil_designer import RoutePlannerTemplate


class RoutePlanner(RoutePlannerTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.start_pos = []
        try:
            navigator.geolocation.getCurrentPosition(lambda p: self.success(p))
        except Exception as e:
            alert(f"Error: {str(e)}")

    def file_loader_change(self, file, **event_args):
        """
        This method is called when the user uploads their calendar file.
        It retrieves the route and displays the stops on the map.
        """
        result = anvil.server.call(
            "call_me", self.start_pos[0], self.start_pos[1], file
        )
        self.map.clear()
        for location, bus_stop in result.items():
            print(f"Closest stop to {location} is {bus_stop}")
            marker = GoogleMap.Marker(
                animation=GoogleMap.Animation.DROP,
                position=GoogleMap.LatLng(
                    float(bus_stop["Latitude"]), float(bus_stop["Longitude"])
                ),
                label=location,
            )
            self.map.add_component(marker)
        Notification("Route successfully added to the map!", title="Success").show()

    def map_show(self, **event_args):
        """
        This method is called when the GoogleMap is shown on the screen.
        It configures the map center and zoom level.
        """
        self.map.center = GoogleMap.LatLng(37.2296, -80.4139)
        self.map.zoom = 13

    def success(self, pos):
        self.start_pos.append(pos.coords.latitude)
        self.start_pos.append(pos.coords.longitude)
